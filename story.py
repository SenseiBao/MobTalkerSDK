from core.modules import VisualNovelModule
from core.compiler import compile
# This is the Example Script, obviously~

from characters import Cupa,Andr # Import characters you've defined in characters.py
vn = VisualNovelModule()
c = Cupa 
p = "Player" 
storyName = "First Meeting" # This will be the name of the Json File

def story():
    
    # Come on now, it's intuitive enough~
    vn.setVar("aff",0)
    vn.setVar("gamemode","None for now")

    vn.initialize(storyName)
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

    vn.label("yes")
    vn.say(c,"I was being rhetoric")
    vn.say(p,"I mean... I can lend you some...")
    vn.jumpTo("engarde")

    vn.label("no")
    vn.say(c,"I was being rhetoric")
    vn.say(p,"I mean...")
    vn.jumpTo("engarde")

    vn.label("engarde")
    vn.show(c,"normal")
    vn.say(c,"Since you're asking for a fight, why don't we?")
    vn.say(c,"You're not on hardcore, right?")
    vn.modVar("gamemode",vn.getGamemode())# modvar just changes the variable
    vn.condSame("gamemode","hardcore",[ # conditional to check if "gamemode" is "hardcore"
        vn.show(c,"scared",True), # Fuck, I hate this part...
        vn.say(c,"What the hell?!",True), # So basically, you have to add 'True' for nested stuff
        vn.say(c,"You're not supposed to play this mod on Hardcore!",True), # Don't ask what it is
        vn.show(c,"angry",True), # You just have to add it, okay?
        vn.say(c,"Screw it, I'm sending you back to World Creation, the hard way!",True) # Nothing I can do about it
    ]) # For now
    vn.say(p,"What does that have anything to do with us fighting?")
    vn.say(c,"It means I respawn after death")
    vn.say(c, "Anyway, let's duke it out! I think I got a few gunpowders in my pocket~")
    vn.finish()

    vn.label("gunpowder")
    vn.say(c,"Hmm... You know what? You're not that bad a person")
    vn.givePlayer("minecraft:gunpowder",6) # Minecraft specific command (might put this in another class)
    vn.say(c,"You know what to do with it~")
    vn.show(c,"happy")
    vn.say(c,"Pop off stranger!")
    vn.finish() # This ends the game

    return vn.dialogueDict


def main():compile(storyname=storyName,script=story()) # Yeah, just run this file :v

if __name__ == "__main__":
    main() 