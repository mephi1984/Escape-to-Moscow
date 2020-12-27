
label day4_imran_house_new_escape_failed:

    scene black with dissolve

    "Я ждал, что мне ответит Алия..." with dissolve

    scene imran_house_doorway with dissolve

    show imran_room_drawers_food_full_near

    show Aliya tshirt_stand_straight_eyes_open_neutral at aliya_imran_room_pos with dissolve:
        zoom 0.75*SCALE

    aliya "Извини, Семен. Ты уже сделал все что мог." with dissolve

    aliya "Мне больше не нужна твоя помощь. Дальше я буду действовать сама." with dissolve

    show Aliya special_turned at aliya_imran_room_pos with dissolve:
        zoom 0.75*SCALE

    "Алия развернулась, вышла в дверь." with dissolve

    hide Aliya with dissolve

    "А затем ушла вниз по лестнице." with dissolve

    scene black with dissolve

    "Чувство бессилия и слабости охватило меня на какое-то время, и я присел на кровать, чтобы немного прийти в себя..." with dissolve

    scene imran_house_living_room with dissolve

    show imran watching at imran_house_pos1:
        zoom 0.75*SCALE
        alpha 0.0
        linear 0.5 alpha 1.0

    show Aliya tshirt_stand_straight_eyes_open_sad_worried at imran_house_pos2:
        zoom 0.75*SCALE*0.9
        alpha 0.0
        linear 0.5 alpha 1.0

    show aslan neutral at imran_house_pos3:
        zoom 0.75*SCALE
        alpha 0.0
        linear 0.5 alpha 1.0

    show fatima neutral at imran_house_pos4:
        zoom 0.75*SCALE
        alpha 0.0
        linear 0.5 alpha 1.0

    "Спустя какое-то время я вышел в гостиную и поставил посуду на стол. В гостиной были Алия, ее родители, и Имран." with dissolve

    me "Спасибо большое за обед!" with dissolve

    show fatima talking at imran_house_pos4 with dissolve:
        zoom 0.75*SCALE
        alpha 1.0

    fatima "Я рада что вам понравилось!" with dissolve

    show fatima neutral at imran_house_pos4 with dissolve:
        zoom 0.75*SCALE
        alpha 1.0

    show imran talking at imran_house_pos1 with dissolve:
        zoom 0.75*SCALE
        alpha 1.0

    imran "Семен, я бы предложил остаться на подольше." with dissolve

    imran "Но я должен отвезти Аслана и его семью в аэропорт." with dissolve

    show imran neutral at imran_house_pos1 with dissolve:
        zoom 0.75*SCALE
        alpha 1.0

    show fatima talking at imran_house_pos4 with dissolve:
        zoom 0.75*SCALE
        alpha 1.0

    fatima "Спасибо за помощь, Семен!" with dissolve

    fatima "Здоровья тебе и благополучия!" with dissolve

    show fatima neutral at imran_house_pos4 with dissolve:
        zoom 0.75*SCALE
        alpha 1.0

    show aslan talking at imran_house_pos3 with dissolve:
        zoom 0.75*SCALE
        alpha 1.0


    aslan "Пока, Семен." with dissolve

    show aslan neutral at imran_house_pos3 with dissolve:
        zoom 0.75*SCALE
        alpha 1.0

    me "Алия, было приятно познакомиться с тобой! Желаю тебе удачи!" with dissolve

    show Aliya tshirt_stand_straight_eyes_closed_sad_worried_open_mouth at imran_house_pos2 with dissolve:
        zoom 0.75*SCALE*0.9

    aliya "Спасибо" with dissolve

    show Aliya tshirt_stand_straight_eyes_closed_sad at imran_house_pos2 with dissolve:
        zoom 0.75*SCALE*0.9

    me "Я напишу тебе потом!" with dissolve

    "Алия не ответила." with dissolve

    "Я в последний раз посмотрел на Алию. Она избегала смотреть на меня, и выглядела немного расстроенной." with dissolve

    show imran talking at imran_house_pos1 with dissolve:
        zoom 0.75*SCALE
        alpha 1.0

    imran "Давай я открою тебе ворота! Пойдем!" with dissolve

    scene black with dissolve

    "Я в сопровождении Имрана вышел во двор..." with dissolve

    scene imran_house_outside_open_gate with dissolve

    show imran neutral at any_right_pos with dissolve:
        zoom 0.75*SCALE

    "Имран открыл ворота, и мы вышли со двора на улицу, заставленную высокими заборами." with dissolve

    show imran talking at any_right_pos with dissolve:
        zoom 0.75*SCALE

    imran "Отсюда если идти в ту сторону, то там будет Киевское шоссе, и автобусная остановка." with dissolve

    show imran neutral at any_right_pos with dissolve:
        zoom 0.75*SCALE

    me "Хорошо. Тогда я пойду." with dissolve

    show imran talking at any_right_pos with dissolve:
        zoom 0.75*SCALE

    imran "Счастливого пути!" with dissolve

    show imran neutral at any_right_pos with dissolve:
        zoom 0.75*SCALE

    me "Спасибо! Вам тоже удачи!" with dissolve

    hide imran with dissolve

    "Имран вернулся домой." with dissolve

    scene black with dissolve

    "Ну а я медленно пошел пешком по направлению к Киевскому шоссе..." with dissolve

    jump day4_the_end_part1_option2_airplane


label day4_the_end_part1_option2_airplane:

    play music "music/Runaway_01 (Pre_Loop).ogg" fadein 1.0

    queue music "music/Runaway_01 (Loop).ogg"

    scene apt_kitchen with dissolve

    show apartment_kitchen_food_spoon_eaten as apartment_kitchen_food at apartment_kitchen_food_pos zorder 2:
        zoom 0.6

    $ changeDialogToAliya()

    $ addSentMessage(5)

    $ addSentMessage(5)

    $ addSentMessage(5)

    $ showMessengerPhone(is_night=False, force_no_transition=True)


    "Был уже глубокий вечер. Я сидел на кухне съемной квартиры." with dissolve

    "Алия с родителями уже давно должны были прилететь в аэропорт Минеральные Воды." with dissolve

    "Я написал ей несколько сообщений, но она не отвечала." with dissolve

    "В последний раз она была онлайн несколько часов назад." with dissolve

    "Возможно, она все еще не включила телефон после самолета?" with dissolve

    "Или может быть..." with dissolve

    "У нее все-таки отобрали телефон?" with dissolve

    "Я старался отгонять плохие мысли, но очень сложно не думать об этом." with dissolve

    "Перед мной на столе стоял недоеденный салат." with dissolve

    "У меня просто не было сил или желания выкинуть его в мусорку." with dissolve

    "Моих сил хватало лишь для того, чтобы сидеть в телефоне, перечитывая переписку в мессенджере." with dissolve

    "И ожидая, когда наконец то Алия будет онлайн." with dissolve

    if var_day3_photo_made:

        $ clearDisplayMessages()

        hide cg_screen_phone_top

        show cg_screen_phone_aliya_photo2 as cg_screen_phone with dissolve

        "Периодически я открывал и смотрел фотографию Алии в своем телефоне." with dissolve

        "Это та фотография, которую я украдкой заснял в Таганском парке." with dissolve

        "Это единственная фотография Алии, которая у меня есть - не считая, конечно, фотографии в паспорте." with dissolve

        "Алия с фотографии улыбалась и смотрела мне прямо в глаза." with dissolve

        "Именно такой я ее и запомню теперь на всю жизнь..." with dissolve

    $ clearDisplayMessages()

    $ hidePhone()

    show black zorder 10 with dissolve

    "Прошла, как мне казалось, целая вечность..." with dissolve

    hide black with dissolve

    messenger "Новое сообщение" with dissolve # with hpunch

    show cg_screen_phone_new_message_day4_evening_athome_alone as cg_screen_phone with dissolve

    "Я дернулся и резко включил телефон." with dissolve

    $ changeDialogToCoach()

    $ showMessengerPhone(is_night=False, force_no_transition=True)

    $ addReceivedMessage(2)

    coach "Привет! Как дела?" with dissolve

    $ addSentMessage(2)

    me "Привет. Все плохо" with dissolve

    $ addSentMessage(4)

    me "Мне удалось уговорить родителей Алии полететь на самолете" with dissolve

    $ addSentMessage(4)

    me "Но я не смог уговорить ее бежать снова" with dissolve

    $ addReceivedMessage(4)

    coach "Значит, она тебе недостаточно доверяет" with dissolve

    $ addReceivedMessage(4)

    coach "Может, ты ее обидел чем-то, или напугал" with dissolve

    $ addSentMessage(2)

    me "Что мне делать?" with dissolve

    jump day4_the_end_part2
