label day2_success_end:



    if isMobileWeb:
        scene bkg_movie_slide

        show night_road_foreground

        show black zorder 10

        $ renpy.pause(1.0)

        hide black with dissolve

    else:
        scene black

        show bkg_movie

        show night_road_foreground

        show white zorder 10

        $ renpy.pause(1.0)

        hide white with dissolve

    $ persistent.gallery1unlock = True

    $ savegame_picture = "savegame_night_road"

    "Время перевалило за одиннадцать, я сижу в машине Ярика на переднем сидении." with dissolve

    "Мы на полпути до аэропорта. Ярик действительно водит быстро, мы уже выехали за город и едем по трассе." with dissolve

    "Наскоро собранный рюкзак лежал у меня в ногах и теперь я мог наконец собраться с мыслями." with dissolve

    "В салоне играет евробит. Обычно я не фанат такой музыки, но сейчас она придавала мне уверенности." with dissolve

    show cg_screen_phone_airplane_app1_night as cg_screen_phone with dissolve

    "Я достал телефон и открыл приложение авиакомпании, чтобы зарегистрироваться на рейс." with dissolve

    show cg_screen_phone_airplane_app2_night as cg_screen_phone with dissolve

    "Я выбрал место и нажал пару галочек - регистрация завершена!" with dissolve

    $ hidePhone()

    "Судя по тому, как быстро Ярик едет, я действительно приеду в аэропорт вовремя." with dissolve

    messenger "Новое сообщение"  with dissolve

    show cg_screen_phone_new_message_day2_night2 as cg_screen_phone with dissolve

    "Я снова достал телефон." with dissolve

    $ changeDialogToAliya()

    $ showMessengerPhone(is_night=True, force_no_transition=True)

    $ addReceivedMessage(2)

    aliya_mobile "Я сегодня позвонила маме." with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Она удивилась, почему я такая грустная. Может она что-то подозревает?" with dissolve

    $ addSentMessage(2)

    me "Все будет хорошо." with dissolve

    $ addSentMessage(2)

    me "Документы у тебя под рукой?" with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Да, паспорт в сумке. ИНН лежат на полке в гостиной. Я заберу его, когда поеду завтра в аэропорт." with dissolve

    $ addSentMessage(3)

    me "Хорошо. А сейчас лучше ложись спать." with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Я наверное не смогу уснуть." with dissolve

    $ addSentMessage(1)

    me "Верь мне!" with dissolve

    $ addSentMessage(2)

    me "Всё будет хорошо!" with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Ладно. Спокойной ночи!" with dissolve

    $ addSentMessage(1)

    me "Спокойной ночи!" with dissolve

    $ hidePhone()

    "Я закрыл чат с Алией." with dissolve

    jump day2_night_choice


label day2_night_choice:

    if ((day2_night_car_coach_talked == True) and (day2_night_car_yarik_talked == True)):
        jump day2_car_end

    "Что сделать?" with dissolve

    menu:

        "Что сделать?"

        "Посоветоваться с Напарником." if day2_night_car_coach_talked == False:
            jump day2_car_coach

        "Поговорить с Яриком." if day2_night_car_yarik_talked == False:
            jump day2_car_jarik

        "Просто смотреть на дорогу и думать.":
            jump day2_car_end



label day2_car_coach:

    $ day2_night_car_coach_talked = True

    show cg_screen_phone_night as cg_screen_phone with dissolve

    $ changeDialogToCoach()

    $ showMessengerPhone(is_night=True, force_no_transition=True)

    "Я открыл чат с Напарником." with dissolve

    $ addSentMessage(2)

    me "Ярик меня встретил, я еду в аэропорт." with dissolve

    $ addReceivedMessage(4)

    coach "Хорошо! Ты задумал хорошее дело, мысленно я с тобой!" with dissolve

    $ addSentMessage(2)

    me "Что мне делать?" with dissolve

    $ addReceivedMessage(4)

    coach "Постарайся хорошо поспать в пути." with dissolve

    $ addReceivedMessage(3)

    coach "Завтра тебе предстоит тяжёлый день." with dissolve

    $ addReceivedMessage(4)

    coach "Когда встретишь Алию, разговаривай с ней спокойно и доброжелательно." with dissolve

    $ addReceivedMessage(4)

    coach "Желательно в многолюдном месте, чтобы ей не было страшно." with dissolve

    $ addReceivedMessage(5)

    coach "Тебе нужно расположить её к себе. Не дави, просто расскажи ей свой план. Ответь на её вопросы." with dissolve

    $ addReceivedMessage(4)

    coach "Затем спроси её, готова ли она последовать за тобой." with dissolve

    $ addSentMessage(3)

    me "А если она испугается и передумает?" with dissolve

    $ addReceivedMessage(5)

    coach "Если она передумает, то тут уже ничего не сделать. Выдай ей деньги на обратную дорогу и лети в Москву один." with dissolve

    $ addReceivedMessage(4)

    coach "Да и вообще, выдай ей немного наличных денег, чтобы она чувствовала себя увереннее." with dissolve

    $ addSentMessage(0)

    me "Ладно..." with dissolve

    $ addReceivedMessage(5)

    coach "Завтра сообщи мне свои новости. Когда вы будете в Москве, я помогу вам поискать и забронировать подходящее жилье." with dissolve

    $ addSentMessage(0)

    me "Спасибо!" with dissolve

    $ addReceivedMessage(5)

    coach "Мне пора спать ^^ удачи! Спишемся завтра." with dissolve

    $ addSentMessage(1)

    me "Спокойной ночи!" with dissolve

    $ clearDisplayMessages()

    $ hidePhone()

    "Я выключил телефон." with dissolve

    jump day2_night_choice


label day2_car_jarik:

    $ day2_night_car_yarik_talked = True

    "Ярик не проронил ни слова за всю дорогу." with dissolve

    "Мы поприветствовали друг друга при встрече, но с тех пор он молчал." with dissolve

    "Кажется, он сконцентрировался на вождении." with dissolve

    "Я решил начать небольшой разговор с ним." with dissolve

    me "Отличная машина." with dissolve

    yarik "Спасибо." with dissolve

    yarik "Машина считай что новая." with dissolve

    yarik "В этом году заказал свою красавицу на аукционе в Японии." with dissolve

    yarik "Я сам пригнал аж из Владика." with dissolve

    me "Круто!" with dissolve

    me "Спасибо, что решил помочь мне." with dissolve

    yarik "Да без проблем." with dissolve

    yarik "Я всегда за любую движуху." with dissolve

    yarik "Когда вернёшься из Москвы, пиши! Встретимся, расскажешь, как всё прошло!" with dissolve

    me "Конечно! Я сообщу!" with dissolve

    "Впрочем, я ещё даже не знаю, когда вернусь из Москвы." with dissolve

    "Ярик, кажется, снова сконцентрировался на дороге." with dissolve

    jump day2_night_choice


label day2_car_end:

    show black with dissolve

    $ renpy.pause(1.0)

    hide black with dissolve

    "Итак, я ввязался в историю и понятия не имею как она закончится." with dissolve

    "Но кажется, что-то внутри меня поменялось." with dissolve

    "Как будто в моей жизни появился смысл." with dissolve

    "Словно до этого я смотрел скучный фильм, и сейчас в этом фильме наконец началось основное действие." with dissolve

    "Возможно, я всю жизнь готовился именно к этому моменту. Вся моя жизнь до этого - всего лишь предыстория." with dissolve

    "Это выглядит как завязка сериала. Пилотная серия, первый эпизод." with dissolve

    "У меня слегка дрожат руки то ли от холода, то ли от страха." with dissolve

    "Конечно, мне немного страшно. Однако я решил, что если испугаюсь и передумаю сейчас, буду жалеть об этом всю оставшуюся жизнь." with dissolve

    "Разуеется, я настроен решительно, но мне всё равно не по себе. Не каждый день мне приходится похищать дочь следователя из Дагестана." with dissolve

    "Мог ли я отказаться? Да, легко. Но я почему-то решил вмешаться в эту историю и помочь Алие." with dissolve

    "Всё ли я делаю правильно? Этого я тоже не знаю. Возможно, своим вмешательством я только всё испорчу." with dissolve

    "Для себя я сделал выбор. Я помогу Алие сбежать и обустроиться в Москве." with dissolve

    "Нужно проследить, чтобы родители не нашли её и не увезли обратно в Пятигорск." with dissolve

    "Вообще, на первое время я могу поселиться в Москве вместе с ней, помогу с документами и поиском работы." with dissolve

    "У меня с собой в рюкзаке вся моя электроника, документы и сменная одежда." with dissolve

    "Этого достаточно на первое время, а всё остальное можно будет докупить при необходимости." with dissolve

    "Интересно, если взять среднестатистического человека, у которого есть работа, дом, семья, собака - согласился бы он на такую авантюру?" with dissolve

    "Чтобы вот так сорваться в Москву минимум на несколько недель, бросив работу, дом, привычный образ жизни?" with dissolve

    "Наверное, нет. Для этого нужно быть фрилансером... или безработным... и, конечно, немного отчаянным романтиком в душе." with dissolve

    scene black with dissolve

    $ savegame_picture = "savegame_black"

    #play music "music/Runaway_01 (Pre_Loop).ogg" fadein 1.0

    #queue music "music/Runaway_01 (Loop).ogg"

    "Вот мы уже подъезжаем к аэропорту. Я поблагодарил Ярика, взял рюкзак, вышел из машины..." with dissolve

    "И вошёл в здание нашего провинциального аэропорта..." with dissolve

    "Я успешно прошёл досмотр и сел ждать возле выхода на посадку." with dissolve

    "Завтра мне предстоял длинный день, и мне следовало бы выспаться как можно лучше." with dissolve

    "Мой мозг находился в возбуждённом состоянии, но я всё равно попробовал заставить себя заснуть." with dissolve

    show night_dream_scene_empty as night_dream_scene with dissolve

    "Мозг не успокаивался и рисовал передо мной образы." with dissolve

    show night_dream_scene_aliya_straight as night_dream_scene with dissolve

    "Я ещё не знаю как выглядит Алия." with dissolve

    "Я видел только её фотографию в паспорте." with dissolve

    show night_dream_scene_aliya_half_turned2 as night_dream_scene with dissolve

    "Она, наверное, сейчас уже спит." with dissolve

    "Или так же как и я пытается уснуть, борясь со страхом и волнением?" with dissolve

    show night_dream_scene_aliya_half_turned as night_dream_scene with dissolve

    "Может быть, она уже передумала лететь со мной?" with dissolve

    show night_dream_scene_empty as night_dream_scene with dissolve

    "Было очень обидно, если бы оказалось, что я зря ввязался в эту историю." with dissolve

    "Хотя с другой стороны, кто знает к чему приведёт эта история?" with dissolve

    "Может быть, для Алии было бы лучше остаться дома?" with dissolve

    "Я не знаю." with dissolve

    "Но я решил для себя, если она хочет сбежать - я помогу ей в этом." with dissolve

    stop music fadeout 2.0

    hide night_dream_scene with dissolve

    "И в этом я абсолютно уверен..." with dissolve

    $ renpy.pause(2.0)

    jump day3_intro
