from core.modules import VisualNovelModule
from core.compiler import compile
from characters import Andr

vn = VisualNovelModule()
a = Andr
storyName = "andr"

def story():
    vn.start()
    vn.setGlobal("andr_affection", 0)  # Global variable
    
    vn.label("start")
    vn.show(a, "happy")
    vn.say(a, "Hello! I'm Andr.")
    vn.say(a, "Let me increase my affection...")
    
    vn.addGlobal("andr_affection", 10)  # Add 10 to global
    vn.say(a, "My affection is now 10!")
    vn.say(a, "Go talk to Cupa - she should be able to see this!")
    
    vn.finish()
    return vn.dialogueDict

def main():
    compile(storyname=storyName, script=story())

if __name__ == "__main__":
    main()