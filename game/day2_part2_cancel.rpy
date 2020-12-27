
label day2_cancel:

    $ addSentMessage(3)

    me "Извини, но тут я уже ничем не могу помочь" with dissolve

    $ addSentMessage(3)

    me "За столь короткое время мы ничего не успеем" with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Я поняла" with dissolve

    $ addSentMessage(3)

    me "Желаю тебе удачи и все такое" with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Спасибо" with dissolve

    "Наступило молчание." with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "В таком случае прости что побеспокоила" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Я попробую придумать что-нибудь сама" with dissolve

    $ aliya_banned = True

    $ showMessengerWithRightOrder()

    "Пока я думал, что ответить - аватарка Миса Амане пропала." with dissolve

    $ clearMessagesAfterBan()

    "Вслед за аватаркой пропали все сообщения." with dissolve

    "\"Миса Амане - был(а) в сети давно\"." with dissolve

    play music "music/Runaway_01 (Pre_Loop).ogg"  fadein 1.0

    queue music "music/Runaway_01 (Loop).ogg"

    "Кажется, она добавила меня в черный список." with dissolve

    "Жалко ее, конечно, но я действительно не могу ничем помочь." with dissolve

    "Максимум что я мог бы сделать - дать телефоны и адреса каких-нибудь женских правозащитных организаций." with dissolve

    "Но у меня среди друзей нет знакомых в этой сфере." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    scene semen_room_night with dissolve

    "Ладно, она отправила меня в ЧС. Поэтому сейчас я уже ничем не могу помочь ей." with dissolve

    "Я пойду спать, пожалуй," with dissolve

    "Мне еще нужно завтра заставить себя работать." with dissolve

    "Нужно очистить свои мысли от ненужных беспокойств..." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    return


    #"THE END, спасибо что поиграли! Концовка 3, \"Второй день, Семен слился\"" with dissolve
