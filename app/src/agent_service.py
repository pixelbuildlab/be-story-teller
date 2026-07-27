import json
import openai
from app.src.ai_service import AIService
from app.src.agent_tools.story_outline_planner_tool import story_outline_planner_tool
from app.src.agent_tools.story_writer_tool import story_writer_tool
from app.src.agent_tools.story_scene_exactor_tool import story_scene_exactor_tool
from app.src.agent_tools.story_prompt_optimizer_tool import story_prompt_optimizer_tool

# from app.src.agent_tools.markdown_writer_tool import markdown_writer_tool
from app.src.agent_tools.image_generation_tool import image_generation_tool
from app.src.custom_class import StoryResult


class AgentService:

    def __init__(self, ai, tools):
        self.MESSAGES_LIST = []
        self.ai: AIService = ai
        self.tools = tools

        self.metadata = None
        self.story = None
        self.image = None

    async def flow(self, prompt: str, META_PROMPT: str):
        try:
            messages = [
                {"role": "system", "content": META_PROMPT},
                {
                    "role": "user",
                    "content": f"{prompt}",
                },
            ]
            self.MESSAGES_LIST.extend(messages)

            while True:
                print("STARTING AGENT")
                chat_completion = self.ai.AI(self.MESSAGES_LIST, self.tools)
                response_message = chat_completion.choices[0].message

                self.MESSAGES_LIST.append(response_message.model_dump())
                print(f"MAIN chat output: {response_message}")

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
                            agent_args = []

                            tool_function = globals()[function_name]

                            tool_result, tool_chat_completion = await tool_function(
                                *agent_args, **function_args
                            )

                            if hasattr(tool_result, "content"):
                                content = tool_result.content
                                if function_name == "story_writer_tool":
                                    self.story = content

                                if function_name == "story_outline_planner_tool":
                                    self.metadata = json.loads(content)

                                self.MESSAGES_LIST.append(
                                    {
                                        "role": "tool",
                                        "tool_name": function_name,
                                        "tool_call_id": tool_call.id,
                                        "content": content,
                                    }
                                )
                            else:
                                if function_name == "image_generation_tool":
                                    print(f"IMAGE OUTPUT")
                                    print(tool_result)
                                    self.image = tool_result
                                self.MESSAGES_LIST.append(
                                    {
                                        "role": "tool",
                                        "tool_name": function_name,
                                        "tool_call_id": tool_call.id,
                                        "content": tool_result,
                                    }
                                )

                    except Exception as e:
                        print("got an exception while invoking tool", e)
                        # maybe handle these exception by tools itself?

                else:
                    return StoryResult(
                        story=self.story, metadata=self.metadata, image=self.image
                    )

        except openai.APIConnectionError as e:
            print(f"Network connectivity issue: {e}")
        except openai.RateLimitError as e:
            print(f"Rate limits hit or out of funds: {e}")
        except openai.APIStatusError as e:
            print(f"HTTP Error received (Status: {e.status_code}): {e.response}")
