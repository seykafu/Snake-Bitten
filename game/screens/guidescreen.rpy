screen tipScreen(tip):
    drag:
        drag_name "Hint"
        yalign 0.5
        xalign 0.5
        drag_handle (0,0,1,0,1.0)

        frame:
            xpadding 25
            ypadding 30
            yalign 0.5
            xalign 0.5
            xmaximum 610
            ymaximum 400
            has vbox
            label "Hint" xminimum 400
            text tip
