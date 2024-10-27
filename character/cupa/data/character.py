from dataclasses import dataclass

@dataclass
class Character:
    name: str|None = None
    spriteFolder:list|None = None
    outfit: list|None = None
    states: list|None = None
    maxhealth: int = 40
    traits: list|None = None

    affection: int = 0
    # It's possible to add more stuff here~