label day4_parents_part6_parent_persuade_fail:

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

    show fatima talking at imran_house_pos4:
        zoom 0.75*SCALE
        alpha 0.0
        linear 0.5 alpha 1.0

    fatima "Нет Семен, не нужно беспокоиться." with dissolve

    show fatima neutral at imran_house_pos4 with dissolve:
        zoom 0.75*SCALE
        alpha 1.0

    me "Почему?" with dissolve

    show fatima talking at imran_house_pos4 with dissolve:
        zoom 0.75*SCALE
        alpha 1.0

    fatima "Мы поедем на автобусе, так дешевле и надежнее." with dissolve

    fatima "Имран нас отвезет на автовокзал, и купит билеты на автобус." with dissolve

    show fatima neutral at imran_house_pos4 with dissolve:
        zoom 0.75*SCALE
        alpha 1.0

    "Ох, черт, кажется эта часть плана провалилась?" with dissolve

    me "Зачем торопиться? Вы же все-таки в Москве, может погуляете по городу?" with dissolve

    "Фатима посмотрела на меня внимательно." with dissolve

    show fatima talking at imran_house_pos4 with dissolve:
        zoom 0.75*SCALE
        alpha 1.0

    fatima "Семен, я же говорю, вам не нужно беспокоиться по этому поводу." with dissolve

    fatima "Алия должна вернуться домой. Это уже наше дело, не ваше." with dissolve

    show fatima neutral at imran_house_pos4 with dissolve:
        zoom 0.75*SCALE
        alpha 1.0

    show Aliya tshirt_stand_straight_eyes_closed_sad at imran_house_pos2 with dissolve:
        zoom 0.75*SCALE*0.9
        alpha 1.0

    "Я посмотрел на Алию. Алия отвела взгляд и стала смотреть в пол." with dissolve

    scene black with dissolve

    "Прошло некоторое время..." with dissolve

    scene imran_house_living_room with dissolve

    "Мать Алии приготовила обед - сэндвичи и чай." with dissolve

    "Мы сели за стол, и молча пообедали." with dissolve

    "Алия молчала. Родители Алии тоже словно бы не хотели что-то лишнее сказать при мне." with dissolve

    "Я допил чай и приготовился встать из-за стола." with dissolve

    show imran neutral at imran_house_pos1:
        zoom 0.75*SCALE
        alpha 0.0
        linear 0.5 alpha 1.0

    show Aliya tshirt_stand_straight_eyes_closed_sad at imran_house_pos2:
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

    "Дождавшись меня, родители Алии и Имран тоже встали." with dissolve

    show imran angry at imran_house_pos1 with dissolve:
        zoom 0.75*SCALE
        alpha 1.0

    imran "Семен, мы сейчас поедем на автовокзал." with dissolve

    imran "Здесь есть рядом автобусная остановка, оттуда едут маршрутки до метро." with dissolve

    imran "Я бы вас подбросил, но вам будет быстрее и проще дойти самостоятельно. Хорошо?" with dissolve

    show imran neutral at imran_house_pos1 with dissolve:
        zoom 0.75*SCALE
        alpha 1.0

    me "Ладно..." with dissolve

    "Я в последний раз посмотрел на Алию." with dissolve

    "Она смотрела в пол, и выглядела очень грустной." with dissolve

    show imran angry at imran_house_pos1 with dissolve:
        zoom 0.75*SCALE
        alpha 1.0

    imran "Давайте я вас провожу до ворот, Семен." with dissolve

    scene black with dissolve

    "Я вышел из дома во двор в сопровождении Имрана..." with dissolve

    scene imran_house_outside_open_gate with dissolve

    show imran neutral at any_right_pos with dissolve:
        zoom 0.75*SCALE

    "Имран открыл ворота, и мы вышли со двора на улицу, заставленную высокими заборами." with dissolve

    show imran angry at any_right_pos with dissolve:
        zoom 0.75*SCALE

    imran "Отсюда если идти в ту сторону, то там будет Киевское шоссе, и автобусная остановка." with dissolve

    imran "Удачи, Семен!" with dissolve

    hide imran with dissolve

    "Имран вывел меня на дорогу, ушел и закрыл за мной ворота." with dissolve

    scene black with dissolve

    "И я медленно пошел по направлению к автобусной остановке..." with dissolve

    jump day4_the_end_part1_option1_bus



label day4_the_end_part1_option1_bus:

    play music "music/Runaway_01 (Pre_Loop).ogg"  fadein 1.0

    queue music "music/Runaway_01 (Loop).ogg"

    scene apt_kitchen

    show black zorder 10

    show apartment_kitchen_food_spoon_eaten as apartment_kitchen_food at apartment_kitchen_food_pos zorder 2:
        zoom 0.6

    hide black with dissolve

    $ changeDialogToAliya()

    $ addSentMessage(5)

    $ addSentMessage(5)

    $ addSentMessage(5)

    $ showMessengerPhone(is_night=False, force_no_transition=True)


    "Был уже глубокий вечер. Я сидел на кухне съемной квартиры." with dissolve

    "Алия с родителями сейчас ехала в автобусе, наверное где-то под Ростовом." with dissolve

    "Я написал ей несколько сообщений, но она не отвечала." with dissolve

    "В последний раз она была онлайн несколько часов назад." with dissolve

    "Может быть просто в дороге нет связи? Не ловит телефон?" with dissolve

    "Может Алия просто устала, и решила поспать?" with dissolve

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

    me "Мне не удалось уговорить родителей Алии выбрать самолет" with dissolve

    $ addSentMessage(4)

    me "Они просто забрали Алию у меня и уехали на автобусе" with dissolve

    $ addReceivedMessage(4)

    coach "Значит ты не смог завоевать их доверие" with dissolve

    $ addReceivedMessage(2)

    coach "Как там Алия?" with dissolve

    $ addSentMessage(5)

    me "Мне не удалось поговорить с ней наедине. Кажется, родители постоянно следили за ней" with dissolve

    $ addSentMessage(5)

    me "В последний раз когда я ее видел, она была очень грустной и обреченной" with dissolve

    jump day4_the_end_part2
