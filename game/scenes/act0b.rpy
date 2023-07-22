define config.rollback_enabled = False

define playlist = ["saving.mp3", "japan.mp3"]
$ renpy.random.shuffle(playlist) 
play music playlist fadeout 1.0 fadein 1.0 # This should now play the full randomized playlist and then repeat from the begining.


init python:
    #import npc
    import chatgpt1
    from apikey import openai_api_key

screen select_character:
    vbox:
        hbox:
            add "clove clear.png"
            textbutton _("MC") action Return("MC")
        hbox:
            add "enpa clear.png"
            textbutton _("FMC") action Return("FMC") 

label fmc_start:

    m "Cool, you'll play Enpa then!"

    m "Before I go further, please start by inputing your OpenAI API key. If you don't have one, that's okay! The game will go on under its default script. You'll still have fun regardless."

    m "If you're unsure where to find your API, just search 'Where do I find my Secret OPENAI API Key?' on Google. Note that you need to create an OPENAI account."

    python:
        #We get the API Key from the User. Because you should NEVER give your API key in any form with your game let alone share it on a public repository
        #How to distribute your game with an embbed API KEY ? I'll soon make a special server system to make it possible
         apikey = renpy.input("What is your OPENAI API Key? (leave empty if you don't have any)", length=64)

    if apikey != "":
        m "Success!"
    else:
        m "If you don't have any, I'll be using my proxy to give you the best experience possible."

    m "Oh! And last but not least! When conversing with the AI, please keep your convos civil. Don't say anything impudent please..."

    m "Okie, let's go. Welcome... to {i}'Snake Bitten!'{/i}"

    scene black with dissolve

    stop music fadeout 1.0

    play music "dramatic.mp3" fadeout 1.0 fadein 1.0 noloop

    "The hallway was as dark as a blackhole, and its walls were slathered with an unfinished crimson red paint job that reminded Enpa of blood. "

    "She kept pacing to the exit at the end, hoping for more light to emerge."

    nvl clear

    scene red_hallway
    with fade

    show enpa happy at right
    with moveinright

    enpa "{i}What a long day it's been..."

    enpa "{i}First I get yelled at by my boss last week, and now they've decided to fire me because I 'don't fit with the team culture.'"

    enpa "{i}Which is just a stupid euphimism for 'we're a bunch of racists and you don't fit in with our people.'"

    enpa "{i}I'll just hurry home for dinner and start job-hunting tomorrow morning. Oh great, someone's coming..."

    show clove happy at left
    with moveinleft

    clove "Good evening."

    enpa "Good evening. Please excuse me."

    hide enpa happy with moveoutleft

    stop music fadeout 1.0

    jump act1b