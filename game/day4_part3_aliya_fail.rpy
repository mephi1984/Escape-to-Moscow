
label day4_imran_house_new_escape_failed:

    scene black with dissolve

    "Я ждал, что мне ответит Алия..." with dissolve

    scene imran_house_doorway with dissolve

    show imran_room_drawers_food_full_near

    show Aliya_stand_straight tshirt eyes_open_neutral as Aliya at aliya_imran_room_pos with dissolve:
        zoom 1.0

    aliya "Извини, Семён. Ты уже сделал всё, что мог." with dissolve

    aliya "Мне больше не нужна твоя помощь. Дальше я буду действовать сама." with dissolve

    show Aliya special_turned as Aliya at aliya_imran_room_pos with dissolve:
        zoom 1.0

    "Алия развернулась и покинула комнату." with dissolve

    hide Aliya with dissolve

    "Я слышал звук удаляющихся шагов, спускающихся вниз по лестнице." with dissolve

    scene black with dissolve

    "Чувство бессилия и слабости охватило меня на какое-то время.Я присел на кровать, чтобы немного прийти в себя..." with dissolve

    scene imran_house_living_room with dissolve

    $ savegame_picture = "savegame_imran_house_living_room"

    show imran watching at imran_house_pos1:
        zoom 1.0
        alpha 0.0
        linear 0.5 alpha 1.0

    show Aliya_stand_straight tshirt eyes_open_sad_worried as Aliya at imran_house_pos2:
        zoom 1.0*0.9
        alpha 0.0
        linear 0.5 alpha 1.0

    show aslan neutral at imran_house_pos3:
        zoom 1.0
        alpha 0.0
        linear 0.5 alpha 1.0

    show fatima neutral at imran_house_pos4:
        zoom 1.0
        alpha 0.0
        linear 0.5 alpha 1.0

    "Спустя какое-то время я вышел в гостиную и поставил посуду на стол. В гостиной были Алия, её родители и дядя Имран." with dissolve

    me "Спасибо большое за обед!" with dissolve

    show fatima talking at imran_house_pos4 with dissolve:
        zoom 1.0
        alpha 1.0

    fatima "Я рада, что вам понравилось!" with dissolve

    show fatima neutral at imran_house_pos4 with dissolve:
        zoom 1.0
        alpha 1.0

    show imran talking at imran_house_pos1 with dissolve:
        zoom 1.0
        alpha 1.0

    imran "Семён, я бы предложил вам остаться на подольше," with dissolve

    imran "но я должен отвезти Аслана и его семью в аэропорт." with dissolve

    show imran neutral at imran_house_pos1 with dissolve:
        zoom 1.0
        alpha 1.0

    show fatima talking at imran_house_pos4 with dissolve:
        zoom 1.0
        alpha 1.0

    fatima "Спасибо за помощь, Семён!" with dissolve

    fatima "Здоровья тебе и благополучия!" with dissolve

    show fatima neutral at imran_house_pos4 with dissolve:
        zoom 1.0
        alpha 1.0

    show aslan talking at imran_house_pos3 with dissolve:
        zoom 1.0
        alpha 1.0


    aslan "Пока, Семён." with dissolve

    show aslan neutral at imran_house_pos3 with dissolve:
        zoom 1.0
        alpha 1.0

    me "Алия, было приятно познакомиться с тобой! Желаю тебе удачи!" with dissolve

    show Aliya_stand_straight tshirt eyes_closed_sad_worried_open_mouth as Aliya at imran_house_pos2 with dissolve:
        zoom 1.0*0.9

    aliya "Спасибо!" with dissolve

    show Aliya_stand_straight tshirt eyes_closed_sad as Aliya at imran_house_pos2 with dissolve:
        zoom 1.0*0.9

    me "Я напишу тебе потом!" with dissolve

    "Алия не ответила." with dissolve

    "Я в последний раз посмотрел на неё. Она избегала моего взгляда и выглядела немного расстроенной." with dissolve

    show imran talking at imran_house_pos1 with dissolve:
        zoom 1.0
        alpha 1.0

    imran "Давай я открою тебе ворота! Пойдем!" with dissolve

    scene black with dissolve

    "Я в сопровождении Имрана вышел во двор..." with dissolve

    scene imran_house_outside_open_gate with dissolve

    $ savegame_picture = "savegame_imran_house_outside"

    show imran neutral at any_right_pos with dissolve:
        zoom 1.0

    "Он открыл ворота и мы вышли со двора на улицу, заставленную высокими заборами." with dissolve

    show imran talking at any_right_pos with dissolve:
        zoom 1.0

    imran "Если пойдёшь в ту сторону, выйдешь на Киевское шоссе, там и находится автобусная остановка." with dissolve

    show imran neutral at any_right_pos with dissolve:
        zoom 1.0

    me "Хорошо. Тогда я пойду." with dissolve

    show imran talking at any_right_pos with dissolve:
        zoom 1.0

    imran "Счастливого пути!" with dissolve

    show imran neutral at any_right_pos with dissolve:
        zoom 1.0

    me "Спасибо! Вам тоже удачи!" with dissolve

    hide imran with dissolve

    "Имран вернулся домой." with dissolve

    scene black with dissolve

    "Ну а я медленно пошёл по направлению к Киевскому шоссе..." with dissolve

    jump day4_the_end_part1_option2_airplane


label day4_the_end_part1_option2_airplane:

    if renpy.emscripten:
        $ import emscripten
        $ emscripten.run_script("playRunaway01()")
    else:

        play music "music/Runaway_01 (Loop).ogg" # fadein 3.0

        queue music "music/Runaway_01 (Loop).ogg"

    scene apt_kitchen with dissolve

    $ savegame_picture = "savegame_apt_kitchen"

    show apartment_kitchen_food_spoon_eaten as apartment_kitchen_food at apartment_kitchen_food_pos zorder 2:
        zoom 0.6

    $ changeDialogToAliya()

    $ addSentMessage(5)

    $ addSentMessage(5)

    $ addSentMessage(5)

    $ showMessengerPhone(is_night=False, force_no_transition=True)


    "Был уже глубокий вечер. Я сидел на кухне съёмной квартиры." with dissolve

    "Алия с родителями уже давно должны были прилететь в аэропорт Минеральные Воды." with dissolve

    "Я написал ей несколько сообщений, но ответа не было." with dissolve

    "В последний раз Алия была онлайн несколько часов назад." with dissolve

    "Может, она всё ещё не включила телефон после перелёта?" with dissolve

    "Или... что, если" with dissolve

    "у неё всё-таки отобрали телефон?" with dissolve

    "Я старался отгонять плохие мысли, но очень сложно не думать об этом." with dissolve

    "Передо мной на столе стоял недоеденный салат." with dissolve

    "У меня просто не было сил или желания выкинуть его в мусорку." with dissolve

    "Моей энергии хватало лишь для того, чтобы сидеть в телефоне, перечитывая переписку в мессенджере" with dissolve

    "и ожидая, когда наконец-то Алия будет онлайн." with dissolve

    if var_day3_photo_made:

        $ clearDisplayMessages()

        hide cg_screen_phone_top

        show cg_screen_phone_aliya_photo2 as cg_screen_phone with dissolve

        "Периодически я открывал и смотрел фотографию Алии в своём телефоне." with dissolve

        "Это тот снимок, который я украдкой заснял в Таганском парке." with dissolve

        "Единственное фото Алии, которое у меня есть - не считая, конечно, фотографии в паспорте." with dissolve

        "Алия с фотографии улыбалась и смотрела мне прямо в глаза." with dissolve

        "Именно такой я её и запомню теперь на всю жизнь..." with dissolve

    $ clearDisplayMessages()

    $ hidePhone()

    show black zorder 10 with dissolve

    "Прошла, как мне казалось, целая вечность..." with dissolve

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

    $ addSentMessage(4)

    me "Мне удалось уговорить родителей Алии лететь самолётом," with dissolve

    $ addSentMessage(4)

    me "но я не смог уговорить её бежать снова." with dissolve

    $ addReceivedMessage(4)

    coach "Значит, она тебе недостаточно доверяет?" with dissolve

    $ addReceivedMessage(4)

    coach "Может, ты её обидел чем-то или напугал?" with dissolve

    $ addSentMessage(2)

    me "Что мне делать?" with dissolve

    jump day4_the_end_part2
