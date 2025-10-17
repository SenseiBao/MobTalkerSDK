from core.modules import VisualNovelModule
from core.compiler import compile
from characters import Cupa

vn = VisualNovelModule()
c = Cupa
r = Rei
storyName = "rei"  # ← This becomes the filename

def story():
    vn.start()
    vn.setGlobal("rei_affection", 0)
    vn.setVar("cupa_affection", 0)
    
    vn.label("start")
    vn.show(r, "happy")
    vn.say(r, "Hey there!")
    vn.finish()
    
    return vn.dialogueDict

def main():
    compile(storyname=storyName, script=story())

if __name__ == "__main__":
    main()
