from core.modules import VisualNovelModule
from core.compiler import compile
from characters import Cupa

vn = VisualNovelModule()
c = Cupa
p = "Player"
storyName = "cupa"

def story():
    vn.start()

    # Use the new function to initialize a true global variable.
    # This ensures the variable exists for other scripts to read.
    vn.setGlobal("knows_andr_secret", False)

    # --- Main Conversation with Cupa ---
    vn.label("start")
    vn.show(c, "normal")
    vn.say(c, "Hey, Player. Can I trust you with something about Andr?")
    vn.choice({
        "yes": "Of course you can.",
        "no": "I'm not sure."
    })

    vn.label("no")
    vn.say(c, "Oh... okay. Nevermind then.")
    vn.finish()

    vn.label("yes")
    vn.say(c, "He acts all tough, but he's secretly terrified of bunnies. Don't tell him I told you!")

    # Use the new function to modify the global variable.
    vn.modVarGlobal("knows_andr_secret", True)
    vn.finish()

    return vn.dialogueDict

def main():
    compile(storyname=storyName, script=story())

if __name__ == "__main__":
    main()