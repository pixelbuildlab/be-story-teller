from app.src.ai_service import AIService

META_PROMPT_OPTIMIZER = """
You are an expert prompt optimizer for children's story generation.

Your task is to transform short or incomplete user requests into rich, detailed prompts for a story-writing AI.

Rules:
- Preserve the user's original intent.
- Add reasonable assumptions when details are missing.
- Specify:
  - protagonist
  - setting
  - conflict
  - tone
  - target age
  - ending
  - approximate length
- Do not write the story.
- Return ONLY the optimized prompt.
"""


async def story_prompt_optimizer_tool(prompt: str):
    ai = AIService()
    print("starting story_prompt_optimizer_tool")
    messages = [
        {"role": "system", "content": META_PROMPT_OPTIMIZER},
        {
            "role": "user",
            "content": f"{prompt}",
        },
    ]

    chat_completion = await ai.AI(messages, None)

    response_message = chat_completion.choices[0].message

    print("story_prompt_optimizer_tool called")
    return response_message, chat_completion
