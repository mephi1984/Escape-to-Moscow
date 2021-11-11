
label day2_cancel:

    $ addSentMessage(3)

    me "Извини, но тут я уже ничем не могу помочь." with dissolve

    $ addSentMessage(3)

    me "За столь короткое время мы ничего не успеем." with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Я поняла." with dissolve

    $ addSentMessage(3)

    me "Желаю тебе удачи и всё такое." with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Спасибо!" with dissolve

    "Наступило молчание." with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "В таком случае прости, что побеспокоила." with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Я попробую придумать что-нибудь сама." with dissolve

    $ aliya_banned = True

    $ showMessengerWithRightOrder()

    "Пока я думал что ответить, аватарка Миса Амане пропала." with dissolve

    $ clearMessagesAfterBan()

    "Вслед за аватаркой пропали все сообщения." with dissolve

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("stopAllMusic()")
            $ emscripten.run_script("playRunaway03()")

    $ last_playing_music = "playRunaway01()"

    "\"Миса Амане - был(а) в сети давно\"." with dissolve

    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("playRunaway01()")
    else:

        play music "music/Runaway_01 (Main).ogg"  # fadein 1.0

        queue music "music/Runaway_01 (Loop).ogg"

    "Кажется, она добавила меня в чёрный список." with dissolve

    "Жалко её, конечно, но я действительно не могу ничем помочь." with dissolve

    "Максимум, что я мог бы сделать - дать телефоны и адреса каких-нибудь женских правозащитных организаций." with dissolve

    "Но у меня среди друзей нет знакомых в этой сфере." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    scene semen_room_night with dissolve

    $ savegame_picture = "savegame_semen_room_night"

    "Она отправила меня в ЧС и я не могу ей больше ничего писать." with dissolve

    "Ладно, пожалуй, пойду спать." with dissolve

    "Мне же ещё нужно завтра заставить себя работать." with dissolve

    "Нужно очистить свои мысли от ненужных беспокойств..." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    return


    #"THE END, спасибо что поиграли! Концовка 3 - \"Второй день, Семён слился\"" with dissolve
