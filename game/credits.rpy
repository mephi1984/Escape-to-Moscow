
define player_skipped_credits = False

screen credits_helper():

    key "dismiss" action [ SetVariable("player_skipped_credits", True), Jump("after_credits")]
    key 'button_select' action [ SetVariable("player_skipped_credits", True), Jump("after_credits")]
    key 'input_enter' action [ SetVariable("player_skipped_credits", True), Jump("after_credits")]
    key 'bar_activate' action [ SetVariable("player_skipped_credits", True), Jump("after_credits")]
    key 'bar_deactivate' action  [ SetVariable("player_skipped_credits", True), Jump("after_credits")]


label credits:
    $ renpy.pause(0.5)

    $ quick_menu = False
    $ show_say_menu = False

    show screen credits_helper

    show perlin at credits_perlin_pos with dissolve:
        xpos 0.0
        linear 80.0 xpos -2.0

    show semyon_credits at credits_semyon1_pos1 zorder 10 with dissolve:
        xpos 0.7
        linear 30.0 xpos 0.6

    show text Text(_("{color=#FFD800}Продюсер:{/color}\nВладислав Хорев"), size=int(50*SCALE)) as credits_text1_line1 at credits_text1_line1_pos zorder 10 with dissolve:
        xpos 0.05
        linear 5.0 xpos 0.15

    $ renpy.pause(0.2)

    show text Text(__("{color=#FFD800}Разработчик:{/color}\nВладислав Хорев"), size=int(50*SCALE)) as credits_text1_line2 at credits_text1_line2_pos zorder 10 with dissolve:
        xpos 0.05
        linear 5.0 xpos 0.15

    $ renpy.pause(2)

    hide semyon_credits with dissolve

    hide credits_text1_line1 with dissolve

    hide credits_text1_line2 with dissolve

    show aliya_anim at credits_aliya1_pos1 zorder 10 with dissolve:
        zoom 0.75*SCALE
        xpos 0.2
        linear 30.0 xpos 0.35

    $ renpy.pause(0.2)

    show text Text(__("{color=#FFD800}Автор сценария:{/color}\nВладислав Хорев"), size=int(50*SCALE)) as credits_text1_line3 at credits_text1_line3_pos zorder 10 with dissolve:
        xpos 0.55
        linear 5.0 xpos 0.52

    $ renpy.pause(0.2)

    show text Text(__("{color=#FFD800}Тексты:{/color}\nВладислав Хорев\nЯна \"Samadreal\" Однорог"), size=int(50*SCALE)) as credits_text1_line4 at credits_text1_line4_pos zorder 10 with dissolve:
        xpos 0.55
        linear 5.0 xpos 0.52


    $ renpy.pause(2)

    hide aliya_anim with dissolve

    hide credits_text1_line3 with dissolve

    hide credits_text1_line4 with dissolve

    show imran angry at credits_imran1_pos1 zorder 10 with dissolve:
        zoom 0.75*SCALE
        xpos 0.25
        linear 30.0 xpos 0.45

    $ renpy.pause(0.2)

    show text Text(_("{color=#FFD800}Спрайты персонажей:{/color}\nДарья \"miZaria\" Фролова\nSsurikin\nMarys (Маша Свиридова)\nТатьяна \"Akinago\" Аверина"), size=int(50*SCALE)) as credits_text1_line5 at credits_text1_line5_pos zorder 10 with dissolve:
        xpos 0.45
        linear 5.0 xpos 0.52


    $ renpy.pause(2)

    hide imran with dissolve

    hide credits_text1_line5 with dissolve

    show aslan watching_imran at credits_aslan1_pos1 zorder 11:
        zoom 0.75*SCALE
        xpos 0.65
        alpha 0.0
        linear 0.5 alpha 1.0
        linear 30.0 xpos 0.55

    show fatima smile at credits_fatima1_pos1 zorder 10:
        alpha 0.0
        zoom 0.75*SCALE
        xpos 0.9
        linear 0.5 alpha 0.0
        linear 0.5 alpha 1.0
        linear 30.0 xpos 0.8

    $ renpy.pause(0.2)


    show text Text(_("{color=#FFD800}Фоны:{/color}\nQuandial\nАнонимный художник"), size=int(50*SCALE)) as credits_text1_line61 at credits_text1_line61_pos zorder 10 with dissolve:
        xpos 0.05
        linear 5.0 xpos 0.12

    show text Text(_("{color=#FFD800}Прочие изображения:{/color}\nДарья \"miZaria\" Фролова\nЕлизавета \"Lyss\" Попкова\nАнонимный художник"), size=int(50*SCALE)) as credits_text1_line62 at credits_text1_line62_pos zorder 10 with dissolve:
        xpos 0.05
        linear 5.0 xpos 0.12

    $ renpy.pause(2)

    hide aslan with dissolve

    hide fatima with dissolve

    hide credits_text1_line61 with dissolve

    hide credits_text1_line62 with dissolve


    show officer neutral at credits_officer_pos1 zorder 10:
        zoom 0.75*SCALE
        xpos 0.15
        alpha 0.0
        linear 0.5 alpha 1.0
        linear 30.0 xpos 0.3

    $ renpy.pause(0.2)

    show text Text(_("{color=#FFD800}Музыка:{/color}\nRomull"), size=int(50*SCALE)) as credits_text1_line7 at credits_text1_line7_pos zorder 10 with dissolve:
        xpos 0.47
        linear 5.0 xpos 0.44

    show text Text(_("{color=#FFD800}Звуки и амбиент:{/color}\nВладислав Хорев\nflorianreichelt (freesound.org)"), size=int(50*SCALE)) as credits_text1_line8 at credits_text1_line8_pos zorder 10 with dissolve:
        xpos 0.47
        linear 5.0 xpos 0.44

    $ renpy.pause(2)

    hide officer with dissolve

    hide credits_text1_line7 with dissolve

    hide credits_text1_line8 with dissolve

    show salesman neutral at credits_salesman_pos1 zorder 11:
        zoom 0.75*SCALE
        xpos 0.75
        alpha 0.0
        linear 0.5 alpha 1.0
        linear 30.0 xpos 0.6


    $ renpy.pause(0.2)


    show text Text(_("{color=#FFD800}Моушн-дизайн:{/color}\nДмитрий Журавский (night_xevf)"), size=int(50*SCALE)) as credits_text1_line9 at credits_text1_line9_pos zorder 10 with dissolve:
        xpos 0.05
        linear 5.0 xpos 0.12

    $ renpy.pause(2)

    hide salesman with dissolve

    hide credits_text1_line9 with dissolve


    $ renpy.pause(0.2)


    show text Text(_("Все персонажи и произошедшие в игре события - вымышлены."), size=int(36*SCALE)) as credits_text10_line1 at credits_text10_line1_pos zorder 10 with dissolve

    $ renpy.pause(2)

    show text Text(_("Все совпадения с реальными личностями и событиями случайны."), size=int(36*SCALE)) as credits_text10_line2 at credits_text10_line2_pos zorder 10 with dissolve

    $ renpy.pause(2)

    show text Text(_("Сюжет игры был создан под впечатлением от событий, описанных в СМИ и в блогах."), size=int(36*SCALE)) as credits_text10_line3 at credits_text10_line3_pos zorder 10 with dissolve

    $ renpy.pause(4)



    if _preferences.language == None:

        hide credits_text10_line1 with dissolve

        hide credits_text10_line2 with dissolve

        hide credits_text10_line3 with dissolve

        show text Text("Если ваша знакомая окажется в похожей затруднительной ситуации,", size=int(36*SCALE)) as credits_text11_line1 at credits_text11_line1_pos zorder 10 with dissolve

        $ renpy.pause(2)

        show text Text("Сообщите ей мои контактные данные:", size=int(36*SCALE)) as credits_text11_line2 at credits_text11_line2_pos zorder 10 with dissolve

        $ renpy.pause(2)

        show text Text("VK: ", size=int(36*SCALE)) as credits_text11_line311 at credits_text11_line311_pos zorder 10 with dissolve

        show text Text("{b}vk.com/id677718{/b}", size=int(36*SCALE)) as credits_text11_line312 at credits_text11_line312_pos zorder 10 with dissolve

        show text Text("Telegram: ", size=int(36*SCALE)) as credits_text11_line321 at credits_text11_line321_pos zorder 10 with dissolve

        show text Text("{b}mephi1984{/b}", size=int(36*SCALE)) as credits_text11_line322 at credits_text11_line322_pos zorder 10 with dissolve

        show text Text("Телефон: ", size=int(36*SCALE)) as credits_text11_line331 at credits_text11_line331_pos zorder 10 with dissolve

        show text Text("{b}+7 926 049 2730{/b}", size=int(36*SCALE)) as credits_text11_line332 at credits_text11_line332_pos zorder 10 with dissolve

        $ renpy.pause(2)

        show text Text("Я постараюсь ей помочь или найду кого-нибудь, кто сможет помочь.", size=int(36*SCALE)) as credits_text11_line4 at credits_text11_line4_pos zorder 10 with dissolve


        $ renpy.pause(2)

        show text Text("Помните,", size=int(36*SCALE)) as credits_text11_line5 at credits_text11_line5_pos zorder 10 with dissolve

        $ renpy.pause(0.5)

        show text Text("Лишнее самоубийство не нужно ни кому.", size=int(36*SCALE)) as credits_text11_line6 at credits_text11_line6_pos zorder 10 with dissolve

        $ renpy.pause(10)

    jump after_credits

label after_credits:



    if player_skipped_credits:

        stop music_crossfade fadeout 1.0

        hide semyon1

        hide credits_text1_line1

        hide credits_text1_line2

        hide aliya_anim

        hide credits_text1_line3

        hide credits_text1_line4

        hide imran

        hide credits_text1_line5



        hide aslan

        hide fatima

        hide credits_text1_line7

        hide credits_text10_line1

        hide credits_text10_line2

        hide credits_text10_line3


        hide credits_text11_line1

        hide credits_text11_line2

        hide credits_text11_line311
        hide credits_text11_line312
        hide credits_text11_line321
        hide credits_text11_line322
        hide credits_text11_line331
        hide credits_text11_line332

        hide credits_text11_line4

        hide credits_text11_line5

        hide credits_text11_line6


        $ player_skipped_credits = False # return the original value back



    else:


        if _preferences.language == None:

            stop music_crossfade fadeout 5.0

            hide credits_text11_line1 with dissolve

            hide credits_text11_line2 with dissolve

            hide credits_text11_line311 with dissolve
            hide credits_text11_line312 with dissolve
            hide credits_text11_line321 with dissolve
            hide credits_text11_line322 with dissolve
            hide credits_text11_line331 with dissolve
            hide credits_text11_line332 with dissolve

            hide credits_text11_line4 with dissolve

            hide credits_text11_line5 with dissolve

            hide credits_text11_line6 with dissolve

        else:
            stop music_crossfade fadeout 3.0

            hide credits_text10_line1 with dissolve

            hide credits_text10_line2 with dissolve

            hide credits_text10_line3 with dissolve


    hide perlin with dissolve

    $ quick_menu = True
    $ show_say_menu = True

    return
