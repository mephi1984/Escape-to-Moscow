
label teaser_start:

    $ quick_menu = False
    $ show_say_menu = False

    scene black

    stop music fadeout 2.0

    $ renpy.pause(2.0)

    show text Text(_("Несколько дней спустя..."), size=80) as credits_text1_line1 zorder 10:
        xpos 0.5
        ypos 0.5
        alpha 0.0
        linear 2.0 alpha 1.0


    $ renpy.pause(2.0)

    hide credits_text1_line1 with dissolve

    $ renpy.pause(1.0)

    play music "teaser/teaser.ogg"

    $ renpy.movie_cutscene("teaser/teaser.mp4", stop_music=False)

    scene black

    show text Text(_("Побег в Москву 2"), size=100) as credits_text1_line1 zorder 10:
        xpos 0.5
        ypos 0.3
        alpha 0.0
        linear 2.0 alpha 1.0

    $ renpy.pause(2.0)

    show text Text(__("В 2023 году"), size=75) as credits_text1_line2 zorder 10 with dissolve:
        xpos 0.5
        ypos 0.45
        alpha 0.0
        linear 2.0 alpha 1.0

    $ renpy.pause(2.0)

    show text Text(__("vk.com/escapetomoscow"), size=75) as credits_text1_line3 zorder 10 with dissolve:
        xpos 0.5
        ypos 0.6
        alpha 0.0
        linear 2.0 alpha 1.0


    $ renpy.pause(7.0)

    stop music fadeout 3.0

    hide credits_text1_line1 with dissolve

    hide credits_text1_line2 with dissolve

    hide credits_text1_line3 with dissolve

    $ renpy.pause(3.0)

    jump after_branch1_cutscene





label after_branch1_cutscene:

    #$ quick_menu = True
    #$ show_say_menu = True


    #return

    play music "music/Runaway_16 (Pre_Loop).ogg" fadein 1.0

    queue music "music/Runaway_16 (Loop).ogg"

    jump credits
