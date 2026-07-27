tools = [
    {
        "type": "function",
        "function": {
            "name": "story_prompt_optimizer_tool",
            "description": "Optimize user input prompt to a level it creates stunning storyline. Not required if input prompt is valid and meaningful for a story",
            "parameters": {
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "User input prompt to optimize",
                    }
                },
                "required": ["prompt"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "story_outline_planner_tool",
            "description": "Work on storyline, scenes and characters for the story. It outputs a formatted JSON for storyline planning.",
            "parameters": {
                "type": "object",
                "properties": {
                    "optimized_prompt": {
                        "type": "string",
                        "description": "Optimized prompt to draft a storyline",
                    }
                },
                "required": ["optimized_prompt"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "story_writer_tool",
            "description": "Writes the final children's story from the structured story plan.",
            "parameters": {
                "type": "object",
                "properties": {
                    "planned_story_json": {
                        "type": "object",
                        "description": "Structured story plan produced by the story planner.",
                        "properties": {
                            "title": {"type": "string"},
                            "characters": {
                                "type": "array",
                                "items": {"type": "string"},
                            },
                            "setting": {"type": "string"},
                            "plot": {"type": "array", "items": {"type": "string"}},
                            "lesson": {"type": "string"},
                            "tone": {"type": "string"},
                        },
                        "required": ["characters", "setting", "plot", "lesson"],
                    }
                },
                "required": ["planned_story_json"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "story_scene_exactor_tool",
            "description": "Extracts and curates a prompt for image generation from the final created story",
            "parameters": {
                "type": "object",
                "properties": {
                    "created_story": {
                        "type": "string",
                        "description": "Finalized bed time story.",
                    }
                },
                "required": ["created_story"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "image_generation_tool",
            "description": "Generates and stores an image related to story using input prompt",
            "parameters": {
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "Prompt to generate images based on.",
                    }
                },
                "required": ["prompt"],
            },
        },
    },
]
