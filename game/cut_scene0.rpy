
label cutscene0:

    scene black with dissolve


    $ quick_menu = False
    $ show_say_menu = False

    $ renpy.pause(1.0)

    play music "music/Runaway_04.ogg" fadein 1.0 fadeout 1.0


    #Change here for settning scale 1920x1080 to 1280x720
    #$ renpy.movie_cutscene("video1280/cutscene.mp4", stop_music=False)
    $ renpy.movie_cutscene("video1920/cutscene.mp4", stop_music=False)

    scene white

    $ renpy.pause(0.3)

    $ quick_menu = True
    $ show_say_menu = True


    jump day2_success_end
