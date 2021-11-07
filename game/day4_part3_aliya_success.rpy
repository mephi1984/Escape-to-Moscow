label day4_imran_house_new_escape_succeed:

    if isMobileWeb:
        $ renpy.free_memory()

    play music "music/Runaway_14 (Pre_Loop).ogg" fadein 1.0

    queue music "music/Runaway_14 (Loop).ogg"

    scene black with dissolve

    "Я ждал, что мне ответит Алия..." with dissolve

    scene imran_house_doorway with dissolve

    show imran_room_drawers_food_full_near

    show Aliya_stand_straight tshirt eyes_closed_neutral as Aliya at aliya_imran_room_pos with dissolve:
        zoom 1.0

    "Воцарилось долгое молчание. Наконец Алия ответила." with dissolve

    show Aliya_stand_straight tshirt eyes_open_sad_smile as Aliya at aliya_imran_room_pos with dissolve:
        zoom 1.0

    aliya "Хорошо, Семён. Я верю тебе. Пожалуйста, не подведи меня!" with dissolve

    show Aliya special_pocket as Aliya at aliya_imran_room_pos with dissolve:
        zoom 1.0

    aliya "И вот ещё..." with dissolve

    show Aliya special_mask as Aliya at aliya_imran_room_pos with dissolve:
        zoom 1.0

    "Алия достала из кармана маску для лица, одну из тех, что я дал ей." with dissolve

    aliya "Возьми. Тебе это понадобится!" with dissolve

    show Aliya_stand_straight tshirt eyes_open_neutral as Aliya at aliya_imran_room_pos with dissolve:
        zoom 1.0

    "Я взял маску и положил к себе в карман." with dissolve

    show Aliya special_turned as Aliya at aliya_imran_room_pos with dissolve:
        zoom 1.0

    "Алия развернулась и покинула мою комнату." with dissolve

    hide Aliya with dissolve

    "А затем ушла вниз по лестнице." with dissolve

    "Я же остался один" with dissolve

    scene black with dissolve

    "наедине со своими мыслями, сэндвичем и чаем..." with dissolve

    scene imran_house_bedroom with dissolve

    $ savegame_picture = "savegame_imran_house_bedroom"

    show imran_room_drawers_food_empty_far as imran_room_drawers_food

    show imran_room_drawers_tea_no_cup_far as imran_room_drawers_cup

    show imran_room_hand_left_sandwich_eaten as imran_room_hand_left at imran_room_hand_pos with dissolve

    show imran_room_hand_right_cup as imran_room_hand_right at imran_room_hand_pos with dissolve

    "С момента, когда я оказался в доме Имрана, в голове вертелись тревожные мысли, а на душе - смятение." with dissolve

    "Но после слов Алии: \"Я верю тебе\", у меня в голове прояснилось, а все тревоги растворились." with dissolve

    hide imran_room_hand_left with dissolve

    "Как это удивительно, когда я живу для себя, то отношусь к себе снисходительно и расслабленно." with dissolve

    "Однако теперь мне нужно заботиться ещё об одном человеке, так что придётся постараться сделать всё возможное, чтобы не подвести её." with dissolve

    "Я знаю Алию только четвыре дня и за это время мы сбежали из Пятигорска, чтобы так глупо угодить в ловушку." with dissolve

    "В Пятигорске возбуждено уголовное дело и я рискую, в том числе, оказаться за решёткой." with dissolve

    "Возможно, мне не удастся вернуться в Россию ещё некоторое время. Может, придётся жить в Казахстане или в Киргизии." with dissolve

    "Конечно, сначала придется туговато, но без денег уж точно не останусь — я же фрилансер и могу работать где угодно." with dissolve

    "Все мои вещи остались в квартире родного города. А тут в съёмной квартире Москвы остался ноутбук, кое-какая электроника и шмотки." with dissolve

    "Надеюсь, по пути в аэропорт, я успею туда вернуться и забрать их. Надо также забрать вещи Алии." with dissolve

    "Алия... эта девушка за четыре дня перевернула всю мою жизнь и навсегда изменила моё будущее." with dissolve

    "И самое удивительное —  моя новая жизнь кажется мне намного привлекательнее той, что была раньше." with dissolve

    show imran_room_hand_right_cup_empty as imran_room_hand_right at imran_room_hand_pos with dissolve

    "Я допил остатки чая из чашки." with dissolve

    hide imran_room_hand_right with dissolve

    show imran_room_drawers_tea_cup_empty_far as imran_room_drawers_cup with dissolve

    show cg_screen_phone_tickets_buy1_search as cg_screen_phone with dissolve

    "Затем достал телефон и открыл приложение для покупки авиабилетов." with dissolve

    show cg_screen_phone_tickets_buy2_select as cg_screen_phone with dissolve

    "Родители Алии улетают в Минеральные Воды в пять часов вечера." with dissolve

    "И как раз за полчаса до этого рейса из Домодедово вылетает рейс той же авиакомпании в Усть-Каменогорск." with dissolve

    "Было бы удобнее лететь в Астану или в Алматы, но почему-то из Домодедово нет прямых рейсов туда." with dissolve

    "Ладно, выбора нет. Паспортные данные Алии у меня сохранены в телефоне." with dissolve

    show cg_screen_phone_tickets_buy3_pay as cg_screen_phone with dissolve

    show cg_foreground_card_hands_day with dissolve

    "Я достал свою кредитную карту-выручалку и купил нам билеты." with dissolve

    hide cg_foreground_card_hands_day with dissolve

    show cg_screen_phone_tickets_buy4_paid as cg_screen_phone with dissolve

    "Платёж прошёл, на телефоне появилось уведомление. Как обычно, я смахнул его не глядя." with dissolve

    show cg_screen_phone_tickets_buy5_paid_msg_gone as cg_screen_phone with dissolve

    "Страшно смотреть, сколько уже потрачено кредитных денег." with dissolve

    show cg_screen_phone_new_message_day4_afternoon_imran_home as cg_screen_phone with dissolve

    "Я посмотрел на время. Сейчас 12:37. До вылета примерно четыре часа." with dissolve

    $ hidePhone()

    "Если поеду прямо сейчас, успею заглянуть на съёмную квартиру и забрать вещи." with dissolve

    "Мне нужно покинуть комнату, не вызывая подозрений попрощаться со всеми, затем взять такси домой за вещами..." with dissolve

    "...скрытно приехать в аэропорт, снова помочь Алие сбежать и при этом не спалиться перед её родителями." with dissolve

    "Чтобы остаться неузнанным, мне придётся переодеться и надеть маску, которую мне дала Алия." with dissolve

    "Я слегка улыбнулся. План готов — пора действовать!" with dissolve

    hide imran_room_drawers_food with dissolve

    hide imran_room_drawers_cup with dissolve

    "Я взял пустые тарелку с чашкой и пошёл вниз." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    scene imran_house_living_room with dissolve

    $ savegame_picture = "savegame_imran_house_living_room"

    show imran neutral at imran_house_pos1:
        zoom 1.0
        alpha 0.0
        linear 0.5 alpha 1.0

    show Aliya_stand_straight tshirt eyes_open_sad_worried at imran_house_pos2:
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

    "В гостиной были Алия, её родители и дядя Имран. Я поставил посуду на стол," with dissolve

    "постарался придать себе спокойное выражение лица и начал говорить:" with dissolve

    me "Спасибо большое за обед, мне понравилось! К сожалению, мне пора уходить." with dissolve

    me "Я помог с авиабилетами, вам всего лишь потребуется приехать в аэропорт к трём часам дня и зарегистрироваться на рейс." with dissolve

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

    show Aliya_stand_straight tshirt eyes_open_sad_worried_open_mouth as Aliya at imran_house_pos2 with dissolve:
        zoom 1.0*0.9
        alpha 1.0

    aliya "Удачи!" with dissolve

    show Aliya_stand_straight tshirt eyes_open_sad_worried as Aliya at imran_house_pos2 with dissolve:
        zoom 1.0*0.9
        alpha 1.0


    show imran talking at imran_house_pos1 with dissolve:
        zoom 1.0
        alpha 1.0

    imran "Давай я открою тебе ворота!" with dissolve

    show imran neutral at imran_house_pos1 with dissolve:
        zoom 1.0
        alpha 1.0

    "Я мысленно улыбнулся: никто из них и не догадывается о моём плане, кроме Алии, конечно." with dissolve

    scene black with dissolve

    "В сопровождении Имрана я вышел во двор..." with dissolve

    scene imran_house_outside_open_gate with dissolve

    $ savegame_picture = "savegame_imran_house_outside"

    show imran neutral at any_right_pos with dissolve:
        zoom 1.0

    "Имран открыл ворота и мы вышли со двора на улицу, заставленную высокими заборами." with dissolve

    show imran talking at any_right_pos with dissolve:
        zoom 1.0

    imran "Если пойдёшь в ту сторону, выйдешь на Киевское шоссе, там находится автобусная остановка." with dissolve

    show imran neutral at any_right_pos with dissolve:
        zoom 1.0

    me "Спасибо, я вызову такси." with dissolve

    show imran talking at any_right_pos with dissolve:
        zoom 1.0

    imran "Ладно. Здесь шлагбаум, такси не проедет. Тебе всё равно нужно идти в том направлении." with dissolve

    show imran neutral at any_right_pos with dissolve:
        zoom 1.0

    me "Хорошо. Тогда я пошёл." with dissolve

    show imran talking at any_right_pos with dissolve:
        zoom 1.0

    imran "Счастливого пути!" with dissolve

    show imran neutral at any_right_pos with dissolve:
        zoom 1.0

    me "Спасибо! Вам тоже удачи!" with dissolve

    hide imran with dissolve

    "Имран вернулся домой, а я пошёл до Киевского шоссе по пути запустив приложение для вызова такси..." with dissolve

    scene black with dissolve

    "Я забрал со съёмной квартиры свои вещи, оставил ключи в почтовом ящике и поехал в аэропорт..." with dissolve

    jump airport_scene1


label airport_scene1:

    scene black with dissolve

    show day4_domodedovo_background zorder 1

    show day4_domodedovo_pillar_semyon_blurred at day4_domodedovo_pillar_pos zorder 4

    $ savegame_picture = "savegame_domodedovo"

    "План, предложенный Напарником, был довольно прост:" with dissolve

    "я должен приехать в аэропорт заранее," with dissolve

    "чтобы иметь достаточно времени для регистрации на рейс в Казахстан." with dissolve

    show day4_aliya_parents zorder 1 with dissolve

    "Чтобы к моменту прибытия Алии с родителями в аэропорт," with dissolve

    show day4_domodedovo_pillar_semyon at day4_domodedovo_pillar_pos zorder 3

    show day4_domodedovo_pillar_semyon_blurred at day4_domodedovo_pillar_pos zorder 4:
        alpha 1.0
        linear 1.0 alpha 0.0

    show day4_domodedovo_background_blurred zorder 2:
        alpha 0.0
        linear 1.0 alpha 1.0

    "я уже ждал их с посадочными талонами наготове." with dissolve

    $ persistent.gallery10unlock = True

    scene black with dissolve

    show day4_domodedovo_toilet

    $ savegame_picture = "savegame_domodedovo_toilet"

    show black zorder 10

    show day4_domodedovo_toilet_semyon1 as semyon

    hide black with dissolve

    "В Домодедово на первом этаже есть только один туалет." with dissolve

    "Чтобы туда пройти, нужно спустится вниз по лестнице, а затем пройти коридор." with dissolve

    "Там всегда тесно и ходит много людей." with dissolve

    "Согласно плану, я должен встать в этом коридоре, держа в руках посадочный талон Алии." with dissolve

    "Моё лицо должно быть скрыто маской, а голова — покрыта капюшоном." with dissolve

    show day4_domodedovo_toilet_aliya1 as aliya with dissolve

    "В определённое время Алия захочет пойти в туалет" with dissolve

    show day4_domodedovo_toilet_semyon2 as semyon with dissolve

    show day4_domodedovo_toilet_aliya2 as aliya with dissolve

    "и проходя мимо меня, незаметно заберёт из рук посадочный талон." with dissolve

    "Всё должно пройти быстро и скрытно." with dissolve

    hide aliya with dissolve

    "Когда посадочный талон будет у неё, моя часть плана будет завершена." with dissolve

    hide semyon with dissolve

    "Дождавшись когда Алия скроется из виду, я должен проследовать к рамкам досмотра и ждать её в чистой зоне." with dissolve

    $ persistent.gallery11unlock = True

    scene black with dissolve

    $ renpy.pause(1.0)

    scene domodedovo_check with dissolve

    $ savegame_picture = "savegame_domodedovo_check"

    "Ожидая Алию, я встал прямо возле эскалатора." with dissolve

    "Отсюда видны все запущенные в работу металлодетекторы." with dissolve

    "Я ждал и высматривал Алию в проходящих досмотр людях." with dissolve

    "Их было много и все они, проходя рамки, не торопясь собирали свои вещи и шли мимо меня..." with dissolve

    show aliya_airport after_security1 as Aliya with dissolve:
        zoom SCALE

    "Наконец, я увидел знакомый силуэт. Моё сердце забилось быстрее." with dissolve

    show aliya_airport after_security2 as Aliya with dissolve:
        zoom SCALE

    "Алия вышла из рамок, огляделась и, увидев меня," with dissolve

    play music "music/Runaway_15 (Pre_Loop).ogg" fadein 1.0
    queue music "music/Runaway_15 (Loop).ogg"


    "побежала сжимая в руках паспорт и посадочный талон." with dissolve


    hide Aliya with dissolve

    $ renpy.pause(0.3)

    show Aliya_stand_half_turned jacket_armsdown_light eyes_open_neutral as Aliya at any_right_pos with dissolve:
        zoom 1.0

    me "Ты в порядке?" with dissolve

    aliya "Да!" with dissolve

    "Она схватила меня за руку и мы побежали вниз по эскалатору." with dissolve

    scene black with dissolve

    "Бежали очень быстро..." with dissolve

    scene domodedovo_border with dissolve

    $ savegame_picture = "savegame_domodedovo_border"

    show Aliya_stand_half_turned jacket_armsdown_light eyes_open_neutral as Aliya at any_right_pos with dissolve:
        zoom 1.0

    "Турникеты позади, зелёный коридор мы преодолели не останавливаясь." with dissolve

    "И вот перед нами будки пограничного перехода: людей было немного, но ждать в очереди не хотелось." with dissolve

    "В большом зале было ощущение, что мы тут видны прямо как на ладони." with dissolve

    "К тому же родители Алии где-то недалеко, менее чем в 100 метрах от нас." with dissolve

    "Конечно, турникеты их не пустят, а в попытке проникнуть сюда, охрана их задержит, но всё же..." with dissolve

    "По совету Напарника, я начал высматривать пограничника, который дежурит в зале. Вот и он!" with dissolve

    show officer neutral at any_left_pos with dissolve:
        zoom 1.0

    me "Помогите пожалуйста, мы опаздываем на рейс! Вы не могли бы пропустить нас без очереди?" with dissolve

    "Ох, как же это звучало жалко и беспомощно, но, кажется, помогло. " with dissolve

    "Офицер взял наши посадочные талоны, посмотрел время вылета, взглянул на часы." with dissolve

    show officer talking at any_left_pos with dissolve:
        zoom 1.0

    officer "Следуйте сюда!" with dissolve

    show officer neutral at any_left_pos with dissolve:
        zoom 1.0

    "Пограничник указал на будку, на которой было написано \"Только для членов экипажа\"." with dissolve

    hide officer with dissolve

    "Я повернулся к Алие. Её глаза выражали уверенность, примерно так же, как в первый день нашего знакомства в аэропорту Минеральные Воды." with dissolve

    me "Когда загорится зелёная лампочка, проходи туда, отдай пограничнице свой паспорт и посадочный талон." with dissolve

    me "Она спросит, куда ты летишь - отвечай: \"В Казахстан, в Усть-Каменогорск, по внутреннему паспорту.\"." with dissolve

    me "Цель поездки - \"навестить знакомых\". Всё понятно?" with dissolve

    show Aliya_stand_half_turned jacket_armsdown_light eyes_open_sad_worried_open_mouth as Aliya at any_right_pos with dissolve:
        zoom 1.0

    aliya "Да." with dissolve

    hide Aliya with dissolve

    show aliya_airport at_border as Aliya at any_center_pos with dissolve:
        zoom SCALE

    "Вскоре загорелся зеленый свет, Алия подошла к будке и протянула свои документы." with dissolve

    "Пограничница что-то долго проверяла и я немного забеспокоился." with dissolve

    "Наконец, я услышал как она поставила печать на посадочный талон и вернула документы Алие." with dissolve

    hide Aliya with dissolve

    "Девушка прошла дальше. Следом к пограничнице подошёл я и протянул свои документы." with dissolve

    "Вскоре и мой посадочный талон украсила печать..." with dissolve

    scene black with dissolve

    #$ renpy.start_predict("images/sprites/Aliya/Pose4/*.*")

    "Я вышел в зону Duty Free вслед за Алией..." with dissolve

    scene domodedovo_duty_free with dissolve

    $ savegame_picture = "savegame_domodedovo_duty_free"

    show aliya_turn_around no_backpack eyes_open_neutral as Aliya at duty_free_aliya_pos with dissolve:
        zoom 1.0

    show cg_screen_phone_time_day4_afternoon_airport_duty_free as cg_screen_phone with dissolve

    $ persistent.gallery12unlock = True

    "Время на телефоне показывало 16:12, а это означало, что посадка скоро закончится. Надо скорее узнать какой у нас гейт и бежать туда!" with dissolve

    $ hidePhone()

    announcement "Внимание! Заканчивается посадка на рейс в Усть-Каменогорск." with dissolve

    announcement "Пассажиры Гаджиева Алия, Персунов Семён, опаздывающие на посадку," with dissolve

    announcement "Срочно приглашаются к выходу номер семь!" with dissolve

    "Я взял Алию за руку и побежал вперёд по коридору к гейту номер семь, ориентируясь по указателям." with dissolve

    "Мы подбежали к гейту, буквально, когда там проходили последние пассажиры." with dissolve

    "Сотрудница авиакомпании быстро пробила наши билеты, мы прошли через рукав в самолет, зашли в салон и сели на свои места." with dissolve

    jump day4_end_success
