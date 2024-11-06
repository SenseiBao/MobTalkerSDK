from core.modules import VisualNovelModule
from core.compiler import compile
# -------------------------------------------------------
# This is the Example Script for Handling Multiple Script
# -------------------------------------------------------

# If you're into organization, this is how you go about it.
# This file is the 'core' file

# Import characters you've defined in characters.py
from characters import Cupa,Andr 
# Import your scripts (all the .py file inside the script folder)
from workshop.script import script1,script2,script3
# YES You still have to import the modules characters and everything.
# Because dumb fuck developer didn't set up proper Python Environment
# Just import everything that your script needs

vn = VisualNovelModule()
c = Cupa 
p = "Player" 
storyName = "cupa" # This will be the name of the Json File

# This is the list of your script.

scripts = [
    script1.story(),
    script2.story(),
    script3.story()
]

# Yes, it's that simple
# I have Overengineering Phobia
def compileMultiStory():
    for script in scripts:
        vn.dialogueDict+=script
    return vn.dialogueDict


def main():compile(storyname=storyName,script=compileMultiStory()) 

# Run the file, if you're in VS Code, top right play button.

if __name__ == "__main__":
    main() 