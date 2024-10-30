import characterBase as char

class Dialogue():

    def __init__(self):
        self.dialogueDict = []

    def initialize(self):
        self.dialogueDict.append({
            "type":"meta",
            "action":"initialize"
        })
    
    def start(self):
        result = {
            "type":"meta",
            "action":"start"
        }
        self.dialogueDict.append(result)
        return result

    def say(self,character,content,transition = False):
        name = ""
        if isinstance(character, char.Character):
            name = character.name
        elif(character  == None):
            name = ""
        else:
            name = character
        print("Compiling: "+content)
        result = {
            "type":"dialogue",
            "action":"say",
            "label":name,
            "content":content
        }
        if(transition==False):
            self.dialogueDict.append(result)
        return result

    def show(self,character,sprite,transition=False):
        if isinstance(character, char.Character): 
            sprite = character.id+"/"+character.outfit+"/"+sprite+".png"
            print("Compiling: "+sprite)
            result = {
                "type":"show_sprite",
                "action":"show",
                "sprite":sprite
            }
            if(transition==False):
                self.dialogueDict.append(result)
            return result
        else:
            pass
        
        
    def choice(self,choice: dict):
        print(choice)
        result = {
            "type":"choice",
            "action":"choice",
            "choice":[{"label": key, "display": value} for key, value in choice.items()]
        }
        self.dialogueDict.append(result)
        return result
        

    def label(self,labelName:str):
        print("Compiling: "+labelName)
        result = {
            "type":"label",
            "action" : "label",
            "label":labelName
        }
        self.dialogueDict.append(result)
        return result

    def jumpTo(self,labelName:str,transition=False):
        print("Compiling:" + labelName)
        result = {
            "type":"transition",
            "action":"jump",
            "label": labelName
        }
        if(transition==False):
            self.dialogueDict.append(result)
        return result

    def finish(self):
        print("Compiling A Finish Line")
        result = {
            "type":"finish_dialogue",
            "action": "finish_dialogue"
        }
        self.dialogueDict.append(result)
        return result
        

    def setVar(self,varName:str,init:any):
        print("Compiling: "+varName)
        result = {
            "type":"meta",
            "action": "create_var", 
            "var": varName,
            "init":init
        }
        self.dialogueDict.append(result)
        return result

    # You can use (-) instead of subVar
    def addVar(self,varName:str, addAmount:int):
        print("Compiling: "+varName)
        result = {
            "type":"modify_variable",
            "action": "increment_var", 
            "var": varName, 
            "value": addAmount
            }
        self.dialogueDict.append (result)
        return result

    def subVar(self,varName:str, subAmount:int):
        print("Compiling: "+varName)
        result = {
            "type":"modify_variable",
            "action": "subtract_var", 
            "var": varName, 
            "value": subAmount
        }
        self.dialogueDict.append(result)
        return result

    def modVar(self,varName:str, value:any):
        print("Compiling: "+varName)
        result = {
            "type":"modify_variable",
            "action": "modify_var", 
            "var": varName, 
            "value": value
        }
        self.dialogueDict.append(result)

    def condSame(self,varName: str, equalValue, actions):
        print("Compiling: "+varName)
        result = {
            "type":"conditional",
            "action":"conditional",
            "condition": "equal",
            "var": varName,
            "value": equalValue,
            "actions":actions
        }
        self.dialogueDict.append(result)
        return result

    def condNotSame(self,varName: str, equalValue, actions: list):
        print("Compiling: "+varName)
        result = {
            "type":"conditional",
            "action":"conditional",
            "condition": "not_equal",
            "var": varName,
            "value": equalValue,
            "actions": actions
        }
        self.dialogueDict.append(result)
        return result

    def condLessThan(self,varName:str, lessThanValue, actions: list):
        print("Compiling: "+varName)
        result = {
            "type":"conditional",
            "action":"conditional",
            "condition": "less_than",
            "var": varName,
            "value": lessThanValue,
            "actions": actions
        }
        self.dialogueDict.append(result)
        return result

    def condMoreThan(self,varName:str, moreThanValue, actions: list):  
        print("Compiling: "+varName)
        result = {
            "type":"conditional",
            "action":"conditional",
            "condition": "greater_than",
            "var": varName,
            "value": moreThanValue,
            "actions": actions
        }
        self.dialogueDict.append(result)
        return result

    def givePlayer(self,itemId:str,amount:int):
        result = {
            "type":"give_player",
            "action":"give_player",
            "item_id":itemId,
            "amount":amount
        }
        self.dialogueDict.append(result)
        return result

    def getGamemode(self,transition = True):
        result = {
            "type":"command",
            "action":"get_gamemode"
        }
        if(transition==False):
            self.dialogueDict.append(result)
        
        return result

    def customCommand(self,minecraftCommmand:str):
        result = {
            "type":"command",
            "action":"custom_commmand",
            "command":minecraftCommmand
        }
        self.dialogueDict.append(result)
        return result

