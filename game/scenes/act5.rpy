define config.rollback_enabled = False

init python:
    #import npc
    import chatgpt1
    from apikey import openai_api_key

# The script of the game goes in this file.

# The game starts here.

label act5:

    nvl clear
    scene clove_room with fade

    show clove happy at center 
    with moveinleft

    clove "..."

    