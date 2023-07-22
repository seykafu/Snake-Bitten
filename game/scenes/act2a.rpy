define config.rollback_enabled = False

define playlist = ["saving.mp3", "japan.mp3"]
$ renpy.random.shuffle(playlist) 
play music playlist fadeout 1.0 fadein 1.0 # This should now play the full randomized playlist and then repeat from the begining.

label act2:
    show screen dice
    scene red_hallway with dissolve

    show clove happy at right
    with moveinright

    clove "The name's Clove. Yourself?"

    show enpa happy at left
    with moveinleft

    enpa "Well, Clove... Go fuck yourself."

    clove "That's not very nice. We just met..."

    enpa "I know who you are. You're that hentai-loving freak everyone's been talking about."

    enpa "I'm gonna get outta here. Got better things to do."

    hide enpa happy with moveoutleft

    # This ends the game.