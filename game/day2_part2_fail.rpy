label day2_escape_now_fail:

    hide black with dissolve

    play music "music/Runaway_16 (Pre_Loop).ogg" fadein 1.0

    queue music "music/Runaway_16 (Loop).ogg"

    $ addSentMessage(3)

    me "Ну ладно, давай скидывай паспортные данные." with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Нет, не стоит." with dissolve

    $ addSentMessage(0)

    me "Почему?" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Я думаю, лучше справлюсь как-нибудь сама." with dissolve

    $ addSentMessage(3)

    me "Ты боишься меня? Я обещаю, что не трону тебя." with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Сказала же, не надо. Спасибо!" with dissolve

    $ addSentMessage(4)

    me "Почему ты мне не веришь? Я же могу помочь тебе!" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "То есть ты так и не понял, что мне никто не нужен?" with dissolve

    $ addSentMessage(1)

    me "Я нужен!" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Не хочу тебя ранить, но нет!" with dissolve

    $ addSentMessage(0)

    me "Почему?" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Просто не хочу. Что тут непонятного?" with dissolve

    $ addSentMessage(2)

    me "Не парь мне мозги!" with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Я не парю тебе мозги," with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "а говорю прямо!" with dissolve

    $ aliya_banned = True

    $ showMessengerWithRightOrder()

    "Пока я думал, что ответить - аватарка Алии пропала." with dissolve

    $ clearMessagesAfterBan()

    "Вслед за аватаркой пропали все сообщения." with dissolve

    "\"Миса Амане - был(а) в сети давно\"." with dissolve

    "Кажется, она добавила меня в чёрный список." with dissolve

    "Я хотел ей помочь, но видимо сделал только хуже." with dissolve

    "Она не доверяет мне и теперь будет решать свою проблему одна." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    scene semen_room_night with dissolve

    "Она отправила меня в ЧС и я не могу ей больше ничего писать." with dissolve

    "Ладно, пожалуй, пойду спать." with dissolve

    "Мне ещё нужно завтра заставить себя работать." with dissolve

    "Необходимо очистить свои мысли от лишних беспокойств..." with dissolve

    scene black with dissolve

    #"THE END, спасибо что поиграли! Концовка 2 - \"Второй день, Алия не доверяет Семёну\"" with dissolve

    $ renpy.pause(1.0)

    return
