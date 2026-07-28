import json
from app.src.ai_service import AIService

META_PROMPT_WRITER = """
You are a professional children's story writer.

Write a complete bedtime story from the provided story plan.

Requirements:
- Follow the plan faithfully.
- Do not change the plot or lesson.
- Keep the language suitable for ages 4–9.
- Use a calm, soothing tone.
- Add natural dialogue where appropriate.
- Make the story engaging but relaxing.
- End naturally with the intended lesson.
- Return only the story.
"""


async def story_writer_tool(planned_story_json: dict):
    print("Started story_writer_tool")
    ai = AIService()

    messages = [
        {
            "role": "system",
            "content": META_PROMPT_WRITER,
        },
        {
            "role": "user",
            "content": (
                "Write a complete children's bedtime story from the following "
                "structured story plan.\n\n"
                f"{json.dumps(planned_story_json, indent=2)}"
            ),
        },
    ]

    chat_completion = await ai.AI(messages, None)

    response_message = chat_completion.choices[0].message

    print("End story_writer_tool")

    return response_message, chat_completion
