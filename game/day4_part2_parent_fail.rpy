label day4_parents_part6_parent_persuade_fail:

    scene imran_house_living_room with dissolve

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

    show fatima talking at imran_house_pos4:
        zoom 1.0
        alpha 0.0
        linear 0.5 alpha 1.0

    fatima "Нет, Семён, не нужно беспокоиться." with dissolve

    show fatima neutral at imran_house_pos4 with dissolve:
        zoom 1.0
        alpha 1.0

    me "Почему?" with dissolve

    show fatima talking at imran_house_pos4 with dissolve:
        zoom 1.0
        alpha 1.0

    fatima "Мы поедем на автобусе - так дешевле и надёжнее." with dissolve

    fatima "Имран нас отвезёт на автовокзал и купит билеты." with dissolve

    show fatima neutral at imran_house_pos4 with dissolve:
        zoom 1.0
        alpha 1.0

    "Ох чёрт, кажется, эта часть плана провалилась" with dissolve

    me "Зачем торопиться? Вы же всё-таки в Москве, может погуляете по городу?" with dissolve

    "Фатима внимательно посмотрела на меня." with dissolve

    show fatima talking at imran_house_pos4 with dissolve:
        zoom 1.0
        alpha 1.0

    fatima "Семён, я же говорю, вам не нужно беспокоиться по этому поводу." with dissolve

    fatima "Алия должна вернуться домой. Это уже наше дело, не ваше." with dissolve

    show fatima neutral at imran_house_pos4 with dissolve:
        zoom 1.0
        alpha 1.0

    show Aliya_stand_straight tshirt eyes_closed_sad at imran_house_pos2 with dissolve:
        zoom 1.0*0.9
        alpha 1.0

    "Я посмотрел на Алию. Она отвела взгляд и стала смотреть в пол." with dissolve

    scene black with dissolve

    "Прошло некоторое время..." with dissolve

    scene imran_house_living_room with dissolve

    "Мать Алии приготовила обед: сэндвичи и чай." with dissolve

    "Мы сели за стол и молча поели." with dissolve

    "Девушка молчала. Её родители тоже, словно бы не хотели сказать при мне что-то лишнее." with dissolve

    "Я допил чай и приготовился встать из-за стола." with dissolve

    show imran neutral at imran_house_pos1:
        zoom 1.0
        alpha 0.0
        linear 0.5 alpha 1.0

    show Aliya_stand_straight tshirt eyes_closed_sad as Aliya at imran_house_pos2:
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

    "Дождавшись меня, родители Алии и дядя Имран тоже встали." with dissolve

    show imran angry at imran_house_pos1 with dissolve:
        zoom 1.0
        alpha 1.0

    imran "Семён, мы сейчас поедем на автовокзал." with dissolve

    imran "Здесь рядом находится автобусная остановка, оттуда едут маршрутки до метро." with dissolve

    imran "Я бы вас подбросил, но вам будет быстрее и проще дойти самостоятельно. Хорошо?" with dissolve

    show imran neutral at imran_house_pos1 with dissolve:
        zoom 1.0
        alpha 1.0

    me "Ладно..." with dissolve

    "Я в последний раз посмотрел на Алию." with dissolve

    "Она смотрела в пол и выглядела очень грустной." with dissolve

    show imran angry at imran_house_pos1 with dissolve:
        zoom 1.0
        alpha 1.0

    imran "Давайте я вас провожу до ворот, Семён." with dissolve

    scene black with dissolve

    "Я вышел из дома в сопровождении Имрана..." with dissolve

    scene imran_house_outside_open_gate with dissolve

    $ savegame_picture = "savegame_imran_house_outside"

    show imran neutral at any_right_pos with dissolve:
        zoom 1.0

    "Он открыл ворота и мы вышли со двора на улицу, заставленную высокими заборами." with dissolve

    show imran angry at any_right_pos with dissolve:
        zoom 1.0

    imran "Если пойдёте в ту сторону, выйдете на Киевское шоссе. Там и находится автобусная остановка." with dissolve

    imran "Удачи, Семён!" with dissolve

    hide imran with dissolve

    "Мужчина вывел меня на дорогу, ушел и закрыл за мной ворота." with dissolve

    scene black with dissolve

    "Я медленно пошёл по направлению к автобусной остановке..." with dissolve

    jump day4_the_end_part1_option1_bus



label day4_the_end_part1_option1_bus:

    #play music "music/Runaway_01 (Pre_Loop).ogg"  fadein 1.0

    #queue music "music/Runaway_01 (Loop).ogg"

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

    "Был уже глубокий вечер. Я сидел на кухне съёмной квартиры." with dissolve

    "Алия с родителями сейчас ехала в автобусе, наверное, где-то под Ростовом." with dissolve

    "Я написал ей несколько сообщений, но ответа не было." with dissolve

    "В последний раз она была онлайн несколько часов назад." with dissolve

    "Может быть, в дороге нет связи или разрядился телефон?" with dissolve

    "Возможно, Алия просто устала и решила поспать?" with dissolve

    "Или... что, если" with dissolve

    "у неё все-таки отобрали телефон?" with dissolve

    "Я старался отгонять плохие мысли, но очень сложно не думать об этом." with dissolve

    "Передо мной на столе стоял недоеденный салат." with dissolve

    "У меня просто не было сил или желания выкинуть его в мусорку." with dissolve

    "Их хватало лишь для того, чтобы сидеть в телефоне, перечитывая переписку в мессенджере" with dissolve

    "и ожидая, когда наконец-то Алия будет онлайн." with dissolve

    if var_day3_photo_made:

        $ clearDisplayMessages()

        hide cg_screen_phone_top

        show cg_screen_phone_aliya_photo2 as cg_screen_phone with dissolve

        "Периодически я открывал и смотрел фотографию Алии в своём телефоне." with dissolve

        "Это тот снимок, который я украдкой заснял в Таганском парке." with dissolve

        "Единственное фото Алии, которое у меня есть - не считая, конечно, фотографии в паспорте." with dissolve

        "Алия улыбалась и смотрела мне прямо в глаза." with dissolve

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

    me "Мне не удалось уговорить родителей Алии лететь самолётом." with dissolve

    $ addSentMessage(4)

    me "Они просто забрали её у меня и уехали на автобусе." with dissolve

    $ addReceivedMessage(4)

    coach "Значит, ты не смог завоевать их доверие?" with dissolve

    $ addReceivedMessage(2)

    coach "Как там Алия?" with dissolve

    $ addSentMessage(5)

    me "Мне не удалось поговорить с ней наедине. Кажется, родители постоянно следили за ней." with dissolve

    $ addSentMessage(5)

    me "В последний раз, когда я её видел, она была очень грустной и обречённой." with dissolve

    jump day4_the_end_part2
