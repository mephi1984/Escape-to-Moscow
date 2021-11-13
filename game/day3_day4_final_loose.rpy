
label day3_and_day4_final_loose:

    $ addReceivedMessage(3)

    coach "Я не виню тебя в произошедшем." with dissolve

    $ addReceivedMessage(4)

    coach "Тебе нужно успокоиться. Всё уже позади." with dissolve

    $ addReceivedMessage(4)

    coach "Прошлое не вернуть. Эта глава твоей жизни завершена." with dissolve

    $ addReceivedMessage(3)

    coach "Тебе нужно начать следующую." with dissolve

    $ addReceivedMessage(3)

    coach "Какая она будет - зависит только от тебя." with dissolve

    $ addReceivedMessage(5)

    coach "Свяжись с хозяйкой квартиры, скажи, что ты скоро съезжаешь. Пусть вернёт деньги за неиспользованные дни." with dissolve

    $ addReceivedMessage(3)

    coach "Собери вещи, купи авиабилеты" with dissolve

    $ addReceivedMessage(3)

    coach "и возвращайся к себе домой." with dissolve

    "Мне очень хотелось возразить, но я не знал даже, что и ответить." with dissolve

    $ addSentMessage(0)

    me "Ладно..." with dissolve

    $ addReceivedMessage(3)

    coach "Мне пора, я отключаюсь. Не падай духом!" with dissolve

    $ addSentMessage(0)

    $ last_playing_music = "playRunaway16()"

    $ music_stage_preload = "music_Runaway16_Runaway11"

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("stopAllMusic()")
            $ emscripten.run_script("playRunaway01()")

    me "Пока." with dissolve

    $ clearDisplayMessages()

    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("playRunaway16()")
    else:

        play music "music/Runaway_16 (Loop).ogg" # fadein 3.0

        queue music "music/Runaway_16 (Loop).ogg"

    show cg_screen_phone_messenger_contact_list as cg_screen_phone with dissolve

    "Я вышел из диалога с Напарником и открыл список контактов." with dissolve

    "Краем глаза я заметил, что Алия в сети!" with dissolve

    $ changeDialogToAliya()

    $ showMessengerPhone(is_night=False, force_no_transition=True)

    "Я немедленно открыл диалог и написал ей сообщение." with dissolve

    $ addSentMessage(5)

    me "Привет, Алия! Я беспокоюсь о тебе, пожалуйста, ответь!" with dissolve

    "Сообщение отправлено!" with dissolve

    "Сообщение прочитано..." with dissolve

    "... Ну же, она ответит что-нибудь?" with dissolve

    $ aliya_banned = True

    $ clearMessagesAfterBan()

    "Внезапно все сообщения пропали." with dissolve

    "Весь наш диалог испарился, как будто его и не было." with dissolve

    show cg_screen_phone_messenger_top_aliya_banned as cg_screen_phone_top with dissolve

    "Вслед за диалогом испарилась аватарка Алии - персонаж из аниме." with dissolve

    "\"Миса Амане - был(а) в сети давно\"." with dissolve

    "Кажется, меня кинули в ЧС." with dissolve

    $ hidePhone()

    "Я обессиленно выключил телефон и закрыл глаза." with dissolve

    scene black with dissolve

    "Я чувствовал себя усталым и разбитым." with dissolve

    show perlin at credits_perlin_pos zorder 2 with dissolve:
        xpos 0.0
        linear 120.0 xpos -2.0

    "Я погрузился в полудрёму и меня снова окружил туман." with dissolve

    "Мне теперь было ещё хуже, чем до встречи с Алией." with dissolve

    show perlin as perlin2 at credits_perlin_pos zorder 4 with dissolve:
        xpos -1.0
        linear 80.0 xpos -2.0

    "Я взялся помочь и, кажется, всё испортил." with dissolve

    show Aliya_stand_half_turned eyes_open_surprised zorder 1 as Aliya with dissolve:
        xalign 0.5
        yalign -0.1
        zoom 1.0

    "Как там Алия? Всё ли с ней в порядке?" with dissolve

    "Я не знаю и даже понятия не имею как узнать." with dissolve

    "Она появилась в моей жизни резко как взрыв, как фейерверк." with dissolve

    hide Aliya with dissolve

    "И так же резко исчезла." with dissolve

    "Увидимся ли мы снова в будущем? Без понятия." with dissolve

    hide perlin2 with dissolve

    "Мне остаётся лишь надеяться, что с ней всё будет в порядке." with dissolve

    "И, наверное... мне стоит изменить свою жизнь." with dissolve

    hide perlin with dissolve

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("playRunaway16()")

    $ last_playing_music = ""

    "Я всё равно больше не смогу жить как раньше..." with dissolve

    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("stopAllMusic()")

    jump teaser_start

    #jump credits
