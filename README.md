# Mob Talker Redux SDK

### Yes, I'm doing this...

## Foreword

This thing is made because of how bloody frustrating it is to integrate scripting language like Lua to Minecraft. From the path files that just asking for trouble and the way JVM is... Yeah, no, hell no, I am not compiling anything in Minecraft.

So I ditched Lua and I put together THIS!

What this does is that, you can use this to comfortably build and test your Mob Talker Script. It's a Mini VN Engine Written in Python, a Java version of this VN Engine is what powers the Mob Talker Mod. You can use this mini VN Engine to transpile and test the Mob Talker script in terminal.

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

## Features

- An example script to reverse engineer!
- Somewhat Organized Codebase 
- Extensible By Design, just yoink and extend.
- ~~A Terminal VN Engine "That Just Works" written by Claude!~~ 
- Everything is written by human. AI Coding Attempts have been tried and fail spectacularly and is immortalized somewhere in the commit history. Do not use AI. Believe in yourself. Whatever messs you cook up is always better than the sophisticated BS an AI can cook up. I learned this the hard way.

(No, I am not a good programmer if you're wondering)

## Getting Started

1. Fork This Project To Your Favorite IDE
2. Run demo.py
3. Run main.py Demo.json

...

Yeah, that's it, what else do you want???

Right... That

## Development Workflow

1. story.py

You can think of this as a 'template' file that you can use to create your script.
There's comments in there explaining the bare basics. 

I suggest start with trying to make simple short story here.

Once done, just do `python story.py` or whatever file you name it as.
That'll create your `First Meeting.json` file.

2. characters.py

This is where the characters are at. You can add more stuff in it too.
the `models.py` file contains the 'dataclass', feel free to add more.

3. main.py

You can think of this as your very own debugger to test the script. 
Just run
`python main.py "First Meeting.json"`
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
Read More Comments and Instructions on how each method do stuff in the story.py (Still WIP, sorry)
