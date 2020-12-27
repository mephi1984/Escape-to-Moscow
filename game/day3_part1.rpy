
label day3_intro:

    play music "ambience/airplane_1ambience_before_landing_loop.ogg" fadein 1.0 fadeout 1.0

    "В ушах звучал гул летящего самолета." with dissolve

    "Я был словно наполовину во сне, наполовину осознавая, что происходит вокруг." with dissolve

    play sound "sound/seatbelt.ogg"

    "Прозвучал звуковой сигнал \"пристегните ремни безопасности\"." with dissolve

    scene black

    announcement "Уважаемые дамы и господа, наш самолет приступил к снижению. Мы готовимся к посадке в аэропорту Минеральные Воды." with dissolve

    announcement "Просим вас пристегнуть ремни, привести спинки кресел в вертикальное положение, закрыть раскладные столики и открыть шторки на иллюминаторах." with dissolve

    show airplane_night at airplane_scene_pos with dissolve:
        ypos 0.525
        zoom 1.05

    "Я открыл глаза и нехотя потянулся в тесном кресле, прогоняя дрему." with dissolve

    show airplane_night at airplane_scene_pos:
        ypos 0.525
        zoom 1.05
        easein 4.0 ypos 0.475

    "Меня слегка дернуло вниз. Всем своим телом я почувствовал, как самолет, снижаясь, задрал нос вверх." with dissolve

    "От этого движения я окончательно проснулся." with dissolve

    "Я попытался вспомнить, как я оказался в самолете, прогоняя в голове воспоминания вчерашнего дня." with dissolve

    "Итак, вчера вечером я сидел за ноутбуком." with dissolve

    "Затем мне написала Алия." with dissolve

    "Затем я купил билеты в Минеральные Воды, чтобы полететь за ней." with dissolve

    "Я собрал вещи в рюкзак." with dissolve

    "За мной приехал Ярик на своем спортивном авто и отвез в аэропорт." with dissolve

    "Там я сел на рейс до Москвы, аэропорт Домодедово." with dissolve

    "Я прилетел в Москву. Погулял по ночному аэропорту как зомби." with dissolve

    "Потом сел на рейс до Минеральных Вод, и сразу же уснул в кресле." with dissolve

    "И вот я тут, сижу в кресле самолета." with dissolve

    "Самолет заходит на посадку в аэропорт Минеральные Воды." with dissolve

    "Я чувствую всем своим телом как самолет медленно снижается." with dissolve

    play music "ambience/airplane_2landed_shortened.ogg"

    queue music "ambience/airplane_3after_landing_loop.ogg"

    show airplane_night:
        ypos 0.475
        zoom 1.05
        linear 2.0 ypos 0.5
        linear 5.0 zoom 1.075

    "Бум! Самолет коснулся посадочной полосы и дернулся." with hpunch

    "Посадка была чуть более жестковатой, чем я ожидал." with dissolve

    "На крыльях поднялись спойлеры, и шум торможения наполнил мои уши." with dissolve

    "Самолет снизил скорость, и шум тоже заметно снизился." with dissolve

    announcement "Уважаемые дамы и господа, добро пожаловать в международный аэропорт Минеральные Воды." with dissolve

    announcement "Температура воздуха в Минеральных Водах плюс двенадцать градусов." with dissolve

    announcement "Местное время девять часов тридцать минут." with dissolve

    announcement "Для вашей безопасности, мы рекомендуем вам оставаться на местах с пристегнутыми ремнями безопасности до выключения светового табло \"пристегните ремни\"." with dissolve

    announcement "От имени авиакомпании благодарим вас за полет и будем рады новой встрече!" with dissolve

    show cg_screen_phone_time_day3_airplane_morning as cg_screen_phone with dissolve

    "Я проверил телефон, он был в авиарежиме. Время действительно было 9:30 утра." with dissolve

    "Алия должна меня встретить в 10 часов возле входа в аэропорт." with dissolve

    "Как раз достаточно времени. Пока самолет остановится, высадит всех пассажиров." with dissolve

    "Еще и неизвестно, может нас довезут от самолета до аэровокзала на автобусе." with dissolve

    stop music

    scene black with dissolve

    $ renpy.pause(1.0)

    scene mrv_interior2 with dissolve

    play music "music/Runaway_05 (Pre_Loop).ogg" fadein 1.0

    queue music "music/Runaway_05 (Loop).ogg"

    "Я вошел в здание аэровокзала один из первых, поскольку у меня не было багажа, только ручная кладь." with dissolve

    "Было утро, но в аэропорту уже было много людей." with dissolve

    $ renpy.show('cg_screen_phone', tag='cg_screen_phone')

    "Ой, я кажется еще не выключил авиарежим в телефоне. Включаю сеть..." with dissolve

    show cg_screen_phone_time_day3_airport_morning as cg_screen_phone with dissolve

    "Секундная пауза..." with dissolve

    show cg_screen_phone_new_message_day3_morning_airport1 as cg_screen_phone with dissolve

    messenger "Новое сообщение"  with dissolve # with hpunch

    $ changeDialogToAliya()

    $ showMessengerPhone(is_night=False, force_no_transition=True)

    $ addReceivedMessage(2)

    aliya_mobile "Привет! Ты уже прилетел?" with dissolve

    $ addSentMessage(2)

    me "Привет, да. Ты в порядке?" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Купи пожалуйста в аптеке маски на лицо" with dissolve

    $ addSentMessage(0)

    me "Хорошо" with dissolve

    $ clearDisplayMessages()

    $ hidePhone()

    "Итак, где же в этом аэропорту аптека? Перед глазами у меня только такси, аренда авто и сим-карты." with dissolve

    "Нужно оглянуться. Вот табло, вот стойки регистрации... ага, вот и аптека!" with dissolve

    "Я купил на всякий случай три маски - \"вдруг одну сломаю, а вторую потеряю\", по привычке, благо они дешевые." with dissolve

    "Маски у меня есть, и в запасе есть еще немного времени до того, как Алия приедет." with dissolve

    "Я чувствую легкое волнение, которое наполнило мое тело." with dissolve

    "Такое же чувство я испытывал давным-давно, когда еще был школьником и ходил на свидания с девушками." with dissolve

    "С тех пор прошло много лет, а я до сих пор чувствую некоторую робость в общении с женским полом." with dissolve

    "Так, надо взять себя в руки, я уже не застенчивый школьник, я должен вести себя взрослее!" with dissolve

    "И вообще это не свидание." with dissolve

    "В первую очередь мне нужно доставить Алию в Москву и обустроить ее жизнь там." with dissolve

    messenger "Новое сообщение"  with dissolve

    show cg_screen_phone_new_message_day3_morning_airport2 as cg_screen_phone with dissolve

    "Я снова достал телефон." with dissolve

    $ showMessengerPhone(is_night=False, force_no_transition=True)

    $ addReceivedMessage(3)

    aliya_mobile "Привет! Я приехала, ты где?" with dissolve

    $ addSentMessage(1)

    me "Я внутри!" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Подходи к главному входу" with dissolve

    $ addSentMessage(1)

    me "Окей, выхожу!" with dissolve

    $ clearDisplayMessages()

    $ hidePhone()

    "Я убрал телефон и пошел к главному входу..." with dissolve

    jump day3_meet_aliya


label day3_meet_aliya:

    scene mrv_exterior with dissolve

    "... я вышел наружу и огляделся." with dissolve

    me "Алия!.." with dissolve

    play music_crossfade "music/Runaway_06 (Loop).ogg" fadein 1.0

    queue music_crossfade "music/Runaway_06 (Loop).ogg"

    stop music fadeout 1.0

    # Now here we need to unlock Aliya in the main menu
    $ persistent.menu_unlocked_aliya = True

    show aliya_anim_frame1 as aliya_anim at any_center_pos with dissolve:
        zoom 0.75*SCALE

    me "Это ты?.." with dissolve

    show aliya_anim at any_center_pos with dissolve:
        zoom 0.75*SCALE

    "Алия обернулась..." with dissolve

    aliya "Привет..." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    scene mrv_exterior with dissolve

    show Aliya stand_straight_mask_eyes_open_neutral at any_center_pos with dissolve:
        zoom 0.75*SCALE

    "А она довольно маленькая девушка. Меньше, чем я себе представлял." with dissolve

    "Неловкое молчание... так, Семен, не тупи, скажи что-нибудь!" with dissolve

    me "Как себя чувствуешь?" with dissolve

    show Aliya stand_half_turned2_eyes_closed_sad_worried_open_mouth extra_stand_half_turned2_mask at any_center_pos with dissolve:
        zoom 0.75*SCALE

    aliya "Сойдет." with dissolve

    show Aliya stand_half_turned2_eyes_open_sad_worried_open_mouth extra_stand_half_turned2_mask at any_center_pos with dissolve:
        zoom 0.75*SCALE

    "Опять неловкая пауза!" with dissolve

    "Кажется мой мозг решил взять перерыв. Как обычно, в самый важный момент." with dissolve

    me "Ты очень смелая. Я думал, что ты испугаешься и передумаешь в самый последний момент." with dissolve

    aliya "Я тоже так думала." with dissolve

    "Что теперь? Ах да, маски." with dissolve

    show airport_semyon_gives_mask with dissolve

    me "Я купил тебе маски. Вот, возьми!" with dissolve

    hide airport_semyon_gives_mask with dissolve

    show Aliya special_jacket_pocket no_mask at any_center_pos with dissolve:
        zoom 0.75*SCALE

    "Алия ловким движением сняла свою старую маску, положила в карман..." with dissolve

    show Aliya special_jacket_mask_wear at any_center_pos with dissolve:
        zoom 0.75*SCALE

    "Затем распечатала новую маску и надела ее." with dissolve

    show Aliya stand_half_turned2_eyes_closed_smile extra_stand_half_turned2_mask at any_center_pos with dissolve:
        zoom 0.75*SCALE

    aliya "Спасибо." with dissolve

    show Aliya stand_half_turned2_eyes_open_smile extra_stand_half_turned2_mask at any_center_pos with dissolve:
        zoom 0.75*SCALE

    me "Ты носишь маску, потому что боишься что тебя узнают?" with dissolve

    show Aliya stand_straight_mask_eyes_open_angry no_mask at any_center_pos with dissolve:
        zoom 0.75*SCALE

    "Алия посмотрела на меня настороженно." with dissolve

    aliya "У меня аллергия." with dissolve

    aliya "Поэтому я ношу маску." with dissolve

    me "Понятно." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    scene mrv_exterior with dissolve

    show Aliya stand_straight_mask_eyes_open_neutral at any_center_pos with dissolve:
        zoom 0.75*SCALE

    "Ладно, поприветствовали друг друга, теперь возвращаемся к первоначальному плану." with dissolve

    if day2_night_car_coach_talked==True: # Coach adviced to give money

        "Я решил воспользоваться советом Напарника и дать Алие немного наличных денег." with dissolve

        show airport_semyon_gives_money with dissolve

        me "И вот держи, деньги. Три тысячи рублей." with dissolve

        hide airport_semyon_gives_money with dissolve

        show Aliya special_jacket_pocket_mask at any_center_pos with dissolve:
            zoom 0.75*SCALE

        "Алия недоверчиво взяла пачку купюр и положила в карман." with dissolve

        show Aliya stand_straight_mask_eyes_closed_neutral at any_center_pos with dissolve:
            zoom 0.75*SCALE

        aliya "Спасибо." with dissolve

        show Aliya stand_straight_mask_eyes_open_neutral at any_center_pos with dissolve:
            zoom 0.75*SCALE

        me "Это тебе, на случай если мы вдруг потеряемся. Или если ты передумаешь, и захочешь вернуться назад." with dissolve



    # At this point aliya_trust_points_hard: max=2 min=0



    me "Давай теперь пройдем внутрь?" with dissolve

    show Aliya stand_straight_mask_eyes_open_sad3 at any_center_pos with dissolve:
        zoom 0.75*SCALE

    aliya "Хорошо, пошли." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    scene mrv_interior2 with dissolve

    show aliya_turn_around eyes_open_watching mask as Aliya at any_left_pos with dissolve:
        zoom 0.75*SCALE

    "Мы вошли в здание аэровокзала. Здесь становилось многолюдно." with dissolve

    "Я нашел наконец пару свободных сидений в отдаленном углу. Надеюсь, нас никто не будет подслушивать." with dissolve

    me "Вон там свободно. Пойдем туда?" with dissolve

    aliya "Хорошо." with dissolve

    scene black with dissolve

    "Я сел на сиденье, и Алия села рядом с мной..." with dissolve

    scene mrv_interior2_chair with dissolve

    show aliya_sit eyes_open_neutral mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    "Я вздохнул, и начал разговор." with dissolve

    me "Итак, вот он я, Семен. Я обычный человек, не маньяк, как ты видишь." with dissolve

    me "Сейчас по плану, мы регистрируемся на рейс и затем проходим в чистую зону. Там мы садимся на самолет." with dissolve

    me "Если я покажусь тебе страшным, или если ты передумаешь сбегать, ты можешь в любой момент до посадки на рейс передумать." with dissolve

    me "Выйдешь из аэропорта, садишься на такси и едешь домой." with dissolve

    me "После посадки на самолет ты уже не сможешь вернуться назад. Мы с тобой высадимся уже в Москве." with dissolve

    show aliya_sit eyes_closed_sad mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Понимаю." with dissolve

    me "Все в порядке?" with dissolve

    show aliya_sit eyes_open_sad_worried mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Да." with dissolve

    show aliya_sit_bench_phone eyes_open_watching_phone mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    "Телефон Алии завибрировал два раза. Алия взяла в руки телефон и разблокировала его." with dissolve

    show aliya_sit_bench_phone eyes_open_watching_phone4 mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    "Кажется, она немного испугалась." with dissolve

    show aliya_sit eyes_open_cry_sad2 mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Сестра мне написала. Спрашивает, где я." with dissolve

    aliya "Что мне ответить?" with dissolve

    me "Пока ничего не отвечай. А лучше переведи телефон в авиарежим." with dissolve

    aliya "Хорошо." with dissolve

    show aliya_sit eyes_closed_sad mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    "Алия быстро включила авиарежим и убрала телефон в карман." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    scene mrv_interior2_chair with dissolve

    show aliya_sit eyes_open_neutral mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    me "Когда мы приедем в Москву, нам нужно будет сделать тебе новую сим-карту." with dissolve

    aliya "Да, конечно." with dissolve

    show aliya_sit eyes_closed_sad_worried_open_mouth mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "И еще мне нужно будет купить кое-что." with dissolve

    me "Что тебе нужно?" with dissolve

    show aliya_sit eyes_open_neutral mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Нужно будет купить коврик для намаза." with dissolve

    aliya "И платье, закрывающее ноги и рукава." with dissolve

    aliya "Я не хочу сегодня пропускать намаз." with dissolve

    me "Ты молишься пять раз в день?" with dissolve

    show aliya_sit eyes_open_sad_worried_question mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Стараюсь. Но раз в день уж точно нужно." with dissolve

    me "Ты сегодня еще не молилась?" with dissolve

    show aliya_sit eyes_open_neutral mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Нет. И мне желательно до вечера успеть сделать намаз." with dissolve

    menu:

        "Согласиться купить коврик и платье?"

        "Да":
            jump day3_meet_aliya_success

        "Нет":
            jump day3_meet_aliya_almost_fail


label day3_meet_aliya_success:

    scene black with dissolve

    $ renpy.pause(1.0)

    scene mrv_interior2_chair with dissolve

    show aliya_sit eyes_open_sad_worried_open_mouth mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    me "Хорошо. Когда мы приедем в Москву, мы поищем тебе коврик и платье." with dissolve

    show aliya_sit eyes_closed_smile mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Спасибо." with dissolve

    show aliya_sit eyes_open_smile mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    me "Еще тебе нужно будет купить обычную ежедневную одежду." with dissolve

    me "Но это можно будет сделать завтра." with dissolve

    show aliya_sit eyes_open_neutral mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Хорошо." with dissolve

    show aliya_sit eyes_open_sad_worried_question mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "А где мы будем ночевать?" with dissolve

    me "В обычную гостиницу мы не поедем." with dissolve

    me "Когда ты регистрируешься в гостинице, ты предъявляешь паспорт." with dissolve

    show aliya_sit eyes_closed_sad mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Мне нельзя показывать паспорт. Родители же узнают, где я остановилась!" with dissolve

    show aliya_sit eyes_open_sad_worried_open_mouth mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Есть другие места?" with dissolve

    me "Можно снять квартиру или найти хостел, где не требуется паспорт." with dissolve

    show aliya_sit eyes_open_sad_worried mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Что такое хостел?" with dissolve

    me "Что-то типа общежития. Там есть женские и мужские спальни." with dissolve

    me "В каждой комнате от 4 до 8 спальных мест. Обычно это двухъярусные кровати." with dissolve

    show aliya_sit eyes_closed_neutral mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Я поняла." with dissolve

    me "Там есть туалеты, душевые, общая кухня. В хостелах обычно останавливаются студенты." with dissolve

    show aliya_sit eyes_open_neutral mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE


    aliya "Хорошо." with dissolve

    me "Можно также снять квартиру, но это будет дороже." with dissolve

    me "Впрочем, я пока еще не решил точно. Мы решим это позже." with dissolve

    aliya "Хорошо." with dissolve

    me "А на следующий день, нужно будет открыть для тебя банковскую карточку." with dissolve

    aliya "Там нужно показывать паспорт?" with dissolve

    me "Да, конечно." with dissolve

    show aliya_sit eyes_open_surprised mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Мне нельзя! Родители вычислят меня!" with dissolve

    me "Тебе нужно будет сходить в банк всего два раза." with dissolve

    me "Чтобы оформить карточку, и чтобы забрать ее." with dissolve

    me "Родители не смогут вычислить твое местонахождение по карточке." with dissolve

    me "Максимум что они узнают - это в каком отделении ты открыла карточку." with dissolve

    me "А мы можем открыть карточку в любом банке в любом месте Москвы." with dissolve

    show aliya_sit eyes_open_sad_worried_open_mouth mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE


    aliya "Хорошо. А мне не нужна прописка в Москве?" with dissolve

    me "Нет, чтобы сделать карточку, нужно всего лишь иметь российский паспорт." with dissolve

    show aliya_sit eyes_open_sad_worried mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "А зачем мне нужна карточка?" with dissolve

    me "В будущем ты будешь получать на нее зарплату." with dissolve

    aliya "А нам обязательно оформлять карточку прямо сразу?" with dissolve

    me "Я просто опасаюсь, что родители объявят твой паспорт в розыск." with dissolve

    me "После этого он попадет в список недействительных паспортов." with dissolve

    me "И тогда уже с ним мало что можно будет сделать." with dissolve

    me "Поэтому я хочу чтобы ты оформила банковскую карточку поскорее." with dissolve

    show aliya_sit eyes_open_neutral mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Поняла." with dissolve

    aliya "А что я буду делать, когда мой паспорт станет недействительным?" with dissolve

    me "Если ты успеешь до этого найти работу и открыть счет в банке, то ничего страшного." with dissolve

    me "Если не успеешь найти работу, то будет сложно устроиться в крупную компанию." with dissolve

    aliya "В крупную компанию?" with dissolve

    me "Ну типа Макдоналдс, Икея, Декатлон." with dissolve

    show aliya_sit eyes_open_sad_worried mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "И где я тогда буду работать?" with dissolve

    me "Вероятно, мелкие магазины и кафе не пробивают паспорт по базам недействительных паспортов." with dissolve

    me "Можно устроиться работать там." with dissolve

    show aliya_sit eyes_open_neutral mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Хорошо. Я буду работать официанткой?" with dissolve

    me "Возможно." with dissolve

    me "В Москве много вакансий для массовых позиций." with dissolve

    me "Ты можешь работать кассиршей, официанткой, бариста, продавцом-консультантом, поваром." with dissolve

    aliya "Сколько я могу заработать?" with dissolve

    me "Я думаю, от 25 до 30 тысяч рублей в месяц." with dissolve

    show aliya_sit eyes_open_surprised mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Это много?" with dissolve

    me "Нет, не очень. Этого хватит, чтобы снимать комнату где-нибудь на окраине и более-менее сносно жить." with dissolve

    show aliya_sit eyes_open_neutral mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Я поняла." with dissolve

    aliya "Наверное, мне еще нужно будет заново поступить учиться." with dissolve

    me "Да, это несложно. В Москве много студентов, которые учатся и работают одновременно." with dissolve

    show aliya_sit eyes_open_sad_worried mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Как они совмещают?" with dissolve

    me "Ну днем учеба, вечером смена. Как-то так." with dissolve

    show aliya_sit eyes_open_neutral mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Поняла." with dissolve

    me "Об этом можно будет подумать уже после того, как ты обустроишься в Москве." with dissolve

    aliya "Хорошо." with dissolve

    aliya "И еще нужно оформить загранпаспорт!" with dissolve

    me "Это можно сделать через МФЦ, либо удаленно через сайт Госуслуги." with dissolve

    me "Но если твой отец объявит твой паспорт в розыск, то сделать загранпаспорт не получится." with dissolve

    aliya "И что тогда?" with dissolve

    me "Я вижу несколько вариантов." with dissolve

    me "Мы можем подождать, пока тебя не перестанут искать. И уже тогда начать делать все документы." with dissolve

    me "Либо мы можем, например, выехать в Беларусь и попробовать получить загранпаспорт там." with dissolve

    me "В крайнем случае, попробуем сделать тебе поддельные документы на чужое имя и использовать их." with dissolve

    aliya "Понятно..." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    scene mrv_interior2_chair with dissolve

    show aliya_sit eyes_open_neutral mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Я готова, пойдем. Авиабилеты у тебя?" with dissolve

    me "Да, билеты у меня в телефоне. Нам нужно зарегистрироваться на рейс, распечатать посадочный талон и пройти досмотр." with dissolve

    show cg_screen_phone_airplane_app1 as cg_screen_phone with dissolve

    "Я достал телефон и открыл приложение авиакомпании." with dissolve

    show cg_screen_phone_airplane_app2 as cg_screen_phone with dissolve

    me "Какое место тебе выбрать, возле окна?" with dissolve

    show aliya_sit eyes_closed_smile mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    "Алия слегка улыбнулась." with dissolve

    aliya "Да." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    scene mrv_interior2 with dissolve

    "Я уже летал сегодня этой авиакомпанией, поэтому процесс регистрации не занял долгое время." with dissolve

    "Багажа у нас нет, поэтому мы просто подошли к автомату самостоятельной регистрации и распечатали посадочные талоны." with dissolve

    "Получив посадочные талоны, мы отправились в зону досмотра и к выходам на посадку." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    jump day3_airport_inner


label day3_meet_aliya_almost_fail:

    $ aliya_trust_points_hard = aliya_trust_points_hard - 1

    show aliya_sit eyes_open_sad_worried_open_mouth mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    me "У нас навряд ли будет на это время, уж очень накладно будет искать в Москве нужные магазинчики." with dissolve

    me "Да и не ты ли говорила, что в Москве у тебя родня. Вдруг с ними столкнёшься." with dissolve

    show aliya_sit eyes_closed_annoyed mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Они точно не станут искать подобные вещи, всё это есть у каждого мусульманина." with dissolve

    me "А без этого никак? Ну иначе там помолиться ты не можешь?" with dissolve

    show aliya_sit eyes_open_angry mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Иначе? Ты себе это, как представляешь?" with dissolve

    me "Ну, не знаю, к примеру как христиане?" with dissolve

    aliya "Семен, ты уж прости, но я не христианка. Я мусульманка и следую нашим традициям." with dissolve

    me "Хорошо-хорошо, следуй, но разве без платья и коврика ты уже и помолиться не можешь?" with dissolve

    aliya "А разве ваши девушки ходят в церковь без головных уборов, или же бабки сидят в церквях? Нет, хотя в других верах есть и такое." with dissolve

    me "И к чему ты это?" with dissolve

    show aliya_sit eyes_closed_annoyed mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Да, к тому, что не будь мне нужно это платье и коврик я бы и простить не стала." with dissolve

    aliya "Моя религия очень важна для меня, разве это не понятно. Я ведь и раньше об этом говорила." with dissolve

    menu:

        "Согласиться купить коврик и платье?"

        "Да":
            jump day3_meet_aliya_success

        "Нет, продолжать настаивать":
            jump day3_meet_aliya_fail


label day3_meet_aliya_fail:

    scene black with dissolve

    $ renpy.pause(1.0)

    scene mrv_interior2_chair with dissolve

    show aliya_sit eyes_open_sad_worried_open_mouth mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    me "Мне всё же кажется, что это странно. Столько приготовлений ради простой молитвы." with dissolve

    me "Ну что, пойдем?" with dissolve

    show aliya_sit eyes_closed_sad mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Подожди..." with dissolve

    show aliya_sit_bench_phone eyes_open_watching_phone mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    "Алия поколебалась, посмотрела в телефон, вздохнула." with dissolve

    show aliya_sit eyes_open_sad_worried_question mask as aliya_sit at any_center_pos with dissolve:
        zoom SCALE

    aliya "Мне нужно сходить в туалет." with dissolve

    me "Хорошо, это где-то в той стороне." with dissolve

    "Я указал пальцем в сторону туалетов." with dissolve

    hide aliya_sit with dissolve

    "Алия резко встала, накинула рюкзак и пошла в ту сторону." with dissolve

    "Как-то очень резко... наверное ей очень нужно." with dissolve

    "Я сел и стал ждать..." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    scene mrv_interior2_chair with dissolve

    "Прошло как-то много времени. Я начал беспокоиться." with dissolve

    $ changeDialogToAliya()

    $ showMessengerPhone(is_night=False, force_no_transition=True)

    "Я достал телефон и проверил мессенджер. Алия недавно была в сети." with dissolve

    "Я решил написать ей." with dissolve

    $ addSentMessage(3)

    me "Привет, ты там долго еще?" with dissolve

    "Сообщение прочитано." with dissolve

    $ aliya_banned = True

    show cg_screen_phone_messenger_top_aliya_banned as cg_screen_phone_top with dissolve

    "Аватарка исчезла." with dissolve

    "\"Миса Амане была в сети давно\"." with dissolve

    $ clearMessagesAfterBan()

    "Вслед за аватаркой исчезли все сообщения." with dissolve

    "Кажется меня кинули в ЧС." with dissolve

    $ hidePhone()

    "Я убрал телефон, оглянулся и попытался глазами найти Алию в зале. Но ее нигде не было рядом." with dissolve

    stop music_crossfade fadeout 1.0

    play music "music/Runaway_16 (Pre_Loop).ogg" fadein 1.0

    queue music "music/Runaway_16 (Loop).ogg"

    scene black with dissolve

    "Кажется, она сбежала. Ничего теперь не поделать." with dissolve

    "Похоже, мне придется возвращаться домой..." with dissolve

    #"THE END, спасибо что поиграли! Концовка 4, \"Третий день, Семен поругался с Алией из-за религии\"" with dissolve

    $ renpy.pause(1.0)

    jump credits



label day3_airport_inner:

    scene mrv_interior3 with dissolve

    "Предпосадочный досмотр мы прошли довольно быстро." with dissolve

    "Алию немного задержали в момент проверки паспорта и посадочного талона." with dissolve

    "Наверное, сотрудник аэропорта вычислял в уме, было ли ей 18 лет или нет." with dissolve

    "Но ее все-таки пропустили, и вот мы оказались в чистой зоне." with dissolve

    "Мы нашли свободное место возле нашего выхода на посадку. Я сел на сиденье." with dissolve

    show aliya_sit_front eyes_open_neutral with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    "Алия села напротив меня." with dissolve

    "Еще есть время перед посадкой. Итак, о чем бы поговорить?" with dissolve

    me "Ты хочешь есть?" with dissolve

    show aliya_sit_front eyes_closed_sad with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Нет." with dissolve

    "Неудачное начало." with dissolve

    me "Нас будут кормить в самолете, во время полета. Рекомендую тебе поесть. Нельзя оставаться голодной" with dissolve

    show aliya_sit_front eyes_open_thinking_hands_inside with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Ладно." with dissolve

    me "Как ты себя чувствуешь, в целом?" with dissolve

    show aliya_sit_front eyes_open_neutral with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Сойдет." with dissolve

    "Я не очень хорошо разбираюсь в людях, но сейчас я вижу, что Алия все еще чувствует себя неспокойно." with dissolve

    "Возможно надо бы ее успокоить." with dissolve

    "Может поговорить о чем-то отвлеченном?" with dissolve

    me "У нас еще есть время перед посадкой." with dissolve

    me "Что ты обычно делаешь, когда у тебя появляется свободное время?" with dissolve

    show aliya_sit_front eyes_open_sad_worried_open_mouth with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Слушаю музыку, смотрю аниме. Или корейские драмы" with dissolve

    show aliya_sit_front eyes_open_sad_worried with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    me "Тебе нравится аниме?" with dissolve

    show aliya_sit_front eyes_open_sad_worried_open_mouth with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Да. Там короткие серии, по 20 минут." with dissolve

    aliya "В корейских драмах один эпизод длится час. Это очень долго смотреть." with dissolve

    aliya "Хотя я иногда смотрю, например вечером." with dissolve

    show aliya_sit_front eyes_open_sad_worried with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    me "А почему ты заинтересовалась Кореей?" with dissolve

    show aliya_sit_front eyes_closed_smile with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    "Алия улыбнулась." with dissolve

    show aliya_sit_front eyes_open_smile with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "У меня есть лучшая подруга. Она меня и подсадила." with dissolve

    aliya "Она русская. Мы учимся вместе." with dissolve

    aliya "Она познакомила меня с корейскими группами." with dissolve

    show aliya_sit_front eyes_open_playful with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "У меня даже есть биас... но я не скажу, кто это." with dissolve

    "Надо будет в свободное время узнать об этом побольше." with dissolve

    show black zorder 10 with dissolve

    show aliya_sit_front eyes_open_cry_sad2:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    "Прошло еще немного времени..." with dissolve

    hide black with dissolve

    "Наконец, прозвучало очередное объявление по громкоговорителю." with dissolve

    show aliya_sit_front eyes_open_sad_worried_question with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    announcement "Начинается посадка на рейс номер сто пятьдесят четыре, выполняющий рейс в Москву, аэропорт Домодедово." with dissolve

    announcement "Пассажиров просим пройти к выходу номер один." with dissolve

    me "Это наш рейс." with dissolve

    show aliya_sit_front eyes_open_sad_worried_open_mouth with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE


    aliya "Да." with dissolve

    me "Если ты хочешь передумать и вернуться домой, сейчас у тебя есть последний шанс." with dissolve

    show aliya_sit_front eyes_closed_sad with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE


    aliya "Я лечу с тобой в Москву." with dissolve

    me "Хорошо. Тогда приготовь посадочный талон, пойдем на посадку!" with dissolve

    show aliya_sit_front eyes_open_smile with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Хорошо." with dissolve

    stop music_crossfade fadeout 1.0

    stop music fadeout 1.0

    scene black with dissolve

    "Мы поднялись на борт самолета, заняли свои места, и самолет отправился в Москву..." with dissolve

    $ renpy.pause(1.0)

    jump day3_airplane




label day3_airplane:

    play music "ambience/airplane_1ambience_before_landing_loop.ogg" fadein 1.0 fadeout 1.0

    scene airplane_day with dissolve

    "Наш самолет только что набрал высоту и выровнялся." with dissolve

    play sound "sound/seatbelt.ogg"

    "Прозвучал звук отключения индикатора \"пристегните ремни\"." with dissolve

    announcement "Уважаемые пассажиры, вы можете отстегнуть ремни безопасности, однако мы рекомендуем вам оставаться пристегнутыми на протяжении всего полета." with dissolve

    announcement "Туалеты находятся в хвостовой части самолета. Вам будут предложены обед и напитки. Желаем вам приятного полета!" with dissolve

    scene black as airplane_background with dissolve

    show black zorder 10

    #‭6998 / 1920 = 3.6447916666666666666666666666667‬  ~ 3.64479167

    show cg_airplane_window1 as airplane_window_left at cg_airplane_window_pos_start zorder 1:
        xpos 0.0
        linear 365.0 xpos -3.64479167
        repeat

    show cg_airplane_window1 as airplane_window_right at cg_airplane_window_pos_start zorder 1:
        xpos 3.64479167
        linear 365.0 xpos 0.0
        repeat


    show airplane_day_side as airplane_scene at airplane_scene_pos zorder 2:
        zoom 1.02

    show aliya_sit_no_earphones special_airplane_window as aliya_sit at any_center_pos zorder 3:
        zoom SCALE

    hide black with dissolve

    "Алия сидела рядом и смотрела в окно на облака." with dissolve

    me "Как ощущения?" with dissolve

    aliya "Красиво." with dissolve

    me "Ты ведь до этого вообще не летала на самолете?" with dissolve

    show aliya_sit_no_earphones eyes_open_smile as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Не летала." with dissolve

    aliya "Только на поезде и на автобусе." with dissolve

    aliya "И на автомобиле, конечно же." with dissolve

    me "Ты умеешь водить автомобиль?" with dissolve

    show aliya_sit_no_earphones eyes_closed_grin as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Нет. Обычно меня возит мой отец." with dissolve

    me "Понятно." with dissolve

    show aliya_sit_no_earphones eyes_open_smile as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "У меня ощущение, что я в автобусе еду. Сиденья такие же." with dissolve

    aliya "Только здесь совсем не трясет. Как будто едем по очень ровной дороге." with dissolve

    me "Да. И очень быстро." with dissolve

    aliya "Сколько нам еще лететь?" with dissolve

    me "Мы только взлетели. Будем еще лететь два часа." with dissolve

    aliya "Поняла." with dissolve

    show black zorder 10 with dissolve

    $ renpy.pause(1.0)

    jump day3_airplane2

label day3_airplane2:

    show aliya_sit_no_earphones special_airplane_take_out_from_bag as aliya_sit zorder 3 at any_center_pos:
        zoom SCALE

    hide black with dissolve

    "Алия достала из своей сумки небольшую книжку." with dissolve

    show aliya_sit_no_earphones special_airplane_watching_book_neutral as aliya_sit zorder 3 at any_center_pos with dissolve:
        zoom SCALE

    me "Что это?" with dissolve

    show aliya_sit_no_earphones special_airplane_watching_book_look_aside as aliya_sit zorder 3 at any_center_pos with dissolve:
        zoom SCALE

    aliya "Это стихи." with dissolve

    me "Ты любишь читать стихи?" with dissolve

    aliya "Да, это же так красиво. А ты не любишь?" with dissolve

    me "Я учил стихи давно, еще когда был в школе." with dissolve

    me "Да и вообще, стихи очень сложно читать." with dissolve

    show aliya_sit_no_earphones special_airplane_watching_book_look_aside_talk as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Почему? Ты же хорошо знаешь русский язык?" with dissolve

    me "Ну да, но там образы, метафоры." with dissolve

    show aliya_sit_no_earphones special_airplane_watching_book_search as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Алия быстро начала листать страницы в книжке." with dissolve

    show aliya_sit_no_earphones special_airplane_pass_book as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Затем Алия протянула мне книжку." with dissolve

    aliya "Вот, прочитай это. И скажи, что ты думаешь." with dissolve

    show aliya_sit_no_earphones eyes_open_neutral as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    me "Белеет парус одинокой." with dissolve

    me "В тумане моря голубом!.." with dissolve

    show aliya_sit_no_earphones eyes_closed_smile as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Алия слегка усмехнулась." with dissolve

    show aliya_sit_no_earphones eyes_open_smile as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Можешь читать про себя." with dissolve

    "Да, точно. Ладно, продолжу читать про себя." with dissolve

    "Итак..." with dissolve

    "Белеет парус одинокой" with dissolve

    "В тумане моря голубом!.." with dissolve

    "Что ищет он в стране далекой?" with dissolve

    "Что кинул он в краю родном?.." with dissolve

    "Играют волны — ветер свищет," with dissolve

    "И мачта гнется и скрыпит..." with dissolve

    "Увы! он счастия не ищет" with dissolve

    "И не от счастия бежит!" with dissolve

    "Под ним струя светлей лазури," with dissolve

    "Над ним луч солнца золотой..." with dissolve

    "А он, мятежный, просит бури," with dissolve

    "Как будто в бурях есть покой!" with dissolve

    "... я закончил читать и посмотрел на Алию." with dissolve

    show aliya_sit_book eyes_open_sad_worried_open_mouth as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "И что ты думаешь?" with dissolve

    me "Эээ, ну, корабль плывет, с белым парусом." with dissolve

    show aliya_sit_book eyes_open_neutral as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Да, ты прямо как компьютер." with dissolve

    "Алия сделала паузу." with dissolve

    aliya "Белый парус в синем море - это душа, ищущая перемен." with dissolve

    aliya "Этот стих о важных решениях, которые меняют твою жизнь." with dissolve

    me "Хмм, да, в этом есть смысл." with dissolve

    show aliya_sit_book eyes_open_smile as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Мне нравятся стихи. В них есть идеи и мысли, уложенные в складную рифму." with dissolve

    show aliya_sit_no_earphones special_airplane_watching_book_smile as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Алие определенно нравится говорить о литературе и поэзии." with dissolve

    "Может стоит поговорить с ней об этом?" with dissolve

    menu:

        "Что сделать?"

        "Спросить о стихах":
            jump day3_airplane2_part1_poetry

        "\"Извини, мне это не интересно\"":
            jump day3_airplane2_part1_ignore


label day3_airplane2_part1_poetry:

    $ aliya_trust_points_hard = aliya_trust_points_hard + 1 # aliya_trust_points_hard by that point max = 3

    me "А кто тебе больше из поэтов нравится?" with dissolve

    show aliya_sit_no_earphones special_airplane_watching_book_look_aside as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Из русских, наверное, больше всего Анна Ахматова, Александр Блок, ещё Борис Пастернак и Михаил Лермонтов." with dissolve

    me "А кто любимый из них?" with dissolve

    aliya "Наверное Ахматова, она интересная личность и стихи у неё очень глубокие, как-никак представительница серебряного века." with dissolve

    me "Ясно... Кстати, вот объясни мне ты что вообще люди под серебряным веком подразумевают? Я помню что-то из школьных лет, но..." with dissolve

    show aliya_sit_book eyes_open_sad_worried_open_mouth as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Ну... Если простыми словами, то это был период, когда поэты и писатели 19 века дали толчок развитию литературы, вывели на новый уровень." with dissolve

    show aliya_sit_book eyes_open_neutral as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Название, кстати, дали по аналогии с золотым веком. Ахматова, как по мне по праву может носить звание поэтессы этого периода." with dissolve

    "Я почувствовал себя как будто я снова в школе на уроке литературы." with dissolve

    me "И чем же она тебе так приглянулась?" with dissolve

    show aliya_sit_book eyes_closed_neutral as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Сложно сказать, у неё много стихов, что цепляют, наверное, этим." with dissolve

    show aliya_sit_book eyes_open_neutral as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "У неё есть стихи, о любви о войне, о родине, о жизни... И при этом каждый вызывает эмоции." with dissolve

    me "Есть любимые?" with dissolve

    show aliya_sit_book eyes_open_smile as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Да, «Реквием», «Сероглазый король» и «Когда погребают эпоху»." with dissolve

    me "И, о чём они?" with dissolve

    show aliya_sit_book eyes_open_neutral as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Серьёзно? Это же классика." with dissolve

    me "Извини, но поэзия мне как-то не особо..." with dissolve

    show aliya_sit_book eyes_closed_neutral as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Ясно... Но объяснять будет долго, особенно, если ты их не читал." with dissolve

    me "А хотя бы вкратце." with dissolve

    show aliya_sit_book eyes_open_neutral as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Это будет неуважительно, особенно к «Реквиему» у него весьма серьёзная предыстория. Почитай, а там я объясню." with dissolve

    me "Договорились." with dissolve

    show aliya_sit_book eyes_open_sad_smile as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Кстати, я тоже немного стихи пишу, но пока выходит не очень." with dissolve

    me "А можешь что-нибудь прочесть?" with dissolve

    show aliya_sit_no_earphones eyes_open_sad_smile as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Да, есть пару небольших стишков." with dissolve

    show aliya_sit_no_earphones eyes_closed_neutral as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Алия сделала паузу и приготовилась читать." with dissolve

    show aliya_sit_no_earphones eyes_open_sad_worried_open_mouth as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Темных глаз загадочный мрак," with dissolve

    aliya "Алых губ заманчивая сладость." with dissolve

    aliya "Как увижу попадаю впросак," with dissolve

    aliya "Ты моя последняя слабость." with dissolve

    show aliya_sit_no_earphones eyes_open_neutral as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    me "Неплохо, даже очень." with dissolve

    aliya "И ещё из неплохих." with dissolve

    show aliya_sit_no_earphones eyes_closed_neutral as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Алия сделала паузу." with dissolve

    show aliya_sit_no_earphones eyes_open_sad_worried_open_mouth as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Я давно не верю в сказку и чудеса," with dissolve

    aliya "Не прошу подарков у сказочного деда." with dissolve

    aliya "Но, как и в детстве я смотрю на небеса," with dissolve

    aliya "Всё дожидаясь, твоего последнего совета." with dissolve

    show aliya_sit_no_earphones eyes_open_neutral as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    me "Сильно. Мне нравится!" with dissolve

    show aliya_sit_no_earphones eyes_open_sad_smile as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Спасибо!" with dissolve

    jump day3_airplane2_part2


label day3_airplane2_part1_ignore:

    show aliya_sit_book eyes_open_neutral as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    me "Извини, но я лично очень плохо такие идеи улавливаю." with dissolve

    me "Мне проще читать простой текст, прозу." with dissolve

    aliya "Я поняла." with dissolve

    show aliya_sit_no_earphones special_airplane_watching_book_smile as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Алия отвернулась и стала читать книгу." with dissolve

    jump day3_airplane2_part2


label day3_airplane2_part2:

    show black zorder 10 with dissolve

    $ renpy.pause(1.0)

    show airplane_day_side as airplane_scene at airplane_scene_pos zorder 2:
        zoom 1.02

    show aliya_sit_no_earphones special_airplane_watching_book_smile as aliya_sit zorder 3 at any_center_pos:
        zoom SCALE

    hide black with dissolve

    "Тем временем, тележки с напитками и сэндвичами уже приближалась к нашему ряду." with dissolve

    me "Что ты будешь пить и есть?" with dissolve

    show aliya_sit_book eyes_open_neutral as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Я не хочу есть." with dissolve

    me "Возьми хотя бы воду." with dissolve

    show aliya_sit_no_earphones eyes_open_sad_worried as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Хорошо." with dissolve

    me "Там на выбор дают два сэндвича - с курицей или с сыром." with dissolve

    me "Ты точно не хочешь есть?" with dissolve

    show aliya_sit_no_earphones eyes_open_sad_worried_open_mouth as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Я не в настроении. Если я что-то съем, боюсь, меня стошнит." with dissolve

    show aliya_sit_no_earphones eyes_open_neutral as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    me "Ладно." with dissolve

    me "А ты завтракала?" with dissolve

    aliya "Нет." with dissolve

    "Если Алия с утра ничего не ела и не будет есть сейчас, то это не хорошо." with dissolve

    "Мне бы не хотелось, чтобы она упала в голодный обморок в конце дня." with dissolve

    "Надо будет напомнить себе, чтобы вечером купить ей что-нибудь поесть." with dissolve

    show airplane_day_side_table as airplane_scene at airplane_scene_pos zorder 2:
        zoom 1.02

    "Я открыл откидные столики." with dissolve

    "Тележка с напитками приехала к нашему ряду." with dissolve

    flight_attendant "Что будете пить?" with dissolve

    me "Воду и апельсиновый сок." with dissolve

    aliya "Воду пожалуйста." with dissolve

    "Бортпроводница передала два стакана мне и один стакан Алие." with dissolve

    show aliya_sit_no_earphones special_airplane_hold_cap as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Я после разговоров очень хотел пить, поэтому сразу же выпил полстакана воды." with dissolve

    show aliya_sit_no_earphones eyes_open_neutral as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    show airplane_cap zorder 4 with dissolve

    "Алия лишь слегка отхлебнула, и поставила стакан на откидной столик." with dissolve

    "Вскоре приехала и тележка с едой." with dissolve

    flight_attendant "Вам сендвич с курицей или с сыром?" with dissolve

    me "С курицей." with dissolve

    "Бортпроводница передала сэндвич с курицей." with dissolve

    "Поскольку в последний раз я ел несколько часов назад, я с аппетитом набросился на еду." with dissolve

    show aliya_sit_no_earphones special_airplane_watching_book_neutral as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Алия даже не посмотрела. Она взяла в руки книгу, начала читать, и, видимо, думала о чем-то своем." with dissolve

    show black zorder 10 with dissolve

    show airplane_day_side as airplane_scene at airplane_scene_pos zorder 2:
        zoom 1.02

    show aliya_sit_no_earphones special_airplane_watching_book_neutral as aliya_sit at any_center_pos zorder 3:
        zoom SCALE

    hide airplane_cap

    $ renpy.pause(1.0)

    hide black with dissolve

    "Наконец, я закончил есть." with dissolve

    show aliya_sit_no_earphones eyes_open_neutral as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    me "Предлагаю теперь поспать. Нам еще лететь примерно час." with dissolve

    aliya "Хорошо." with dissolve

    show aliya_sit_no_earphones special_airplane_take_out_from_bag as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Алия достала сумку и положила туда книгу." with dissolve

    show aliya_sit_no_earphones special_airplane_sleep as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Затем она устроилась в кресле поудобнее, и закрыла глаза." with dissolve

    "Я немного задержал взгляд на ней." with dissolve

    "Волосы частично закрывали ее лицо. Но я все равно отметил про себя, что она очень красивая." with dissolve

    "Ладно, наверное и мне лучше тоже прилечь поспать." with dissolve

    show black zorder 10 with dissolve

    "Я прилег в кресле и закрыл глаза." with dissolve

    "И погрузился в сон..." with dissolve

    jump day3_airplane3



label day3_airplane3:

    play sound "sound/seatbelt.ogg"

    "Прозвучал звук включения индикатора \"пристегните ремни\"." with dissolve

    announcement "Уважаемые пассажиры, мы готовимся к посадке в городе Москва, аэропорт Домодедово." with dissolve

    announcement "Пожалуйста, пристегните ремни, приведите спинки кресел в горизонтальное положение, уберите откидные столики и откройте шторки на иллюминаторах." with dissolve

    show aliya_sit_no_earphones special_airplane_sleep as aliya_sit at any_center_pos zorder 3:
        zoom SCALE


    show cg_airplane_window1 as airplane_window_left at cg_airplane_window_pos_start zorder 1:
        xpos 0.0
        linear 365.0 xpos -3.64479167
        repeat

    show cg_airplane_window1 as airplane_window_right at cg_airplane_window_pos_start zorder 1:
        xpos 3.64479167
        linear 365.0 xpos 0.0
        repeat

    hide black with dissolve

    "Я открыл глаза и огляделся. Как же быстро пролетело время." with dissolve

    show aliya_sit_no_earphones eyes_closed_neutral as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Алия тоже проснулась." with dissolve

    show aliya_sit_no_earphones eyes_open_neutral as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Мы уже в Москве?" with dissolve

    me "Да. Уже совсем скоро мы приземлимся в Москве." with dissolve

    "Алия ничего не ответила." with dissolve

    show aliya_sit_no_earphones special_airplane_phone_earphones as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Вместо ответа, она достала телефон, надела наушники и включила музыку." with dissolve

    show aliya_sit_no_earphones special_airplane_phone_semen_watch2 as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Затем она повернулась ко мне." with dissolve

    show aliya_sit_no_earphones special_airplane_phone_semen_watch1 as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Ты слушаешь рок-музыку?" with dissolve

    show aliya_sit_no_earphones special_airplane_phone_semen_watch2 as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    me "Иногда." with dissolve

    show aliya_sit_no_earphones special_airplane_phone_semen_watch1 as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Хочешь послушать мой плейлист?" with dissolve

    show aliya_sit_no_earphones special_airplane_phone_semen_watch2 as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    me "Давай." with dissolve

    aliya "Мне нравится пост-рок. Сейчас включу тебе одну из моих любимых песен." with dissolve

    show aliya_sit_no_earphones special_airplane_pass_earphones as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Алия протянула мне наушник." with dissolve

    show aliya_sit_no_earphones special_airplane_window_earphones as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    play music_crossfade "music/Runaway_07 (Main_Theme).ogg" fadein 1.0
    queue music_crossfade "music/Runaway_07 (Main_Theme_Loop).ogg"

    "Я вставил наушник в ухо. В наушниках заиграла рок-музыка." with dissolve

    #1998 / 1080 = 1.85

    #8638 / 1920 = 4.4989583333333333333333333333333‬  ~ 4.49896


    show cg_airplane_window2 as airplane_window2_left_top zorder 0:
        xpos 0.0
        ypos 0.07
        linear 450.0*0.5 xpos -4.49896 ypos (-1.85 + 0.07)
        repeat

    show cg_airplane_window2 as airplane_window2_right_top zorder 0:
        xpos 4.49896
        ypos 0.07
        linear 450.0*0.5 xpos 0.0 ypos (-1.85 + 0.07)
        repeat

    show cg_airplane_window2 as airplane_window2_left_bottom zorder 0:
        xpos 0.0
        ypos (1.85 + 0.07)
        linear 450.0*0.5 xpos -4.49896 ypos 0.07
        repeat

    show cg_airplane_window2 as airplane_window2_right_bottom zorder 0:
        xpos 4.49896
        ypos (1.85 + 0.07)
        linear 450.0*0.5 xpos 0.0 ypos 0.07
        repeat

    show airplane_day_side as airplane_scene at airplane_scene_pos zorder 2:
        zoom 1.02
        ypos 0.5
        linear 0.2 ypos 0.51
        easeout 2.0 ypos 0.5

    show aliya_sit_no_earphones special_airplane_window_earphones as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE
        ypos 1.0
        linear 0.2 ypos 1.01
        easeout 2.0 ypos 1.0

    hide airplane_window_left with dissolve

    hide airplane_window_right with dissolve

    "Самолет слегка дернулся, и начал идти на снижение." with dissolve

    "Погода была довольно ясной, и из иллюминатора можно было видеть Подмосковье." with dissolve

    "Алия слушала музыку и внимательно смотрела в иллюминатор." with dissolve

    "Хотя она была неподвижна, я чувствовал, что она сильно волнуется." with dissolve

    "Ее беспокойство немного передавалось мне." with dissolve

    "Возможно, ее родители все еще думают, что она на учебе." with dissolve

    "А может быть, они уже хватились и ищут ее?" with dissolve

    "Назад уже не вернуться, мы уже почти приземлились в Москве." with dissolve

    "Надо довести начатое до конца." with dissolve

    "Я снова бросил взгляд на Алию." with dissolve

    "Она все так же неподвижно смотрит в иллюминатор." with dissolve

    "Несмотря на волнение, в ее глазах читалась некоторая обреченность и уверенность." with dissolve

    "Интересно, если бы она не встретилась бы со мной - сбежала бы она из дома?" with dissolve

    "С ее-то характером - очень может быть!" with dissolve

    "Возможно, она сбежала бы одна. Автостопом добралась бы до Краснодара или Ростова." with dissolve

    "Возможно, ей бы помог сбежать какой-нибудь другой человек." with dissolve

    "Может быть, это был бы какой-нибудь плохой парень." with dissolve

    "С нехорошими намерениями..." with dissolve

    "Брр! Даже не хочу об этом думать." with dissolve

    "Самое важное - Алия сейчас сидит здесь, рядом со мной." with dissolve

    "Она доверяет мне, и я не должен разрушить ее доверие." with dissolve

    "Пока она со мной, она в безопасности." with dissolve

    "Если я обману ее или воспользуюсь ей - она сбежит уже и от меня." with dissolve

    "И вот тогда я уже не смогу ей ничем помочь." with dissolve

    "Так уж получилось, что я оставил свои дела и решил ввязаться в эту историю." with dissolve

    "И я не буду бросать все на полпути." with dissolve

    "Сейчас уже вторая половина дня, что мы еще успеем сделать за сегодня?" with dissolve

    "Купим платье для намаза, раз уж Алия этого очень хочет." with dissolve

    "Сделаем сим-карту, заселимся в гостиницу или в хостел." with dissolve

    "Поужинаем, возможно купим что-нибудь по мелочи." with dissolve

    "Все остальное - банковская карта, покупка сменной одежды и бытовых вещей, поиск работы и т. д. - оставим на завтра." with dissolve

    "Я думаю, я потрачу немало денег на это приключение." with dissolve

    "По крайней мере до тех пор, пока Алия не обустроится в Москве, не найдет работу, съемное жилье." with dissolve

    "Но почему-то денег мне не жалко." with dissolve

    "Я свое еще заработаю. А вот Алия действительно нуждается в моей поддержке." with dissolve

    "И я постараюсь ее не подвести!" with dissolve

    show aliya_sit_no_earphones special_airplane_window_earphones as aliya_sit at any_center_pos zorder 3:
        zoom SCALE

    "Самолет уверенно снижался." with dissolve

    "В иллюминаторе уже можно было разглядеть дома, деревья, автомобили на дорогах." with dissolve

    # x 2.271875
    # y 0.74074



    show cg_airplane_window3 as airplane_window_left at cg_airplane_window_pos_start3 zorder 1:
        parallel:
            xpos 0.0
            linear 45.0 xpos -2.271875
        parallel:
            ypos 0.12
            easein 5.5 ypos -0.04

        block:
            xpos 0.0
            ypos -0.04
            linear 45.0 xpos -2.271875
            repeat

    show cg_airplane_window3 as airplane_window_right at cg_airplane_window_pos_start3 zorder 1:
        xpos 2.271875
        ypos -0.04
        linear 45.0 xpos 0.0
        repeat

    hide airplane_window2_right_top

    hide airplane_window2_right_bottom

    hide airplane_window2_left_top

    hide airplane_window2_left_bottom

    "И вот наконец внизу под крылом показалась широкое полотно взлетно-посадочной полосы." with dissolve

    "Мы уже летим прямо над широким серым полотном." with dissolve

    "Еще чуть-чуть и шасси коснутся взлетно-посадочной полосы." with dissolve

    play music "ambience/airplane_2landed_shortened.ogg"

    queue music "ambience/airplane_3after_landing_loop.ogg"

    "Бух!" with hpunch

    "И сразу самолет начал тормозить. Всех пассажиров дернуло вперед." with dissolve

    "С громким шумом и грохотом самолет снизил скорость." with dissolve

    "Мы уже медленно катились по посадочной полосе." with dissolve

    show aliya_sit_no_earphones special_airplane_phone as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    stop music_crossfade fadeout 1.0

    "Пришло время вытащить наушник." with dissolve

    announcement "Уважаемые дамы и господа, добро пожаловать в Москву, международный аэропорт Домодедово." with dissolve

    announcement "Местное время четырнадцать часов, двадцать минут. Погода в Москве ясная, температура воздуха плюс двадцать градусов тепла." with dissolve

    announcement "Пожалуйста, оставайтесь на своих местах с пристегнутыми ремнями безопасности до выключения светового табло \"пристегните ремни\"." with dissolve

    announcement "От имени авиакомпании благодарим вас за полет и будем рады новой встрече!" with dissolve

    show cg_screen_phone_time_day3_afternoon_airplane as cg_screen_phone with dissolve

    "Я достал телефон и выключил авиарежим." with dissolve

    $ hidePhone()

    show aliya_sit_no_earphones special_airplane_phone as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    show aliya_sit_no_earphones eyes_open_neutral as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Алия посмотрела на меня." with dissolve

    show aliya_sit_no_earphones eyes_open_sad_worried_question as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Мне тоже выключить авиарежим?" with dissolve

    me "Лучше пока не надо." with dissolve

    show aliya_sit_no_earphones special_airplane_phone as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Ладно." with dissolve

    show aliya_sit_no_earphones eyes_open_watching as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Алия убрала телефон." with dissolve

    show aliya_sit_no_earphones eyes_open_neutral as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Мы от аэропорта долго будем ехать?" with dissolve

    me "Да, 40 минут примерно." with dissolve

    me "Мы возьмем Аэроэкспресс до Москвы, он отправляется в 15:00." with dissolve

    me "И мы приедем на Павелецкий вокзал примерно в 15:40. Оттуда нужно будет поехать на метро." with dissolve

    show aliya_sit_no_earphones eyes_open_sad_worried_question as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Ты не забыл, что нам нужно будет купить коврик и одежду?" with dissolve

    me "Да, конечно." with dissolve

    show aliya_sit_no_earphones eyes_open_neutral as aliya_sit at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    scene black with dissolve

    $ renpy.pause(1.0)

    scene airplane_day with dissolve

    "Наконец самолет остановился." with dissolve

    announcement "Бортпроводникам, приготовится к переводу селекторов в положение Disarmed." with dissolve

    announcement "Бортпроводникам, перевести селекторы в положение Disarmed." with dissolve

    play sound "sound/seatbelt.ogg"

    "Прозвучал звук выключения индикатора \"пристегните ремни\"." with dissolve

    play music "ambience/airplane_stopped_loop.ogg"

    scene airplane_day2 with dissolve

    "Пассажиры начали вставать с кресел, собирать сумки и чемоданы, а затем и выходить из самолета." with dissolve

    "Я и Алия тоже встали, забрали вещи и пошли к выходу." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    scene domodedovo_luggage with dissolve

    play music "music/Runaway_08 (Pre_Loop).ogg" fadein 1.0

    queue music "music/Runaway_08 (Loop).ogg"

    "Мы прошли через телетрап и вышли в зону выдачи багажа." with dissolve

    show Aliya stand_half_turned2_eyes_open_sad_smile at any_center_pos with dissolve:
        zoom 0.75*SCALE

    aliya "Здесь мы должны забрать наш багаж?" with dissolve

    me "Да. Но мы не сдавали сумки в багаж, поэтому мы должны сразу идти на выход." with dissolve

    show Aliya stand_half_turned2_eyes_open_sad_worried_open_mouth at any_center_pos with dissolve:
        zoom 0.75*SCALE

    aliya "Тогда можно я в туалет схожу?" with dissolve

    me "Да, хорошо. Он должен быть где-то справа." with dissolve

    me "Я пока что куплю билеты на аэроэкспресс." with dissolve

    show Aliya stand_half_turned_eyes_open_smile at any_center_pos with dissolve:
        zoom 0.75*SCALE

    aliya "Хорошо. Я быстро!" with dissolve

    hide Aliya with dissolve

    show cg_screen_phone_aeroexpress1 as cg_screen_phone with dissolve

    "Алия ушла, а я зашел в приложение Аэроэкспресса." with dissolve

    "С недавних пор приложение требует вводить паспортные данные пассажира." with dissolve

    "Очередной бред от спецслужб, наверное. Все равно никто не контролирует правильность этих данных." with dissolve

    "Я просто куплю оба наши билета на свой паспорт." with dissolve

    show cg_screen_phone_aeroexpress2 as cg_screen_phone with dissolve

    "Так, тут требуется вводить номер карты." with dissolve

    show semen_room_table_night_foreground_card_hands zorder 2 with dissolve

    "Я достал свою кредитную карту-выручалочку, и ввел данные." with dissolve

    hide semen_room_table_night_foreground_card_hands with dissolve

    show cg_screen_phone_aeroexpress3 as cg_screen_phone with dissolve

    "Пришло СМС с уведомлением об успешной покупке." with dissolve

    show cg_screen_phone_aeroexpress4 as cg_screen_phone with dissolve

    "Я смахнул СМС в сторону не глядя. Мне уже страшно проверять, сколько у меня осталось денег на карточке." with dissolve

    "Тем временем, подошла Алия." with dissolve

    show Aliya stand_straight_eyes_open_smile at any_center_pos with dissolve:
        zoom 0.75*SCALE

    aliya "Мы готовы?" with dissolve

    me "Я тебе отправлю QR-код в мессенджере." with dissolve

    me "Отключи авиарежим на телефоне ненадолго, чтобы получить сообщение с кодом." with dissolve

    me "Когда мы будем проходить на аэроэкспресс, тебе нужно будет поднести телефон с кодом к сканеру." with dissolve

    $ switchMessengerToPhone()

    $ changeDialogToAliya()

    $ showMessengerPhone(is_night=False, force_no_transition=True)

    show Aliya stand_half_turned2_eyes_open_happy at any_center_pos with dissolve:
        zoom 0.75*SCALE

    aliya "Хорошо." with dissolve

    show Aliya stand_half_turned2_eyes_open_watching_phone extra_stand_half_turned2_phone at any_center_pos with dissolve:
        zoom 0.75*SCALE

    $ addSentMessageQr()

    "Я сделал скриншот и отправил Алие." with dissolve

    $ clearDisplayMessages()

    $ hidePhone()

    me "Пошли?" with dissolve

    show Aliya stand_straight_eyes_open_smile no_extra at any_center_pos with dissolve:
        zoom 0.75*SCALE

    aliya "Пошли." with dissolve

    scene black with dissolve

    "Мы отправились к аэроэкспрессу..." with dissolve

    jump day3_aeroexpress



label day3_aeroexpress:

    scene aeroexpress with dissolve

    show aliya_sit_front eyes_open_neutral with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    "Мы успешно прошли к вагонам аэроэкспресса и заняли места на первом этаже." with dissolve

    "Здесь было тихо, других пассажиров, кроме нас, в вагоне не было." with dissolve

    announcement "Уважаемые пассажиры, просим вас занять свои места. Аэроэкспресс отправляется через десять минут!" with dissolve

    "Я попытался подключиться к вайфаю, но в аэроэкспрессе он был очень медленный." with dissolve

    "Так что мне пришлось использовать мобильный интернет." with dissolve

    me "Говоришь, тебе нужно будет купить коврик для намаза?" with dissolve

    show aliya_sit_front eyes_closed_sad with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Да, и платье." with dissolve

    me "Есть идеи, где это можно купить?" with dissolve

    show aliya_sit_front eyes_open_sad_worried_open_mouth with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "На рынке точно продается." with dissolve

    show aliya_sit_front eyes_open_sad_worried with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    me "Это Москва. Здесь с рынками не очень." with dissolve

    me "Я поищу какие-нибудь магазины с мусульманскими товарами." with dissolve

    show aliya_sit_front eyes_open_thinking_hands_inside with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Хорошо." with dissolve

    show cg_screen_phone_map1 as cg_screen_phone with dissolve

    "Я открыл приложение с картой и начал искать." with dissolve

    me "Вот тут на Таганской есть несколько магазинов." with dissolve

    me "Скорее всего там же и одежду продают." with dissolve

    show aliya_sit_front eyes_open_sad_smile with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Это хорошо." with dissolve

    me "Плохо что они закрываются в шесть часов вечера." with dissolve

    show aliya_sit_front eyes_open_sad_worried with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "А во сколько мы там можем быть?" with dissolve

    show aliya_sit_front eyes_open_sad_worried with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    show cg_screen_phone_metro_map as cg_screen_phone with dissolve

    "Я посмотрел карту метро Москвы." with dissolve

    me "Аэроэкспресс привезет нас в 15:40 на станцию метро Павелецкая." with dissolve

    me "Это кольцевая линия метро." with dissolve

    me "Нам нужно будет спуститься в метро, сделать тебе карту Тройка." with dissolve

    me "Проехать одну станцию, затем выйти на Таганской и немного пройтись пешком." with dissolve

    show aliya_sit_front eyes_open_sad_worried_question with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Карту тройка?" with dissolve

    $ hidePhone()

    me "Ну это, карточка для оплаты проезда в Москве. Туда нужно положить деньги, затем оплачивать проезд." with dissolve

    me "Работает и в метро, и на автобусах, троллейбусах, трамваях." with dissolve

    show aliya_sit_front eyes_open_neutral with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "И сколько мы будем ехать туда?" with dissolve

    me "На метро быстро, но нам еще нужно будет пройти пешком. Минут 20-30 займет." with dissolve

    aliya "Я поняла." with dissolve

    me "Если мы не найдем ничего подходящего в мусульманском магазине, скорее всего нам придется искать другой магазин." with dissolve

    me "Думаю, мы сегодня немало на метро будем ездить." with dissolve

    aliya "Хорошо." with dissolve

    show aliya_sit_front eyes_open_sad_worried_question with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Что нам еще нужно будет купить?" with dissolve

    me "Будет уже поздно. Я думаю, мы еще должны сделать тебе новую сим-карту." with dissolve

    me "И больше мы ничего сегодня не успеем сделать." with dissolve

    me "Все остальное оставим на завтра." with dissolve

    aliya "А где мы будем ночевать?" with dissolve

    "Вообще то я до сих пор не забронировал жилье." with dissolve

    me "Пока не знаю. Но я думаю, пора начать искать сейчас." with dissolve

    show aliya_sit_front eyes_open_thinking_hands_outside with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Хорошо!" with dissolve

    show cg_screen_phone_booking as cg_screen_phone with dissolve

    "Я начал смотреть приложения для бронирования." with dissolve

    "В какой-то момент я понял, что совершенно не знаю, где можно арендовать жилье не показывая паспорт." with dissolve

    show cg_screen_phone_booking_new_message as cg_screen_phone with dissolve

    messenger "Новое сообщение"

    $ changeDialogToCoach()

    $ showMessengerPhone(is_night=False, force_no_transition=True)

    $ addReceivedMessage(2)

    coach "Привет Семен! Как дела?" with dissolve

    $ addSentMessage(3)

    me "Мы уже в Москве, сели на Аэроэкспресс" with dissolve

    $ addSentMessage(5)

    me "Но у нас есть небольшая проблема. Нам нужно найти жилье, где не спрашивают паспорт" with dissolve

    $ addReceivedMessage(3)

    coach "В Москве много квартир сдаются посуточно" with dissolve

    $ addReceivedMessage(2)

    coach "На любом столбе есть объявления" with dissolve

    $ addReceivedMessage(3)

    coach "Ты из тех людей, которые не любят звонить по телефону?" with dissolve

    $ addSentMessage(2)

    me "Ну вообще-то да..." with dissolve

    $ addReceivedMessage(0)

    coach ":)" with dissolve

    $ addReceivedMessage(2)

    coach "Давай я забронирую тебе жилье" with dissolve

    $ addReceivedMessage(5)

    coach "Напиши примерный район где вы будете жить, я начну искать там" with dissolve

    $ addSentMessage(4)

    me "В районе недалеко от станции метро Таганская. Квартиру на неделю" with dissolve

    $ addReceivedMessage(5)

    coach "Хорошо. Прямо возле метро не обещаю, но постараюсь найти в том районе Москвы" with dissolve

    $ addReceivedMessage(3)

    coach "Есть какие-то дополнительные пожелания?" with dissolve

    $ addSentMessage(4)

    me "Чистая квартира с ремонтом, раздельные кровати" with dissolve

    $ addSentMessage(1)

    me "Больше ничего" with dissolve

    $ addReceivedMessage(4)

    coach "Хорошо! Я начну искать! Я напишу, когда забронирую вам жилье" with dissolve

    $ addSentMessage(0)

    me "Спасибо!" with dissolve

    $ clearDisplayMessages()

    $ hidePhone()

    stop music fadeout 2.0

    "Я убрал телефон." with dissolve

    "Прошло немного времени..." with dissolve

    play sound "sound/aeroexpress.ogg"

    announcement "Уважаемые пассажиры, аэроэкспресс в Москву отправляется сейчас! Длительность поездки составит сорок минут." with dissolve

    announcement "Осторожно, двери закрываются! Следующая станция - Павелецкий вокзал." with dissolve

    "Двери вагона тихо закрылись." with dissolve

    "Вагон тронулся, затем начал медленно разгоняться." with dissolve

    show aliya_sit_front eyes_open_thinking_hands_inside with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    "Алия начала смотреть в окно." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    play music "ambience/440611__florianreichelt__train-ambience.ogg" fadein 1.0 fadeout 1.0

    scene aeroexpress with dissolve

    show aliya_sit_front eyes_open_thinking_hands_inside with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    "Мы уже въехали в Москву и неторопливо ехали к Павелецкому вокзалу." with dissolve

    "Я решил прервать молчание." with dissolve

    me "Ты в порядке?" with dissolve

    show aliya_sit_front eyes_open_sad_worried_question with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    "Алия посмотрела на меня." with dissolve

    aliya "Да." with dissolve

    me "Есть хочешь?" with dissolve

    aliya "Нет." with dissolve

    "Надо поговорить о чем-нибудь, но о чем?" with dissolve

    me "Расскажи, где ты хочешь учиться?" with dissolve

    me "Ты хочешь учиться в колледже на медика?" with dissolve

    show aliya_sit_front eyes_closed_neutral with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Нет." with dissolve

    show aliya_sit_front eyes_open_neutral with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Я вообще не хочу быть медиком." with dissolve

    aliya "Я туда поступила, потому что отец обещал мне, что если я буду хорошо учиться, то потом смогу пойти в университет." with dissolve

    aliya "Но потом он отказался от своих слов." with dissolve

    aliya "Мне тогда было 16. Мне родители сказали, что не смогут после колледжа отдать меня в университет." with dissolve

    aliya "Мне было очень плохо. Я полностью забила на учебу." with dissolve

    aliya "Я даже пыталась порезать себе вены. В туалете в своем коллежде." with dissolve

    aliya "Мне было уже все равно. Мне не хотелось жить." with dissolve

    aliya "И теперь мой отец хочет, чтобы я вышла замуж." with dissolve

    aliya "У него не хватает денег, чтобы оплатить мою учебу." with dissolve

    me "Если бы у тебя были деньги, куда бы ты хотела поступить учиться?" with dissolve

    show aliya_sit_front eyes_open_smile with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    "Алия улыбнулась." with dissolve

    aliya "В МГИМО." with dissolve

    me "Хороший выбор." with dissolve

    "Надо будет загуглить, сколько там стоит обучение." with dissolve

    me "Может быть когда-нибудь ты сможешь поступить туда." with dissolve

    show aliya_sit_front eyes_closed_smile with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Возможно." with dissolve

    me "А кем ты вообще хочешь быть в жизни?" with dissolve

    show aliya_sit_front eyes_open_sad_worried with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Не знаю." with dissolve

    me "Что тебе нравится делать?" with dissolve

    show aliya_sit_front eyes_open_happy with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Смотреть аниме и драмы, читать стихи. Еще я готовить люблю." with dissolve

    me "Может тебе стоит стать поваром?" with dissolve

    me "В будущем станешь крутым шеф-поваром, откроешь свой ресторан." with dissolve

    show aliya_sit_front eyes_closed_grin with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    "Алия улыбнулась еще больше." with dissolve

    show aliya_sit_front eyes_open_playful with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Я думала открыть свой ресторан, да." with dissolve

    aliya "Я уже мечтала в каком месте он будет, какое там будет меню, интерьер." with dissolve

    show aliya_sit_front eyes_open_neutral with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Но потом как-то передумала." with dissolve

    me "Понятно." with dissolve

    show aliya_sit_front eyes_closed_neutral with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "У меня в этом году брат ЕГЭ сдает. Ему нужно поступить учиться в универ." with dissolve

    aliya "Поэтому сейчас плохо с деньгами." with dissolve

    show aliya_sit_front eyes_open_neutral with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Моему отцу как-то не до меня, он тратит деньги на моего брата." with dissolve

    me "Понимаю." with dissolve

    me "Если у тебя брат спортсмен, то он может и так поступить, бесплатно." with dissolve

    aliya "Нет, он не спортсмен. Он обычный." with dissolve

    me "Ясно." with dissolve

    me "Кроме брата, у тебя еще сестра есть?" with dissolve

    aliya "Да." with dissolve

    aliya "Она очень послушная, и все время меня поучает." with dissolve

    show aliya_sit_front eyes_closed_annoyed with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Все время мне лекции читает, говорит типа \"вот я же говорила\"." with dissolve

    me "Да. Это бесит." with dissolve

    show aliya_sit_front eyes_open_angry with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE


    aliya "Конечно." with dissolve

    aliya "Она не смотрит аниме или корейские драмы." with dissolve

    show aliya_sit_front eyes_closed_sad_worried_open_mouth with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Иногда это удобно. Если я плачу, она может спросить у меня, что случилось." with dissolve

    show aliya_sit_front eyes_open_sad_worried with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Я отвечаю, что вспомнила грустный момент в какой-нибудь драме." with dissolve

    aliya "Она этого все равно не понимает." with dissolve

    aliya "Только говорит \"Опять ты со своими корейцами\"." with dissolve

    me "Хорошая идея. Валить все на драмы." with dissolve

    show aliya_sit_front eyes_open_sad_smile with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE


    aliya "Да." with dissolve

    show aliya_sit_front eyes_open_thinking_hands_inside with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    play sound "sound/aeroexpress.ogg"

    announcement "Уважаемые пассажиры, аэроэкспресс прибывает на конечную станцию Павелецкий вокзал." with dissolve

    stop music fadeout 1.0

    "Поезд медленно остановился." with dissolve

    "Двери тихо открылись." with dissolve

    me "Пойдем!" with dissolve

    show aliya_sit_front eyes_open_sad_smile with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE


    aliya "Пойдем." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    jump day3_metro
