from openai import OpenAI
from requests.exceptions import HTTPError
from app.src.agent_tools.tools import tools
from app.src.config import (
    OPEN_ROUTER_API_KEY,
    OPEN_ROUTER_COMPLETION_MODEL,
)

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=OPEN_ROUTER_API_KEY)


async def openai_chat_completion(prompt: str):
    try:
        chat_completion = client.chat.completions.create(
            model=OPEN_ROUTER_COMPLETION_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": "I need to optimize a prompt?",
                }
            ],
            tools=tools,
        )

        output = chat_completion.choices[0].message.content

        if not output:
            raise ValueError("No response returned from model")
        print(output)
        return output

    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
