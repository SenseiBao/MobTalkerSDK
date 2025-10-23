from core.modules import VisualNovelModule
from core.compiler import compile
from characters import Andr

vn = VisualNovelModule()
a = Andr
storyName = "andr"  # Lowercase is convention

def story():
    vn.start()
    vn.setGlobal("andr_affection", 0)  # Global - Cupa can access this
    vn.setVar("andr_local", 0)         # Local - Only Andr sees this
    
    vn.label("start")
    vn.show(a, "happy")
    vn.say(a, "Hey there!")
    vn.finish()
    
    return vn.dialogueDict

def main():
    compile(storyname=storyName, script=story())

if __name__ == "__main__":
    main()