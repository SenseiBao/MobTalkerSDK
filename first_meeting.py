from vn_dialogue import Dialogue
from characterBase import Character

vn = Dialogue()

def firstMeeting():
    c = Character(
        id="cupa",
        name = "Cupa",
        description = "A creeper girl???",
        thoughts= "Unknown",
        outfit = "default",
        states = None,
        maxhealth = 40,
        traits = None
    )
    p = "Player"
    
    vn.setVar("aff",0)
    vn.setVar("gamemode","None for now")

    vn.initialize()
    vn.start()
    vn.label("start")
    vn.show(c,"normal")
    vn.say("???","Hmm?")
    vn.say(None,"The girl standing before you was strange. She looks like a human wearing a creeper hoodie, is she lost?")
    vn.say("???","Oh, a player, hey")
    vn.choice({
        "hi": "Hi?",
        "who": "Who are you?",
        "engarde": "EN GARDE!!!"
    })

    vn.label("hi")
    vn.addVar("aff", 5)
    vn.show(c,"happy")
    vn.say("???","Hi! Didn't expect to meet you, ever...")
    vn.say(p,"You know me?")
    vn.show(c,"normal")
    vn.say("???","Oh for sure! You're 'The Player")
    vn.say(p,"Is that a big deal?")
    vn.show(c,"happy")
    vn.say("???","Is it a big deal for a creeper to look like a chick?")
    vn.jumpTo("who")

    vn.label("who")
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
    vn.condMoreThan("aff",3,[
        vn.show(c,"angry"),
        vn.say(c,"It's Cupa, by the way, ugh... The nerve..."),
        vn.jumpTo("gunpowder")
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
    vn.modVar("gamemode",vn.getGamemode())
    vn.condSame("gamemode","hardcore",[
        vn.show(c,"scared"),
        vn.say(c,"What the hell?!"),
        vn.say(c,"You're not supposed to play this mod on Hardcore!"),
        vn.show(c,"angry"),
        vn.say(c,"Screw it, I'm sending you back to World Creation, the hard way!")
    ])
    vn.say(p,"What does that have anything to do with us fighting?")
    vn.say(c,"It means I respawn after death")
    vn.say(c, "Anyway, let's duke it out! I think I got a few gunpowders in my pocket~")
    vn.finish()

    vn.label("gunpowder")
    vn.show(c,"normal")
    vn.say(c,"Hmm... You know what? You're not that bad a person")
    vn.givePlayer("minecraft:gunpowder",6)
    vn.show(c,"happy")
    vn.say(c,"Pop off stranger!")
    vn.finish()

    return vn.dialogueDict


