import json
from app.src.ai_service import AIService

META_PROMPT_EXTRACTOR = """
You are a professional prompt engineer.
Your job is to extract some details from the information below.
These details are from a bed time story. It might be the actual story as well.
- You need to process details or story such that you return an optimized prompt for image generation.
- The image generation actual requires a minimal prompt to create image.
- Don't add much details to prompt as currently I only need a minimal image as scenery in story.
"""


async def story_scene_exactor_tool(created_story: str):
    print("Started story_scene_exactor_tool")
    ai = AIService()

    messages = [
        {
            "role": "system",
            "content": META_PROMPT_EXTRACTOR,
        },
        {
            "role": "user",
            "content": (
                "Extract a scene from the following story and generate a prompt for making an image.\n\n"
                f"Story: {created_story}"
            ),
        },
    ]

    chat_completion = ai.AI(messages, None)
    response_message = chat_completion.choices[0].message

    # Ensure the content is directive
    if response_message.content:
        response_message.content = f"Extracted Image Prompt: {response_message.content}\n\nNow, use the image_generation_tool with this prompt to generate the story illustration."

    print("End story_scene_exactor_tool")

    return response_message, chat_completion
