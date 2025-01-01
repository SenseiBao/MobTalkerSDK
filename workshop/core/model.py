from dataclasses import dataclass
# Feel free to expand these base classes~

@dataclass
class Character:
    id:str|None=None
    name: str|None = None
    description: str|None = None
    thoughts:str|None = None
    spriteFolder:list|None = None
    outfit: list|None = None
    outfit: str|None = "default"
    states: list|None = None
    maxhealth: int = 40
    traits: list|None = None
