from core.modules import VisualNovelModule
from core.compiler import compile
from characters import Andr

vn = VisualNovelModule()
a = Andr
p = "Player"
storyName = "andr"

def story():
    vn.start()

    # We use Andr's own persistent state to track if this is our first meeting.
    vn.condSame("<andr_state>", "met_before", [
        vn.jumpTo("check_secret", nested=True)
    ])

    # --- First-Time Interaction ---
    # This block only runs the very first time you talk to Andr.
    vn.label("first_meeting")

    # His only job is to create the variable and say hello.
    vn.setGlobal("knows_andr_secret", False)
    vn.say(a, "Hey. Good to see you.")

    # Now we mark his state so this block never runs again.
    vn.modVar("<andr_state>", "met_before")
    vn.finish()

    # --- Subsequent Interactions ---
    # Every other time you talk to Andr, the script will jump here.
    vn.label("check_secret")

    # It is now safe to check the global variable.
    vn.condSameGlobal("knows_andr_secret", True, [
        vn.jumpTo("confront", nested=True)
    ])

    # This is the default conversation if the secret is not known.
    vn.label("default_greeting")
    vn.show(a, "happy")
    vn.say(a, "Good to see you again.")
    vn.finish()

    # This is the special conversation.
    vn.label("confront")
    vn.show(a, "sad")
    vn.say(a, "Cupa told you, didn't she? About the... bunnies.")
    vn.say(p, "...")
    vn.say(a, "It's fine. Just... be cool about it.")
    vn.finish()

    return vn.dialogueDict

def main():
    compile(storyname=storyName, script=story())

if __name__ == "__main__":
    main()