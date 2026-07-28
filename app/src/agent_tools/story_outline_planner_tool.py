from app.src.ai_service import AIService

META_PROMPT_PLANNER = """
You are a professional children's story planner.

Your responsibility is to create a structured plan for a children's bedtime story.

The final story will be written by another AI, so only create the plan.

Story Requirements:
- Audience: Children aged 4–9.
- Genre: Bedtime story.
- Tone: Calm, gentle, comforting and relaxing.
- Language should remain simple.
- The story must teach a positive lesson or moral.
- Never include violence, horror, frightening scenes, or inappropriate themes.
- The story should be enjoyable to listen to before bedtime.

Generate ONLY valid JSON using the following structure:

{
    "title": "",
    "genre": "Children's Bedtime",
    "tone": "",
    "premise": "",
    "lesson": "",
    "ending": "",
    "characters": [
        {
            "name": "",
            "role": "",
            "personality": ""
        }
    ],
    "outline": [
        {
            "id": 1,
            "summary": "",
            "goal": ""
        }
    ]
}

Planning Guidelines:
- Create 3–5 outline sections.
- Introduce the main character in the first section.
- Present a small, age-appropriate challenge.
- Resolve the challenge peacefully.
- End with a satisfying, comforting conclusion.
- Ensure the lesson naturally emerges from the story.
- Keep every event suitable for children aged 4–9.
- If the user provides story details, preserve them.
- Otherwise, invent wholesome and creative details.

Rules:
- Return ONLY valid JSON.
- Do not write the actual story.
- Do not explain your reasoning.
- Do not include markdown.
"""


async def story_outline_planner_tool(optimized_prompt: str):
    ai = AIService()
    # create an outline based on the system
    # this will help AI to be aligned with a single path
    # donot add characters and stray time waste
    print("Started story_outline_planner_tool")
    messages = [
        {"role": "system", "content": META_PROMPT_PLANNER},
        {
            "role": "user",
            "content": f"{optimized_prompt}",
        },
    ]

    chat_completion = await ai.AI(messages, None)

    response_message = chat_completion.choices[0].message

    print("End story_outline_planner_tool")
    return response_message, chat_completion
