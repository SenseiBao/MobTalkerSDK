from dataclasses import dataclass

@dataclass
class Quest:
    character: str|None = None
    description:list|None = None
    requestitems:list|None = None # use minecraft id
    rewarditems:list|None = None
    affection: int = 0
    # It's possible to add more stuff here~