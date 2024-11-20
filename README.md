# Mob Talker Redux SDK

### Yes, I'm doing this...

## Foreword

This thing is made because of how bloody frustrating it is to integrate scripting language like Lua to Minecraft. From the path files that just asking for trouble and the way JVM is... Yeah, no, hell no, I am not compiling anything in Minecraft.

So I ditched Lua and I put together THIS!

What this does is that, you can use this to comfortably build and test your Mob Talker Script. It also come with a resouece pack compiler. Create your resource pack for  the Mob Talker Script in one click, etc, etc.

This is a tool designed for Mod Developer's use for now. (To Compliment the Mob Talker Redux VN Framework). I want to make a nicer version of this tiny SDK, but eh, this is as far as I can go for now. 

...

Anyway, if I pull this off, consider Mob Talker Mod revived.

## TO DO

- [x] Build A Dummy Script For Testing
- [x] Build A Bunch of Basic Commands
- [x] Build The Compiler
- [x] Build The FSM Reader
- [x] Build The Terminal VN Game Engine
- [x] Build A Better Read Me
- [ ] Build A Better Documentation
- [ ] Organize The SDK into an Actual SDK
- [ ] Organize The Script
- [ ] Set Project Directory
- [ ] Fix The Import (Why is Import so hard? I don't get it)

## Features

- An example script to reverse engineer!
- Somewhat Organized Codebase 
- Extensible By Design, just yoink and extend.
- ~~A Terminal VN Engine "That Just Works" written by Claude!~~ 
- Everything is written by human. AI Coding Attempts have been tried and fail spectacularly and is immortalized somewhere in the commit history. Do not use AI. Believe in yourself. Whatever messs you cook up is always better than the sophisticated BS an AI can cook up. I learned this the hard way.

(No, I am not a good programmer if you're wondering)

## Setting Up Your Workshop

Step 0: Install Python, then `pip install dataclasses` (You might be able to skip the pip install dataclasses part, I forgot if this is default python stuff, I'll consider turning to primitive class)

Step 1: Make an empty folder

Step 2: `git clone https://github.com/Iteranya/MobTalkerSDK`

Step 3: Open the thing in VS code

Step 4: Locate the Workshop folder

Right... That

## Script Development Workflow

0. The Folders

backups - Just some stuff, nothing important

workshop - Where you'll do your script making

workshop/core - Don't touch, unless you're looking to add new features

workshop/script - an example of how to organize your stuff into multiscript

1. `singleFileDemo.py`

You can think of this as a 'template' file that you can use to create your script.
There's comments in there explaining the bare basics. 

You can run this file and it will automatically compile it into a json file.

(if you're in VS Code, that's the run bottom at the top right of the screen)

It'll show up somewhere outside the workshop, near main.py, usually

2. `multiFileDemo.py`

Exactly what it says on the tin. This and the script folder and everything in it, is an example of how you can use this thing work on Multiple Script.

Again, just run the file and it'll create a single Json (the scripts get combined into one, yes)

(More on this later)

3. `characters.py`

This is where you make character.
You can get creative, most of the stuff there are fluff (like description and traits)

The important parts are:

- id - this is the name of the folder containing character sprites
- name - this is the character's displayed name
- outfit - it's "default" by default, it contains character's default outfit (more info on this at the characters file)

3. main.py

You can think of this as your very own debugger to test the script. 
Just run

`python main.py "storyname.json"`

And you should be able to start playing it in your terminal before cracking open Minecraft.

Test the branching, states, make sure stuff happen as you like
It's a terminal, it doesn't support images. 

(Yet, might make a simple UI Presentation after this)

Anyway, the storyname.json is the end product. 

What to do with the storyname.json???

4. Minecraft

Check out the [Mob Talker Redux](https://github.com/Iteranya/MobTalkerRedux) in my repo for the mod itself.

It's currently a framework, not a functional mod. I mean it is a functional mod. Just doesn't have a content beyond the demo...

But VN Engine is already in the mod, just check out the current mod for example implementation.

## The Methods/Scripting
```
from characters import Cupa,Andr # Import characters you've defined in characters.py
vn = VisualNovelModule() # Planned to have Multi Module support, but for now... Yeah, just this... unfortunately...
c = Cupa # Defined in characters folder (Not Inside Core)
p = "Player" # Works with String Too~ (The 'say' function, I mean)
storyName = "First Meeting" # This will be the name of the Json File

def story(): ## This is the main method for running the story.
    vn.setVar("aff",0) # Setup the variables
    vn.setVar("gamemode","None for now") # Initialize them

    vn.initialize(storyName) # Actually unused for now, but good practice for future proof stuff
    vn.start() # Same as above
    vn.label("start") # This is a 'Label', it will be used by the jump and choice to know where to go
    vn.show_left(c,"normal") # c is 'Cupa', "normal" is the sprite name, normal.png. It will be displayed on the left.
    vn.say("???","Hmm?") # Say function (name, content). The name takes either Character class or a regular string.
    vn.show(c,"normal") # just `show()` function makes the character move to the middle
    vn.say(None,"The girl standing before you was strange. She looks like a human wearing a creeper hoodie, is she lost?") # Yes, can be blank too
    vn.say("???","Oh, a player, hey")
    vn.choice({
        "hi": "Hi?", # Format is (label to jump to : displayed text), this goes to the 'hi' label
        "who": "Who are you?",
        "engarde": "EN GARDE!!!"
    })

    vn.label("hi") # This one is hi label
    vn.addVar("aff", 5) # Adds a variable~
    vn.show(c,"happy") # happy.png under cupa/default/happy.png
    vn.say("???","Hi! Didn't expect to meet you, ever...")
    vn.say(p,"You know me?")
    vn.show(c,"normal")
    vn.say("???","Oh for sure! You're 'The Player")
    vn.say(p,"Is that a big deal?")
    vn.show(c,"happy")
    vn.say("???","Is it a big deal for a creeper to look like a chick?")
    vn.jumpTo("who") # Jump~
```
Read More Comments and Instructions on how each method do stuff in the demo files (Still WIP, sorry)
