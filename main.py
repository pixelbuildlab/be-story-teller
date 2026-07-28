import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from app.src.ai_service import AIService
from app.src.agent_service import AgentService
from app.src.prompt import SYSTEM_META_PROMPT
from app.src.agent_tools.tools import tools
from app.src.web_socket_manager import ConnectionManager


class StoryRequest(BaseModel):
    prompt: str
    client_id: str


app = FastAPI()

app.frontend("/", directory="app/static")
app.frontend("/images", directory="outputs")


ai = AIService()
manager = ConnectionManager()
agent = AgentService(ai, tools, manager)


@app.post("/story")
async def create_story(req: StoryRequest):
    generated_stroy = await agent.flow(req.prompt, SYSTEM_META_PROMPT, req.client_id)
    return generated_stroy


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):

    await manager.connect(client_id, websocket)

    try:
        await asyncio.Event().wait()
    except WebSocketDisconnect:
        await manager.disconnect(client_id)

    finally:
        manager.disconnect(client_id)
