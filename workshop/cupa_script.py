from core.modules import VisualNovelModule
from core.compiler import compile
from characters import Cupa

vn = VisualNovelModule()
c = Cupa
storyName = "cupa"

def story():
    vn.start()
    vn.setGlobal("andr_affection", 0)  # Initialize same global variable
    
    vn.label("start")
    vn.show(c, "normal")
    vn.say(c, "Hey! I'm Cupa.")
    vn.say(c, "Let me check Andr's affection...")
    
    # Check if Andr's affection is high
    vn.condGlobalMoreThan("andr_affection", 5, [
        vn.show(c, "happy", True),
        vn.say(c, "Wow! You really like Andr! Her affection is above 5!", True)
    ])
    
    # Check if Andr's affection is still 0
    vn.condGlobalSame("andr_affection", 0, [
        vn.show(c, "normal", True),
        vn.say(c, "Hmm, looks like you haven't talked to Andr yet.", True),
        vn.say(c, "Her affection is still 0.", True)
    ])
    
    vn.finish()
    return vn.dialogueDict

def main():
    compile(storyname=storyName, script=story())

if __name__ == "__main__":
    main()