# User:Create a story about a tiny dinosaur.↓Thought:Need better prompt.↓PromptOptimizerTool↓
# Thought:
# Need story outline.↓StoryPlannerTool↓Thought:Need story.↓StoryWriterTool
# ↓Thought:Need illustrations.↓SceneExtractionTool↓
# ImageGenerationTool↓Thought:Need final book.↓MarkdownWriterTool↓PDFExporterTool↓Done

# ####################################
# Begin optimizer
# ####################################

# inject into local prompt
# PromptOptimizerTool
# tools = [
#     {
#         "type": "function",
#         "function": {
#             "name": "PromptOptimizerTool",
#             "description": "Optimize user input prompt to a level it creates stunning storyline",
#             "parameters": {
#                 "type": "object",
#                 "properties": {"prompt": {"type": "string"}},
#                 "required": ["prompt"],
#             },
#         },
#     }
# ]


async def OptimizePromptTool(prompt: str):
    return f"Optimized prompt: {prompt}"


# built an outline
# StoryPlannerTool done


# Ollama calls
# StoryWriterTool done

# extract data for image generation
# SceneExtractionTool

# pass data for image creation
# ImageGenerationTool


# MarkdownWriterTool


# PDFExporterTool
