from core.modules import VisualNovelModule
from characters import Yuki

vn = VisualNovelModule()
y = Yuki
p = "Player"

def story():
    """
    Defines the main story progression with day and night transitions.
    """
    vn.start()
    vn.setVar("yuki_affection", 0)

    # --- Day 1 ---
    vn.label("day1")
    vn.show(y, "happy")
    vn.say(y, "Hello! What a beautiful morning.")
    vn.say(p, "It really is!")
    vn.unlock_dialogue(["about_the_test"]) # Unlocks an idle chat
    vn.next("night1") # This sets the bookmark for the next interaction
    vn.finish()

    # --- Night 1 ---
    vn.label("night1")
    vn.show(y, "normal")
    vn.say(y, "Good evening. The stars are bright tonight.")
    vn.next("day2") # Sets the next bookmark
    vn.finish()

    # --- Day 2 ---
    vn.label("day2")
    vn.show(y, "happy")
    vn.say(y, "Good morning! Ready for another day?")
    vn.say(p, "You bet!")
    vn.next("menu") # Sets the bookmark to the main menu
    vn.finish()

    # --- Main Menu ---
    vn.label("menu")
    vn.show(y, "normal")
    vn.say(y, "How can I help you today?")
    vn.choice({
        "praise": "Praise Her",
        "idle": "Ask a question"
    })

    # --- Menu Branches ---
    vn.label("praise")
    vn.show(y, "happy")
    vn.say(y, "Oh, thank you! That's sweet of you.")
    vn.addVar("yuki_affection", 1)
    vn.jumpTo("menu")

    vn.label("idle")
    vn.say(p, "I had a question...")
    vn.idle_chats() # This allows access to unlocked idle chats
    vn.jumpTo("menu")


    return vn.dialogueDict