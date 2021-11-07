screen branch1_cutscene_helper():

    key "dismiss" action [ SetVariable("player_skipped_credits", True), Jump("after_branch1_cutscene")]
    key 'button_select' action [ SetVariable("player_skipped_credits", True), Jump("after_branch1_cutscene")]
    key 'input_enter' action [ SetVariable("player_skipped_credits", True), Jump("after_branch1_cutscene")]
    key 'bar_activate' action [ SetVariable("player_skipped_credits", True), Jump("after_branch1_cutscene")]
    key 'bar_deactivate' action  [ SetVariable("player_skipped_credits", True), Jump("after_branch1_cutscene")]


label teaser_start:

    $ quick_menu = False
    $ show_say_menu = False

    show screen branch1_cutscene_helper

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

    #jump trailer_continue

    #jump trailer_continue3

    play sound "sound/teaser/546621__jose-danielms__cinematic-drum-sub.ogg"

    #show branch1_cutscene_city with dissolve:
    #    xalign 0.5
    #    yalign 0.5
    #    linear 20.0 zoom 1.5

    show branch1_cutscene_city2 as branch1_cutscene_city:
        xalign 0.5
        yalign 0.5
        alpha 0.0
        linear 1.2 alpha 1.0
        linear 2.0 alpha 1.0
        linear 1.2 alpha 0.0

    $ renpy.pause(5.0)

    hide branch1_cutscene_city

    #$ renpy.pause(0.5)

    play sound "sound/teaser/546621__jose-danielms__cinematic-drum-sub.ogg"

    show semen_room_night_empty:
        alpha 0.0
        linear 1.2 alpha 1.0
        linear 2.0 alpha 1.0
        linear 1.2 alpha 0.0

    $ renpy.pause(5.0)

    hide semen_room_night_empty

    #$ renpy.pause(0.5)

    show branch1_semyon_room_bedside_table1:
        alpha 0.0
        linear 1.2 alpha 1.0

    $ renpy.pause(3.0)

    play sound "sound/teaser/555154__nomerodin1__vibrating-message.ogg"

    ##play music "audio/nickelback - trying not to love you.ogg"

    show branch1_semyon_room_bedside_table2 with dissolve

    hide branch1_semyon_room_bedside_table1

    $ renpy.pause(3.0)

    ##play music "audio/nickelback - trying not to love you.ogg"

    show branch1_semyon_room_bedside_table3 with dissolve

    hide branch1_semyon_room_bedside_table2

    #show day2_msg_aliya with dissolve

    $ renpy.pause(0.5)

    show cg_screen_phone_begin_night as cg_screen_phone with dissolve:
        xalign 1.0

    show cg_screen_phone_new_message as cg_screen_phone_new_message at cg_screen_phone_new_message_pos with dissolve:
        zoom 0.0
        linear 0.3 zoom 1.0

    $ renpy.pause(1.5)

    ##play music "audio/nickelback - trying not to love you inst.ogg"
    #play music "music/Runaway_11 (Pre_Loop).ogg" fadein 1.5

    #show cg_messenger_cover_above_room at cg_messenger_cover_above_room_pos zorder 20

    hide cg_screen_phone_new_message

    show cg_screen_phone_night_dialog as cg_screen_phone:
        xalign 1.0

    show cg_messenger_title_noname at cg_messenger_title_pos zorder 20

    $ renpy.pause(0.5)

    #$ phoneSayNoNamePromo("Привет")

    show promo_msg1 at promo_msg1_pos:
        zoom 0.0
        linear 0.3 zoom 1.0

    $ renpy.pause(2.0)

    #$ phoneSayNoNamePromo("Это я")

    show promo_msg2 at promo_msg2_pos:
        zoom 0.0
        linear 0.3 zoom 1.0

    $ renpy.pause(4.0)

    #$ clearMessages()

    #hide cg_messenger_cover_above_room
    hide cg_messenger_title_noname
    hide promo_msg1
    hide promo_msg2
    hide cg_screen_phone with dissolve

    $ renpy.pause(1.5)

    scene black with dissolve

    # comment this out if you want to play
    jump trailer_continue



label trailer_continue:

    show black zorder 10

    show branch1_balcony_bkg_1:
        xpos -0.2

    show branch1_balcony_layer1_1:
        xpos -0.2

    show branch1_balcony_semyon_1:
        xpos -0.2

    hide black with dissolve

    show branch1_balcony_bkg_1 zorder 1:
        xpos -0.2
        linear 80.0 xpos -1.0 - 0.2

    show branch1_balcony_bkg_2 zorder 2:
        xpos -0.2
        alpha 0.0
        parallel:
            linear 80.0 xpos -1.0 - 0.2
        parallel:
            time 3.0
            linear 2.0 alpha 1.0

    show branch1_balcony_layer1_1 zorder 3:
        xpos -0.2
        linear 70.0 xpos -1.0 - 0.2

    show branch1_balcony_layer1_2 zorder 4:
        xpos -0.2
        alpha 0.0
        parallel:
            linear 70.0 xpos -1.0 - 0.2
        parallel:
            time 3.0
            linear 2.0 alpha 1.0

    show branch1_balcony_semyon_1 zorder 5:
        xpos -0.2
        linear 60.0 xpos -1.0 - 0.2

    show branch1_balcony_semyon_2 zorder 6:
        xpos -0.2
        alpha 0.0
        parallel:
            linear 60.0 xpos -1.0 - 0.2
        parallel:
            time 3.0
            linear 2.0 alpha 1.0



    $ renpy.pause(8.0)

    jump trailer_continue2

label trailer_continue2:


    #show branch1_daghome_window:
    #    xpos -0.2

    #show branch1_daghome_aliya:
    #    xpos -0.2

    #hide black with dissolve

    show branch1_daghome_bkg zorder 10:
        parallel:
            alpha 0.0
            linear 2.0 alpha 1.0
        parallel:
            xpos -0.2
            linear 180.0 xpos 1.0 - 0.2

    $ renpy.pause(2.5)


    hide branch1_balcony_bkg_1
    hide branch1_balcony_bkg_2

    hide branch1_balcony_layer1_1
    hide branch1_balcony_layer1_2

    hide branch1_balcony_semyon_1
    hide branch1_balcony_semyon_2

    show branch1_daghome_window zorder 11:
        parallel:
            alpha 0.0
            linear 1.0 alpha 1.0
        parallel:
            xpos -0.2
            linear 110.0 xpos 1.0 - 0.2

    show branch1_daghome_aliya zorder 12:
        parallel:
            alpha 0.0
            linear 1.0 alpha 0.0
            linear 1.0 alpha 1.0
        parallel:
            xpos -0.2
            linear 80.0 xpos 1.0 - 0.2


    $ renpy.pause(6.0)

    #scene black

    #$ renpy.movie_cutscene("video/60_fps_vzlet.mp4", stop_music=False)

    if isMobileWeb:

        show cutscene_takeoff1 as takeoff zorder 13:
            alpha 0.0
            linear 2.0 alpha 1.0

        $ renpy.pause(3.5)

        show cutscene_takeoff2 as takeoff2 zorder 14:
            alpha 0.0
            linear 1.0 alpha 1.0

        $ renpy.pause(2.5)

        show cutscene_takeoff3 as takeoff3 zorder 15:
            alpha 0.0
            linear 1.0 alpha 1.0

        $ renpy.pause(2.5)

        show cutscene_takeoff4 as takeoff4 zorder 16:
            alpha 0.0
            linear 1.0 alpha 1.0

        $ renpy.pause(2.5)

        show cutscene_takeoff5 as takeoff5 zorder 17:
            alpha 0.0
            linear 1.0 alpha 1.0

        $ renpy.pause(2.5)

    else:
        scene black

        $ renpy.movie_cutscene("video/60_fps_vzlet~2.mkv", stop_music=False)

    #play movie "movies/file.mkv"
    #scene black

    #show black zorder 10

    show lucoil1 zorder 18:
        alpha 0.0
        linear 1.5 alpha 1.0

    $ renpy.pause(3.0)

    show lucoil2 zorder 19:
        alpha 0.0
        linear 1.5 alpha 1.0

    $ renpy.pause(3.0)

    show lucoil2_people_layer zorder 20:
        alpha 0.0
        linear 2.0 alpha 1.0

    $ renpy.pause(4.0)

    scene lukoil_side_p1 with dissolve

    $ renpy.pause(2.5)

    show lukoil_side_p2:
        alpha 0.0
        linear 0.8 alpha 1.0

    $ renpy.pause(2.5)

    show lukoil_side_p3:
        alpha 0.0
        linear 0.8 alpha 1.0

    $ renpy.pause(2.5)

    show lukoil_side_p4:
        alpha 0.0
        linear 0.8 alpha 1.0

    $ renpy.pause(2.5)

    #jump trailer_continue3
    jump trailer_continue4

label trailer_continue4:

    #scene black with dissolve

    scene minsk_airport with dissolve

    $ renpy.pause(0.5)

    show minsk_airport_layer1 as minsk_airport_layer with dissolve

    $ renpy.pause(2.0)

    show cg_screen_phone_new_photo1 as cg_screen_phone_new_photo zorder 2:
        xalign 1.0
        alpha 0.0
        linear 0.5 alpha 1.0

    show minsk_airport_layer2 as minsk_airport_layer2 zorder 1 with dissolve

    $ renpy.pause(2.0)

    show cg_screen_phone_new_photo2 as cg_screen_phone_new_photo zorder 2 with dissolve:
        xalign 1.0

    $ renpy.pause(1.0)

    show cg_screen_phone_new_photo3 as cg_screen_phone_new_photo zorder 2 with dissolve:
        xalign 1.0

    $ renpy.pause(0.5)

    show white_large zorder 2:
        alpha 0.0
        linear 0.3 alpha 1.0
        linear 0.3 alpha 0.0

    $ renpy.pause(1.0)

    show cg_screen_phone_new_photo4 as cg_screen_phone_new_photo zorder 2 with dissolve:
        xalign 1.0

    $ renpy.pause(2.5)

    #$ renpy.pause(3.0)

    scene black with dissolve

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

    #play music "music/Runaway_16 (Pre_Loop).ogg" fadein 1.0

    #queue music "music/Runaway_16 (Loop).ogg"

    jump credits
