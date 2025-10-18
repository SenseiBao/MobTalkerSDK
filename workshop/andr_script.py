from core.modules import VisualNovelModule
from core.compiler import compile
from characters import Andr

vn = VisualNovelModule()
a = Andr
p = "Player"
storyName = "andr"

def story():
    vn.start()

    # Initialize the global variable with a number (0 for false) to prevent crashes.
    vn.setGlobal("knows_andr_secret", 0)

    # Check the global variable using the number 1 (for true).
    vn.condSameGlobal("knows_andr_secret", 1, [
        vn.jumpTo("confront", nested=True)
    ])

    # This is the default conversation.
    vn.label("default_greeting")
    vn.show(a, "happy")
    vn.say(a, "Hey. Good to see you.")
    vn.finish()

    # This is the special conversation after talking to Cupa.
    vn.label("confront")
    vn.show(a, "sad")
    vn.say(a, "Cupa told you, didn't she? About the... bunnies.")
    vn.say(p, "...")
    vn.say(a, "It's fine. It's just embarrasing...")
    vn.finish()

    return vn.dialogueDict

def main():
    compile(storyname=storyName, script=story())

if __name__ == "__main__":
    main()