
label cutscene0:

    scene black with dissolve


    $ quick_menu = False
    $ show_say_menu = False

    $ renpy.pause(1.0)



    if renpy.emscripten:
        $ import emscripten
        $ emscripten.run_script("playRunaway04()")
    else:
        play music "music/Runaway_04.ogg" # fadein 2.0 # fadeout 1.0

    if isMobileWeb:
        show cutscene_slide1 as cutscene_slide with dissolve

        $ renpy.pause(4.0)

        show cutscene_slide2 as cutscene_slide with dissolve

        $ renpy.pause(2.0)

        show cutscene_slide3 as cutscene_slide with dissolve

        $ renpy.pause(1.0)

        show cutscene_slide4 as cutscene_slide with dissolve

        $ renpy.pause(1.0)

        show cutscene_slide5 as cutscene_slide with dissolve

        $ renpy.pause(1.0)

        show cutscene_slide6 as cutscene_slide with dissolve

        $ renpy.pause(2.0)

        show cutscene_slide7 as cutscene_slide with dissolve

        $ renpy.pause(2.0)

        show cutscene_slide8 as cutscene_slide with dissolve

        $ renpy.pause(2.0)

        show cutscene_slide9 as cutscene_slide with dissolve

        $ renpy.pause(2.0)

        show cutscene_slide10 as cutscene_slide with dissolve

        $ renpy.pause(2.0)

        show cutscene_slide11 as cutscene_slide with dissolve

        $ renpy.pause(2.0)

        hide cutscene_slide with dissolve
    else:
        #Change here for settning scale 1920x1080 to 1280x720
        #$ renpy.movie_cutscene("video1280/cutscene.mp4", stop_music=False)
        $ renpy.movie_cutscene("video1920/cutscene.mp4", stop_music=False)

        scene white





    $ renpy.pause(0.3)

    $ quick_menu = True
    $ show_say_menu = True


    jump day2_success_end
