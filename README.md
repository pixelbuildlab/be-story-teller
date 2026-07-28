# Bedtime Story Agent

An agentic AI application that creates illustrated bedtime stories using LLM function calling.

![Screenshot](screenshot/image.png)

## Features

- Optimize story prompts
- Generate story outline
- Write complete children's stories
- Extract the best scene for illustration
- Generate an image
- Lightweight front-end to interact to agent
- Front-end to view generated content and illustration
- Printing generated stories prints only generated content


## Installation

Clone the repository and install the dependencies.

```bash
uv sync
```

## Configuration

Copy the example environment file.

```bash
cp .env.example .env
cp .env.example .env.docker
```

Update the values inside `.env` and `.env.docker`.

## Run

```bash
docker-compose up --build -V
```

OR

```bash
uv run fastapi dev
```

Open http://localhost:8000/

## Output

Generated stories illustrations are saved inside the `outputs/` directory. Stories as served through API

## Requirements

- Python 3.11+
- OpenAI-compatible API
- Docker, Docker compose (Optional)
- Ollama (optional)