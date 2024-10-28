import characterBase as char

def say(character,content):
    name = ""
    if(character is char.Character):
        name = character.name
    elif(character  == None):
        name = ""
    else:
        name = character
    print("Compiling: "+content)
    return {
        "action":"say",
        "label":name,
        "content":content
    }

def show(character,sprite):
    sprite = ""
    if(character is char.Character):
        sprite = character.id+"/"+character.outfit+"/"+sprite+".png"
        print("Compiling: "+sprite)
        return {
            "action":"show",
            "sprite":sprite
        }
    else:
        pass
    
    
def choice(choice: dict):
    print(choice)
    return {
        "menu":"choice",
        "choice":choice
    }

def label(labelName:str):
    print("Compiling: "+labelName)
    return {
        "label":labelName
    }

def jumpTo(labelName:str):
    print("Compiling:" + labelName)
    return {
        "action":"jump",
        "label": labelName
    }

def finish():
    print("Compiling A Finish Line")
    return {"action": "finish_dialogue"}

def setVar(varName:str):
    print("Compiling: "+varName)
    return {"action": "create_var", "var": varName}

# You can use (-) instead of subVar
def addVar(varName:str, addAmount:int):
    print("Compiling: "+varName)
    return {"action": "increment_var", "var": varName, "amount": addAmount}

def subVar(varName:str, subAmount:int):
    print("Compiling: "+varName)
    return {"action": "subtract_var", "var": varName, "amount": subAmount}

def modVar(varName:str, value:any):
    print("Compiling: "+varName)
    return {"action": "modify_var", "var": varName, "value": value}

def condSame(varName: str, equalValue, actions: list[callable]):
    print("Compiling: "+varName)
    return {
        "condition": "equal",
        "var": varName,
        "value": equalValue,
        "actions": [action() for action in actions]
    }

def condNotSame(varName: str, equalValue, actions: list[callable]):
    return {
        "condition": "not_equal",
        "var": varName,
        "value": equalValue,
        "actions": [action() for action in actions]
    }

def condLessThan(varName:str, lessThanValue, actions: list[callable]):
    return {
        "condition": "less_than",
        "var": varName,
        "value": lessThanValue,
        "actions": [action() for action in actions]
    }

def condMoreThan(varName:str, moreThanValue, actions: list):  # Remove callable annotation
    return {
        "condition": "greater_than",
        "var": varName,
        "value": moreThanValue,
        "actions": actions  # Remove the list comprehension
    }