# This script holds side conversations that can be unlocked.
from core.modules import VisualNovelModule
from characters import Yuki

vn = VisualNovelModule()
y = Yuki

def story():
    """
    Contains self-contained "idle" chats.
    """
    vn.label("about_the_test")
    vn.say(y, "This is a test to show how conversations can be 'unlocked' and accessed separately from the main story.")
    vn.finish()

    return vn.dialogueDict
