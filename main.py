import click
import asyncio
from app.src.ai_service import AIService
from app.src.agent_service import AgentService
from app.src.prompt import SYSTEM_META_PROMPT
from app.src.agent_tools.tools import tools

VERSION = 0.1


@click.command()
@click.version_option(VERSION)
@click.argument("prompt")
def main(prompt: str):
    ai = AIService()
    agent = AgentService(ai, tools)
    asyncio.run(agent.flow(prompt, SYSTEM_META_PROMPT))


if __name__ == "__main__":
    main()
