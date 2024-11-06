from core.modules import VisualNovelModule
# This is the Example Script, obviously~

from characters import Cupa,Andr # Import characters you've defined in characters.py
vn = VisualNovelModule()
c = Cupa 
p = "Player" 

# By the way, if you're wondering how it works
# It's just gonna combine all of the script into one big script
# So jumpTo and label works across file
# Because everything will be in one big file
def story():
    vn.label("who") #this one is who label
    vn.show(c,"normal")
    vn.say(p,"Who are you?")
    vn.say("???","Who am I? A creeper~")
    vn.choice({
        "introduction": "Ask her name",
        "ask_item":"Ask for Gunpowder"
    })

    vn.label("introduction")
    vn.say(p,"What should I call you?")
    vn.addVar("aff", 5)
    vn.show(c,"shy")
    vn.say("???","Aww, a player asked my name instead of asking for gunpowder")
    vn.say(c,"But you can call me Cupa~")
    vn.choice({
        "gunpowder": "Great, Nice to meet you, can we end this peacefully?",
        "engarde": "So... since you're a creeper... does that mean we're gonna duke it out?"
    })

    vn.label("ask_item")
    vn.say(c,"It's Cupa, by the way, ugh... The nerve..."),
    vn.condMoreThan("aff",3,[ # Condition is: (variable name to check, value to check against, the list of action)
        vn.show(c,"angry",True),# Unfortunately, yes, condMoreThan, condLessThan, etc is mandatory. Can't use <>= operation directly
        vn.jumpTo("gunpowder",True)
    ])
    vn.show(c,"angry")
    vn.say(c,"I don't know, do you got diamonds on you?")
    vn.choice({
        "yes": "Yes...",
        "no": "No..."
    })

    return vn.dialogueDict
