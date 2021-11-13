
label day2_escape_now_success:

    # Now here we need to unlock Semyon in the main menu
    $ persistent.menu_unlocked_semyon = True

    hide black zorder 10 with dissolve

    $ addReceivedMessage(4)

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("music_stage_preload = \"" + music_stage_preload + "\"")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracks()")

    $ music_stage_preload = "music_Runaway03_Runaway04"

    aliya_mobile "Эх, гореть мне в аду за то, что я делаю!" with dissolve

    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("music_stage_preload = \"" + music_stage_preload + "\"")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracksAsync()")

    $ addReceivedMessage(3)

    aliya_mobile "Вот мой паспорт. Покупай билеты на завтра." with dissolve

    $ addReceivedMessagePassport()

    "Алия прислала фотографию своего паспорта." with dissolve

    show cg_screen_passport zorder 16 with dissolve

    "Я открыл фото и развернул паспорт Алии во весь экран." with dissolve

    "Алия Гаджиева, 2001-го года рождения." with dissolve

    "Её фотка в паспорте была симпатичной, кстати..." with dissolve

    show cg_screen_new_message_coach zorder 17 with dissolve

    "От мыслей меня отвлекло новое сообщение из диалога с Напарником." with dissolve

    hide cg_screen_new_message_coach with dissolve

    $ changeDialogToCoach()

    $ showMessengerWithRightOrder()

    hide cg_screen_passport with dissolve

    jump day2_escape_now_success_coach




label day2_escape_now_success_coach:


    if day2_coach_advice_asked:
        jump day2_escape_now_success_coach_advice_asked
    elif day2_coach_talked or day1_advice_asked:
        jump day2_escape_now_success_coach_ever_talked
    else:
        jump day2_escape_now_success_coach_not_talked


label day2_escape_now_success_coach_not_talked:

    $ addReceivedMessage(3)

    coach "Привет! Как у тебя дела сегодня?" with dissolve

    $ addSentMessage(5)

    me "Привет! Дела неплохо, я сейчас собираюсь покупать авиабилеты для одной моей новой знакомой..." with dissolve

    $ addReceivedMessage(3)

    coach "Звучит интересно. Поговорим о ней?" with dissolve

    $ addSentMessage(4)

    me "Я с ней познакомился только вчера, я её не знаю." with dissolve

    $ addReceivedMessage(4)

    coach "Не знаешь её и уже покупаешь авиабилеты?" with dissolve

    $ addReceivedMessage(3)

    coach "Что там у тебя происходит?" with dissolve

    $ addSentMessage(3)

    me "Эээ...это долгая история" with dissolve

    $ addReceivedMessage(4)

    coach "Пришли мне свою переписку с ней, я почитаю." with dissolve

    $ addSentMessageHistory()

    "Я скопировал переписку с Алией и отправил Напарнику." with dissolve

    "Прошло достаточно много времени и наконец-но Напарник начал писать ответ." with dissolve

    $ addReceivedMessage(3)

    coach "Я офигеваю от сложившейся ситуации." with dissolve

    $ addReceivedMessage(5)

    coach "Ты молодец, что хочешь помочь, ты выбрал самый разумный вариант." with dissolve

    $ addSentMessage(0)

    me "Спасибо!" with dissolve

    $ addReceivedMessage(5)

    coach "Мне даже не нужно давать тебе советы, ты сам прекрасно справляешься." with dissolve

    $ addReceivedMessage(5)

    coach "Однако я всё-таки хочу кое-что у тебя уточнить." with dissolve

    $ coach_exposition_return_step = 3

    jump dagestan_exposition


label day2_escape_now_success_coach_not_talked_after_exposition:

    $ addReceivedMessage(5)

    coach "Теперь, возвращаясь к текущей ситуации." with dissolve

    $ addReceivedMessage(5)

    coach "Я тоже поддерживаю тебя в твоих делах и хочу помочь тебе." with dissolve

    $ addSentMessage(3)

    me "Спасибо, было бы здорово!" with dissolve

    $ addReceivedMessage(5)

    coach "Я сейчас поищу авиабилеты под твои критерии. Постараюсь найти подходящий вариант. Дай мне пару минут." with dissolve

    $ addSentMessage(1)

    me "Ооо, спасибо!" with dissolve

    "Прошло некоторое время, пока я находился в ожидании ответа от Напарника." with dissolve

    jump day2_escape_now_success_coach_continue


label day2_escape_now_success_coach_ever_talked:

    $ addReceivedMessage(3)

    coach "Привет! Как у тебя дела сегодня?" with dissolve

    $ addSentMessage(5)

    me "Привет! Я сейчас собираюсь покупать авиабилеты для Алии..." with dissolve

    $ addReceivedMessage(4)

    coach "Алии? Это та твоя новая знакомая из Дагестана?" with dissolve

    $ addSentMessage(0)

    me "Да." with dissolve

    $ addReceivedMessage(4)

    coach "Пришли пожалуйста переписку, я прочитаю." with dissolve

    $ addSentMessageHistory()

    "Я скопировал переписку и отправил Напарнику." with dissolve

    $ addReceivedMessage(5)

    coach "Да, вчера ты познакомился с ней, а сегодня тебе уже нужно принимать сложное решение." with dissolve

    $ addReceivedMessage(5)

    coach "Ты молодец, что решил помочь ей. Ты выбрал самый разумный способ." with dissolve

    $ addSentMessage(0)

    me "Спасибо!" with dissolve

    $ addReceivedMessage(5)

    coach "Я тоже поддерживаю тебя в твоих делах и хочу помочь тебе." with dissolve

    $ addSentMessage(3)

    me "Спасибо, было бы здорово!" with dissolve

    $ addReceivedMessage(5)

    coach "Я сейчас поищу авиабилеты, под твои критерии. Постараюсь найти подходящий вариант. Дай пару минут." with dissolve

    $ addSentMessage(1)

    me "Ооо, спасибо!" with dissolve

    "Прошло некоторое время, пока я находился в ожидании ответа от Напарника." with dissolve

    jump day2_escape_now_success_coach_continue



label day2_escape_now_success_coach_advice_asked:

    $ addReceivedMessage(3)

    coach "Ну что там? Что вы решили?" with dissolve

    $ addSentMessage(3)

    me "Я лечу к ней в Минеральные Воды." with dissolve

    $ addSentMessage(4)

    me "Мы договорились встретиться в аэропорту завтра утром." with dissolve

    $ addSentMessage(5)

    me "Там я её встречаю и мы уже вдвоём летим в Москву." with dissolve

    $ addReceivedMessage(3)

    coach "Отлично! Я уже ищу разные варианты авиабилетов." with dissolve

    jump day2_escape_now_success_coach_continue


label day2_escape_now_success_coach_continue:

    $ addReceivedMessage(4)

    coach "На завтра есть недорогие билеты из Минеральных Вод в Москву, в 12 часов дня." with dissolve

    $ addSentMessage(4)

    me "Хорошо, скинь ссылку. А от меня до Минеральных Вод?" with dissolve

    $ addReceivedMessage(5)

    coach "Тут уже похуже. Есть ночной рейс с длительной пересадкой в аэропорту Домодедово." with dissolve

    $ addReceivedMessage(4)

    coach "Ты прилетишь в Минеральные Воды завтра примерно в 9:40 утра." with dissolve

    $ addReceivedMessage(5)

    coach "Правда вылетать тебе придётся сегодня ночью. Ночной рейс вылетает в 00:50, это примерно через 3 часа." with dissolve

    $ addSentMessage(3)

    me "С часу ночи до 9:40 утра? Почему так долго?" with dissolve

    $ addReceivedMessage(4)

    coach "Там будет ночная пересадка в Москве, в аэропорту Домодедово." with dissolve

    $ addSentMessage(2)

    me "Других билетов нет?" with dissolve

    $ addReceivedMessage(4)

    coach "Остальные билеты либо распроданы либо стоят под 40 тысяч рублей." with dissolve

    $ addSentMessage(0)

    me "Да уж..." with dissolve

    $ addReceivedMessage(3)

    coach "Это единственный вариант за адекватные деньги." with dissolve

    $ addReceivedMessage(5)

    coach "Три часа до вылета. Успеешь собрать вещи и приехать в аэропорт?" with dissolve

    $ addSentMessage(2)

    me "Думаю, успею... хотя не знаю." with dissolve

    $ addReceivedMessage(3)

    coach "Если ты зарегистрируешься онлайн и не будешь сдавать багаж, то точно успеешь." with dissolve

    $ addSentMessage(2)

    me "Не сдавать багаж?" with dissolve

    $ addReceivedMessage(4)

    coach "Да. Возьми с собой в салон самолёта лёгкую сумку или рюкзак." with dissolve

    $ addReceivedMessage(4)

    coach "Туда нельзя будет класть жидкости и всякие колюще-режущие предметы." with dissolve

    $ addReceivedMessage(5)

    coach "Когда приедешь в аэропорт, распечатай посадочный талон в автомате и сразу проходи к выходам на посадку." with dissolve

    $ addSentMessage(0)

    me "Хорошо..." with dissolve

    $ addSentMessage(3)

    me "Как бы только добраться до аэропорта побыстрее?" with dissolve

    $ addReceivedMessage(3)

    coach "Я могу тебе помочь!" with dissolve

    $ addReceivedMessage(5)

    coach "У меня есть знакомый стритрейсер. Он как раз живет недалеко от тебя. Его зовут Ярик." with dissolve

    $ addReceivedMessage(4)

    coach "Я свяжусь сейчас с ним и попрошу подбросить тебя до аэропорта." with dissolve

    $ addReceivedMessage(4)

    coach "Думаю, Ярик войдёт в положение и поможет тебе ради хорошего дела!" with dissolve

    $ addSentMessage(3)

    me "Спасибо большое!" with dissolve

    $ addReceivedMessage(5)

    coach "Не бойся, ты не один! У тебя есть люди, которых ты может быть и не знаешь, но которые готовы помочь." with dissolve

    "Приятное чувство благодарности к напарнику растеклось по всему моему телу." with dissolve

    $ addSentMessage(3)

    me "Спасибо ещё раз! Я ценю это!" with dissolve

    $ addReceivedMessage(3)

    coach "Ярик тебе сейчас отпишется, жди." with dissolve

    $ addReceivedMessage(3)

    coach "А пока лови ссылку на авиабилеты." with dissolve

    $ addReceivedMessageLink()

    "Мне пришла ссылка на авиабилеты от Напарника." with dissolve


    show cg_screen_tickets zorder 16 with dissolve

    hide cg_screen_messenger_window
    hide cg_screen_messenger_window_top

    $ clearDisplayMessages()

    "Я открыл ссылку." with dissolve

    "Конечно же это был сайт поиска авиабилетов." with dissolve

    show cg_screen_tickets_pay zorder 16 with dissolve

    hide cg_screen_tickets

    hide semen_room_table_night_foreground_card with dissolve

    show semen_room_table_night_foreground_card_hands zorder 17 with dissolve

    "Кредитная карта словно поощряла меня, как волшебные печеньки из Алисы в Стране чудес - \"возьми меня\", \"потрать меня\"." with dissolve

    show cg_screen_tickets_success with dissolve

    hide cg_screen_tickets_pay

    hide semen_room_table_night_foreground_card_hands zorder 2 with dissolve

    show semen_room_table_night_foreground_card with dissolve

    show semen_room_table_night_foreground_phone_day2_bank as semen_room_table_night_foreground_phone zorder 1 with dissolve

    "Всего несколько кликов - готово!" with dissolve

    show semen_room_table_night_foreground_phone as semen_room_table_night_foreground_phone zorder 1 with dissolve

    hide semen_room_table_night_foreground_card_hands

    show semen_room_table_night_foreground_card zorder 2

    "Я купил билеты себе и Алие на завтра из Минеральных Вод в Москву, а также билеты для себя в Минеральные Воды на сегодня." with dissolve

    show cg_screen_you_were_added_yarik

    messenger "Вас добавили: Ярик"  with dissolve # with hpunch

    hide cg_screen_you_were_added_yarik

    $ changeDialogToYarik()

    $ showMessengerWithRightOrder()

    $ addReceivedMessage(4)

    yarik "Привет, Семён! Слышал про твою историю." with dissolve

    $ addReceivedMessage(3)

    yarik "Буду рад помочь." with dissolve

    $ addReceivedMessage(4)

    yarik "Я сейчас же соберусь, примчусь к тебе и подброшу прямо до терминала!" with dissolve

    $ addReceivedMessage(3)

    yarik "Через час ты уже будешь там, можешь начинать отсчёт!" with dissolve

    $ addSentMessage(1)

    me "Спасибо большое!" with dissolve

    $ addReceivedMessage(3)

    yarik "Я напишу, как буду у твоего дома. Держись!" with dissolve

    $ addSentMessage(0)

    me "Спасибо!" with dissolve

    "Кажется, удача сегодня на моей стороне." with dissolve

    "Все препятствия словно магическим образом исчезают на моём пути." with dissolve

    "Деньги есть, хоть и кредитные. Заказов по работе, конечно, много висит, но дедлайны еще далеко, можно чуть отдохнуть." with dissolve

    "Авиабилеты есть, в аэропорт я успею вовремя. Надо сообщить Алие!" with dissolve

    $ changeDialogToAliya()

    $ showMessengerWithRightOrder()

    $ addSentMessage(4)

    me "Я купил билеты. Буду ждать тебя завтра утром в 10 часов в аэропорту." with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Хорошо!" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Встречаемся возле главного входа?" with dissolve

    $ addSentMessage(3)

    me "Да, буду ждать тебя там." with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Спасибо!" with dissolve

    $ addSentMessage(3)

    me "Возьми с собой все свои документы: паспорт, ИНН." with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Паспорт у меня есть." with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "ИНН лежит где-то в шкафу. Мне его найти и взять с собой?" with dissolve

    $ addSentMessage(5)

    me "Да, ИНН нужен чтобы устроится на работу. Если не найдёшь оригинал, возьми хотя бы копию." with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Ладно..." with dissolve

    $ addSentMessage(5)

    me "Запомнила план? Утром притворись, что идёшь в колледж и вместо этого езжай на автобусе в аэропорт." with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Поняла!" with dissolve

    "Что же, пора собираться." with dissolve

    $ addSentMessage(3)

    me "Желаю тебе удачи! Уверен, у тебя всё будет хорошо!" with dissolve

    $ addSentMessage(3)

    me "Я сейчас буду собираться и поеду в аэропорт." with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Спасибо. Я тоже начну собираться." with dissolve

    scene black with dissolve

    "Времени было мало..." with dissolve

    show black zorder 20

    show semen_room_night

    show semen_room_night_backpack

    hide black with dissolve

    $ savegame_picture = "savegame_semen_room_night"

    "Я достал свой старый рюкзак из шкафа и кинул его в центр комнаты." with dissolve

    "Уже долгое время я не покидал родной город и за это время рюкзак успел заметно покрыться пылью." with dissolve

    "Я наскоро оттряхнул его и начал скидывать в него свои шмотки." with dissolve

    "Не знаю даже, на сколько я покидаю свой дом... На несколько дней? Недель?" with dissolve

    "Поэтому мне нужно взять с собой средства гигиены, сменную одежду, носки." with dissolve

    "Конечно же, зарядные устройства, павербанки, переносные жёсткие диски." with dissolve

    "Последним я положу в свой рюкзак ноутбук - думаю, мне понадобится работать удаленно и быть на связи с заказчиками." with dissolve

    "Я бегал по всей квартире, заглядывая во все углы - вдруг мне что-то понадобится или я что-нибудь забуду." with dissolve

    scene black with dissolve

    #$ renpy.start_predict("images/CG_messenger_phone/*.*")

    "Сборы вышли довольно быстрыми, как ни странно..." with dissolve

    show black zorder 20

    show semen_room_night_empty

    show semen_room_night_backpack

    hide black with dissolve

    "Наконец все вещи вроде бы собраны. Ноутбук я тоже запаковал в рюкзак." with dissolve

    "Ярик должен быть с минуты на минуту. Я вздохнул и окинул взглядом свою квартиру." with dissolve

    "Не думаю, что задержусь в Москве надолго. Но всё равно, было такое странное чувство." with dissolve

    "Если я уезжаю отдохнуть, всегда знаю когда приеду." with dissolve

    "Но сейчас всё произошло так резко. Готов ли я покинуть привычную квартиру и отправиться навстречу приключениям?" with dissolve

    messenger "Новое сообщение"

    show cg_screen_phone_new_message_day2_night1 as cg_screen_phone with dissolve

    "Я достал телефон." with dissolve

    $ switchMessengerToPhone()

    $ changeDialogToYarik()

    $ showMessengerPhone(is_night=True, force_no_transition=True)

    $ addReceivedMessage(3)

    yarik "Я приехал и жду тебя во дворе. Купе красного цвета." with dissolve

    $ addSentMessage(2)

    # The rest if cut_scene0
    $ last_playing_music = "playRunaway04"

    $ music_stage_preload = "music_Runaway03"

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("music_stage_preload = \"" + music_stage_preload + "\"")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracks(stopAllMusic, playRunaway03)")

    me "Хорошо! Выхожу..." with dissolve

    #$ renpy.stop_predict("images/cg_screen/*.*")
    #$ renpy.stop_predict("images/CG_messenger_desktop/*.*")
    #$ renpy.stop_predict("images/semen_room*.*")
    #$ renpy.stop_predict("images/CG_hands/Card.png")

    jump cutscene0
