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
        self.dialogueDict.append({
            "type":"meta",
            "action":"start"
        })

    def say(self,character,content):
        name = ""
        if isinstance(character, char.Character):
            name = character.name
        elif(character  == None):
            name = ""
        else:
            name = character
        print("Compiling: "+content)

        self.dialogueDict.append({
            "type":"script",
            "action":"say",
            "label":name,
            "content":content
        })

    def show(self,character,sprite):
        if isinstance(character, char.Character): 
            sprite = character.id+"/"+character.outfit+"/"+sprite+".png"
            print("Compiling: "+sprite)
            self.dialogueDict.append( {
                "type":"script",
                "action":"show",
                "sprite":sprite
            })
        else:
            pass
        
        
    def choice(self,choice: dict):
        print(choice)
        self.dialogueDict.append({
            "type":"script",
            "action":"choice",
            "choice":choice
        })
        

    def label(self,labelName:str):
        print("Compiling: "+labelName)
        self.dialogueDict.append( {
            "type":"meta",
            "label":labelName
        })

    def jumpTo(self,labelName:str):
        print("Compiling:" + labelName)
        self.dialogueDict.append( {
            "type":"script",
            "action":"jump",
            "label": labelName
        })

    def finish(self):
        print("Compiling A Finish Line")
        self.dialogueDict.append({
            "type":"action",
            "action": "finish_dialogue"
        })
        

    def setVar(self,varName:str):
        print("Compiling: "+varName)
        self.dialogueDict.append({
            "type":"meta",
            "action": "create_var", 
            "var": varName
        })

    # You can use (-) instead of subVar
    def addVar(self,varName:str, addAmount:int):
        print("Compiling: "+varName)

        self.dialogueDict.append ({
            "type":"script",
            "action": "increment_var", 
            "var": varName, 
            "amount": addAmount
            })

    def subVar(self,varName:str, subAmount:int):
        print("Compiling: "+varName)
        self.dialogueDict.append({
            "type":"script",
            "action": "subtract_var", 
            "var": varName, 
            "amount": subAmount
        })

    def modVar(self,varName:str, value:any):
        print("Compiling: "+varName)

        self.dialogueDict.append({
            "type":"script",
            "action": "modify_var", 
            "var": varName, 
            "value": value
        })

    def condSame(self,varName: str, equalValue, actions: list):
        print("Compiling: "+varName)
        self.dialogueDict.append({
            "type":"script",
            "condition": "equal",
            "var": varName,
            "value": equalValue,
            "actions": actions
        })

    def condNotSame(self,varName: str, equalValue, actions: list):
        self.dialogueDict.append({
            "type":"script",
            "condition": "not_equal",
            "var": varName,
            "value": equalValue,
            "actions": actions
        })

    def condLessThan(self,varName:str, lessThanValue, actions: list):
        self.dialogueDict.append({
            "type":"script",
            "condition": "less_than",
            "var": varName,
            "value": lessThanValue,
            "actions": actions
        })

    def condMoreThan(self,varName:str, moreThanValue, actions: list):  
        self.dialogueDict.append( {
            "type":"script",
            "condition": "greater_than",
            "var": varName,
            "value": moreThanValue,
            "actions": actions  
        })

    def givePlayer(self,itemId:str,amount:int):
        self.dialogueDict.append({
            "type":"script",
            "action":"give_player",
            "item_id":itemId,
            "amount":amount
        })

    def getGamemode(self):
        self.dialogueDict.append({
            "type":"script",
            "action":"get_gamemode"
        })

    def customCommand(self,minecraftCommmand:str):
        self.dialogueDict.append({
            "type":"script",
            "action":"custom_commmand",
            "command":minecraftCommmand
        })

