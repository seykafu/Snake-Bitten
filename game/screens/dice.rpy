screen dice:
    zorder 10
    imagebutton:
        xcenter 1810
        ycenter 110
        idle "dice.png"
        hover "dice.png"
        activate_sound "audio/click.mp3"
        at transform:
            zoom 0.1875
        action Jump("dandl")