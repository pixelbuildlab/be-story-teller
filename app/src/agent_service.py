import json
import openai
from app.src.ai_service import AIService
from app.src.web_socket_manager import ConnectionManager
from app.src.agent_tools.story_outline_planner_tool import story_outline_planner_tool
from app.src.agent_tools.story_writer_tool import story_writer_tool
from app.src.agent_tools.story_scene_exactor_tool import story_scene_exactor_tool
from app.src.agent_tools.story_prompt_optimizer_tool import story_prompt_optimizer_tool

# from app.src.agent_tools.markdown_writer_tool import markdown_writer_tool
from app.src.agent_tools.image_generation_tool import image_generation_tool
from app.src.custom_class import StoryResult


class AgentService:

    def __init__(self, ai: AIService, tools: list, manager: ConnectionManager):
        self.ai: AIService = ai
        self.tools = tools
        self.manager: ConnectionManager = manager

    async def flow(self, prompt: str, META_PROMPT: str, client_id: str):
        messages_list = []
        story = None
        metadata = None
        image = None

        try:
            messages = [
                {"role": "system", "content": META_PROMPT},
                {
                    "role": "user",
                    "content": f"{prompt}",
                },
            ]
            messages_list.extend(messages)

            while True:
                print("STARTING AGENT ITERATION")
                await self.manager.send_agent_updates(client_id, "Agent Thinking")
                chat_completion = await self.ai.AI(messages_list, self.tools)
                response_message = chat_completion.choices[0].message

                # Append assistant message to history
                messages_list.append(response_message.model_dump())
                print(
                    f"Assistant: {response_message.content if response_message.content else 'Tool Calls'}"
                )

                await self.manager.send_agent_updates(
                    client_id, "Agent Thoughts finalized"
                )

                # If LLM returned tool calls, process them
                if (
                    hasattr(response_message, "tool_calls")
                    and response_message.tool_calls
                ):
                    try:
                        for tool_call in response_message.tool_calls:
                            function_name = tool_call.function.name
                            function_args = json.loads(tool_call.function.arguments)

                            print(f"Tool call: {function_name}, args: {function_args}")

                            # Dynamically get the tool function
                            tool_function = globals().get(function_name)
                            if not tool_function:
                                print(f"Tool {function_name} not found in globals")
                                continue

                            await self.manager.send_agent_updates(
                                client_id,
                                "Agent invoking tools to build something stunning",
                            )

                            await self.manager.send_agent_updates(
                                client_id, f"Agent invoking tool: [{function_name}]"
                            )

                            tool_result, tool_chat_completion = await tool_function(
                                **function_args
                            )

                            await self.manager.send_agent_updates(
                                client_id,
                                f"Agent tool [{function_name}] invoking completed",
                            )

                            content = ""
                            if hasattr(tool_result, "content"):
                                content = tool_result.content
                                if function_name == "story_writer_tool":
                                    story = content
                                if function_name == "story_outline_planner_tool":
                                    try:
                                        metadata = json.loads(content)
                                    except:
                                        metadata = content
                            else:
                                if function_name == "image_generation_tool":
                                    print("IMAGE GENERATED")
                                    image = tool_result

                                # If it's a dict or other object, stringify it for the tool response
                                if isinstance(tool_result, (dict, list)):
                                    content = json.dumps(tool_result)
                                else:
                                    content = str(tool_result)

                            messages_list.append(
                                {
                                    "role": "tool",
                                    "tool_call_id": tool_call.id,
                                    "content": content,
                                }
                            )

                    except Exception as e:
                        print(f"Error invoking tool {function_name}: {e}")
                        # Optionally add an error message to the history so the AI knows
                        messages_list.append(
                            {
                                "role": "tool",
                                "tool_call_id": tool_call.id,
                                "content": f"Error: {str(e)}",
                            }
                        )

                else:
                    # No more tool calls, return the result
                    await self.manager.send_agent_updates(
                        client_id,
                        f"Agent has done working",
                    )
                    return StoryResult(story=story, metadata=metadata, image=image)

        except openai.APIConnectionError as e:
            print(f"Network connectivity issue: {e}")
            await self.manager.send_agent_updates(
                client_id, "Agent failed to connect to LLM"
            )

        except openai.RateLimitError as e:
            print(f"Rate limits hit or out of funds: {e}")
        except openai.APIStatusError as e:
            print(f"HTTP Error received (Status: {e.status_code}): {e.response}")
        except openai.APIError as e:
            print(f"APIError received (Status: {e.body}): {e.message}")
