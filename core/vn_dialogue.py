from core import character as char

def say(character,content):
    name = ""
    if(character is char.Character):
        name = character.name
    else:
        name = character
    return None

def show(character,sprite):
    sprite = ""
    if(character is char.Character):
        sprite = character.spriteFolder
    else:
        sprite = sprite
    return sprite
    

def choice(choice):
    return None

def label(labelName:str):
    return None

def jumpTo(labelName:str):
    return None

def finish():
    return None

def setVar(varName:str):
    return None

# You can use (-) instead of subVar
def addVar(varName:str, addAmount:int):
    return None

def subVar(varName:str, subAmount:int): 
    return None

def modVar(varName:str, value:any):
    return None

def condSame(varName: str, equalValue, actions: list[callable]):
    return None

def condNotSame(varName: str, equalValue, actions: list[callable] ):
    return None

def condLessThan(varName:str, lessThanValue,actions: list[callable]):
    return None

def condMoreThan(varName:str, moreThanValue,actions: list[callable]):
    return None