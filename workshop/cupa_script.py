from core.modules import VisualNovelModule
from core.compiler import compile
from characters import Cupa

vn = VisualNovelModule()
c = Cupa
p = "Player"
storyName = "cupa"

def story():
    vn.start()

    # Initialize the global variable with a number (0 for false).
    vn.setGlobal("knows_andr_secret", 0)

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
    vn.say(c, "She acts all tough, but she's secretly terrified of bunnies. Don't tell her I told you!")

    # Modify the global variable using a number (1 for true).
    vn.modVarGlobal("knows_andr_secret", 1)
    vn.finish()

    return vn.dialogueDict

def main():
    compile(storyname=storyName, script=story())

if __name__ == "__main__":
    main()