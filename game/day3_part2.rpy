
label day3_metro:

    if isMobileWeb:
        $ renpy.free_memory()

    scene underground with dissolve

    $ savegame_picture = "savegame_underground"

    play music "ambience/metro_station.ogg" fadein 1.0 fadeout 1.0

    "Поток людей шёл из вагонов аэроэкспресса на перрон, затем на вокзал и в метро." with dissolve

    "По пути к метро мужчины кричали нам вслед \"Такси недорого!\", надеясь, что мы не будем спускаться в подземку." with dissolve

    "Здесь же где-то рядом в сторонке предлагали бесплатные сим-карты." with dissolve

    "Я не представляю зачем кому-то раздавать бесплатные сим-карты, но чувствую в этом какой-то подвох." with dissolve

    "Лучше будет просто зарегистрировать новую симку на своё имя и отдать Алие." with dissolve

    "Ладно, потом разберёмся. Сейчас нужно купить карту \"Тройка\"." with dissolve

    show Aliya_stand_straight eyes_open_sad_worried_open_mouth as Aliya at any_center_pos with dissolve:
        zoom 1.0

    aliya "В кассу всегда такая большая очередь?" with dissolve

    me "Здесь вокзал, поэтому да." with dissolve

    me "Но я слышал, что карту тройка можно купить и в автомате." with dissolve

    show Aliya_stand_straight eyes_open_sad_smile as Aliya at any_center_pos with dissolve:
        zoom 1.0

    aliya "Я хочу попробовать купить в автомате!" with dissolve

    me "Давай попробуем." with dissolve

    "Как раз рядом стоял большой красно-серый шкаф с надписью \"Автомат продажи проездных билетов метрополитена\"." with dissolve

    hide Aliya with dissolve

    show Aliya_stand_half_turned jacket_armsdown eyes_open_watching_phone as Aliya at aliya_metro_buy_card_pos with dissolve:
        zoom 0.6*SCALE

    aliya "Вот \"получить карту Тройка\", нажимаю сюда?" with dissolve

    me "Да." with dissolve

    aliya "Залоговая стоимость 50 рублей. Что это значит?" with dissolve

    me "Что за 50 рублей ты покупаешь карточку, на которой ноль рублей. И потом её нужно пополнить." with dissolve

    aliya "Значит, на сколько мне нужно пополнить?" with dissolve

    me "Пополни на двести рублей, на сегодня нам хватит." with dissolve

    aliya "50 за карту и 150 рублей на неё, да?" with dissolve

    me "Да." with dissolve

    "Алия бодро потыкала в сенсорный экран, затем скормила автомату две сотенные купюры. Автомат выдал в ответ маленькую синюю карточку." with dissolve

    show Aliya_stand_straight eyes_open_sad_worried as Aliya at aliya_metro_buy_card_straight_pos with dissolve:
        zoom 0.6*SCALE

    "Затем Алия повернулась ко мне, взглянув вопросительно." with dissolve

    aliya "А тебе надо?" with dissolve

    me "У меня уже есть, я бывал здесь раньше." with dissolve

    show Aliya_stand_straight eyes_open_neutral as Aliya at aliya_metro_buy_card_straight_pos with dissolve:
        zoom 0.6*SCALE

    aliya "Хорошо." with dissolve

    "Мы отошли от автомата..." with dissolve

    scene black with dissolve

    "Затем прошли через турникеты и спустились в метро..." with dissolve

    jump day3_metro_train


label day3_metro_train:


    stop music_crossfade fadeout 1.0

    stop music fadeout 1.0

    play music "ambience/metro_loop_before_train_depart.ogg" fadein 1.0 fadeout 1.0


    show metro_train at metro_scene_pos with dissolve:
        zoom 1.05

    $ savegame_picture = "savegame_metro_train"

    show Aliya_stand_straight eyes_open_neutral as Aliya at any_center_pos with dissolve:
        zoom 1.0

    "Мы вошли в вагон." with dissolve

    me "Далеко не проходи, нам на следующей станции выходить." with dissolve

    aliya "Ладно." with dissolve

    play music "ambience/metro_doors_closing.ogg"

    queue music "ambience/metro_train_loop.ogg"

    announcement "Осторожно, двери закрываются, следующая станция - Таганская" with dissolve

    "Двери шумно закрылись." with dissolve

    "Поезд начал разгоняться. Я ожидал, что в вагоне будет очень шумно, однако внутри было на удивление тихо." with dissolve

    "Можно было даже спокойно говорить голосом." with dissolve

    show Aliya_stand_straight eyes_open_sad_worried_open_mouth as Aliya at any_center_pos with dissolve:
        zoom 1.0

    aliya "Куда мы пойдём теперь?" with dissolve

    show Aliya_stand_straight eyes_open_sad_worried as Aliya at any_center_pos with dissolve:
        zoom 1.0

    me "Сейчас посмотрю по карте." with dissolve

    show cg_screen_phone_map2 as cg_screen_phone with dissolve

    "Я запустил приложение с картами и проложил маршрут." with dissolve

    me "Нам нужно перейти на станцию Марксистская, затем на выход номер 5." with dissolve

    show Aliya_stand_straight eyes_closed_grin as Aliya at any_center_pos with dissolve:
        zoom 1.0

    aliya "Хорошо." with dissolve

    show Aliya_stand_straight eyes_open_smile as Aliya at any_center_pos with dissolve:
        zoom 1.0

    me "Оттуда нужно будет идти вдоль по Таганской улице." with dissolve

    me "Кажется, там будет что-то типа парка или сквера." with dissolve

    me "И где-то рядом со сквером есть магазин мусульманских товаров." with dissolve

    aliya "Ладно." with dissolve

    $ hidePhone()

    "Я убрал телефон." with dissolve

    "Поезд метро мчался по тоннелю, слегка шатаясь." with dissolve

    "Я осмотрелся. Пассажиров в этом вагоне было довольно мало." with dissolve

    "Возможно, потому что сейчас самый разгар рабочего дня." with dissolve

    "Поезд довольно быстро приехал на нужную нам станцию." with dissolve

    play music "ambience/metro_arrived.ogg"

    queue music "ambience/metro_loop_after_arrival.ogg"

    announcement "Станция Таганская. Переход на Таганско-Краснопресненскую линию и станцию Марксистская." with dissolve

    "За моей спиной тоннель сменился перроном станции метро Таганская." with dissolve

    "Я осмотрелся. Все остальные пассажиры в вагоне оставались на своих местах." with dissolve

    "Кажется, мы единственные, кто собрались выходить на этой станции." with dissolve

    me "Пойдём?" with dissolve

    aliya "Пойдём." with dissolve

    "Двери открылись и мы вышли наружу." with dissolve

    play music "music/Runaway_09 (Pre_Loop).ogg" fadein 1.0

    queue music "music/Runaway_09 (Loop).ogg"

    scene black with dissolve

    #$ renpy.stop_predict("images/sprites/Aliya/Pose1/*.*")
    #$ renpy.stop_predict("images/sprites/Aliya/Pose1/mask1/*.*")
    #$ renpy.stop_predict("images/sprites/Aliya/Pose2/*.*")
    #$ renpy.stop_predict("images/sprites/Aliya/Pose2/mask2/*.*")

    #$ renpy.start_predict("images/sprites/Aliya/Pose4/*.*")

    $ renpy.pause(1.0)

    jump day3_taganskaya


label day3_taganskaya:

    scene taganskaya_street with dissolve

    $ savegame_picture = "savegame_taganskaya_street"

    show aliya_turn_around eyes_open_watching as Aliya at any_left_pos with dissolve:
        zoom 1.0

    "Мы вышли из метро и шли вдоль Таганской улицы." with dissolve

    "Тёплая приятная погода согревает не только тело, но и душу, придавая уверенности и веры в успех." with dissolve

    "Солнце ярко освещало наш путь, постепенно идя к закату." with dissolve

    "Погода стояла хорошая. Вокруг нас было много людей, разных...по-разному одетых." with dissolve

    "Мы лавировали в разношёрстной толпе, стараясь ни с кем не столкнуться." with dissolve

    "Мимо нас проходили школьники с вейпами, рядом шла уверенная в себе бизнес-леди." with dissolve

    "Чуть поодаль - бородатый мужчина, а где-то в стороне стояли почтённого возраста москвички." with dissolve

    "Вот проехал молодой человек на гироскутере." with dissolve

    "Здесь, на шумных улицах Москвы, легко затеряться, потому что никому нет до тебя дела." with dissolve

    "Алия прервала молчание." with dissolve

    show aliya_turn_around eyes_open_happy as Aliya at any_left_pos with dissolve:
        zoom 1.0

    aliya "Здесь так красиво. Мне здесь нравится." with dissolve

    me "Да, мне тоже." with dissolve

    me "Хотя если честно, в Москве есть места и покрасивее." with dissolve

    show aliya_turn_around eyes_open_surprised_happy as Aliya at any_left_pos with dissolve:
        zoom 1.0

    aliya "Правда? Какие?" with dissolve

    $ persistent.gallery4unlock = True

    me "Парк Горького и Крымскую набережную очень красиво сделали." with dissolve

    me "Пешеходные улицы вокруг Большой Дмитровки." with dissolve

    me "И парк Зарядье, кстати, тоже очень хорошо сделали." with dissolve

    me "Мы можем посетить их завтра." with dissolve

    show aliya_turn_around eyes_closed_smile as Aliya at any_left_pos with dissolve:
        zoom 1.0

    aliya "Хорошо!" with dissolve

    scene black with dissolve

    "Мы продолжили наш путь вдоль Таганской улицы..." with dissolve

    scene tagansky_park with dissolve

    $ savegame_picture = "savegame_tagansky_park"

    show aliya_turn_around eyes_open_smile as Aliya at any_left_pos with dissolve:
        zoom 1.0

    "Вскоре мы свернули с улицы, и через дворы прошли в Таганский парк." with dissolve

    "Вокруг нас шли мамы с колясками, рядом бегали мальчики. Кто-то катался на скейтбордах, на роликах." with dissolve

    "Атмосфера была невероятно умиротворяющей и неторопливой." with dissolve

    me "Магазин мусульманской одежды находится где-то здесь, но что-то я пока не вижу его." with dissolve

    me "Вот какое-то здание из стекла и пластика, возможно это он. Пойдём туда!" with dissolve

    show aliya_turn_around eyes_open_cry_sad2 as Aliya at any_left_pos with dissolve:
        zoom 1.0

    aliya "Я устала! Давай сядем отдохнём?" with dissolve

    menu:

        "Отдохнем?"

        "Да, сядем отдохнём.":
            jump day3_taganskaya_park_rest

        "Нет, идём дальше.":
            jump day3_taganskaya_park_continue


label day3_taganskaya_park_rest:

    $ aliya_trust_points_hard = aliya_trust_points_hard + 1 # aliya_trust_points by that point max = 4

    me "Хорошо, давай отдохнём!" with dissolve

    "Мы нашли свободную скамейку и сели." with dissolve

    scene black with dissolve

    #$ renpy.stop_predict("images/sprites/Aliya/Pose4/*.*")

    #$ renpy.start_predict("images/sprites/Aliya/Sitting2/bench/*.*")

    $ renpy.pause(1.0)

    scene tagansky_park_sit with dissolve

    $ savegame_picture = "savegame_tagansky_park_sit"

    show aliya_sit_side earphones eyes_open_watching_phone as Aliya at any_center_pos with dissolve:
        zoom SCALE

    "Алия внимательно наблюдала за посетителями парка." with dissolve

    "Высокие деревья приятно шелестели на ветру и скрывали нас от солнца." with dissolve

    show aliya_sit_side earphones eyes_open_sad_smile as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Здесь красиво." with dissolve

    me "Да, мне тоже тут нравится." with dissolve

    show aliya_sit_side earphones eyes_open_happy as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Здесь не как в Пятигорске." with dissolve

    aliya "Люди, дома, машины - в этом месте всё другое." with dissolve

    aliya "В Пятигорске тоже хорошо, но там видно что это маленький город." with dissolve

    me "Тебе понравилось бы тут жить?" with dissolve

    show aliya_sit_side earphones eyes_open_sad_worried_open_mouth as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Наверное, да. Если честно, всё равно я буду скучать по Дагестану." with dissolve

    show aliya_sit_side earphones eyes_open_sad_worried as Aliya at any_center_pos with dissolve:
        zoom SCALE

    me "Да. Здесь город, а в Дагестане природа, горы, свежий воздух." with dissolve

    show aliya_sit_side earphones eyes_open_smile as Aliya at any_center_pos with dissolve:
        zoom SCALE

    "Алия посмотрела на меня и улыбнулась." with dissolve

    aliya "Дагестан это не только горы! У нас есть много интересного!" with dissolve

    aliya "Мы когда-то всей семьей ездили в Дербент, там есть красивая старинная крепость." with dissolve

    aliya "А еще недалеко от моего села есть пустыня, я там тоже была!" with dissolve

    me "Пустыня? Из песка?" with dissolve

    aliya "Да! Из песка." with dissolve

    me "Ты смелая. Я бы побоялся заходить далеко в пустыню." with dissolve

    show aliya_sit_side earphones eyes_open_sad_worried_open_mouth as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Почему?" with dissolve

    show aliya_sit_side earphones eyes_open_sad_worried as Aliya at any_center_pos with dissolve:
        zoom SCALE

    me "Вдруг потеряюсь и так и умру в песках от жары и жажды." with dissolve

    show aliya_sit_side earphones eyes_closed_grin as Aliya at any_center_pos with dissolve:
        zoom SCALE

    "Алия усмехнулась." with dissolve

    show aliya_sit_side earphones eyes_open_happy as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Да эта пустыня же маленькая! В ней невозможно заблудиться!" with dissolve

    me "Маленькая?" with dissolve

    show aliya_sit_side earphones eyes_open_smile as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Очень маленькая!" with dissolve

    aliya "Если приедешь в Дагестан, я тебе обязательно покажу!" with dissolve

    show aliya_sit_side earphones eyes_closed_smile as Aliya at any_center_pos with dissolve:
        zoom SCALE

    me "Договорились!" with dissolve

    show aliya_sit_side earphones eyes_open_smile as Aliya at any_center_pos with dissolve:
        zoom SCALE

    show cg_screen_phone_shoot1_time as cg_screen_phone with dissolve

    "Я достал телефон, чтобы проверить время." with dissolve

    show cg_screen_phone_shoot2 as cg_screen_phone

    "Но взглянув на Алию, я решил переключиться на камеру..." with dissolve

    show cg_screen_phone_shoot2 as cg_screen_phone at any_center_pos:
        xpos 0.5
        linear 0.5 xpos 0.25

    $ var_day3_photo_made = True

    show cg_screen_phone_shoot_anim as cg_screen_phone with dissolve

    "И незаметно сфотографировал её." with dissolve

    show cg_screen_phone_aliya_photo1 as cg_screen_phone with dissolve

    show aliya_sit_side earphones eyes_open_happy as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Ты что меня сфоткал?" with dissolve

    show aliya_sit_side earphones eyes_open_smile as Aliya at any_center_pos with dissolve:
        zoom SCALE

    $ hidePhone()

    me "Да..." with dissolve

    show aliya_sit_side earphones eyes_open_playful as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Отправишь кому-нибудь - убью!" with dissolve

    me "Ладно..." with dissolve

    $ persistent.gallery5unlock = True

    scene black with dissolve

    "Прошло ещё немного времени..." with dissolve

    scene tagansky_park_sit with dissolve

    show aliya_sit_side earphones eyes_open_smile as Aliya at any_center_pos with dissolve:
        zoom SCALE

    me "Нам пора идти. Отдохнула?" with dissolve

    show aliya_sit_side earphones eyes_open_sad_worried_open_mouth as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Да, можно идти дальше!" with dissolve

    scene black with dissolve

    #$ renpy.stop_predict("images/sprites/Aliya/Sitting2/bench/*.*")

    #$ renpy.start_predict("images/sprites/Aliya/Pose1/*.*")
    #$ renpy.start_predict("images/sprites/Aliya/Pose1/mask1/*.*")
    #$ renpy.start_predict("images/sprites/Aliya/Pose2/*.*")
    #$ renpy.start_predict("images/sprites/Aliya/Pose2/mask2/*.*")

    #$ renpy.start_predict("images/sprites/Aliya/dress*.*")

    "Мы встали со скамейки и пошли туда, где, предположительно, был магазин..." with dissolve

    jump day3_taganskaya_park_continue

label day3_taganskaya_park_continue:

    show tagansky_store with dissolve

    $ savegame_picture = "savegame_tagansky_store"

    "Я угадал, действительно - странное здание оказалось небольшим торговым центром, точнее даже - рынком." with dissolve

    "Внутри были магазин, в котором продавалась мусульманская одежда и аксессуары. Мы зашли внутрь." with dissolve

    show Aliya_stand_straight eyes_open_sad_worried as Aliya at any_right_pos with dissolve:
        zoom 1.0

    "Алия нашла продавщицу и подошла к ней." with dissolve

    show saleswoman neutral at any_left_pos with dissolve:
        zoom 1.0

    show Aliya_stand_straight eyes_open_sad_worried_open_mouth as Aliya at any_right_pos with dissolve:
        zoom 1.0

    aliya "У вас есть платье для намаза на мой размер?" with dissolve

    show Aliya_stand_half_turned jacket_armsdown eyes_open_sad_worried as Aliya at any_right_pos with dissolve:
        zoom 1.0

    "Продавщица оценила Алию взглядом." with dissolve

    show saleswoman talking at any_left_pos with dissolve:
        zoom 1.0

    saleswoman "У нас все платья большого размера..." with dissolve

    saleswoman "Впрочем, примерьте это и вот это платье." with dissolve

    show saleswoman neutral at any_left_pos with dissolve:
        zoom 1.0

    aliya "Хорошо!" with dissolve

    hide Aliya with dissolve

    hide saleswoman with dissolve

    show tagansky_store_fitting_room_closed as tagansky_store with dissolve

    show cg_screen_phone_day3_afternoon_muslim_store as cg_screen_phone with dissolve

    "Я не люблю участвовать в шоппинге, поэтому отошёл в сторонку, прислонился к стене и достал телефон..." with dissolve

    show cg_screen_phone_day3_afternoon_muslim_store_new_message as cg_screen_phone with dissolve

    messenger "Новое сообщение" with dissolve

    $ changeDialogToCoach()

    $ showMessengerPhone(is_night=False, force_no_transition=True)

    $ addReceivedMessage(4)

    coach "Привет, Семён! Недалеко от вас сдаётся посуточно квартира, на Бауманской." with dissolve

    $ addReceivedMessage(4)

    coach "Квартира забронирована на неделю. Оплатите наличными лично хозяйке в руки." with dissolve

    $ addReceivedMessage(5)

    coach "Скидываю вам адрес и телефон. Пока мы договорились, что хозяйка приедет туда после шести и передаст вам ключи." with dissolve

    $ addSentMessage(2)

    me "Спасибо большое!" with dissolve

    $ addReceivedMessage(3)

    coach "Не за что! Держи меня в курсе!" with dissolve

    $ clearDisplayMessages()

    $ hidePhone()

    "Я убрал телефон." with dissolve

    show tagansky_store as tagansky_store with dissolve

    show Aliya special_dress_worried as Aliya at any_right_pos with dissolve:
        zoom 1.0

    "Алия вышла из примерочной." with dissolve

    aliya "Как я выгляжу?" with dissolve

    me "Тебе очень идёт!" with dissolve

    show Aliya special_dress_eye_closed as Aliya at any_right_pos with dissolve:
        zoom 1.0
        alpha 1.0

    aliya "Спасибо!" with dissolve

    show Aliya special_dress_smile as Aliya at any_right_pos with dissolve:
        zoom 1.0
        alpha 1.0

    aliya "Мне оно тоже нравится." with dissolve

    $ persistent.gallery6unlock = True

    aliya "Берём?" with dissolve

    me "Да, хорошо." with dissolve

    show saleswoman talking at any_left_pos with dissolve:
        zoom 1.0
        alpha 1.0

    saleswoman "У нас как раз на это платье скидка будет!" with dissolve

    show saleswoman neutral at any_left_pos with dissolve:
        zoom 1.0
        alpha 1.0

    show Aliya special_dress_worried as Aliya at any_right_pos with dissolve:
        zoom 1.0
        alpha 1.0

    aliya "Мне ещё нужен коврик для намаза." with dissolve

    show saleswoman talking at any_left_pos with dissolve:
        zoom 1.0
        alpha 1.0

    saleswoman "Конечно! Вам какой? Есть синий вот, есть зелёный." with dissolve

    show saleswoman neutral at any_left_pos with dissolve:
        zoom 1.0
        alpha 1.0

    aliya "Зелёный дайте, пожалуйста!" with dissolve

    show saleswoman talking at any_left_pos with dissolve:
        zoom 1.0
        alpha 1.0

    saleswoman "Конечно, сейчас!" with dissolve

    show saleswoman neutral at any_left_pos with dissolve:
        zoom 1.0
        alpha 1.0

    aliya "Я переоденусь обратно." with dissolve

    hide Aliya with dissolve

    show tagansky_store_fitting_room_closed as tagansky_store with dissolve

    "Алия ушла в примерочную." with dissolve

    show saleswoman talking at any_left_pos with dissolve:
        zoom 1.0

    saleswoman "Вы будете оплачивать наличными или картой?" with dissolve

    saleswoman "Мы карты не принимаем, но вы можете отправить по номеру карты..." with dissolve

    show saleswoman neutral at any_left_pos with dissolve:
        zoom 1.0

    me "Я заплачу наличными." with dissolve

    "Я отдал деньги. Продавщица начала запаковывать вещи в пакет." with dissolve

    hide saleswoman with dissolve

    show tagansky_store as tagansky_store with dissolve

    show Aliya_stand_straight eyes_open_smile as Aliya at any_center_pos with dissolve:
        zoom 1.0

    aliya "Платье есть, коврик есть! Что ещё осталось?" with dissolve

    me "Теперь нужно сделать тебе сим-карту." with dissolve

    me "Ах да, я нашёл жильё. Мы будем снимать квартиру." with dissolve

    show Aliya_stand_straight eyes_open_sad_worried_open_mouth as Aliya at any_center_pos with dissolve:
        zoom 1.0

    aliya "Квартира далеко отсюда?" with dissolve

    show Aliya_stand_straight eyes_open_neutral as Aliya at any_center_pos with dissolve:
        zoom 1.0

    me "Да, нужно ехать на метро Бауманская." with dissolve

    me "Предлагаю поехать туда и там же в салоне сотовой связи сделать тебе сим-карту. Хорошо?" with dissolve

    show Aliya_stand_straight eyes_closed_smile at any_center_pos with dissolve:
        zoom 1.0

    aliya "Да, пошли!" with dissolve

    scene black with dissolve

    #$ renpy.stop_predict("images/sprites/Aliya/dress*.*")

    #$ renpy.stop_predict("images/sprites/Aliya/Pose1/*.*")
    #$ renpy.stop_predict("images/sprites/Aliya/Pose1/mask1/*.*")
    #$ renpy.stop_predict("images/sprites/Aliya/Pose2/*.*")
    #$ renpy.stop_predict("images/sprites/Aliya/Pose2/mask2/*.*")

    #$ renpy.start_predict("images/sprites/Aliya/Pose4/*.*")

    "И мы отправились в путь до станции Бауманская..." with dissolve

    jump day3_basmannaya_outside

label day3_basmannaya_outside:

    scene baymanskaya with dissolve

    $ savegame_picture = "savegame_baymanskaya"

    show cg_screen_phone_map_to_cellphone_store as cg_screen_phone


    show aliya_turn_around eyes_open_watching as Aliya at any_left_pos with dissolve:
        zoom 1.0

    "Мы вышли из метро Бауманская и пошли к салону сотовой связи, следуя за проложенным по навигатору маршрутом." with dissolve

    "Приложение с картами вело нас вдоль широкой улицы с трамвайными путями." with dissolve

    "Время уже было позднее, вокруг потихоньку закрывались некоторые магазины." with dissolve

    "Вокруг быстро темнело. Рабочий день закончился и люди возвращались из офисов домой." with dissolve

    "Я заметил также, что по мере того, как заходило солнце, Алия становилась всё более мрачной." with dissolve

    "Моё внимание привлекло кафе-кулинария. Наверное, нужно купить еду на вечер, пока не поздно?" with dissolve

    $ hidePhone()

    me "Ты не хочешь есть?" with dissolve

    show aliya_turn_around eyes_open_sad_worried as Aliya at any_left_pos with dissolve:
        zoom 1.0

    aliya "Нет, не хочу." with dissolve

    me "Предлагаю всё-таки зайти внутрь и купить немного продуктов." with dissolve

    me "Пока кулинария ещё открыта, можем купить салатик или выпечку." with dissolve

    show aliya_turn_around eyes_open_sad_worried_open_mouth as Aliya at any_left_pos with dissolve:
        zoom 1.0

    aliya "Хорошо." with dissolve

    show aliya_turn_around eyes_open_sad_worried as Aliya at any_left_pos with dissolve:
        zoom 1.0

    "Мы вошли." with dissolve

    scene black with dissolve

    ##$ renpy.stop_predict("images/sprites/Aliya/Pose4/*.*")

    #$ renpy.start_predict("images/sprites/Aliya/Pose1/*.*")
    #$ renpy.start_predict("images/sprites/Aliya/Pose1/mask1/*.*")
    #$ renpy.start_predict("images/sprites/Aliya/Pose2/*.*")
    #$ renpy.start_predict("images/sprites/Aliya/Pose2/mask2/*.*")


    $ renpy.pause(1.0)

    scene baymanskaya_cafe with dissolve

    $ savegame_picture = "savegame_baymanskaya_cafe"

    show aliya_turn_around eyes_open_watching as Aliya at any_left_pos with dissolve:
        zoom 1.0

    "Внутри было светло и уютно." with dissolve

    "Мы подошли к витрине." with dissolve

    show aliya_turn_around eyes_open_sad_worried as Aliya at any_left_pos with dissolve:
        zoom 1.0

    me "Я возьму себе салат Цезарь и, две слойки с сыром. А чего бы тебе хотелось?" with dissolve

    show Aliya_stand_straight eyes_open_sad_worried as Aliya at any_left_pos with dissolve:
        zoom 1.0

    aliya "Я, наверное, ничего не хочу." with dissolve

    show Aliya_stand_straight eyes_closed_sad as Aliya at any_left_pos with dissolve:
        zoom 1.0

    me "Давай возьмем что-нибудь. Вдруг ты вечером захочешь?" with dissolve

    show Aliya_stand_straight eyes_open_sad_worried_open_mouth as Aliya at any_left_pos with dissolve:
        zoom 1.0

    aliya "Мне нужно что-нибудь без свинины. Есть тут такое?" with dissolve

    show Aliya_stand_straight eyes_open_sad_worried as Aliya at any_left_pos with dissolve:
        zoom 1.0

    me "Не знаю, никогда об этом не задумывался." with dissolve

    aliya "Давай я возьму оливье немного." with dissolve

    me "Хорошо!" with dissolve

    "Я заказал салаты, слойки и взял ещё бутылку воды." with dissolve

    "Продавец сложил продукты в пакет, я заплатил за покупку." with dissolve

    scene black with dissolve

    "Затем мы вышли..." with dissolve

    scene baymanskaya with dissolve

    $ savegame_picture = "savegame_baymanskaya"

    show cg_screen_phone_map_to_cellphone_store as cg_screen_phone

    show aliya_turn_around eyes_open_watching as Aliya at any_left_pos with dissolve:
        zoom 1.0

    "Приложение с картами сообщало, что рядом находился салон сотовой связи." with dissolve

    "Мы с Алией пошли туда." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    scene cellular with dissolve

    $ savegame_picture = "savegame_cellular"

    "Мы зашли в салон сотовой связи, находящийся неподалёку." with dissolve

    show Aliya_stand_straight eyes_open_sad_worried as Aliya at any_right_pos with dissolve:
        zoom 1.0

    show salesman talking at any_left_pos with dissolve:
        zoom 1.0

    salesman_cellular "Добрый день! Вам подсказать что-нибудь?" with dissolve

    show salesman neutral at any_left_pos with dissolve:
        zoom 1.0

    "Я протянул свой паспорт." with dissolve

    me "Сделайте пожалуйста сим-карту." with dissolve

    show salesman talking at any_left_pos with dissolve:
        zoom 1.0

    salesman_cellular "Да, пожалуйста. Вам какой оператор?" with dissolve

    show salesman neutral at any_left_pos with dissolve:
        zoom 1.0

    "Алия указала на рекламный плакат." with dissolve

    show Aliya_stand_half_turned jacket_armsdown eyes_open_sad_worried_open_mouth as Aliya at any_right_pos with dissolve:
        zoom 1.0

    aliya "Этот пожалуйста. У меня сейчас сим-карта этого оператора, уже все приложения стоят." with dissolve

    show Aliya_stand_half_turned jacket_armsdown eyes_open_watching_phone extra_stand_half_turned2_phone at any_right_pos with dissolve:
        zoom 1.0

    "Алия достала свой телефон и открыла приложение с личным кабинетом." with dissolve

    "Краем глаза я обратил внимание, что там отображается другое имя." with dissolve

    me "Сим-карта не на тебя оформлена?" with dissolve

    show Aliya_stand_half_turned jacket_armsdown eyes_open_neutral extra_stand_half_turned2_phone as Aliya at any_right_pos with dissolve:
        zoom 1.0

    aliya "Да, она оформлена на отца." with dissolve

    show Aliya_stand_half_turned jacket_armsdown eyes_closed_sad extra_stand_half_turned2_phone as Aliya at any_right_pos with dissolve:
        zoom 1.0

    "Алия выключила телефон и протянула его продавцу-консультанту." with dissolve

    scene black with dissolve

    "Прошло некоторое время подготовки документов..." with dissolve

    scene cellular with dissolve

    show Aliya_stand_half_turned jacket_armsdown eyes_open_neutral extra_stand_half_turned2_phone as Aliya at any_right_pos with dissolve:
        zoom 1.0

    show salesman talking at any_left_pos with dissolve:
        zoom 1.0

    salesman_cellular "Подпишите вот здесь и вот здесь. С вас 500 рублей." with dissolve

    show salesman neutral at any_left_pos with dissolve:
        zoom 1.0

    "Я подписал договор и оплатил банковской картой." with dissolve

    show salesman talking at any_left_pos with dissolve:
        zoom 1.0

    salesman_cellular "Сим-карта будет активна через 10-15 минут. Мобильный интернет там уже есть, звонки, СМС - всё работает." with dissolve

    salesman_cellular "Приятного использования!" with dissolve

    show salesman neutral at any_left_pos with dissolve:
        zoom 1.0

    me "Спасибо." with dissolve

    "Мы вышли из салона связи на улицу." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    jump day3_basmannaya



label day3_basmannaya:

    scene baymanskaya with dissolve

    $ savegame_picture = "savegame_baymanskaya"

    stop music fadeout 1.0

    play music "music/Runaway_10 (Pre_Loop).ogg" fadein 1.0

    queue music "music/Runaway_10 (Loop).ogg"

    show aliya_turn_around eyes_open_watching as Aliya at any_left_pos with dissolve:
        zoom 1.0

    "Выйдя из салона, мы снова оказались на Бауманской улице." with dissolve

    show cg_screen_phone_map_to_apartment as cg_screen_phone

    "Я снова открыл приложение с картами и вбил туда адрес съёмной квартиры." with dissolve

    show aliya_turn_around eyes_open_sad_worried as Aliya at any_left_pos with dissolve:
        zoom 1.0

    me "Судя по картам, отсюда до съёмной квартиры недалеко." with dissolve

    me "Кажется, надо пройти вдоль по улице, затем свернуть направо." with dissolve

    me "Там нужно будет войти во двор." with dissolve

    aliya "Хорошо, идём." with dissolve

    scene black with dissolve

    "И мы отправились в путь..." with dissolve

    scene apartment_hood with dissolve

    $ savegame_picture = "savegame_apartment_hood"

    show Aliya_stand_half_turned jacket_armsdown eyes_open_sad_worried as Aliya at any_left_pos with dissolve:
        zoom 1.0*0.9

    "Вот мы нашли дом и пришли к нужному подъезду." with dissolve

    "Я позвонил в домофон." with dissolve

    "Мне никто не ответил." with dissolve

    "Наверное, пришло время снова связаться с напарником." with dissolve

    $ changeDialogToCoach()

    $ showMessengerPhone(is_night=False, force_no_transition=True)

    "Я достал телефон и открыл мессенджер." with dissolve

    $ addSentMessage(4)

    me "Привет, хозяйка квартиры ещё не приехала?" with dissolve

    $ addReceivedMessage(2)

    coach "Кажется, нет ещё." with dissolve

    $ addReceivedMessage(4)

    coach "Она вроде писала, что может задержаться." with dissolve

    $ addReceivedMessage(2)

    coach "Сейчас напишу ей." with dissolve

    $ clearDisplayMessages()

    $ hidePhone()

    "Я убрал телефон." with dissolve

    show Aliya_stand_straight eyes_open_sad_much as Aliya at any_left_pos with dissolve:
        zoom 1.0*0.9

    "Когда я убрал телефон, Алия повернулась ко мне." with dissolve

    "Она выглядела встревоженной." with dissolve

    me "Ты в порядке?" with dissolve

    show Aliya_stand_straight eyes_open_sad_worried_open_mouth as Aliya at any_left_pos with dissolve:
        zoom 1.0*0.9

    aliya "Я должна сообщить родителям, чтобы не ждали меня. Они, наверное, уже волнуются." with dissolve

    "Да, рискованно конечно. Но я думаю, что лучше разрешить Алие сделать это. Сейчас мы уже в безопасности." with dissolve

    me "Хорошо. У тебя теперь новая сим-карта и там есть мобильный интернет." with dissolve

    me "Только не звони с нового номера, иначе родители вычислят твоё местоположение." with dissolve

    show Aliya_stand_straight eyes_open_sad_worried_question as Aliya at any_left_pos with dissolve:
        zoom 1.0*0.9

    aliya "Хорошо." with dissolve

    aliya "Я запишу аудиосообщение и отправлю в группу нашей семьи." with dissolve

    me "Окей." with dissolve

    aliya "Нам надо где-нибудь присесть." with dissolve

    me "Да, конечно, сейчас..." with dissolve

    "Как раз рядом с подъездом была свободная скамейка." with dissolve

    me "Присядем здесь?" with dissolve

    aliya "Хорошо." with dissolve

    scene black with dissolve

    #$ renpy.stop_predict("images/sprites/Aliya/Pose4/*.*")

    #$ renpy.stop_predict("images/sprites/Aliya/Pose1/*.*")
    #$ renpy.stop_predict("images/sprites/Aliya/Pose1/mask1/*.*")
    #$ renpy.stop_predict("images/sprites/Aliya/Pose2/*.*")
    #$ renpy.stop_predict("images/sprites/Aliya/Pose2/mask2/*.*")

    #$ renpy.start_predict("images/sprites/Aliya/Sitting2/bench/*.*")

    "И мы подошли поближе к подъезду" with dissolve

    scene basmannaya_hood with dissolve

    $ savegame_picture = "savegame_basmannaya_hood"

    show aliya_sit_side earphones eyes_open_sad_worried_question as Aliya at any_center_pos with dissolve:
        zoom SCALE

    " и присели на скамейку." with dissolve

    show aliya_sit_side phone eyes_closed_sad as Aliya at any_center_pos with dissolve:
        zoom SCALE

    "Алия вздохнула, достала телефон, выключила его и заменила сим-карту." with dissolve

    show aliya_sit_side phone eyes_open_watching_phone as Aliya at any_center_pos with dissolve:
        zoom SCALE

    "Затем включила снова..." with dissolve

    "Небольшая пауза..." with dissolve

    "Телефон завибрировал, принимая в себя сообщения из всех мессенджеров." with dissolve # with hpunch

    "Дождавшись, когда все уведомления стихнут, Алия открыла мессенджер и начала надиктовывать сообщение." with dissolve

    show aliya_sit_side phone eyes_open_watching_phone3 as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Папа и мама простите меня, пожалуйста." with dissolve

    aliya "Я знаю, что причиняю вам боль, но я долго думала и приняла решение." with dissolve

    aliya "Я не хочу выходить замуж и поэтому решила уйти." with dissolve

    aliya "Со мной всё хорошо, не ищите меня. Я уже далеко от дома." with dissolve

    aliya "Папа, я знаю, что у тебя нет денег чтобы оплатить мою учебу, но и выйти замуж я тоже не могу." with dissolve

    aliya "Поэтому я не хочу вам причинять проблем, и вследствие этого я решила уйти." with dissolve

    show aliya_sit_side phone eyes_closed_sad_worried_open_mouth as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Простите меня, пожалуйста, и не сердитесь." with dissolve

    show aliya_sit_side phone eyes_closed_sad as Aliya at any_center_pos with dissolve:
        zoom SCALE

    "Алия завершила запись и отправила сообщение в семейный групповой чат." with dissolve

    "... Что же, это было сильно и смело." with dissolve

    "Любовь к стихам и литературе помогла Алие научиться хорошо и красиво выражать свои мысли." with dissolve

    "Наверное, я должен сказать это вслух." with dissolve

    me "Отлично сказано!" with dissolve

    show aliya_sit_side phone eyes_open_cry_sad3 as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Спасибо." with dissolve

    show aliya_sit_side phone eyes_open_watching_phone as Aliya at any_center_pos with dissolve:
        zoom SCALE

    "Пришло новое сообщение. Это было ответное аудиосообщение." with dissolve # with hpunch

    "Алия включила его." with dissolve

    aslan "Алия, доченька моя! Да как ты могла подумать, что у меня не хватает денег?" with dissolve

    aslan "Пожалуйста, вернись домой, я тебя отправлю учиться куда ты хочешь!" with dissolve

    aslan "Где ты сейчас? Скажи, не молчи!" with dissolve

    show aliya_sit_side phone eyes_open_watching_phone4 as Aliya at any_center_pos with dissolve:
        zoom SCALE

    "Было видно, что Алия едва могла сдержать слёзы." with dissolve

    "Охх... Я никогда не умел утешать людей." with dissolve

    "Я решил, что нужно просто сидеть рядом и молчать." with dissolve

    "Алия тем временем дрожащим голосом записывала следующее сообщение." with dissolve

    show aliya_sit_side phone eyes_open_watching_phone3 as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Папа, со мной всё хорошо. Я долго думала и приняла такое решение." with dissolve

    aliya "Не надо искать меня, я уже далеко от дома." with dissolve

    aliya "Я люблю тебя и маму, но я не могу сделать так как ты хочешь." with dissolve

    aliya "Простите меня, пожалуйста." with dissolve

    show aliya_sit_side phone eyes_closed_sad_worried_open_mouth as Aliya at any_center_pos with dissolve:
        zoom SCALE

    "Затем Алия записала несколько фраз на аварском языке. Я не понял ни слова, конечно же." with dissolve

    show aliya_sit_side phone eyes_open_watching_phone as Aliya at any_center_pos with dissolve:
        zoom SCALE

    "Пришло ещё несколько сообщений от её отца на аварском языке." with dissolve # with hpunch

    show aliya_sit_side phone eyes_open_watching_phone3 as Aliya at any_center_pos with dissolve:
        zoom SCALE

    "Алия также записала ответ на аварском." with dissolve

    show aliya_sit_side phone eyes_open_watching_phone as Aliya at any_center_pos with dissolve:
        zoom SCALE

    "Я не понимал ни слова, но чувствовал, что ей очень тяжело говорить." with dissolve

    show aliya_sit_side earphones eyes_open_cry_sad3 as Aliya at any_center_pos with dissolve:
        zoom SCALE

    "Наконец, она в отчаянии включила авиарежим и посмотрела на меня." with dissolve

    show aliya_sit_side earphones eyes_closed_sad as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Семён, что мне делать?" with dissolve

    "Действительно, что нужно делать, если родители просят вернуться домой?" with dissolve

    "Все инстинкты подсказывают Алие вернуться к родителям, но страх перед свадьбой останавливает её." with dissolve

    "Надо сказать что-нибудь." with dissolve

    me "Твои родители волнуются за тебя," with dissolve

    me "ты хочешь, чтобы они не волновались." with dissolve

    me "Но в то же время не хочешь возвращаться домой." with dissolve

    show aliya_sit_side earphones eyes_open_sad_much as Aliya at any_center_pos with dissolve:
        zoom SCALE

    "Алия кивнула." with dissolve

    me "Потому что дома тебя ждёт свадьба." with dissolve

    aliya "Не просто свадьба. Родители же убьют меня." with dissolve

    aliya "Ну или отберут у меня телефон и запрут дома." with dissolve

    me "Ничего себе. Ты вовремя успела сбежать." with dissolve

    "Это я так попытался подбодрить Алию." with dissolve

    "Но она по-прежнему выглядела несчастной." with dissolve

    show aliya_sit_side earphones eyes_closed_sad_worried_open_mouth as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Мне нужно прекратить с ними общаться?" with dissolve

    show aliya_sit_side earphones eyes_open_sad_worried as Aliya at any_center_pos with dissolve:
        zoom SCALE

    "Действительно, стоит ли прекратить общаться с родителями?" with dissolve

    me "Я думаю, не будет ничего страшного, если ты будешь с ними общаться." with dissolve

    me "Если ты будешь им сообщать, что у тебя всё хорошо, им будет легче" with dissolve

    me "и они будут меньше за тебя переживать." with dissolve

    me "Только самое главное: не сообщай им свой номер телефона" with dissolve

    me "И своё местоположение." with dissolve

    me "Иначе они найдут и вернут тебя обратно." with dissolve

    "Кажется, в этом вопросе она была согласна со мной." with dissolve

    "Алия вздохнула." with dissolve

    show aliya_sit_side earphones eyes_open_cry_sad2 as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Ладно, я сообщила им, что у меня всё в порядке." with dissolve

    aliya "Мы можем идти дальше." with dissolve

    me "Давай ещё немного посидим. Тебе нужно успокоиться." with dissolve

    me "Мы всё равно должны дождаться хозяйку квартиры." with dissolve

    me "Ты за весь день так ничего и не съела. Нужно поесть хотя бы этот салатик." with dissolve

    show aliya_sit_side earphones eyes_closed_sad as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Я не хочу." with dissolve

    "Алия снова вздохнула." with dissolve

    scene black with dissolve

    #$ renpy.stop_predict("images/sprites/Aliya/Sitting2/bench/*.*")

    #$ renpy.start_predict("images/sprites/Aliya/Pose1/*.*")
    #$ renpy.start_predict("images/sprites/Aliya/Pose1/mask1/*.*")
    #$ renpy.start_predict("images/sprites/Aliya/Pose2/*.*")
    #$ renpy.start_predict("images/sprites/Aliya/Pose2/mask2/*.*")



    "Прошло немного времени..." with dissolve

    scene basmannaya_hood with dissolve

    show aliya_sit_side earphones eyes_open_cry_sad2 as Aliya at any_center_pos with dissolve:
        zoom SCALE

    messenger "Новое сообщение" with dissolve

    show cg_screen_phone_new_message_day3_evening_before_rent_apartment as cg_screen_phone with dissolve

    "Я снова достал телефон." with dissolve

    $ changeDialogToCoach()

    $ showMessengerPhone(is_night=False, force_no_transition=True)

    $ addReceivedMessage(1)

    coach "Хозяйка написала." with dissolve

    $ addReceivedMessage(4)

    coach "Говорит, уже приехала, припарковалась и идёт к вам." with dissolve

    $ addSentMessage(1)

    me "Отлично!" with dissolve

    $ clearDisplayMessages()

    $ hidePhone()

    "Я убрал телефон." with dissolve

    me "Ладно, можно вставать. Сейчас сюда придёт хозяйка." with dissolve

    aliya "Хорошо." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    scene apartment_hood with dissolve

    $ savegame_picture = "savegame_apartment_hood"

    show Aliya_stand_half_turned jacket_armsdown eyes_open_sad_worried as Aliya at any_right_pos with dissolve:
        zoom 1.0*0.9

    "Очень скоро к нам подошла женщина." with dissolve

    show realtor talking at any_left_pos with dissolve:
        zoom 1.0

    landlady "Добрый день, Семён, это вы?" with dissolve

    show realtor neutral at any_left_pos with dissolve:
        zoom 1.0

    me "Здравствуйте! Да, это я." with dissolve

    show realtor talking at any_left_pos with dissolve:
        zoom 1.0

    landlady "Пойдёмте я вам покажу квартиру..." with dissolve

    scene black with dissolve

    #$ renpy.start_predict("images/sprites/eating/*.*")
    #$ renpy.start_predict("images/sprites/eating/emotions_home/*.*")
    #$ renpy.start_predict("images/sprites/eating/emotions_cafe/*.*")

    "Мы вошли в подъезд вслед за хозяйкой и зашли в квартиру..." with dissolve

    scene apt_kitchen with dissolve

    $ savegame_picture = "savegame_apt_kitchen"

    show apt_kitchen_foreground zorder 1

    "Это была обычная квартира из тех, которые сдаются посуточно." with dissolve

    "Маленькой, но чистая. Из прихожей можно было сразу же пройти на кухню." with dissolve

    "Здесь было всё необходимое: холодильник, чайник, посуда, микроволновка." with dissolve

    "Хозяйка взяла оплату, оставила ключи и ушла." with dissolve

    scene apt_kitchen_near with dissolve

    show apartment_kitchen_food zorder 2 with dissolve

    "Я поставил продукты на стол, приготовил посуду." with dissolve

    show aliya_sit_meal tshirt eyes_open_sad_worried as Aliya with dissolve:
        zoom SCALE

    show apartment_kitchen_food as apartment_kitchen_food zorder 2

    "Затем мы сели за стол. Наконец-то я почувствовал насколько устал ходить по городу за сегодняшний день." with dissolve

    me "Предлагаю тебе съесть салат. Хотя бы немного." with dissolve

    show apartment_kitchen_food_no_spoon as apartment_kitchen_food zorder 2

    show aliya_sit_meal tshirt_spoon_up eyes_closed_sad as Aliya with dissolve:
        zoom SCALE

    "Алия по-прежнему выглядела немного растерянной, но всё равно взяла в руки ложку." with dissolve

    show aliya_sit_meal tshirt_spoon_up eyes_open_sad_worried_question as Aliya with dissolve:
        zoom SCALE

    aliya "Здесь точно нет свинины?" with dissolve

    "Я думаю, в этом салате нет настоящего мяса вообще." with dissolve

    me "Конечно нет." with dissolve

    show apartment_kitchen_food_no_spoon_eaten as apartment_kitchen_food zorder 2

    show aliya_sit_meal tshirt_spoon_food eyes_open_watching as Aliya with dissolve:
        zoom SCALE

    "Алия недоверчиво съела одну ложку салата. Затем ещё одну." with dissolve

    show aliya_sit_meal tshirt_spoon eyes_closed_sad as Aliya with dissolve:
        zoom SCALE

    aliya "Больше не хочется." with dissolve

    show aliya_sit_meal tshirt eyes_open_watching as Aliya with dissolve:
        zoom SCALE

    show apartment_kitchen_food_spoon_eaten as apartment_kitchen_food zorder 2

    "Я чувствую, что она по-прежнему сильно беспокоится за своих родителей." with dissolve

    "Наверное, я должен что-то сделать." with dissolve

    show aliya_sit_meal tshirt eyes_open_sad_much as Aliya with dissolve:
        zoom SCALE

    $ persistent.gallery7unlock = True

    me "Сообщи своим родителям, что у тебя всё в порядке: есть еда и ночлег." with dissolve

    me "Это должно их немного успокоить." with dissolve

    show aliya_sit_meal tshirt_phone eyes_open_watching as Aliya with dissolve:
        zoom SCALE

    "Алия снова достала телефон и выключила авиарежим." with dissolve

    "Затем включила мессенджер и стала слушать." with dissolve

    show aliya_sit_meal tshirt_phone eyes_open_sad_worried_open_mouth as Aliya with dissolve:
        zoom SCALE

    aliya "Папа уже обратился в отделение полиции в Пятигорске. Они меня ищут." with dissolve

    aliya "Наверное, они думают что меня похитили." with dissolve

    show aliya_sit_meal tshirt_phone eyes_open_watching as Aliya with dissolve:
        zoom SCALE

    "Алия продолжала слушать, пугаясь всё больше." with dissolve

    show aliya_sit_meal tshirt_phone eyes_open_sad_worried_open_mouth as Aliya with dissolve:
        zoom SCALE

    aliya "Пишут, что маме стало плохо." with dissolve

    aliya "Что я наделала!" with dissolve

    show aliya_sit_meal tshirt_phone eyes_open_talking_phone as Aliya with dissolve:
        zoom SCALE

    "Алия снова начала надиктовывать аудиосообщения в общий чат." with dissolve

    show aliya_sit_meal tshirt_phone eyes_open_sad_worried with dissolve:
        zoom SCALE

    aliya "Участковый тоже хочет со мной поговорить." with dissolve

    me "Что там?" with dissolve

    show aliya_sit_meal tshirt_phone eyes_closed_sad as Aliya with dissolve:
        zoom SCALE

    "Алия включила аудиосообщение." with dissolve

    police "Алия, вернись домой! Твои родители тебя ищут! Что ты ведешь себя как маленькая?!" with dissolve

    police "Родители тебя уже обыскались, а ты так безответственно сбежала!" with dissolve

    "Впрочем, чего ещё ждать от полицейских из Пятигорска?!" with dissolve

    show aliya_sit_meal tshirt_phone eyes_open_watching as Aliya with dissolve:
        zoom SCALE

    "Алия прослушала ещё несколько сообщений от матери." with dissolve

    show aliya_sit_meal tshirt_phone eyes_open_sad_worried as Aliya with dissolve:
        zoom SCALE

    aliya "Мама сейчас едет в Пятигорск искать меня." with dissolve

    show aliya_sit_meal tshirt_phone eyes_closed_sad_worried_open_mouth as Aliya with dissolve:
        zoom SCALE

    aliya "Они же до сих пор не знают, что я уже в Москве!" with dissolve

    show aliya_sit_meal tshirt_phone eyes_closed_sad as Aliya with dissolve:
        zoom SCALE

    "Это означает, что операция \"Побег\" прошла блестяще." with dissolve

    "Если бы у Алии был загранпаспорт, к этому моменту она вообще уже была бы в Корее, в аэропорту Сеула." with dissolve

    show aliya_sit_meal tshirt_phone eyes_open_watching as Aliya with dissolve:
        zoom SCALE

    "Алия продолжила слушать аудиосообщения." with dissolve

    show aliya_sit_meal tshirt_phone eyes_open_sad_worried_question as Aliya with dissolve:
        zoom SCALE

    aliya "Мама хочет позвонить мне по мессенджеру." with dissolve

    aliya "Как думаешь, стоит?" with dissolve

    "Если звонить по мессенджеру, мобильный номер не будет скомпрометирован." with dissolve

    me "Да, я думаю, стоит. Поговори с мамой и успокой её." with dissolve

    hide Aliya with dissolve

    "Алия взяла телефон и ушла в другую комнату, чтобы поговорить наедине с мамой." with dissolve

    "Я остался один с недоеденным салатом на столе." with dissolve

    scene black with dissolve

    scene apt_kitchen

    show black zorder 10

    show apt_kitchen_foreground zorder 1

    show apartment_kitchen_food_spoon_eaten as apartment_kitchen_food at apartment_kitchen_food_pos zorder 2:
        zoom SCALE

    hide black with dissolve

    "Я отрывочно слушал, о чём Алия говорит с матерью, но они почти всё время говорили на аварском и я мало что понимал." with dissolve

    "Иногда, впрочем, Алия переходила на русский и я слышал обрывки фраз." with dissolve

    aliya "Мам, никто меня не похищал! Я сама уехала!" with dissolve

    "Да, я представляю, о чём Алия говорит с мамой." with dissolve

    aliya "Мам, я не знаю адрес!" with dissolve

    show Aliya special_phone_give_take as Aliya at aliya_apartment_kitchen_stand_pos with dissolve:
        zoom 1.0

    "Алия вернулась на кухню и протянула мне телефон." with dissolve

    aliya "Моя мама хочет поговорить с тобой. Она хочет проверить, что ты хороший человек." with dissolve

    "Я мог бы и отказаться, но решил поговорить." with dissolve

    show Aliya_stand_straight tshirt eyes_open_neutral as Aliya at aliya_apartment_kitchen_stand_pos with dissolve:
        zoom 1.0

    "Я взял трубку, собрал всю свою доброжелательность и представил, что я на собеседовании с заказчиком." with dissolve

    me "Здраствуйте!" with dissolve

    fatima "Здраствуйте, Семён! Меня зовут Фатима." with dissolve

    "Её голос был усталый и строгий." with dissolve

    fatima "Я с вами хочу поговорить, как мать." with dissolve

    me "Конечно, я слушаю." with dissolve

    fatima "Скажите, Семён, вы женаты?" with dissolve

    me "Нет, я не женат." with dissolve

    fatima "Я хочу узнать, какие у вас намерения? Алия сбежала с вами, она доверилась вам." with dissolve

    fatima "Что вы хотите от неё?" with dissolve

    "Нелегко сформулировать ответ, но я постараюсь." with dissolve

    me "Алия попала в трудную ситуацию и я предложил ей помощь." with dissolve

    fatima "Я не понимаю, почему она вам доверяет больше, чем родной матери?" with dissolve

    "Ещё бы! Вы её замуж собрались выдать против её воли, а теперь спрашиваете, почему она доверяет мне больше, чем вам?!" with dissolve

    "Вслух я это говорить, конечно, не буду." with dissolve

    fatima "Семён, я вас хочу предупредить." with dissolve

    fatima "Алия очень молодая и наивная девушка." with dissolve

    fatima "Она ещё ни разу не была с мужчиной." with dissolve

    "Да понял я уже эти намеки, понял." with dissolve

    me "Да. Я понимаю, о чём вы говорите," with dissolve

    me "Конечно, я не трону Алию." with dissolve

    fatima "Хорошо, Семён. Я надеюсь, что вы хороший, порядочный человек." with dissolve

    fatima "Дайте трубку Алие, пожалуйста." with dissolve

    "Я передал трубку Алие." with dissolve

    hide Aliya with dissolve

    "Девушка взяла трубку и ушла в комнату." with dissolve

    "Теперь можно записать себе в резюме новый пункт - \"есть опыт переговоров с дагестанскими матерями\"." with dissolve

    "Алия мне рассказывала, что она очень любит маму." with dissolve

    "Хотя Алия говорила, что ей с трудом удается достучаться до мамы и как-то изменить её решение..." with dissolve

    show Aliya special_phone_listen as Aliya at aliya_apartment_kitchen_stand_pos with dissolve:
        zoom 1.0

    "А вот Алия вернулась." with dissolve

    show Aliya_stand_half_turned tshirt extra_tshirt_stand_half_turned2_hand_phone as Aliya at aliya_apartment_kitchen_stand_pos with dissolve:
        zoom 1.0

    aliya "Мама сказала, что разрешит остаться мне в Москве," with dissolve

    aliya "но она хочет приехать и увидеть меня." with dissolve

    aliya "Что ты думаешь?" with dissolve

    "Интересный поворот." with dissolve

    "Если это не обман, то всё складывается наилучшим образом для Алии." with dissolve

    me "Им можно верить?" with dissolve

    aliya "Я не знаю." with dissolve

    show Aliya special_phone_listen no_extra as Aliya at aliya_apartment_kitchen_stand_pos with dissolve:
        zoom 1.0

    "Мессенджер на телефоне Алии снова зазвонил. Алия взяла трубку." with dissolve

    "Алия поговорила с мамой по-аварски и повернулась ко мне." with dissolve

    aliya "Она хочет знать наш адрес." with dissolve

    me "Зачем?" with dissolve

    show Aliya special_phone_give_take as Aliya at aliya_apartment_kitchen_stand_pos with dissolve:
        zoom 1.0

    "Вместо ответа Алия протянула мне трубку." with dissolve

    show Aliya_stand_straight tshirt eyes_open_neutral as Aliya at aliya_apartment_kitchen_stand_pos with dissolve:
        zoom 1.0

    "Я взял телефон." with dissolve

    fatima "Семён, вы тут?" with dissolve

    me "Да, слушаю." with dissolve

    fatima "Семён, я все обдумала." with dissolve

    fatima "Если Алия не хочет выходить замуж и уехала в Москву, значит на то воля Аллаха." with dissolve

    fatima "Пусть работает там, учится." with dissolve

    fatima "У себя в селе я скажу всем, что Алия уехала учиться в Москву." with dissolve

    fatima "Я вижу, что вы хороший человек, поможете ей и не дадите в обиду." with dissolve

    me "Спасибо." with dissolve

    fatima "Только я хочу приехать к вам, посмотреть на Алию, убедится, что с ней всё в порядке." with dissolve

    fatima "Ради Аллаха, скажите адрес! Я завтра буду в Москве, приеду к вам и посмотрю, как вы живёте." with dissolve

    fatima "И потом уеду обратно в Дагестан, и не буду вам мешать." with dissolve

    "Интересное предложение. С одной стороны, это реальный шанс успокоить и Алию, и её родителей." with dissolve

    "С другой - а вдруг это ловушка?" with dissolve

    me "Вы приедете одна? Никакие больше родственники не приедут и не будут уговаривать Алию вернуться?" with dissolve

    fatima "Да, даю вам слово матери. Я приеду одна." with dissolve

    "Надо принять сложное решение." with dissolve

    "Если они хотят обмануть меня, то мне лучше не поддаваться и не выдавать свой адрес." with dissolve

    "Но если родители Алии действительно верят мне и согласны разрешить Алие переехать в Москву," with dissolve

    "мне стоит показать, что я им тоже доверяю и согласиться сказать адрес." with dissolve

    me "Алия, что думаешь?" with dissolve

    aliya "Я не знаю..." with dissolve

    menu:

      "Надо принять сложное решение:"

      "Сообщить адрес.":
          jump day3_basmannaya_apartment_accept

      "Не сообщать адрес.":
          jump day3_basmannaya_apartment_decline

label day3_basmannaya_apartment_accept:

    $ day3_address_told = True

    "Несколько лет назад в интернете была популярна страничка - игра про доверие." with dissolve

    "Там нужно было выбирать стратегию поведения: довериться оппоненту или предать его." with dissolve

    "Согласно дилемме заключенного, в одном конкретном раунде выгодно предать оппонента." with dissolve

    "Но если игра повторяется снова и снова с одним и тем же оппонентом, то стратегии, основанные на сотрудничестве, становятся выигрышнее." with dissolve

    "Поэтому, применительно к данной ситуации... моим первым ходом будет доверие." with dissolve

    me "Хорошо, я скажу вам адрес." with dissolve

    show Aliya_stand_straight tshirt eyes_open_smile as Aliya at aliya_apartment_kitchen_stand_pos with dissolve:
        zoom 1.0

    $ changeDialogToCoach()

    $ showMessengerPhone(is_night=False, force_no_transition=True)

    "Я достал свой телефон, посмотрел адрес съёмной квартиры и продиктовал его." with dissolve

    $ clearDisplayMessages()

    $ hidePhone()

    me "Приезжайте завтра. Утром скажете примерное время, когда вы приедете. Мы будем дома." with dissolve

    fatima "Спасибо, Семён! Вы хороший человек!" with dissolve

    me "Не за что! Увидимся завтра!" with dissolve

    "Я прекратил разговор и посмотрел на Алию." with dissolve

    stop music fadeout 1.0

    play music "music/Runaway_11 (Pre_Loop).ogg" fadein 1.0

    queue music "music/Runaway_11 (Loop).ogg"

    "Она улыбалась и, кажется, чувствовала невероятное облегчение." with dissolve

    "Глядя на неё я тоже улыбнулся." with dissolve

    "Алия всё-таки невероятно красива, тем более, когда улыбается." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    jump day3_basmannaya_apartment_after_talk


label day3_basmannaya_apartment_decline:

    "Скорее всего, они хотят узнать адрес, чтобы приехать и силой забрать Алию." with dissolve

    "Но этого не будет." with dissolve

    me "Нет, я не скажу вам адрес!" with dissolve

    me "Если хотите увидеть Алию, приезжайте в Москву. Когда приедете, обсудим." with dissolve

    fatima "Семён, я не буду вас обманывать! Почему вы мне не верите?" with dissolve

    me "Просто я думаю, что так будет лучше для Алии." with dissolve

    "Мать Алии замолчала на некоторое время, видимо обдумывая." with dissolve

    fatima "Хорошо, Семён. Пусть будет по-вашему." with dissolve

    fatima "Когда я приеду в Москву, мы договоримся о встрече. Хорошо?" with dissolve

    me "Хорошо! Увидимся завтра!" with dissolve

    fatima "Передайте трубку Алие, пожалуйста." with dissolve

    show Aliya special_phone_listen no_extra as Aliya at aliya_apartment_kitchen_stand_pos with dissolve:
        zoom 1.0

    "Я передал трубку Алие." with dissolve

    hide Aliya with dissolve

    "Алия ушла в другую комнату и продолжила разговор там." with dissolve

    "Я слышал, как Алия разговаривала с мамой, но я не понимал не слова." with dissolve

    "Впрочем, разговор был недолгим." with dissolve

    show Aliya_stand_straight tshirt eyes_open_sad_worried as Aliya at aliya_apartment_kitchen_stand_pos with dissolve:
        zoom 1.0

    "Вскоре, Алия завершила разговор и вернулась на кухню." with dissolve

    show Aliya_stand_straight tshirt eyes_open_sad_worried_open_mouth as Aliya at aliya_apartment_kitchen_stand_pos with dissolve:
        zoom 1.0

    aliya "Почему ты решил не говорить адрес?" with dissolve

    show Aliya_stand_straight tshirt eyes_open_sad_worried as Aliya at aliya_apartment_kitchen_stand_pos with dissolve:
        zoom 1.0

    me "Я боюсь за тебя. Вдруг они решат забрать тебя силой?" with dissolve

    me "Когда они приедут в Москву, мы договоримся о встрече." with dissolve

    me "Организуем встречу в общественном месте, так будет безопаснее для тебя." with dissolve

    show Aliya_stand_straight tshirt eyes_closed_sad_worried_open_mouth as Aliya at aliya_apartment_kitchen_stand_pos with dissolve:
        zoom 1.0

    aliya "Ладно." with dissolve

    stop music fadeout 1.0

    play music "music/Runaway_11 (Pre_Loop).ogg" fadein 1.0

    queue music "music/Runaway_11 (Loop).ogg"

    show Aliya_stand_straight tshirt eyes_open_smile as Aliya at aliya_apartment_kitchen_stand_pos with dissolve:
        zoom 1.0

    aliya "Спасибо..." with dissolve

    "Алия улыбнулась и посмотрела на меня." with dissolve

    "Глядя на неё, я тоже улыбнулся." with dissolve

    "Алия всё-таки невероятно красива, тем более, когда улыбается." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    jump day3_basmannaya_apartment_after_talk


label day3_basmannaya_apartment_after_talk:

    scene black with dissolve
    scene apt_kitchen

    show black zorder 10

    show apt_kitchen_foreground zorder 1

    show apartment_kitchen_food_no_spoon_eaten as apartment_kitchen_food zorder 2:
        xalign 0.0
        yalign 0.7
        zoom 0.6

    show Aliya_stand_straight tshirt eyes_open_smile as Aliya at aliya_apartment_kitchen_stand_pos with dissolve:
        zoom 1.0

    hide black with dissolve

    aliya "Семён, я чувствую сейчас себя немного лучше," with dissolve

    aliya "И честно говоря, я сейчас очень хочу поесть." with dissolve

    aliya "Не салат, а что-нибудь повкуснее." with dissolve

    "Это меня очень радует!" with dissolve

    me "Да, конечно. Сейчас я что-нибудь придумаю." with dissolve

    me "Мы можем заказать суши, пиццу или просто сходить куда-нибудь поесть." with dissolve

    show Aliya_stand_straight tshirt eyes_open_sad_worried as Aliya at aliya_apartment_kitchen_stand_pos with dissolve:
        zoom 1.0

    aliya "Сейчас уже довольно поздно." with dissolve

    me "Это Москва! Здесь полно круглосуточных кафешек. Мы что-нибудь найдём!" with dissolve

    show Aliya_stand_straight tshirt eyes_open_smile as Aliya at aliya_apartment_kitchen_stand_pos with dissolve:
        zoom 1.0

    aliya "Хорошо." with dissolve

    show cg_screen_phone_food_delivery as cg_screen_phone with dissolve

    "Я достал телефон и открыл приложение по доставке еды." with dissolve

    "И начал смотреть, что можно заказать поесть." with dissolve

    me "Что-то везде сроки доставки больше часа." with dissolve

    $ hidePhone()

    me "Думаю, будет лучше просто найти кафе рядом и сходить туда." with dissolve

    show cg_screen_phone_map_shaurma1 as cg_screen_phone with dissolve

    "Я открыл карты и стал искать кафе поблизости." with dissolve

    show cg_screen_phone_map_shaurma2 as cg_screen_phone with dissolve

    "Как я и ожидал, в Москве полно мест, где можно перекусить вечером." with dissolve

    me "Как ты относишься к шаурме?" with dissolve

    show Aliya_stand_straight tshirt eyes_closed_grin as Aliya at aliya_apartment_kitchen_stand_pos with dissolve:
        zoom 1.0

    aliya "Нормально, можно поесть." with dissolve

    me "Хорошо. Тогда вот тут есть рядом круглосуточная шаурма. Пойдём?" with dissolve

    $ hidePhone()

    show Aliya_stand_straight tshirt eyes_open_happy as Aliya at aliya_apartment_kitchen_stand_pos with dissolve:
        zoom 1.0

    aliya "Пойдём!" with dissolve

    scene black with dissolve

    "И мы отправились за шаурмой..." with dissolve

    jump day3_basmannaya_shaurma

label day3_basmannaya_shaurma:

    scene shaurma with dissolve

    $ savegame_picture = "savegame_shaurma"

    show shaurma_foreground zorder 1

    "Мы зашли в одну из круглосуточных забегаловок с шаурмой неподалеку." with dissolve

    "Внутри было довольно чисто и уютно. \"Столица всё-таки\",- подумал я." with dissolve

    scene shaurma_near with dissolve

    show aliya_sit_meal_jacket jacket eyes_open_sad_smile as Aliya with dissolve:
        zoom SCALE

    show cafe_table_tea_shaurma as cafe_table zorder 2 with dissolve

    "Мы взяли себе по шаурме, чаю и сели за стол." with dissolve

    show aliya_sit_meal_jacket jacket_phone eyes_open_watching as Aliya with dissolve:
        zoom SCALE

    "У Алии зазвонил телефон. Она открыла мессенджер." with dissolve

    show aliya_sit_meal_jacket jacket_phone_talk eyes_open_talking_phone with_phone as Aliya with dissolve:
        zoom SCALE

    aliya "Да, мам," with dissolve

    aliya "я сейчас ужинаю, всё хорошо." with dissolve

    aliya "Мы шаурму едим." with dissolve

    aliya "Хорошо, давай пока." with dissolve

    show aliya_sit_meal_jacket jacket_phone eyes_open_watching no_phone as Aliya with dissolve:
        zoom SCALE

    "Алия убрала телефон." with dissolve

    show aliya_sit_meal_jacket jacket eyes_open_sad_smile as Aliya with dissolve:
        zoom SCALE

    me "Да уж, сегодня был безумный день." with dissolve

    show cafe_table_tea as cafe_table zorder 2

    show aliya_sit_meal_jacket jacket_shaurma eyes_open_sad_smile as Aliya with dissolve:
        zoom SCALE

    me "Однако я считаю, твоя история закончилась довольно хорошо." with dissolve

    show aliya_sit_meal_jacket jacket_shaurma eyes_open_happy as Aliya with dissolve:
        zoom SCALE

    $ persistent.gallery8unlock = True

    "Алия улыбнулась." with dissolve

    aliya "Да." with dissolve

    me "Если так подумать, ты всё-таки выиграла от своего побега." with dissolve

    me "Родители загоняли тебя в рамки и огораживали со всех сторон." with dissolve

    me "Наверное, они ожидали, что ты будешь как вода течь в направлении, которое они задали." with dissolve

    me "Или как в шахматах, загоняли твоего короля в угол." with dissolve

    me "А ты взяла и сбежала. И своим побегом ты просто перевернула доску." with dissolve

    me "Теперь игра идёт по твоим правилам." with dissolve

    show aliya_sit_meal_jacket jacket_shaurma eyes_open_sad_worried_open_mouth as Aliya with dissolve:
        zoom SCALE

    aliya "Надеюсь, что так и будет." with dissolve

    show aliya_sit_meal_jacket jacket_shaurma eyes_open_neutral as Aliya with dissolve:
        zoom SCALE

    aliya "Теперь я в ближайшее время не вернусь в Дагестан," with dissolve

    aliya "а значит свадьбы не будет." with dissolve

    me "Да. Своего жениха ты ещё очень нескоро увидишь." with dissolve

    show aliya_sit_meal_jacket jacket_shaurma eyes_closed_annoyed as Aliya with dissolve:
        zoom SCALE

    aliya "Ага. Как же он меня бесит." with dissolve

    aliya "Моей маме он нравится, а мне - совсем нет." with dissolve

    me "Понимаю, да." with dissolve

    show aliya_sit_meal_jacket jacket_shaurma eyes_open_neutral as Aliya with dissolve:
        zoom SCALE

    aliya "И главное каждый раз, когда я приезжала в Дагестан, мама всё время пыталась нас оставить наедине." with dissolve

    aliya "Я помню, мы с ним сидели в автобусе." with dissolve

    aliya "Он всё время пытался меня приобнять, а я просто сползала вниз по сиденью." with dissolve

    aliya "Я думала, я там на пол упаду." with dissolve

    aliya "До сих пор жалею, что не врезала ему тогда как следует." with dissolve

    me "Ну и ладно. С этого момента, если он будет к тебе лезть, смело бей." with dissolve

    me "Ногами. Чтобы в другой раз трижды подумал." with dissolve

    aliya "Ещё у меня есть детское прозвище, как меня звали родители, когда я была маленькой." with dissolve

    aliya "Моя мама зачем-то ему сказала и теперь он часто так меня называет." with dissolve

    aliya "Я говорила не делать так, а ему всё равно." with dissolve

    show aliya_sit_meal_jacket jacket_shaurma eyes_closed_annoyed as Aliya with dissolve:
        zoom SCALE

    aliya "Бесит он меня." with dissolve

    show aliya_sit_meal_jacket jacket_shaurma eyes_open_neutral as Aliya with dissolve:
        zoom SCALE

    "Хорошо, что Алие больше не нужно будет разговаривать с женихом." with dissolve

    "Однако ей нужно будет ещё поговорить с мамой." with dissolve

    me "Не боишься встретиться завтра с мамой?" with dissolve

    show aliya_sit_meal_jacket jacket_shaurma eyes_open_sad_worried_open_mouth as Aliya with dissolve:
        zoom SCALE

    aliya "Не знаю. Я надеюсь, всё пройдёт хорошо." with dissolve

    show aliya_sit_meal_jacket jacket_shaurma eyes_open_neutral as Aliya with dissolve:
        zoom SCALE

    aliya "Моя мама хорошая, но она любит всё делать по-своему." with dissolve

    aliya "Она меня никогда не спрашивает, просто не берёт в расчёт моё мнение." with dissolve

    aliya "Даже про свадьбу я случайно узнала, она уже и ресторан начала подыскивать, и дату выбирать." with dissolve

    aliya "Меня даже не спросила, хочу ли я этого." with dissolve

    me "Я думаю, теперь твоя мама будет говорить с тобой по-другому." with dissolve

    show aliya_sit_meal_jacket jacket_shaurma eyes_open_sad_worried as Aliya with dissolve:
        zoom SCALE

    aliya "Надеюсь." with dissolve

    show aliya_sit_meal_jacket jacket_shaurma eyes_open_smile as Aliya with dissolve:
        zoom SCALE

    "Алия посмотрела на меня и снова улыбнулась." with dissolve

    aliya "Ты совсем не страшный." with dissolve

    "Теперь уже улыбнулся я." with dissolve

    show aliya_sit_meal_jacket jacket_shaurma eyes_open_happy as Aliya with dissolve:
        zoom SCALE

    aliya "Спасибо большое." with dissolve

    me "Не за что." with dissolve

    show aliya_sit_meal_jacket jacket eyes_open_smile as Aliya with dissolve:
        zoom SCALE

    show cafe_table_empty as cafe_table zorder 2

    "Мы доели шаурму и допили чай." with dissolve

    show aliya_sit_meal_jacket jacket eyes_open_sad_worried_open_mouth as Aliya with dissolve:
        zoom SCALE

    aliya "Я наелась. Идём?" with dissolve

    me "Да, пойдём." with dissolve

    scene black with dissolve

    #$ renpy.stop_predict("images/sprites/eating/*.*")
    #$ renpy.stop_predict("images/sprites/eating/emotions_home/*.*")
    #$ renpy.stop_predict("images/sprites/eating/emotions_cafe/*.*")

    "И мы пошли назад к съёмной квартире..." with dissolve

    jump day3_basmannaya_imran

label day3_basmannaya_imran:

    play music "music/Runaway_03 (Pre_Loop).ogg" fadein 1.0

    queue music "music/Runaway_03 (Loop).ogg"

    scene apartment_hood_night_car with dissolve

    $ savegame_picture = "savegame_apartment_hood_night_car"

    show Aliya_stand_half_turned jacket_armsdown eyes_open_neutral as Aliya at aliya_hood_right_pos with dissolve:
        zoom 1.0*0.9

    "Когда мы подходили к подъездной двери," with dissolve

    "я не сразу заметил, что кое-что поменялось." with dissolve

    "Во дворе стоял черный седан, которого тут раньше не было." with dissolve

    show Aliya_stand_half_turned jacket_armsdown eyes_open_shock as Aliya at aliya_hood_right_pos with dissolve:
        zoom 1.0*0.9

    "Я заметил это только когда открылась дверь автомобиля, из машины вышел мужчина и подошёл к нам." with dissolve

    show imran neutral at any_left_pos with dissolve:
        zoom 1.0

    imran_unknown "Семён и Алия, можно вас на минуту?" with dissolve

    "Внутри меня всё напряглось. Я взглянул на незнакомца." with dissolve

    "Мужчина кавказской национальности, в тёмной одежде, с лёгкой небритостью на лице и с проседью." with dissolve

    "Кто это?" with dissolve

    imran "Меня зовут Имран. Приятно познакомиться." with dissolve

    imran "Я двоюродный дядя Алии, я живу здесь в Москве." with dissolve

    show Aliya_stand_half_turned jacket_armsdown eyes_closed_sad as Aliya at aliya_hood_right_pos with dissolve:
        zoom 1.0*0.9

    "Я посмотрел на Алию. Её лицо выражало ужас и растерянность." with dissolve

    "Надо что-то сказать, наверное." with dissolve

    me "Что вам нужно?" with dissolve

    imran "Аслан, отец Алии, позвонил мне и попросил о ней позаботиться." with dissolve

    if day3_address_told:
        "Это ловушка! Зря я сказал им адрес! Зря я доверился!" with dissolve
    else:
        "Я отказался сообщить им свой адрес! Откуда же они его узнали?" with dissolve

    me "Что вы собираетесь делать с Алией?" with dissolve

    imran "Я должен её забрать. Алия не должна оставаться ночевать с незнакомым человеком." with dissolve

    "Да, и затем передать сразу в руки родителей!" with dissolve

    "Я не могу позволить, чтобы весь план побега так тупо накрылся крахом." with dissolve

    "Что же делать... давай, соображай голова!" with dissolve

    "Напасть? У меня в руках ничего нет, драться со взрослым дагестанцем голыми руками это безумие." with dissolve

    "И Алия вряд ли обрадуется если я нападу на её дядю." with dissolve

    "Сбежать? Я, допустим, могу убежать от этого мужчины, но Алия не может же!" with dissolve

    "Кажется, Имран прочитал мои размышления на моём лице, но интерпретировал их по-своему." with dissolve

    imran "Семён, я вас не буду задерживать, вы можете идти." with dissolve

    imran "Или, если хотите, вы тоже можете поехать с нами." with dissolve

    "Если я поеду с Алией, мне предстоит встреча с родителями девушки, которой я помог сбежать." with dissolve

    "Что же делать?" with dissolve

    menu:

        "Что же делать?"

        "Поехать с Имраном и Алией.":
            jump day3_basmannaya_imran_accept

        "Остаться.":
            jump day3_basmannaya_imran_decline


label day3_basmannaya_imran_accept:

    "Я не могу бросить Алию сейчас, это точно. Я готов встретиться с её родителями, если это потребуется." with dissolve

    me "Я поеду с вами." with dissolve

    show Aliya_stand_straight eyes_open_cry_sad3 as Aliya at aliya_hood_right_pos with dissolve:
        zoom 1.0*0.9

    "Я постарался произнести это как можно спокойнее." with dissolve

    "Хотя мои мысли метались, пытаясь оценить сложившуюся обстановку." with dissolve

    "Я бросил взгляд на Алию - кажется, она по-прежнему была в ужасе." with dissolve

    "Чувствую, этот вечер ещё только начинается..." with dissolve

    scene black with dissolve



    show black zorder 10

    if isMobileWeb:
        show bkg_movie_slide2

    else:
        show bkg_movie2


    show night_road_foreground2

    $ savegame_picture = "savegame_night_road2"

    "Мы сели в автомобиль Имрана, и поехали..." with dissolve

    $ renpy.pause(1.0)

    hide black with dissolve

    "Я сидел на переднем сидении, Алия - на заднем." with dissolve

    "Турбулентный водоворот моих мыслей наконец оформился в несколько выводов." with dissolve

    "Итак, я доверился, а родители Алии меня обманули. Теперь у меня развязаны руки." with dissolve

    "Я могу блефовать, притворяться и врать им о чем угодно, не чувствуя угрызений совести." with dissolve

    "Следовательно, количество возможных стратегий поведения возрастает многократно." with dissolve

    "Нужно лишь решить, что делать дальше..." with dissolve

    imran "Семен, скажите пожалуйста, как давно вы знаете Алию?" with dissolve

    "Здесь я врать не буду, так как проверяется легко." with dissolve

    me "Три дня." with dissolve

    imran "Хах." with dissolve

    imran "Семён, а вы в Москве живёте?" with dissolve

    "Кажется, Имран решил узнать меня получше." with dissolve

    "Думаю, нужно усыпить его бдительность. Надо наплести ему про себя какой-нибудь шаблонной чуши." with dissolve

    me "Нет, но я как раз планировал переезжать в Москву." with dissolve

    me "Я работаю в сфере ИТ." with dissolve

    imran "Ага! Сайты делаете, да?" with dissolve

    me "Да, можно и так сказать." with dissolve

    "Так, раз уж я решил втереться в доверие, нужно тоже что-то спросить." with dissolve

    me "А вы давно в Москве живёте?" with dissolve

    imran "Уже больше двадцати лет." with dissolve

    imran "У меня здесь работа, бизнес." with dissolve

    imran "Но мне уже тут надоело. Я сейчас собираюсь продать свой дом и уехать домой на юг." with dissolve

    me "Понимаю. Москва очень шумный и грязный город." with dissolve

    imran "Это точно. Мои родители там в Краснодарском крае, они уже старые." with dissolve

    imran "Я уже скоро перееду туда, поближе к ним." with dissolve

    "На некоторое время мне показалось, что я просто еду в такси и разговариваю с таксистом." with dissolve

    "Но нет, он нас вёз к себе домой, чтобы потом сдать родителям Алии." with dissolve

    "Нельзя расслабляться." with dissolve

    "Имран повернулся к Алие." with dissolve

    imran "Алия, если тебе нужно будет чем-то помочь или за что-то перед родителями просить - скажи." with dissolve

    imran "Просто скажи мне, если тебе что-то понадобится." with dissolve

    aliya "Хорошо." with dissolve

    "Наступило молчание." with dissolve

    "Мне хотелось достать телефон и написать Напарнику, чтобы обсудить ситуацию." with dissolve

    "Но я решил пока не доставать телефон. Если Имран увидит, что я что-то кому-то пишу, он может заподозрить меня." with dissolve

    "Поэтому надо просто обдумать ситуацию." with dissolve

    "Итак... у меня с собой есть паспорт, телефон с мобильным интернетом, деньги, кредитная карта." with dissolve

    "Много вещей осталось в съёмной квартире. Сумка с одеждой, плюс купленные нами коврик и одежда." with dissolve

    "У Алии с собой все вещи и документы. Плюс у неё в телефоне стоит купленная на моё имя сим-карта с подключенным интернетом." with dissolve

    "Мы сейчас едем к Имрану домой. Поскольку родители Алии прилетят не раньше завтрашнего утра, мы будем ночевать у него." with dissolve

    "Имран пригласил меня к себе гостем, получается. Я думаю, он ничего со мной делать не будет." with dissolve

    "Но и Алию он так просто не отпустит, конечно же." with dissolve

    "Возможно, мы сможем как-то сбежать из его дома." with dissolve

    "Или, когда родители будут везти Алию домой, можно будет организовать побег где-то по пути." with dissolve

    "Это сложнее, так как родители будут водить её за ручку везде, я уверен." with dissolve

    "Если они поедут на поезде - можно будет сойти с него." with dissolve

    "Если отправятся автобусом - можно организовать побег во время остановки." with dissolve

    "Ну а если они выберут самолет - возможно, получится организовать побег в аэропорту." with dissolve

    "А и еще, если усыпить их бдительность, возможно, Алия уговорит их остаться в Москве подольше и ,например, погулять по городу." with dissolve

    "Тогда будет ещё одна возможность для побега." with dissolve

    "Есть ли ещё какие-нибудь дополнительные варианты? Надо думать дальше." with dissolve

    "Я чувствую себя как Доктор Стрэндж из Войны Бесконечности." with dissolve

    "Обдумываю все возможные варианты нашего завтрашнего дня, оценивая шансы помочь Алие в каждом из них." with dissolve

    "Мне однозначно нужно посоветоваться с Напарником." with dissolve

    "Если я успею придумать новый план, вероятнее всего, смогу обсудить его с Алией наедине, когда Имран будет спать." with dissolve

    "Либо напишу ей в мессенджер, если Имран не отберёт у неё телефон." with dissolve

    "Утром приедут родители Алии и я уже не смогу ничего обсудить наедине с ней." with dissolve

    "Нужно успеть сегодня продумать план и согласовать с Алией." with dissolve

    "Договориться о совместных действиях с ней, блефануть когда нужно, совместно солгать о чём-то." with dissolve

    "Или подыграть в какой-то момент, чтобы усыпить бдительность." with dissolve

    "Кажется, Имран уже сделал какие-то выводы обо мне." with dissolve

    "Я думаю, он решил, что я обычный русский парень и не представляю опасности." with dissolve

    "Если мне удастся убедить в этом и её родителей, то они расслабятся и мне будет проще выполнить новый побег." with dissolve

    "Итак, главное не вызывать подозрений, вести себя естественно..." with dissolve

    "Как бы себя вёл обычный русский парень в такой ситуации?" with dissolve

    "Я как-то даже затрудняюсь представить..." with dissolve

    scene black with dissolve

    "Мысли вертелись у меня в голове, как пузырьки в кипящей воде..." with dissolve

    jump day3_imran_house


label day3_imran_house:

    scene imran_house_outside_night with dissolve

    $ savegame_picture = "savegame_imran_house_outside_night"

    "Наконец мы приехали к коттеджу в каком-то из садовых товариществ в Подмосковье." with dissolve

    "Участок вокруг коттеджа был огорожен высоким забором." with dissolve

    "Имран открыл ворота, заехал во двор и заглушил автомобиль." with dissolve

    show imran neutral at any_left_pos with dissolve:
        zoom 1.0

    imran "Мы приехали." with dissolve

    show Aliya_stand_straight eyes_open_sad_worried as Aliya at any_right_pos with dissolve:
        zoom 1.0*0.9

    "Алия вышла из автомобиля и растерянно оглянулась. Кажется, она успела поспать немного во время поездки." with dissolve

    imran "Здесь я и живу" with dissolve

    "Это был двухэтажный коттедж из кирпича, не слишком большой, но и не слишком маленький." with dissolve

    "Такие коттеджи появлялись в пригородах российских городов в начале двухтысячных, вызывая зависть у соседей." with dissolve

    "Решеток на окнах нет, отметил я. Однако сам участок был огорожен забором, через который не так-то просто перелезть." with dissolve

    imran "Проходите в дом." with dissolve

    "Имран открыл дверь и пригласил нас войти внутрь." with dissolve

    scene black with dissolve

    "Мы вошли в дом..." with dissolve

    scene imran_house_living_room_night with dissolve

    $ savegame_picture = "savegame_imran_house_living_room_night"

    "Имран проводил нас в гостиную." with dissolve

    show imran neutral at any_left_pos with dissolve:
        zoom 1.0

    show Aliya_stand_half_turned jacket_armsdown eyes_closed_sad as Aliya at any_right_pos with dissolve:
        zoom 1.0*0.9

    imran "Ваши спальни на втором этаже. Это вон туда и потом дальше вверх по лестнице." with dissolve

    imran "Хотите чаю?" with dissolve

    show Aliya_stand_half_turned jacket_armsdown eyes_open_sad_worried_question as Aliya at any_right_pos with dissolve:
        zoom 1.0*0.9

    aliya "Нет." with dissolve

    me "Нет, спасибо. Мы недавно поели." with dissolve

    "Имран оценивающе посмотрел на меня и Алию." with dissolve

    imran "Вы, наверное, очень устали и хотите спать." with dissolve

    imran "Давайте я вас провожу наверх?" with dissolve

    scene black with dissolve

    "Мы поднялись наверх по лестнице..." with dissolve

    scene imran_house_bedroom_night with dissolve

    $ savegame_picture = "savegame_imran_house_bedroom_night"

    "Как я и ожидал, Имран разместил меня и Алию в разных комнатах." with dissolve

    "Моя комната была довольно уютной. Однако отсюда нельзя было поговорить с Алией, не привлекая внимание Имрана." with dissolve

    "Остаётся только связь через телефон." with dissolve

    $ changeDialogToAliya()

    $ showMessengerPhone(is_night=True, force_no_transition=True)

    "Едва я остался один, я достал телефон и открыл мессенджер." with dissolve

    $ addSentMessage(1)

    me "Это была ловушка." with dissolve

    $ addReceivedMessage(1)

    aliya_mobile "Я знаю." with dissolve

    $ addSentMessage(4)

    me "Не переживай, я постараюсь придумать способ снова сбежать." with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Надеюсь это не понадобится." with dissolve

    $ addSentMessage(5)

    me "Я на твоей стороне, я переживаю за тебя и сделаю всё возможное, чтобы помочь тебе." with dissolve

    "Алия ничего не ответила." with dissolve

    $ changeDialogToCoach()

    $ showMessengerPhone(is_night=True, force_no_transition=True)

    "Тем временем я переключился на Напарника." with dissolve

    $ addSentMessage(0)

    me "Привет!" with dissolve

    $ addReceivedMessage(2)

    coach "Привет! Какие новости?" with dissolve

    $ addSentMessage(1)

    me "Все очень плохо." with dissolve

    $ addSentMessage(4)

    $ addSentMessage(5)

    $ addSentMessage(5)

    $ addSentMessage(4)

    $ addSentMessage(3)

    "И я обрисовал ситуацию Напарнику." with dissolve

    $ addReceivedMessage(3)

    coach "Да, действительно, вы попали." with dissolve

    $ addReceivedMessage(5)

    coach "С тобой Семён, скорее всего, ничего не будет. Ты всё-таки гость теперь." with dissolve

    $ addReceivedMessage(5)

    coach "Возможно, родители скажут тебе спасибо за то, что присмотрел за их дочкой." with dissolve

    $ addSentMessage(4)

    me "Для меня сейчас самое главное - что будет с Алией?" with dissolve

    $ addReceivedMessage(5)

    coach "Как она и сказала, скорее всего, у неё заберут телефон и запрут дома до свадьбы." with dissolve

    $ addReceivedMessage(5)

    coach "Когда она окажется снова в Дагестане или в Пятигорске, сбежать снова будет очень сложно." with dissolve

    $ addReceivedMessage(5)

    coach "Если она хочет сбежать, нужно это сделать пока вы еще в Москве." with dissolve

    $ addReceivedMessage(5)

    coach "Я постараюсь придумать какой-нибудь способ или найти какую-нибудь лазейку." with dissolve

    $ addReceivedMessage(3)

    coach "Но тут есть другая сложность." with dissolve

    $ addSentMessage(0)

    me "Какая?" with dissolve

    $ addReceivedMessage(3)

    coach "Родители попытаются убедить её вернуться домой." with dissolve

    $ addReceivedMessage(5)

    coach "Возможно, они будут запугивать, давить или уговаривать, или что-то обещать." with dissolve

    $ addReceivedMessage(5)

    coach "Возможно, Алия поверит своим родителям и захочет вернуться с ними." with dissolve

    $ addReceivedMessage(4)

    coach "Тем более сейчас убежать намного сложнее." with dissolve

    $ addReceivedMessage(5)

    coach "Чтобы сбежать ещё раз, нужно чтобы она тебе очень сильно доверяла." with dissolve

    $ addReceivedMessage(5)

    coach "Если она тебе недостаточно доверяет, ты  не сможешь её убедить сбежать повторно." with dissolve

    "Да, я представил себя на её месте." with dissolve

    "Алия меня знает всего три дня, в то время как с родителями она всю сознательную жизнь." with dissolve

    "Сбежать от родителей в первый раз — это по сути просто уйти и сесть на автобус до аэропорта." with dissolve

    "Но сбежать, когда родители поняли серьезность намерений и уговаривают вернуться - намного сложнее." with dissolve

    "Довольно сложно оценить сейчас, что будет делать Алия." with dissolve

    $ addReceivedMessage(4)

    coach "Ладно. Она рядом с тобой, подумай об этом, поговори с ней." with dissolve

    $ addReceivedMessage(5)

    coach "Тем временем я постараюсь придумать способы сбежать в тех условиях, которые ты назвал." with dissolve

    $ addReceivedMessage(1)

    coach "Спокойной ночи!" with dissolve

    $ addSentMessage(2)

    me "Спасибо. Спокойной ночи!" with dissolve

    $ changeDialogToAliya()

    $ showMessengerPhone(is_night=True, force_no_transition=True)

    "Я открыл сообщения с Алией. Она по-прежнему ничего не ответила." with dissolve

    "Возможно, она легла спать." with dissolve

    $ clearDisplayMessages()

    $ hidePhone()

    "Я убрал телефон и почувствовал наконец, насколько сегодня был безумный день." with dissolve

    "Тем более, с этими перелетами я практически не спал прошлой ночью." with dissolve

    "Я расстелил постель и лег спать с тяжёлыми мыслями." with dissolve

    scene black with dissolve

    "Вскоре я погрузился в сон." with dissolve

    jump day4_intro




label day3_basmannaya_imran_decline:

    me "Я лучше останусь здесь." with dissolve

    show Aliya_stand_half_turned eyes_open_angry as Aliya at aliya_hood_right_pos with dissolve:
        zoom 1.0*0.9

    "Алия сверкнула глазами на меня, но промолчала." with dissolve

    imran "Хорошо! Алия, садись в машину." with dissolve

    hide Aliya

    imran "Прощайте, Семён! Спасибо, что присмотрели за Алией!" with dissolve

    hide imran with dissolve

    "Имран посадил Алию в автомобиль, затем сел сам." with dissolve

    scene apartment_hood_night with dissolve

    "Чёрный автомобиль выехал со двора, а я стоял возле подъезда и смотрел ему вслед." with dissolve

    scene black with dissolve

    play music "music/Runaway_01 (Pre_Loop).ogg" fadein 1.0

    queue music "music/Runaway_01 (Loop).ogg"

    "Мне больше ничего не оставалось сделать, кроме как вернуться в квартиру..." with dissolve

    scene apt_kitchen

    $ savegame_picture = "savegame_apt_kitchen"

    show black zorder 10

    show apartment_kitchen_food_spoon_eaten as apartment_kitchen_food at apartment_kitchen_food_pos zorder 2:
        zoom 0.6

    hide black with dissolve

    $ changeDialogToAliya()

    $ addSentMessage(5)

    $ addSentMessage(5)

    $ addSentMessage(5)

    $ showMessengerPhone(is_night=False, force_no_transition=True)

    "Уже прошло больше часа. Я сидел на кухне съёмной квартиры." with dissolve

    "Алия, наверное, уже приехала в дом к Имрану." with dissolve

    "Я написал ей несколько сообщений, но она не отвечала." with dissolve

    "В последний раз она была онлайн больше часа назад." with dissolve

    "Возможно, она всё ещё так и не решилась достать свой телефон?" with dissolve

    "Или может быть..." with dissolve

    "Имран всё-таки забрал у неё телефон?" with dissolve

    "Я старался отгонять плохие мысли, но очень сложно не думать об этом." with dissolve

    "Передо мной на столе стоял недоеденный салат." with dissolve

    "У меня просто не было сил или желания выкинуть его в мусорку." with dissolve

    "Моих сил хватало лишь на то, чтобы сидеть в телефоне, перечитывая переписку в мессенджере." with dissolve

    "И ожидая, когда наконец-то Алия будет онлайн." with dissolve

    if var_day3_photo_made:

        $ clearDisplayMessages()

        hide cg_screen_phone_top

        show cg_screen_phone_aliya_photo2 as cg_screen_phone with dissolve

        "Периодически я открывал и смотрел фотографию Алии в своём телефоне." with dissolve

        "Это та фотография, которую я украдкой заснял в Таганском парке." with dissolve

        "Это единственная фотография Алии, которая у меня есть. Не считая, конечно, фотографии в паспорте." with dissolve

        "Алия с фотографии улыбалась и смотрела мне прямо в глаза." with dissolve

        "Именно такой я её и запомню теперь на всю жизнь..." with dissolve

    $ clearDisplayMessages()

    $ hidePhone()

    show black zorder 10 with dissolve

    $ renpy.pause(1.0)

    hide black with dissolve

    messenger "Новое сообщение" with dissolve # with hpunch

    show cg_screen_phone_new_message_day4_evening_athome_alone as cg_screen_phone with dissolve

    "Я дёрнулся и резко включил телефон." with dissolve

    $ changeDialogToCoach()

    $ showMessengerPhone(is_night=False, force_no_transition=True)

    $ addReceivedMessage(2)

    coach "Привет! Как дела?" with dissolve

    $ addSentMessage(2)

    me "Привет. Всё плохо." with dissolve

    $ addSentMessage(5)

    $ addSentMessage(5)

    $ addSentMessage(4)

    $ addSentMessage(4)

    $ addSentMessage(5)

    "И я обрисовал ситуацию Напарнику." with dissolve

    $ addReceivedMessage(5)

    coach "Ну, я не могу осуждать тебя за то, что ты решил бросить Алию." with dissolve

    $ addReceivedMessage(4)

    coach "Хотя я думаю, она сейчас очень зла на тебя." with dissolve

    $ addSentMessage(2)

    me "Что мне делать?" with dissolve

    $ addReceivedMessage(3)

    coach "Ты можешь с ней связаться в мессенджере?" with dissolve

    $ addSentMessage(4)

    me "Нет, она не отвечает на мои сообщения и не появляется в сети." with dissolve

    $ addSentMessage(3)

    me "Я подозреваю, Имран забрал у неё телефон." with dissolve

    $ addReceivedMessage(0)

    coach "Возможно." with dissolve

    $ addSentMessage(4)

    me "Затем приедут родители и заберут её обратно в Дагестан." with dissolve

    $ addSentMessage(4)

    me "Где её до самой свадьбы не будут выпускать из дома." with dissolve

    $ addReceivedMessage(4)

    coach "И это ещё не самый худший вариант." with dissolve

    $ addReceivedMessage(5)

    coach "Высока вероятность, что она попытается совершить самоубийство." with dissolve

    "Меня как из холодного душа окатило." with dissolve

    $ addSentMessage(2)

    me "Что же мне делать?" with dissolve

    $ addReceivedMessage(4)

    coach "Я не знаю. Наверное, ты сделал всё, что мог." with dissolve

    $ addReceivedMessage(5)

    coach "У тебя, наверное, была причина, по которой ты решил сдаться зайдя так далеко." with dissolve

    jump day3_and_day4_final_loose
