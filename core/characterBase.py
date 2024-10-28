from dataclasses import dataclass

@dataclass
class Character:
    id:str|None=None
    name: str|None = None
    description: str|None = None
    thoughts:str|None = None
    outfit: str|None = "default"
    states: list|None = None
    maxhealth: int = 40
    traits: list|None = None

    affection: int = 0
    # It's possible to add more stuff here~