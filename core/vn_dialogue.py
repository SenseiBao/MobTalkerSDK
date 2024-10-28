from core import character as char

def say(character,content):
    name = ""
    if(character is char.Character):
        name = character.name
    else:
        name = character
    return {
        "action":"say",
        "label":name,
        "content":content
    }

def show(character,sprite):
    sprite = ""
    if(character is char.Character):
        sprite = character.spriteFolder+"/"+sprite+".png"
    else:
        sprite = sprite
    return {
        "action":"show",
        "sprite":sprite
    }
    
def choice(choice: dict):
    return {
        "menu":"choice",
        "choice":choice
    }

def label(labelName:str):
    return {
        "label":labelName
    }

def jumpTo(labelName:str):
    return {
        "action":"jump",
        "label": labelName
    }

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