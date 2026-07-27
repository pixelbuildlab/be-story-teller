from uuid import uuid4 as uuid
from pathlib import Path
from app.src.ai_service import AIService

META_PROMPT_FILE_WRITER = """
You will be given a story in almost md format and image for presenting the story.
- You need to just work on story formatting for md file only.
- Never rewrite story or improve any thing.
- Your main purpose is to return a formatted story with image embedded in md format.
- Return formatted markdown
- use <br> tag for newline.
- file will be available locally so need to work on adding as a pic only.
"""


async def markdown_writer_tool(created_story: str, generated_image_path: str):
    print("Started markdown_writer_tool")
    ai = AIService()

    messages = [
        {
            "role": "system",
            "content": META_PROMPT_FILE_WRITER,
        },
        {
            "role": "user",
            "content": (
                "Story:" f"{created_story}" f"image path: {generated_image_path}"
            ),
        },
    ]

    chat_completion = ai.AI(messages, None)

    response_message = chat_completion.choices[0].message

    formatted_story_markdown = response_message.content

    story_id = uuid()
    story_path = Path("outputs") / f"story_{story_id}.md"

    with open(story_path, "w", encoding="utf-8") as f:
        f.write(formatted_story_markdown)

    print("End markdown_writer_tool")
    return response_message, chat_completion
