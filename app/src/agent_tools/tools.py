tools = [
    {
        "type": "function",
        "function": {
            "name": "PromptOptimizerTool",
            "description": "Optimize user input prompt to a level it creates stunning storyline",
            "parameters": {
                "type": "object",
                "properties": {"prompt": {"type": "string"}},
                "required": ["prompt"],
            },
        },
    }
]
