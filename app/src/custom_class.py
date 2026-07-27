from dataclasses import dataclass
from typing import Optional


@dataclass
class StoryResult:
    metadata: dict
    story: str
    image: Optional[dict] = None
