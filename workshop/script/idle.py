from core.modules import VisualNovelModule
from core.compiler import compile
# -------------------------------------------------------
# This is the Example of a Single File Script
# -------------------------------------------------------

# So like, a standalone script will compile into a single script
# Think of it like a single 100k words word document.
# If that your style, this is how you do it

from characters import Cupa, Andr, Yuki  # Import characters you've defined in characters.py
vn = VisualNovelModule()
c = Cupa
a = Andr
y = Yuki
p = "Player"
storyName = "yuki" # This will be the name of the Json File

def story():


    # Come on now, it's intuitive enough~
    vn.setVar("background",False)
    vn.start()
    vn.label("start") # This is a 'Label', it will be used by the jump and choice to know where to go
    vn.show(y,"happy")
    vn.say(y,"Oh hey Player! Long time no see! Ahaha~")
    vn.say(p,"Yeah, been a while huh?")
    vn.label("end")
    vn.show(a,"happy")
    vn.say(a,"Happy to Help, see you later Player!")
    vn.finish()


    return vn.dialogueDict


def main():compile(storyname=storyName,script=story()) # Yeah, just run this file :v

if __name__ == "__main__":
    main()
