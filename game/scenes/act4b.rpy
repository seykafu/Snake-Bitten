define config.rollback_enabled = False

init python:
    #import npc
    import chatgpt1
    from apikey import openai_api_key

# The script of the game goes in this file.

# The game starts here.

label act4b:

    scene elevator with fade

    show enpa happy at right
    with moveinright

    show allen at left
    with moveinleft

    enpa "I didn't even know there was a thirteenth floor on this building."

    allen "That's because it was hidden. We're using a different elevator than the one you usually take on a daily basis."

    "Enpa's eyes widened in surprise, and goosebumps developed on her skin out of excitement."

    enpa "{i}A secret floor?!"

    allen "Once we step out, please whisper."

    enpa "...hmph."

    "Once the elevator arrived at the floor, the doors opened faster than usual."

    nvl clear
    scene clove_hallway with fade
    show enpa happy at right
    with moveinright

    show allen at left
    with moveinleft

    enpa "So why are we here?"

    allen "There's a certain man whom I want you to see. But we're not going to disturb him today. I only want to show you what he's up to."

    "Enpa tilted her head in confusion."

    enpa "{i}Is this old man trying to recommend his son to me for marriage or something...?"

    "Enpa followed Allen from behind as they approached a door at the end of the hallway. Once they got halfway there, Allen slowed his footsteps and pointed down at his phone."

    allen "I want you to watch this."

    enpa "{i}Why the hell is he showing me a video?"

    "Allen tapped the play icon."

    jump act5
