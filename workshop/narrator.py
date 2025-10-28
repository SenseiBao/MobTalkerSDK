from core.modules import VisualNovelModule
from core.compiler import compile

vn = VisualNovelModule()
storyName = "narrator"
player = "You"

def start():
    # Show a line of dialogue
    vn.show_dialogue("Hello, this is the narrator.")
    
    # End the script
    vn.end()
def story():
    vn.start()
    vn.setGlobal("world_intro_seen", 0)  # Track if intro was seen
    
    vn.label("start")
    
    # Check if already seen
    vn.condSameGlobal("world_intro_seen", 1, [
        vn.finish(True)  # Skip if already seen
    ])
    
    # Opening cutscene
    #dark room, bright screen
    vn.say(None, "11:58 PM")
    vn.say(player, "*Yawn*")
    vn.say(player, "I'm so tired.")
    vn.say(player, "*Sigh*")
    vn.say(None, "Your eyes feel heavy and you can no longer think straight.")
    vn.say(None, "Your boss has had you working overtime all week to meet your upcoming deadline. It's taken a brutal toll on your health.")
    vn.say(player, "I need to find a USB drive to put my Powerpoint presentation on for tomorrow. Then I'll finally be done!")
    vn.say(None, "You feel around your desk in your dimly lit room, until you find it.")
    vn.say(player, "Okay, put it in, and...download my Powerpoint, then...")
    vn.say(player, "...")
    vn.say(None, "You've kept this USB for over 10 years, using it whenever you needed to. But this time you see a strange folder, which distracts you.")
    vn.say(None, "My World")
    vn.say(None, "On a whim, you open it and see a directory full of content—folders and data files.")
    vn.say(player, "What's this? \"playerdata?\" \"advancements?\" Is this from a game?")
    vn.say(None, "You haven't played many games ever since you started working. These files were last edited...")
    vn.say(player, "...10 years ago.... I must've been in middle school or something. At that time... hm... I played a lot of Minecraft.")
    vn.say(None, "It would be smart to just make sure the Powerpoint was ready and then go to sleep. But something inside of you piques your curiosity.")
    vn.say(player, "If I'm already this sleep-deprived, a few less hours of sleep won't hurt. I think I should still have Minecraft somewhere.")
    vn.say(None, "You decide to open this ancient Minecraft world for the first time in a decade.")
    vn.say(player, "How do I do this again...?")
    vn.say(None, "It took a brief back and forth with ChatGPT, but you eventually figure out how to update your Minecraft launcher, transfer the world, and open it.")
    #sweden
    #minecraft menu
    vn.say(None, "The familiar menu greets you, like a long-lost friend whose face you never forgot.")
    vn.say(player, "Let's see how much I still remember.")
    vn.say(None, "You open the world and wait for it to load.")
    vn.say(None, " ")
    #loading screen
    vn.say(None, "The loading screen pauses for what feels like minutes.")
    vn.say(player, "Is it supposed to take this long?")
    vn.say(None, "Suddenly, without warning, the screen flashes white.")
    #white screen, flashbang sfx
    vn.say(player, "Shit.")
    
    # Mark as seen
    vn.modVarGlobal("world_intro_seen", 1)
    
    vn.finish()
    return vn.dialogueDict

def main():
    compile(storyname=storyName, script=story())

if __name__ == "__main__":
    main()