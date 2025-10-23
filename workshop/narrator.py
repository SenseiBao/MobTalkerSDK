from core.modules import VisualNovelModule
from core.compiler import compile

vn = VisualNovelModule()
storyName = "narrator"
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
    vn.say(None, "Welcome to a world where mobs have gained consciousness...")
    vn.say(None, "They can now speak, feel, and interact with you.")
    vn.say(None, "Your choices will determine your relationships with them.")
    vn.say(None, "Good luck, adventurer.")
    
    # Mark as seen
    vn.modVarGlobal("world_intro_seen", 1)
    
    vn.finish()
    return vn.dialogueDict

def main():
    compile(storyname=storyName, script=story())

if __name__ == "__main__":
    main()