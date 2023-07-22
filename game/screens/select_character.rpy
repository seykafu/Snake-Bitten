screen select_character:
    vbox:
        text "{color=#fff}{b}Male Character - Clove" outlines [ (2.5, "#230F06", 0, 0) ] pos(400, 280)
        text "{color=#fff}{b}Female Character - Enpa" outlines [ (2.5, "#230F06", 0, 0) ] pos(1100, 240)

        hbox:
            imagebutton:
                xalign 1.0
                yalign 0.005
                xpos 800
                ypos 280
                idle "clove clear.png"
                hover "clove_dark.png"
                action Return("MC")
        hbox:
            imagebutton:
                xalign 1.0
                yalign 1.05
                xpos 1500
                ypos 280
                idle "enpa clear.png"
                hover "enpa_dark.png"
                action Return("FMC")
