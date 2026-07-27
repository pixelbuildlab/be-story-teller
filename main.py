from fastapi import FastAPI

from app.src.ai_service import AIService
from app.src.agent_service import AgentService
from app.src.prompt import SYSTEM_META_PROMPT
from app.src.agent_tools.tools import tools
from pydantic import BaseModel


class StoryRequest(BaseModel):
    prompt: str


VERSION = 0.1

app = FastAPI()

app.frontend("/", directory="app/static")
app.frontend("/images", directory="outputs")


ai = AIService()
agent = AgentService(ai, tools)


@app.post("/story")
async def create_story(req: StoryRequest):
    generated_stroy = await agent.flow(req.prompt, SYSTEM_META_PROMPT)
    return generated_stroy
