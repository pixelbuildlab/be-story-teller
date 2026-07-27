from openai import OpenAI
from typing import Optional
from app.src.config import API_KEY, API_URL, HEADERS, MODEL


class AIService:
    def __init__(self):
        self.client = OpenAI(
            base_url=API_URL,
            api_key=API_KEY,
            default_headers=HEADERS,
        )

    def AI(self, messages: list, tools: Optional[list] | None):
        chat_completion = self.client.chat.completions.create(
            model=MODEL, messages=messages, tools=tools
        )
        return chat_completion
