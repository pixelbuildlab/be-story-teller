import click
import asyncio
from app.src.ai_helper import openai_chat_completion

VERSION = 0.1


@click.command()
@click.version_option(VERSION)
@click.argument("prompt")
def main(prompt: str):
    asyncio.run(openai_chat_completion(prompt))
    pass


if __name__ == "__main__":
    main()
