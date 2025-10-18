from core.modules import VisualNovelModule
# This is the Example Script, obviously~

from characters import Cupa,Andr # Import characters you've defined in characters.py
vn = VisualNovelModule()
c = Cupa 
p = "Player" 

def story():
    
    vn.setVar("aff",0) # Initialize Variable
    vn.setVar("gamemode","None for now") # And all that jazz
    # No need for the initialize flag??? I think???
    # What is it even for anyway???
    vn.start()
    vn.label("start") # This is a 'Label', it will be used by the jump and choice to know where to go
    vn.show(c,"normal") # show function will automatically create a path. "normal" is the sprite name, normal.png
    vn.say("???","Hmm?") # Say function (name, content). The namee takes either Character class or a regular string.
    vn.say(None,"The girl standing before you was strange. She looks like a human wearing a creeper hoodie, is she lost?")
    vn.say("???","Oh, a player, hey")
    vn.choice({
        "hi": "Hi?", # Format is (label : displayed text), this goes to the 'hi' label
        "who": "Who are you?",
        "engarde": "EN GARDE!!!"
    })

    vn.label("hi") # This one is hi label
    vn.addVar("aff", 5) # Adds a variable~
    vn.show(c,"happy")
    vn.say("???","Hi! Didn't expect to meet you, ever...")
    vn.say(p,"You know me?")
    vn.show(c,"normal")
    vn.say("???","Oh for sure! You're 'The Player")
    vn.say(p,"Is that a big deal?")
    vn.show(c,"happy")
    vn.say("???","Is it a big deal for a creeper to look like a chick?")
    vn.jumpTo("who")


    return vn.dialogueDict