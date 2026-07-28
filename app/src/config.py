from dotenv import load_dotenv
import os

load_dotenv()

USE_OLLAMA = os.getenv("USE_OLLAMA")
OPEN_ROUTER_API_KEY = os.getenv("OPEN_ROUTER_API_KEY")
OPEN_ROUTER_COMPLETION_MODEL = "nvidia/nemotron-3-ultra-550b-a55b:free"
OPEN_ROUTER_URL = "https://openrouter.ai/api/v1"

OLLAMA_COMPLETION_MODEL = (
    "qwen3:latest"
    # "gemma4:e4b"
)


OLLAMA_API_URL = os.getenv("OLLAMA_API_URL")
OLLAMA_API_KEY = "ollama"


OPEN_ROUTER_HEADERS = {
    "HTTP-Referer": "https://github.com/pixelbuildlab/be-story-teller",
    "X-OpenRouter-Title": "Be story teller - Agentic way to stories",
}

WORKER_API_KEY = os.getenv("WORKER_API_KEY")
WORKER_API_URL = os.getenv("WORKER_API_URL")


MODEL = OLLAMA_COMPLETION_MODEL if USE_OLLAMA else OPEN_ROUTER_COMPLETION_MODEL
API_URL = OLLAMA_API_URL if USE_OLLAMA else OPEN_ROUTER_URL
API_KEY = OLLAMA_API_KEY if USE_OLLAMA else OPEN_ROUTER_API_KEY
HEADERS = None if USE_OLLAMA else OPEN_ROUTER_HEADERS
