import requests
from pathlib import Path
from uuid import uuid4 as uuid
from app.src.config import WORKER_API_KEY, WORKER_API_URL


async def image_generation_tool(prompt: str):
    print("Started image_generation_tool")

    response = requests.post(
        WORKER_API_URL,
        json={
            "prompt": prompt,
            "model": "@cf/stabilityai/stable-diffusion-xl-base-1.0",
        },
        headers={"Authorization": f"Bearer {WORKER_API_KEY}"},
    )
    response.raise_for_status()
    if response.ok:
        image_id = uuid()
        image_path = Path("outputs") / f"{image_id}.png"
        print("Ending image_generation_tool")
        with open(image_path, "wb") as file:
            file.write(response.content)
            return {
                "path": f"/images/{image_id}.png",
                "metadata": "Image created for story success",
                "status": "Image has been generated",
            }, None
