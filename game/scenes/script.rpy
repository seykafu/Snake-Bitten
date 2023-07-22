#The rollback creates some bugs, so I disable it
define config.rollback_enabled = False

init python:
    import npc
    import chatgpt1
    import re

##BASIC GAME STRUCTURE##
label start:

    #Let's start with the intro
    call intro from _call_intro

    #Now start act 1
    call act1a from _call_act1a

    call act2a from _call_act2a

    return