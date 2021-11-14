
label day3_intro:

    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("play_airplane_1ambience_before_landing_loop()")
            $ emscripten.run_script("music_stage_preload = \"music_airplane_sounds_Runaway05\"")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracks()")
    else:
        play music "ambience/airplane_1ambience_before_landing_loop.ogg" # fadein 1.0 # fadeout 1.0

    "В ушах звенит гул летящего самолёта." with dissolve

    "Я словно наполовину во сне, наполовину осознаю, что происходит вокруг." with dissolve

    if renpy.emscripten:
        $ import emscripten
        $ emscripten.run_script("play_sound_seatbelt()")
    else:
        play sound "sound/seatbelt.ogg"

    "Прозвучал звуковой сигнал \"пристегните ремни безопасности\"." with dissolve

    scene black

    announcement "Уважаемые дамы и господа, наш самолёт приступил к снижению. Мы готовимся к посадке в аэропорту Минеральные Воды." with dissolve

    announcement "Просим вас пристегнуть ремни, привести спинки кресел в вертикальное положение, закрыть раскладные столики и открыть шторки на иллюминаторах." with dissolve

    $ savegame_picture = "savegame_airplane_night"

    show airplane_night at airplane_scene_pos with dissolve:
        ypos 0.525
        zoom 1.05

    "Я открыл глаза и потянулся в тесном кресле, прогоняя дрёму." with dissolve

    show airplane_night at airplane_scene_pos:
        ypos 0.525
        zoom 1.05
        easein 4.0 ypos 0.475

    "Меня слегка дёрнуло вниз. Всем своим телом я почувствовал как самолёт, снижаясь, задрал нос вверх." with dissolve

    "От этого движения я окончательно проснулся." with dissolve

    "Я попытался вспомнить, как оказался в самолёте, восстанавливая в голове воспоминания вчерашнего дня." with dissolve

    "Итак. Вчера вечером я сидел за ноутбуком." with dissolve

    "Затем мне написала Алия." with dissolve

    "Потом я купил авиабилеты, чтобы полететь за ней и вместе с ней улететь в Москву." with dissolve

    "Я собрал вещи в рюкзак." with dissolve

    "За мной приехал Ярик на своём спортивном авто и отвёз в аэропорт." with dissolve

    "Там я сел на рейс до Москвы, аэропорт Домодедово." with dissolve

    "Я прилетел в Москву, погулял по ночному аэропорту как зомби." with dissolve

    "Потом сел на рейс до Минеральных Вод и сразу же уснул в кресле." with dissolve

    "И вот я тут, сижу в кресле самолёта." with dissolve

    "Самолёт заходит на посадку в аэропорт Минеральные Воды." with dissolve

    $ last_playing_music = "play_audio_ambience_airplane_3after_landing_loop"

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("stopAllMusic()")
            $ emscripten.run_script("play_airplane_1ambience_before_landing_loop(2.5)")

    "Я чувствую всем своим телом как воздушное судно медленно снижается." with dissolve

    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("play_airplane_2landed_shortened()")
            $ emscripten.run_script("play_audio_ambience_airplane_3after_landing_loop(19.856)")

    else:

        play music "ambience/airplane_2landed_shortened.ogg"

        queue music "ambience/airplane_3after_landing_loop.ogg"


    show airplane_night:
        ypos 0.475
        zoom 1.05
        linear 2.0 ypos 0.5
        linear 5.0 zoom 1.075

    "Бум! Самолёт коснулся посадочной полосы и дёрнулся." with hpunch

    "Посадка была чуть более жестковатой, чем я ожидал." with dissolve

    "На крыльях поднялись спойлеры и шум торможения наполнил мои уши." with dissolve

    "Самолет снизил скорость и шум тоже заметно снизился." with dissolve

    announcement "Уважаемые дамы и господа, добро пожаловать в международный аэропорт Минеральные Воды." with dissolve

    announcement "Температура воздуха в Минеральных Водах плюс двенадцать градусов." with dissolve

    announcement "Местное время девять часов тридцать минут." with dissolve

    announcement "Для вашей безопасности мы рекомендуем вам оставаться на местах с пристегнутыми ремнями безопасности до выключения светового табло \"пристегните ремни\"." with dissolve

    announcement "От имени авиакомпании благодарим вас за полёт и будем рады новой встрече!" with dissolve

    #show cg_screen_phone_time_day3_airplane_morning as cg_screen_phone with dissolve

    show right_hand phone_night day3_airplane_morning as cg_screen_phone with dissolve

    "Я проверил телефон, он был в авиарежиме. Время действительно было 9:30 утра." with dissolve

    "Алия должна меня встретить в 10 часов возле входа в аэропорт." with dissolve

    "Как раз достаточно времени. Пока самолёт остановится, высадит всех пассажиров." with dissolve

    $ last_playing_music = "playRunaway05"

    #$ music_stage_preload = "music_Runaway05_Runaway06"

    if renpy.emscripten:
        if renpy.in_rollback():
            $ emscripten.run_script("music_stage_preload = \"music_airplane_sounds_Runaway05\"")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracks(stopAllMusic, play_audio_ambience_airplane_3after_landing_loop)")

    "Еще и неизвестно, может нас довезут от самолёта до аэровокзала на автобусе." with dissolve

    $ music_stage_preload = "music_Runaway05_Runaway06"

    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("music_stage_preload = \"music_Runaway05_Runaway06\"")
            $ emscripten.run_script("playRunaway05()")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracksAsync()")
    else:
        play music "music/Runaway_05 (Loop).ogg" # fadein 3.0

        queue music "music/Runaway_05 (Loop).ogg"

    scene black with dissolve

    $ renpy.pause(1.0)

    scene mrv_interior2 with dissolve

    $ savegame_picture = "savegame_mrv_interior"

    "Я вошёл в здание аэровокзала один из первых, поскольку у меня не было багажа, только ручная кладь." with dissolve

    "Было утро, но в аэропорту уже было много людей." with dissolve

    #show cg_screen_phone as cg_screen_phone with dissolve

    show right_hand phone_day day_black_screen as cg_screen_phone with dissolve

    "Ой, я кажется ещё не выключил авиарежим в телефоне. Включаю сеть..." with dissolve

    #show cg_screen_phone_time_day3_airport_morning as cg_screen_phone with dissolve

    show right_hand phone_day day3_airport_morning1 as cg_screen_phone with dissolve

    "Секундная пауза..." with dissolve

    #show cg_screen_phone_new_message_day3_morning_airport1 as cg_screen_phone with dissolve

    show right_hand phone_day day3_airport_morning2 as cg_screen_phone with dissolve

    messenger "Новое сообщение"  with dissolve # with hpunch

    $ changeDialogToAliya()

    $ showMessengerPhone(is_night=False, force_no_transition=True)

    $ addReceivedMessage(2)

    aliya_mobile "Привет! Ты уже прилетел?" with dissolve

    $ addSentMessage(2)

    me "Привет, да. Ты в порядке?" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Купи пожалуйста в аптеке маски для лица." with dissolve

    $ addSentMessage(0)

    me "Хорошо!" with dissolve

    $ clearDisplayMessages()

    $ hidePhone()

    "Итак, где же в этом аэропорту аптека? Перед глазами у меня только такси, аренда авто и сим-карты." with dissolve

    "Нужно оглянуться. Вот табло, вот стойки регистрации... ага, вот и аптека!" with dissolve

    "Я купил на всякий случай три маски - вдруг, как в армии, \"одну сломаю, а вторую потеряю\", по привычке, благо они дешевые." with dissolve

    "Маски у меня есть и в запасе есть ещё немного времени до прихода Алии." with dissolve

    "Я чувствую лёгкое волнение, которое наполняет моё тело." with dissolve

    "Такое же чувство я испытывал давным-давно, когда ещё был школьником и ходил на свидания с девушками." with dissolve

    "С тех пор прошло много лет, а я до сих пор чувствую некоторую робость в общении с женским полом." with dissolve

    "Так, надо взять себя в руки, я уже не застенчивый школьник и должен вести себя взрослее!" with dissolve

    "И вообще это не свидание." with dissolve

    "В первую очередь мне нужно доставить Алию в Москву и обустроить её жизнь там." with dissolve

    messenger "Новое сообщение"  with dissolve

    #show cg_screen_phone_new_message_day3_morning_airport2 as cg_screen_phone with dissolve

    show right_hand phone_day day3_airport_morning3 as cg_screen_phone with dissolve

    "Я снова достал телефон." with dissolve

    $ showMessengerPhone(is_night=False, force_no_transition=True)

    $ addReceivedMessage(3)

    aliya_mobile "Привет! Я приехала, ты где?" with dissolve

    $ addSentMessage(1)

    me "Я внутри!" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Подходи к главному входу." with dissolve

    $ addSentMessage(1)

    me "Окей, выхожу!" with dissolve

    $ clearDisplayMessages()

    $ hidePhone()

    "Я убрал телефон и пошёл к главному входу..." with dissolve

    jump day3_meet_aliya


label day3_meet_aliya:

    #$ renpy.start_predict("images/aliya_anim/*.*")

    scene mrv_exterior with dissolve

    $ savegame_picture = "savegame_mrv_exterior"

    "... я вышел наружу и огляделся." with dissolve

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("music_stage_preload = \"music_Runaway05_Runaway06\"")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracks(stopAllMusic, playRunaway05)")
            #$ emscripten.run_script("stopAllMusic()")
            #$ emscripten.run_script("playRunaway05()")

    $ last_playing_music = "playCrossFadeRunaway06"

    me "Алия!.." with dissolve

    $ music_stage_preload = "music_Runaway06_Runaway16"

    #$ renpy.start_predict("images/sprites/Aliya/Pose1/*.*")
    #$ renpy.start_predict("images/sprites/Aliya/Pose1/mask1/*.*")
    #$ renpy.start_predict("images/sprites/Aliya/Pose2/*.*")
    #$ renpy.start_predict("images/sprites/Aliya/Pose2/mask2/*.*")
    #$ renpy.start_predict("images/sprites/Aliya/jacket*.*")
    # Stop predicting them when enter Airport

    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("playCrossFadeRunaway06()")
            $ emscripten.run_script("music_stage_preload = \"music_Runaway06_Runaway16\"")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracksAsync()")
    else:

        play music_crossfade "music/Runaway_06 (Loop).ogg" # fadein 3.0

        queue music_crossfade "music/Runaway_06 (Loop).ogg"

        stop music # fadeout 1.0

    # Now here we need to unlock Aliya in the main menu
    $ persistent.menu_unlocked_aliya = True

    show aliya_anim_frame1 as aliya_anim at any_center_pos with dissolve:
        zoom 1.0

    me "Это ты?.." with dissolve

    show aliya_anim at any_center_pos with dissolve:
        zoom 1.0

    "Алия обернулась..." with dissolve

    aliya "Привет..." with dissolve

    scene black with dissolve

    #$ renpy.stop_predict("images/aliya_anim/*.*")

    $ renpy.pause(1.0)

    scene mrv_exterior with dissolve

    show Aliya_stand_straight mask_eyes_open_neutral at any_center_pos as Aliya with dissolve:
        zoom 1.0

    $ persistent.gallery2unlock = True

    "А она довольно маленькая девушка. Меньше, чем я себе представлял." with dissolve

    "Неловкое молчание... так, Семён, не тупи! Скажи что-нибудь!" with dissolve

    me "Как себя чувствуешь?" with dissolve

    show Aliya_stand_half_turned jacket_armsdown eyes_closed_sad_worried_open_mouth extra_stand_half_turned2_mask at any_center_pos as Aliya with dissolve:
        zoom 1.0

    aliya "Сойдёт." with dissolve

    show Aliya_stand_half_turned jacket_armsdown eyes_open_sad_worried_open_mouth extra_stand_half_turned2_mask at any_center_pos as Aliya with dissolve:
        zoom 1.0

    "Опять неловкая пауза!" with dissolve

    "Кажется мой мозг решил взять перерыв. Как обычно, в самый важный момент." with dissolve

    me "Ты очень смелая. Я думал, что ты испугаешься и передумаешь в самый последний момент." with dissolve

    aliya "Я тоже так думала." with dissolve

    "Что теперь? Ах да, маски." with dissolve

    #show airport_semyon_gives_mask with dissolve
    show right_hand hand_mask with dissolve

    me "Я купил тебе маски. Вот, возьми!" with dissolve

    #hide airport_semyon_gives_mask with dissolve
    hide right_hand with dissolve

    show Aliya special_jacket_pocket no_mask at any_center_pos as Aliya with dissolve:
        zoom 1.0

    "Алия ловким движением сняла свою старую маску, положила в карман..." with dissolve

    show Aliya special_jacket_mask_wear at any_center_pos as Aliya with dissolve:
        zoom 1.0

    "Затем распечатала новую и надела." with dissolve

    show Aliya_stand_half_turned jacket_armsdown eyes_closed_smile extra_stand_half_turned2_mask as Aliya at any_center_pos with dissolve:
        zoom 1.0

    aliya "Спасибо." with dissolve

    show Aliya_stand_half_turned jacket_armsdown eyes_open_smile extra_stand_half_turned2_mask as Aliya at any_center_pos with dissolve:
        zoom 1.0

    me "Ты носишь маску, потому что боишься что тебя узнают?" with dissolve

    show Aliya_stand_straight mask_eyes_open_angry at any_center_pos as Aliya with dissolve:
        zoom 1.0

    "Алия посмотрела на меня настороженно." with dissolve

    aliya "У меня аллергия." with dissolve

    aliya "Поэтому я ношу маску." with dissolve

    me "Понятно." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    scene mrv_exterior with dissolve

    show Aliya_stand_straight mask_eyes_open_neutral at any_center_pos as Aliya with dissolve:
        zoom 1.0

    "Ладно, поприветствовали друг друга, теперь возвращаемся к первоначальному плану." with dissolve

    if day2_night_car_coach_talked==True: # Coach adviced to give money

        "Я решил воспользоваться советом Напарника и дать Алие немного наличных денег." with dissolve

        #show airport_semyon_gives_money with dissolve
        show right_hand hand_money with dissolve

        me "Вот держи деньги. Три тысячи рублей." with dissolve

        #hide airport_semyon_gives_money with dissolve
        hide right_hand with dissolve

        show Aliya special_jacket_pocket_mask at any_center_pos as Aliya with dissolve:
            zoom 1.0

        "Алия недоверчиво взяла пачку купюр и положила в карман." with dissolve

        show Aliya_stand_straight mask_eyes_closed_neutral at any_center_pos as Aliya with dissolve:
            zoom 1.0

        aliya "Спасибо." with dissolve

        show Aliya_stand_straight mask_eyes_open_neutral at any_center_pos as Aliya with dissolve:
            zoom 1.0

        me "Это тебе на случай, если мы вдруг потеряемся. Или вдруг ты передумаешь и захочешь вернуться назад." with dissolve



    # At this point aliya_trust_points_hard: max=2 min=0



    me "Давай теперь пройдём внутрь?" with dissolve

    show Aliya_stand_straight mask_eyes_open_sad3 at any_center_pos as Aliya with dissolve:
        zoom 1.0

    aliya "Хорошо, пошли." with dissolve

    scene black with dissolve


    #$ renpy.stop_predict("images/sprites/Aliya/Pose1/*.*")
    #$ renpy.stop_predict("images/sprites/Aliya/Pose1/mask/*.*")
    #$ renpy.stop_predict("images/sprites/Aliya/Pose2/*.*")
    #$ renpy.stop_predict("images/sprites/Aliya/Pose2/mask/*.*")
    #$ renpy.stop_predict("images/sprites/Aliya/jacket*.*")



    #$ renpy.start_predict("images/sprites/Aliya/Sitting2/bench/*.*")
    #$ renpy.start_predict("images/sprites/Aliya/Pose4/*.*")


    $ renpy.pause(1.0)

    scene mrv_interior2 with dissolve

    $ savegame_picture = "savegame_mrv_interior"

    show aliya_turn_around eyes_open_watching mask at any_left_pos as Aliya with dissolve:
        zoom 1.0

    "Мы вошли в здание аэровокзала. Здесь становилось многолюдно." with dissolve

    "Я нашёл наконец пару свободных сидений в отдаленном углу. Надеюсь, нас никто не будет подслушивать." with dissolve

    show aliya_turn_around eyes_open_neutral mask at any_left_pos as Aliya with dissolve:
        zoom 1.0

    me "Вон там свободно. Пойдём туда?" with dissolve

    aliya "Хорошо." with dissolve

    scene black with dissolve

    #$ renpy.stop_predict("images/sprites/Aliya/Pose4/*.*")

    "Я сел на сидение и Алия села рядом со мной..." with dissolve

    scene mrv_interior2_chair with dissolve

    $ savegame_picture = "savegame_mrv_interior2_chair"

    show aliya_sit_side earphones eyes_open_neutral mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    "Я вздохнул и начал разговор." with dissolve

    me "Итак, вот он я - Семён. Я обычный человек, не маньяк, как ты видишь." with dissolve

    me "Сейчас по плану мы регистрируемся на рейс и затем проходим в чистую зону. Там мы садимся в самолёт." with dissolve

    me "Если я покажусь тебе страшным или ты передумаешь сбегать, ты можешь в любой момент до посадки на рейс передумать." with dissolve

    me "Выйдешь из аэропорта, сядешь на такси и уедешь домой." with dissolve

    me "После посадки на самолёт ты уже не сможешь вернуться назад. Мы с тобой выйдем уже в Москве." with dissolve

    show aliya_sit_side earphones eyes_closed_sad mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Понимаю." with dissolve

    me "Всё в порядке?" with dissolve

    show aliya_sit_side earphones eyes_open_sad_worried mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Да." with dissolve

    show aliya_sit_side phone eyes_open_watching_phone mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    "Телефон Алии завибрировал два раза. Она взяла в руки телефон и разблокировала его." with dissolve

    show aliya_sit_side phone eyes_open_watching_phone4 mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    "Кажется, она немного испугалась." with dissolve

    show aliya_sit_side earphones eyes_open_cry_sad2 mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Сестра мне написала. Спрашивает, где я." with dissolve

    aliya "Что мне ответить?" with dissolve

    me "Пока ничего не отвечай. А лучше переведи телефон в авиарежим." with dissolve

    aliya "Хорошо." with dissolve

    show aliya_sit_side earphones eyes_closed_sad mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    "Алия быстро включила авиарежим и убрала телефон в карман." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    scene mrv_interior2_chair with dissolve

    show aliya_sit_side earphones eyes_open_neutral mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    me "Когда мы приедем в Москву, нам нужно будет сделать тебе новую сим-карту." with dissolve

    aliya "Да, конечно." with dissolve

    show aliya_sit_side earphones eyes_closed_sad_worried_open_mouth mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "И ещё мне нужно будет купить кое-что." with dissolve

    me "Что тебе нужно?" with dissolve

    show aliya_sit_side earphones eyes_open_neutral mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Нужно будет купить коврик для намаза." with dissolve

    aliya "И платье, закрывающее ноги и руки." with dissolve

    aliya "Я не хочу сегодня пропускать намаз." with dissolve

    me "Ты молишься?" with dissolve

    show aliya_sit_side earphones eyes_open_sad_worried_question mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Стараюсь. Раз в день уж точно нужно." with dissolve

    me "Ты сегодня ещё не молилась?" with dissolve

    show aliya_sit_side earphones eyes_open_neutral mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Нет. И мне желательно до вечера успеть сделать намаз." with dissolve

    menu:

        "Согласиться купить коврик и платье?"

        "Да.":
            jump day3_meet_aliya_success

        "Нет.":
            jump day3_meet_aliya_almost_fail


label day3_meet_aliya_success:

    scene black with dissolve

    $ renpy.pause(1.0)

    scene mrv_interior2_chair with dissolve

    show aliya_sit_side earphones eyes_open_sad_worried_open_mouth mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("music_stage_preload = \"music_Runaway06_Runaway16\"")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracks()")

    me "Хорошо. Когда мы приедем в Москву, мы поищем тебе коврик и платье." with dissolve

    $ music_stage_preload = "music_Runaway06_airplane2"

    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("music_stage_preload = \"music_Runaway06_airplane2\"")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracksAsync()")

    show aliya_sit_side earphones eyes_closed_smile mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Спасибо." with dissolve

    show aliya_sit_side earphones eyes_open_smile mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    me "Ещё тебе нужно будет купить обычную повседневную одежду." with dissolve

    me "Но это подождёт до завтра." with dissolve

    show aliya_sit_side earphones eyes_open_neutral mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Хорошо." with dissolve

    show aliya_sit_side earphones eyes_open_sad_worried_question mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "А где мы будем ночевать?" with dissolve

    me "В обычную гостиницу мы не поедем." with dissolve

    me "Потому что при регистрации в гостинице нужно предъявлять паспорт." with dissolve

    show aliya_sit_side earphones eyes_closed_sad mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Мне нельзя показывать паспорт. Родители же узнают, где я остановилась!" with dissolve

    show aliya_sit_side earphones eyes_open_sad_worried_open_mouth mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Есть другие места?" with dissolve

    me "Можно снять квартиру или найти хостел, где не требуется паспорт." with dissolve

    show aliya_sit_side earphones eyes_open_sad_worried mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Что такое хостел?" with dissolve

    me "Что-то типа общежития. Там есть женские и мужские спальни." with dissolve

    me "В каждой комнате от 4 до 8 спальных мест. Обычно это двухъярусные кровати." with dissolve

    show aliya_sit_side earphones eyes_closed_neutral mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Я поняла." with dissolve

    me "Там есть туалеты, душевые, общая кухня. В хостелах обычно останавливаются студенты." with dissolve

    show aliya_sit_side earphones eyes_open_neutral mask as Aliya at any_center_pos with dissolve:
        zoom SCALE


    aliya "Хорошо." with dissolve

    me "Можно также снять квартиру, но это будет дороже." with dissolve

    me "Впрочем, я пока ещё не решил точно. Мы позаботимся об этом позже." with dissolve

    aliya "Хорошо." with dissolve

    me "А на следующий день нужно будет открыть для тебя банковскую карточку." with dissolve

    aliya "Там нужно показывать паспорт?" with dissolve

    me "Да, конечно." with dissolve

    show aliya_sit_side earphones eyes_open_surprised mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Мне нельзя! Родители вычислят меня!" with dissolve

    me "Тебе потребуется сходить в банк всего два раза:" with dissolve

    me "оформить карточку и забрать её." with dissolve

    me "Родители не смогут вычислить твоё местонахождение по карточке." with dissolve

    me "Максимум что они узнают - это в каком отделении ты её открыла." with dissolve

    me "А мы можем открыть счёт в любом банке в Москве." with dissolve

    show aliya_sit_side earphones eyes_open_sad_worried_open_mouth mask as Aliya at any_center_pos with dissolve:
        zoom SCALE


    aliya "Хорошо. А мне не нужна прописка в Москве?" with dissolve

    me "Нет, чтобы сделать карточку, нужно всего лишь иметь российский паспорт." with dissolve

    show aliya_sit_side earphones eyes_open_sad_worried mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "А зачем мне нужна карточка?" with dissolve

    me "В будущем ты будешь получать на нее зарплату." with dissolve

    aliya "А нам обязательно оформлять её прямо сразу?" with dissolve

    me "Я просто опасаюсь, что родители объявят твой паспорт в розыск." with dissolve

    me "После этого он попадет в список недействительных паспортов." with dissolve

    me "И тогда уже с ним мало что можно будет сделать." with dissolve

    me "Поэтому я хочу, чтобы ты оформила банковскую карту поскорее." with dissolve

    show aliya_sit_side earphones eyes_open_neutral mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Поняла." with dissolve

    aliya "А что мне делать, когда мой паспорт станет недействительным?" with dissolve

    me "Если ты успеешь до этого найти работу и открыть счёт в банке, то ничего страшного." with dissolve

    me "Если не успеешь найти работу, будет сложно устроиться в крупную компанию." with dissolve

    aliya "В крупную компанию?" with dissolve

    me "Ну типа Макдоналдс, Икея, Декатлон." with dissolve

    show aliya_sit_side earphones eyes_open_sad_worried mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "И где я тогда буду работать?" with dissolve

    me "Вероятно, мелкие магазины и кафе не пробивают паспорт по базам недействительных паспортов." with dissolve

    me "Можно устроиться туда." with dissolve

    show aliya_sit_side earphones eyes_open_neutral mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Хорошо. Я буду работать официанткой?" with dissolve

    me "Возможно." with dissolve

    me "В Москве много вакансий для массовых позиций." with dissolve

    me "Ты можешь работать кассиршей, официанткой, бариста, продавцом-консультантом, поваром." with dissolve

    aliya "Сколько я могу заработать?" with dissolve

    me "Я думаю, от 25 до 30 тысяч рублей в месяц." with dissolve

    show aliya_sit_side earphones eyes_open_surprised mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Это много?" with dissolve

    me "Нет, не очень. Этого хватит, чтобы снимать комнату где-нибудь на окраине и более-менее сносно жить." with dissolve

    show aliya_sit_side earphones eyes_open_neutral mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Я поняла." with dissolve

    aliya "Наверное, мне ещё придётся заново поступить учиться." with dissolve

    me "Да, это несложно. В Москве много студентов, которые учатся и работают одновременно." with dissolve

    show aliya_sit_side earphones eyes_open_sad_worried mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Как они совмещают?" with dissolve

    me "Днём учеба, вечером смена. Как-то так." with dissolve

    show aliya_sit_side earphones eyes_open_neutral mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Поняла." with dissolve

    me "Об этом можно подумать уже после того, как ты обустроишься в Москве." with dissolve

    aliya "Хорошо." with dissolve

    aliya "И ещё нужно оформить загранпаспорт!" with dissolve

    me "Это можно сделать через МФЦ либо удаленно через сайт Госуслуги." with dissolve

    me "Но если твой отец объявит твой паспорт в розыск, сделать загранпаспорт не получится." with dissolve

    aliya "И что тогда?" with dissolve

    me "Я вижу несколько вариантов." with dissolve

    me "Когда тебя перестанут искать родители, ты можешь сняться с розыска и начать делать документы." with dissolve

    me "Либо можем, например, выехать в Беларусь и попробовать получить загранпаспорт там." with dissolve

    aliya "Понятно..." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    scene mrv_interior2_chair with dissolve

    show aliya_sit_side earphones eyes_open_neutral mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Я готова, пойдём. Авиабилеты у тебя?" with dissolve

    me "Да, билеты у меня в телефоне. Нам нужно зарегистрироваться на рейс, распечатать посадочный талон и пройти досмотр." with dissolve

    #show cg_screen_phone_airplane_app1 as cg_screen_phone with dissolve

    show right_hand phone_day day_check_in1 as cg_screen_phone with dissolve

    "Я достал телефон и открыл приложение авиакомпании." with dissolve

    #show cg_screen_phone_airplane_app2 as cg_screen_phone with dissolve

    show right_hand phone_day day_check_in2 as cg_screen_phone with dissolve

    me "Какое место тебе выбрать, возле окна?" with dissolve

    show aliya_sit_side earphones eyes_closed_smile mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    "Алия слегка улыбнулась." with dissolve

    aliya "Да." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    scene mrv_interior2 with dissolve

    $ savegame_picture = "savegame_mrv_interior"

    "Я уже летал сегодня этой авиакомпанией, поэтому процесс регистрации не занял долгое время." with dissolve

    "Багажа у нас нет, поэтому мы просто подошли к автомату самостоятельной регистрации и распечатали посадочные талоны." with dissolve

    "Получив посадочные талоны, мы отправились в зону досмотра и к выходам на посадку." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    jump day3_airport_inner


label day3_meet_aliya_almost_fail:

    $ aliya_trust_points_hard = aliya_trust_points_hard - 1

    show aliya_sit_side earphones eyes_open_sad_worried_open_mouth mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    me "У нас навряд ли будет на это время, уж очень накладно будет искать в Москве нужные магазинчики." with dissolve

    me "Да и не ты ли говорила, что в Москве у тебя родня? Вдруг с ними столкнёшься?" with dissolve

    show aliya_sit_side earphones eyes_closed_annoyed mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Они точно не станут искать подобные вещи, всё это есть у каждого мусульманина." with dissolve

    me "А без этого никак? Ну иначе там помолиться ты не можешь?" with dissolve

    show aliya_sit_side earphones eyes_open_angry mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Иначе? Ты себе это как представляешь?" with dissolve

    me "Ну не знаю, к примеру, как христиане?" with dissolve

    aliya "Семён, ты уж прости, но я не христианка. Я мусульманка и следую нашим традициям." with dissolve

    me "Хорошо-хорошо, следуй, но разве без платья и коврика ты уже и помолиться не можешь?" with dissolve

    aliya "А разве ваши девушки ходят в церковь без головных уборов или же бабки сидят в церквях? Нет, хотя в других верах есть и такое." with dissolve

    me "И к чему ты это?" with dissolve

    show aliya_sit_side earphones eyes_closed_annoyed mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Да к тому, что не будь мне нужно это платье и коврик, я бы и просить не стала." with dissolve

    aliya "Моя религия очень важна для меня, разве это не понятно? Я ведь и раньше об этом говорила." with dissolve

    menu:

        "Согласиться купить коврик и платье?"

        "Да.":
            jump day3_meet_aliya_success

        "Нет, продолжать настаивать.":
            jump day3_meet_aliya_fail


label day3_meet_aliya_fail:

    scene black with dissolve

    $ renpy.pause(1.0)

    scene mrv_interior2_chair with dissolve

    show aliya_sit_side earphones eyes_open_sad_worried_open_mouth mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    me "Мне всё же кажется это странным. Столько приготовлений ради простой молитвы." with dissolve

    me "Ну что, пойдём?" with dissolve

    show aliya_sit_side earphones eyes_closed_sad mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Подожди..." with dissolve

    show aliya_sit_side phone eyes_open_watching_phone mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    "Алия поколебалась, посмотрела в телефон, вздохнула." with dissolve

    show aliya_sit_side earphones eyes_open_sad_worried_question mask as Aliya at any_center_pos with dissolve:
        zoom SCALE

    aliya "Мне нужно сходить в туалет." with dissolve

    me "Хорошо, это где-то в той стороне." with dissolve

    "Я указал пальцем в сторону туалетов." with dissolve

    hide Aliya with dissolve

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

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("stopAllMusic()")
            $ emscripten.run_script("playCrossFadeRunaway06()")

    $ last_playing_music = "playRunaway16"

    "Я убрал телефон, оглянулся и попытался глазами найти Алию в зале. Её нигде не было." with dissolve


    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("playRunaway16()")
    else:

        stop music_crossfade # fadeout 1.0

        play music "music/Runaway_16 (Loop).ogg" # fadein 3.0

        queue music "music/Runaway_16 (Loop).ogg"

    scene black with dissolve

    "Кажется, она сбежала. Ничего теперь не поделать." with dissolve

    "Похоже мне придется возвращаться домой..." with dissolve

    #"THE END, спасибо что поиграли! Концовка 4 - \"Третий день, Семён поругался с Алией из-за религии\"" with dissolve

    $ renpy.pause(1.0)

    return



label day3_airport_inner:

    scene mrv_interior3 with dissolve

    $ savegame_picture = "savegame_mrv_interior3"

    #$ renpy.stop_predict("images/sprites/Aliya/Sitting2/bench/*.*")

    #$ renpy.start_predict("images/sprites/Aliya/Sitting1/*.*")

    #$ renpy.start_predict("images/sprites/Aliya/Sitting1/alt/*.*")

    "Предпосадочный досмотр мы прошли довольно быстро." with dissolve

    "Алию немного задержали в момент проверки паспорта и посадочного талона." with dissolve

    "Наверное, сотрудник аэропорта вычислял в уме было ей 18 лет или нет." with dissolve

    "Но её всё-таки пропустили и вот мы оказались в чистой зоне." with dissolve

    "Мы нашли свободное место возле нашего выхода на посадку. Я сел на сидение." with dissolve

    show aliya_sit_front_hands_aside eyes_open_neutral as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    "Алия села напротив меня." with dissolve

    "Ещё есть время перед посадкой. Итак, о чём бы поговорить?" with dissolve

    me "Ты хочешь есть?" with dissolve

    show aliya_sit_front_hands_aside eyes_closed_sad as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Нет." with dissolve

    "Неудачное начало." with dissolve

    me "Нас будут кормить в самолёте во время полёта. Рекомендую тебе поесть. Нельзя оставаться голодной." with dissolve

    show aliya_sit_front_hands_together eyes_open_thinking_hands_inside as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Ладно." with dissolve

    me "Как ты себя чувствуешь в целом?" with dissolve

    show aliya_sit_front_hands_aside eyes_open_neutral as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Сойдёт." with dissolve

    "Я не очень хорошо разбираюсь в людях, но сейчас я вижу, что Алия всё ещё чувствует себя неспокойно." with dissolve

    "Возможно, надо бы её успокоить." with dissolve

    "Может поговорить о чём-то отвлечённом?" with dissolve

    me "У нас ещё есть время перед посадкой." with dissolve

    me "Что ты обычно делаешь, когда у тебя появляется свободное время?" with dissolve

    show aliya_sit_front_hands_together eyes_open_sad_worried_open_mouth as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Слушаю музыку, смотрю аниме или корейские дорамы." with dissolve

    show aliya_sit_front_hands_together eyes_open_sad_worried as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    me "Тебе нравится аниме?" with dissolve

    show aliya_sit_front_hands_together eyes_open_sad_worried_open_mouth as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Да. Там короткие серии по 20 минут." with dissolve

    aliya "В корейских дорамах один эпизод длится час, это очень долго." with dissolve

    aliya "Хотя я иногда смотрю, например, вечером." with dissolve

    show aliya_sit_front_hands_together eyes_open_sad_worried as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    me "А почему ты заинтересовалась Кореей?" with dissolve

    show aliya_sit_front_hands_aside eyes_closed_smile as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    "Алия улыбнулась." with dissolve

    show aliya_sit_front_hands_aside eyes_open_smile as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "У меня есть лучшая подруга. Она меня и подсадила." with dissolve

    aliya "Она русская. Мы учимся вместе." with dissolve

    aliya "Она познакомила меня с корейскими группами." with dissolve

    show aliya_sit_front_hands_aside eyes_open_playful as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "У меня даже есть биас... но я не скажу, кто это." with dissolve

    "Надо будет в свободное время узнать об этом побольше." with dissolve

    show black zorder 10 with dissolve

    show aliya_sit_front_hands_together eyes_open_cry_sad2 as Aliya:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    "Прошло ещё немного времени..." with dissolve

    hide black with dissolve

    "Наконец, прозвучало очередное объявление по громкоговорителю." with dissolve

    show aliya_sit_front_hands_together eyes_open_sad_worried_question as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    announcement "Начинается посадка на рейс номер сто пятьдесят четыре, выполняющий рейс в Москву, аэропорт Домодедово." with dissolve

    announcement "Пассажиров просим пройти к выходу номер один." with dissolve

    me "Это наш рейс." with dissolve

    show aliya_sit_front_hands_together eyes_open_sad_worried_open_mouth as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE


    aliya "Да." with dissolve

    me "Если ты передумала и хочешь вернуться домой, это твой последний шанс." with dissolve

    show aliya_sit_front_hands_aside eyes_closed_sad as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE


    aliya "Я лечу с тобой в Москву." with dissolve

    me "Хорошо. Тогда приготовь посадочный талон, пойдём на посадку!" with dissolve

    show aliya_sit_front_hands_aside eyes_open_smile as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    $ last_playing_music = ""

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("stopAllMusic()")
            $ emscripten.run_script("playCrossFadeRunaway06()")

    aliya "Хорошо." with dissolve

    $ persistent.gallery3unlock = True

    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("stopAllMusic()")
    else:

        stop music_crossfade # fadeout 1.0

        stop music # fadeout 1.0

    scene black with dissolve

    #$ renpy.stop_predict("images/sprites/Aliya/Sitting1/*.*")

    #$ renpy.stop_predict("images/sprites/Aliya/Sitting1/alt/*.*")


    #$ renpy.start_predict("images/sprites/Aliya/Sitting2/bench/*.*")
    #$ renpy.start_predict("images/sprites/Aliya/Sitting2/airplane/*.*")

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("music_stage_preload = \"music_Runaway06_airplane2\"")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracks(stopAllMusic)")

    $ last_playing_music = "play_airplane_1ambience_before_landing_loop"

    "Мы поднялись на борт, заняли свои места и самолёт отправился в Москву..." with dissolve

    $ renpy.pause(1.0)

    $ music_stage_preload = "music_airplane2_Runaway07"

    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("play_airplane_1ambience_before_landing_loop()")
            $ emscripten.run_script("music_stage_preload = \"music_airplane2_Runaway07\"")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracksAsync()")
    else:

        play music "ambience/airplane_1ambience_before_landing_loop.ogg" # fadein 1.0 # fadeout 1.0

    scene airplane_day with dissolve

    $ savegame_picture = "savegame_airplane_day"

    "Наш самолет только что набрал высоту и выровнялся." with dissolve


    if renpy.emscripten:
        $ import emscripten
        $ emscripten.run_script("play_sound_seatbelt()")
    else:
        play sound "sound/seatbelt.ogg"

    "Прозвучал звук отключения индикатора \"пристегните ремни\"." with dissolve

    announcement "Уважаемые пассажиры, вы можете отстегнуть ремни безопасности, однако мы рекомендуем вам оставаться пристегнутыми на протяжении всего полёта." with dissolve

    announcement "Туалеты находятся в хвостовой части самолёта. Вам будут предложены обед и напитки. Желаем вам приятного полёта!" with dissolve

    scene black as airplane_background with dissolve

    show black zorder 10

    #‭6998 / 1920 = 3.6447916666666666666666666666667‬  ~ 3.64479167

    if isMobileWeb:
        show airplane_day_side_mobile_web as airplane_scene at airplane_scene_pos zorder 2

        show cg_airplane_window1_mobile_web as cg_airplane_window_mobile_web at airplane_window_pos zorder 2

    else:

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

    show aliya_sit_side no_emotion_layer special_airplane_window as Aliya at any_center_pos zorder 3:
        zoom SCALE

    hide black with dissolve

    $ savegame_picture = "savegame_airplane_day_side"

    "Алия сидела рядом и смотрела в окно на облака." with dissolve

    me "Как тебе?" with dissolve

    aliya "Красиво!" with dissolve

    me "Ты ведь до этого вообще не летала на самолёте?" with dissolve

    show aliya_sit_side no_earphones eyes_open_smile as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Не летала." with dissolve

    aliya "Только на поезде и на автобусе." with dissolve

    aliya "И на автомобиле, конечно же." with dissolve

    me "Ты умеешь водить автомобиль?" with dissolve

    show aliya_sit_side no_earphones eyes_closed_grin as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Нет. Обычно меня возит отец." with dissolve

    me "Понятно." with dissolve

    show aliya_sit_side no_earphones eyes_open_smile as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "У меня ощущение, что я в автобусе еду. Сидения такие же." with dissolve

    aliya "Только здесь совсем не трясет. Как будто едем по очень ровной дороге." with dissolve

    me "Да. И очень быстро." with dissolve

    aliya "Сколько нам ещё лететь?" with dissolve

    me "Мы только взлетели. Будем на месте через два часа." with dissolve

    aliya "Поняла." with dissolve

    show black zorder 10 with dissolve

    $ renpy.pause(1.0)

    jump day3_airplane2

label day3_airplane2:

    show aliya_sit_side no_emotion_layer special_airplane_take_out_from_bag as Aliya zorder 3 at any_center_pos:
        zoom SCALE

    hide black with dissolve

    "Алия достала из своей сумки небольшую книжку." with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_watching_book_neutral as Aliya zorder 3 at any_center_pos with dissolve:
        zoom SCALE

    me "Что это?" with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_watching_book_look_aside as Aliya zorder 3 at any_center_pos with dissolve:
        zoom SCALE

    aliya "Это стихи." with dissolve

    me "Ты любишь читать стихи?" with dissolve

    aliya "Да, это же так красиво. А ты не любишь?" with dissolve

    me "Я учил стихи давно, когда был в школе." with dissolve

    me "Да и вообще, стихи очень сложно читать." with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_watching_book_look_aside_talk as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Почему? Ты же хорошо знаешь русский язык?" with dissolve

    me "Ну да, но там образы, метафоры." with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_watching_book_search as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Алия быстро начала листать страницы." with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_pass_book as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Затем Алия протянула мне книжку." with dissolve

    aliya "Вот, прочитай это и скажи, что ты думаешь." with dissolve

    show aliya_sit_side no_earphones eyes_open_neutral as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    me "Белеет парус одинокой." with dissolve

    me "В тумане моря голубом!.." with dissolve

    show aliya_sit_side no_earphones eyes_closed_smile as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Алия слегка усмехнулась." with dissolve

    show aliya_sit_side no_earphones eyes_open_smile as Aliya at any_center_pos zorder 3 with dissolve:
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

    show aliya_sit_side book eyes_open_sad_worried_open_mouth as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Что думаешь?" with dissolve

    me "Эээ, ну, корабль плывет с белым парусом." with dissolve

    show aliya_sit_side book eyes_open_neutral as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Да ты прямо как компьютер." with dissolve

    "Алия сделала паузу." with dissolve

    aliya "Белый парус в синем море - это душа, ищущая перемен." with dissolve

    aliya "Этот стих о важных решениях, которые меняют твою жизнь." with dissolve

    me "Хмм, да, в этом есть смысл." with dissolve

    show aliya_sit_side book eyes_open_smile as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Мне нравятся стихи. В них есть идеи и мысли, уложенные в складную рифму." with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_watching_book_smile as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Алие определенно нравится говорить о литературе и поэзии." with dissolve

    "Может стоит поговорить с ней об этом?" with dissolve

    menu:

        "Что сделать?"

        "Спросить о стихах.":
            jump day3_airplane2_part1_poetry

        "\"Извини, мне это не интересно\"":
            jump day3_airplane2_part1_ignore


label day3_airplane2_part1_poetry:

    $ aliya_trust_points_hard = aliya_trust_points_hard + 1 # aliya_trust_points_hard by that point max = 3

    me "А кто тебе больше из поэтов нравится?" with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_watching_book_look_aside as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Из русских, наверное, больше всего Анна Ахматова, Александр Блок." with dissolve

    aliya "Ещё Борис Пастернак и Михаил Лермонтов." with dissolve

    me "А кто любимый из них?" with dissolve

    aliya "Наверное Ахматова, она интересная поэтесса." with dissolve

    aliya "И стихи у неё очень глубокие, как-никак представительница серебряного века." with dissolve

    me "Ясно... Кстати, вот объясни мне, что вообще люди под серебряным веком подразумевают? Я помню что-то из школьных лет, но..." with dissolve

    show aliya_sit_side book eyes_open_sad_worried_open_mouth as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Ну... Если простыми словами, то это был период, когда поэты и писатели 19 века дали толчок развитию литературы." with dissolve

    aliya "Вывели её на новый уровень." with dissolve

    show aliya_sit_side book eyes_open_neutral as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Название, кстати, дали по аналогии с золотым веком." with dissolve

    aliya "Ахматова, как по мне, по праву может носить звание поэтессы этого периода." with dissolve

    "Я почувствовал себя как будто снова в школе на уроке литературы." with dissolve

    me "И чем же она тебе так приглянулась?" with dissolve

    show aliya_sit_side book eyes_closed_neutral as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Сложно сказать, у неё много стихов, что цепляют. Наверное, этим." with dissolve

    show aliya_sit_side book eyes_open_neutral as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "У неё есть стихи о любви, о войне, о родине, о жизни... И при этом каждый вызывает эмоции." with dissolve

    me "Есть любимые?" with dissolve

    show aliya_sit_side book eyes_open_smile as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Да, «Реквием», «Сероглазый король» и «Когда погребают эпоху»." with dissolve

    me "И о чём они?" with dissolve

    show aliya_sit_side book eyes_open_neutral as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Серьёзно? Это же классика." with dissolve

    me "Извини, но поэзия мне как-то не особо..." with dissolve

    show aliya_sit_side book eyes_closed_neutral as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Ясно... Но объяснять будет долго, особенно, если ты их не читал." with dissolve

    me "А хотя бы вкратце?" with dissolve

    show aliya_sit_side book eyes_open_neutral as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Это будет неуважительно, особенно к «Реквиему» у него весьма серьёзная предыстория. Почитай, а там я объясню." with dissolve

    me "Договорились." with dissolve

    show aliya_sit_side book eyes_open_sad_smile as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Кстати, я тоже немного стихи пишу, но пока выходит не очень." with dissolve

    me "А можешь что-нибудь прочесть?" with dissolve

    show aliya_sit_side no_earphones eyes_open_sad_smile as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Да, есть пару небольших стишков." with dissolve

    show aliya_sit_side no_earphones eyes_closed_neutral as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Алия сделала паузу и приготовилась читать." with dissolve

    show aliya_sit_side no_earphones eyes_open_sad_worried_open_mouth as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Тёмных глаз загадочный мрак," with dissolve

    aliya "Алых губ заманчивая сладость." with dissolve

    aliya "Как увижу попадаю впросак," with dissolve

    aliya "Ты моя последняя слабость." with dissolve

    show aliya_sit_side no_earphones eyes_open_neutral as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    me "Неплохо, даже очень." with dissolve

    aliya "И ещё из неплохих." with dissolve

    show aliya_sit_side no_earphones eyes_closed_neutral as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Алия сделала паузу." with dissolve

    show aliya_sit_side no_earphones eyes_open_sad_worried_open_mouth as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Я давно не верю в сказку и чудеса," with dissolve

    aliya "Не прошу подарков у сказочного деда." with dissolve

    aliya "Но, как и в детстве я смотрю на небеса," with dissolve

    aliya "Всё дожидаясь, твоего последнего совета." with dissolve

    show aliya_sit_side no_earphones eyes_open_neutral as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    me "Сильно. Мне нравится!" with dissolve

    show aliya_sit_side no_earphones eyes_open_sad_smile as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Спасибо!" with dissolve

    jump day3_airplane2_part2


label day3_airplane2_part1_ignore:

    show aliya_sit_side book eyes_open_neutral as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    me "Извини, но лично я очень плохо такие идеи улавливаю." with dissolve

    me "Мне легче читать более простой текст, прозу." with dissolve

    aliya "Я поняла." with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_watching_book_smile as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Алия отвернулась и стала читать книгу." with dissolve

    jump day3_airplane2_part2


label day3_airplane2_part2:

    show black zorder 10 with dissolve

    $ renpy.pause(1.0)

    if isMobileWeb:
        show airplane_day_side_mobile_web as airplane_scene at airplane_scene_pos zorder 2

        show cg_airplane_window1_mobile_web as cg_airplane_window_mobile_web at airplane_window_pos zorder 2
    else:

        show airplane_day_side as airplane_scene at airplane_scene_pos zorder 2:
            zoom 1.02

    show aliya_sit_side no_emotion_layer special_airplane_watching_book_smile as Aliya zorder 3 at any_center_pos:
        zoom SCALE

    hide black with dissolve

    "Тем временем тележки с напитками и сэндвичами уже приближалась к нашему ряду." with dissolve

    me "Хочешь что-нибудь?" with dissolve

    show aliya_sit_side book eyes_open_neutral as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Ничего, я не голодна, спасибо." with dissolve

    me "Возьми хотя бы воду." with dissolve

    show aliya_sit_side no_earphones eyes_open_sad_worried as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Хорошо." with dissolve

    me "Там на выбор дают два сэндвича - с курицей или с сыром." with dissolve

    me "Ты точно не хочешь есть?" with dissolve

    show aliya_sit_side no_earphones eyes_open_sad_worried_open_mouth as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Мне немного не по себе. Если я что-то съем, боюсь, меня стошнит." with dissolve

    show aliya_sit_side no_earphones eyes_open_neutral as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    me "Ладно." with dissolve

    me "Ты завтракала?" with dissolve

    aliya "Нет." with dissolve

    "Если Алия с утра ничего не ела и не будет есть сейчас, это не хорошо." with dissolve

    "Мне бы не хотелось, чтобы она упала в голодный обморок в конце дня." with dissolve

    "Надо будет напомнить себе, вечером купить ей что-нибудь поесть." with dissolve

    if isMobileWeb:
        show airplane_day_side_mobile_web as airplane_scene at airplane_scene_pos zorder 2

        show cg_airplane_window1_mobile_web as cg_airplane_window_mobile_web at airplane_window_pos zorder 2

        show airplane_day_side_table_mobile_web as airplane_day_side_table_mobile_web at airplane_side_table_pos zorder 4 with dissolve

    else:

        show airplane_day_side_table as airplane_scene at airplane_scene_pos zorder 2:
            zoom 1.02


    "Я открыл откидные столики." with dissolve

    "Тележка с напитками приехала к нашему ряду." with dissolve

    flight_attendant "Что будете пить?" with dissolve

    me "Воду и апельсиновый сок." with dissolve

    aliya "Воду пожалуйста." with dissolve

    "Бортпроводница передала два стакана мне и один стакан Алие." with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_hold_cap as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Я после разговоров очень хотел пить, поэтому сразу же выпил полстакана воды." with dissolve

    show aliya_sit_side no_earphones eyes_open_neutral as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    if isMobileWeb:

        show airplane_day_side_table_cap_mobile_web as airplane_day_side_table_mobile_web at airplane_side_table_pos zorder 4 with dissolve

    "Алия лишь слегка отхлебнула и поставила стакан на откидной столик." with dissolve

    "Вскоре приехала и тележка с едой." with dissolve

    flight_attendant "Вам сэндвич с курицей или с сыром?" with dissolve

    me "С курицей." with dissolve

    "Бортпроводница передала сэндвич с курицей." with dissolve

    "Поскольку в последний раз я ел несколько часов назад, я с аппетитом набросился на еду." with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_watching_book_neutral as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Алия даже не посмотрела. Она взяла в руки книгу, начала читать и, видимо, думала о чём-то своём." with dissolve

    show black zorder 10 with dissolve

    if isMobileWeb:
        show airplane_day_side_mobile_web as airplane_scene at airplane_scene_pos zorder 2
        show cg_airplane_window1_mobile_web as cg_airplane_window_mobile_web at airplane_window_pos zorder 2

        hide airplane_day_side_table_mobile_web

    else:

        show airplane_day_side as airplane_scene at airplane_scene_pos zorder 2:
            zoom 1.02

    show aliya_sit_side no_emotion_layer special_airplane_watching_book_neutral as Aliya at any_center_pos zorder 3:
        zoom SCALE

    $ renpy.pause(1.0)

    hide black with dissolve

    "Наконец, я закончил есть." with dissolve

    show aliya_sit_side no_earphones eyes_open_neutral as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    me "Предлагаю теперь поспать. Нам ещё лететь примерно час." with dissolve

    aliya "Хорошо." with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_take_out_from_bag as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Алия достала сумку и положила туда книгу." with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_sleep as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Затем она устроилась в кресле поудобнее и закрыла глаза." with dissolve

    "Я немного задержал на ней взгляд." with dissolve

    "Волосы частично закрывали её лицо, но я всё равно отметил про себя, что она очень красивая." with dissolve

    "Ладно, пожалуй и мне тоже лучше немного вздремнуть." with dissolve

    show black zorder 10 with dissolve

    "Я прилёг в кресле, закрыл глаза" with dissolve

    "и медленно погрузился в сон..." with dissolve

    jump day3_airplane3



label day3_airplane3:

    if renpy.emscripten:
        $ import emscripten
        $ emscripten.run_script("play_sound_seatbelt()")
    else:
        play sound "sound/seatbelt.ogg"

    "Прозвучал звук включения индикатора \"пристегните ремни\"." with dissolve

    announcement "Уважаемые пассажиры, мы готовимся к посадке в городе Москва, аэропорт Домодедово." with dissolve

    announcement "Пожалуйста, пристегните ремни, приведите спинки кресел в вертикальное положение," with dissolve

    announcement "уберите откидные столики и откройте шторки на иллюминаторах." with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_sleep as Aliya at any_center_pos zorder 3:
        zoom SCALE


    if not isMobileWeb:

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

    show aliya_sit_side no_earphones eyes_closed_neutral as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Алия тоже проснулась." with dissolve

    show aliya_sit_side no_earphones eyes_open_neutral as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Мы уже в Москве?" with dissolve

    me "Да. Уже совсем скоро мы приземлимся в Москве." with dissolve

    "Алия ничего не ответила." with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_phone_earphones as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Вместо ответа она достала телефон, надела наушники и включила музыку." with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_phone_semen_watch2 as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Затем она повернулась ко мне." with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_phone_semen_watch1 as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Ты слушаешь рок-музыку?" with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_phone_semen_watch2 as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    me "Иногда." with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_phone_semen_watch1 as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Хочешь послушать мой плейлист?" with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_phone_semen_watch2 as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    me "Давай." with dissolve

    aliya "Мне нравится пост-рок. Сейчас включу тебе одну из моих любимых песен." with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_pass_earphones as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("stopAllMusic()")
            $ emscripten.run_script("play_airplane_1ambience_before_landing_loop()")

    $ last_playing_music = "playRunaway07, play_airplane_1ambience_before_landing_loop"

    "Алия протянула мне наушник." with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_window_earphones as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE


    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("playRunaway07()")
    else:
        play music_crossfade "music/Runaway_07 (Main_Theme).ogg" # fadein 1.0
        queue music_crossfade "music/Runaway_07 (Main_Theme_Loop).ogg"



    "Я вставил наушник в ухо и заиграла рок-музыка." with dissolve

    #1998 / 1080 = 1.85

    #8638 / 1920 = 4.4989583333333333333333333333333‬  ~ 4.49896


    if isMobileWeb:
        show airplane_day_side_mobile_web as airplane_scene at airplane_scene_pos zorder 2

        show cg_airplane_window1_mobile_web as cg_airplane_window_mobile_web at airplane_window_pos zorder 2

        show aliya_sit_side no_emotion_layer special_airplane_window_earphones as Aliya at any_center_pos zorder 3 with dissolve:
            zoom SCALE
    else:
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

        show aliya_sit_side no_emotion_layer special_airplane_window_earphones as Aliya at any_center_pos zorder 3 with dissolve:
            zoom SCALE
            ypos 1.0
            linear 0.2 ypos 1.01
            easeout 2.0 ypos 1.0

    if not isMobileWeb:

        hide airplane_window_left with dissolve

        hide airplane_window_right with dissolve

    "Самолёт слегка дёрнулся и начал идти на снижение." with dissolve

    "Погода была довольно ясной и из иллюминатора можно было видеть Подмосковье." with dissolve

    "Алия слушала музыку и внимательно смотрела в иллюминатор." with dissolve

    "Хотя она была неподвижна, я чувствовал, что она сильно волнуется." with dissolve

    "Её беспокойство немного передавалось мне." with dissolve

    "Возможно, её родители всё ещё думают, что она на учёбе." with dissolve

    "А может быть, они уже хватились и ищут её?" with dissolve

    "Но назад дороги нет, мы уже почти приземлились в Москве." with dissolve

    "Надо довести начатое до конца." with dissolve

    "Я снова бросил взгляд на Алию." with dissolve

    "Она всё так же неподвижно смотрит в иллюминатор." with dissolve

    "Несмотря на волнение, в её глазах читалась некоторая обречённость и уверенность." with dissolve

    "Интересно, если бы она не встретилась со мной - сбежала бы она из дома?" with dissolve

    "С её-то характером - очень может быть!" with dissolve

    "Возможно, она сбежала бы одна, автостопом добралась бы до Краснодара или Ростова." with dissolve

    "Возможно, ей бы помог сбежать какой-нибудь другой человек." with dissolve

    "Может быть, это был бы какой-нибудь плохой парень." with dissolve

    "С нехорошими намерениями..." with dissolve

    "Брр! Даже не хочу об этом думать." with dissolve

    "Самое важное - Алия сейчас сидит здесь, рядом со мной." with dissolve

    "Судьба Алии в моих руках." with dissolve

    "Она доверяет мне и я не должен разрушить её доверие." with dissolve

    "Пока она со мной, она в безопасности." with dissolve

    "Если обману её или воспользуюсь ей - она сбежит уже и от меня." with dissolve

    "И вот тогда я уже не смогу ей ничем помочь." with dissolve

    "Так уж получилось, что я оставил свои дела и решил ввязаться в эту историю." with dissolve

    "И я не брошу всё на полпути." with dissolve

    "Сейчас уже вторая половина дня, что мы ещё успеем сделать за сегодня?" with dissolve

    "Купим платье для намаза, раз уж Алия этого очень хочет." with dissolve

    "Сделаем сим-карту, заселимся в гостиницу или в хостел." with dissolve

    "Поужинаем, возможно, купим что-нибудь по мелочи." with dissolve

    "Всё остальное: банковскую карту, покупку сменной одежды и бытовых вещей, поиск работы и т. д. - оставим на завтра." with dissolve

    "Я думаю, я потрачу немало денег на это приключение." with dissolve

    "По крайней мере до тех пор, пока Алия не обустроится в Москве, не найдёт работу, съёмное жильё." with dissolve

    "Но денег мне совсем не жалко." with dissolve

    "Я своё ещё заработаю, а вот Алия действительно нуждается в моей поддержке." with dissolve

    "И я постараюсь её не подвести!" with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_window_earphones as Aliya at any_center_pos zorder 3:
        zoom SCALE

    "Самолёт уверенно снижался." with dissolve

    "В иллюминаторе уже можно было разглядеть дома, деревья, автомобили на дорогах." with dissolve

    # x 2.271875
    # y 0.74074


    if isMobileWeb:
        show airplane_day_side_mobile_web as airplane_scene at airplane_scene_pos zorder 2

        show cg_airplane_window2_mobile_web as cg_airplane_window_mobile_web at airplane_window_pos zorder 2
    else:
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

    "И вот, наконец, внизу под крылом показалась широкое полотно взлётно-посадочной полосы." with dissolve

    "Мы уже летим прямо над широким серым полотном." with dissolve

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("stopAllMusic()")
            $ emscripten.run_script("playRunaway07()")
            $ emscripten.run_script("play_airplane_1ambience_before_landing_loop()")

    $ last_playing_music = "playRunaway07, play_audio_ambience_airplane_3after_landing_loop"

    "Ещё чуть-чуть и шасси коснётся земли." with dissolve

    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("play_airplane_2landed_shortened()")
            $ emscripten.run_script("play_audio_ambience_airplane_3after_landing_loop(19.856)")
    else:
        play music "ambience/airplane_2landed_shortened.ogg"
        queue music "ambience/airplane_3after_landing_loop.ogg"

    if isMobileWeb:
        "Бух!" with dissolve
    else:
        "Бух!" with vpunch

    "Самолёт начал тормозить и всех пассажиров тут же дёрнуло вперёд." with dissolve

    "С громким шумом и грохотом авиалайнер снизил скорость." with dissolve

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("music_stage_preload = \"music_airplane2_Runaway07\"")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracks(stopAllMusic, playRunaway07, play_audio_ambience_airplane_3after_landing_loop)")
            #$ emscripten.run_script("stopAllMusic()")
            ##$ emscripten.run_script("playRunaway07()")
            #$ emscripten.run_script("play_audio_ambience_airplane_3after_landing_loop()")

    $ last_playing_music = "play_audio_ambience_airplane_3after_landing_loop"

    "Мы уже медленно катились по посадочной полосе." with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_phone as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    $ music_stage_preload = "music_airplane2_Runaway08"

    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("stopRunaway07()")
            $ emscripten.run_script("music_stage_preload = \"music_airplane2_Runaway08\"")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracksAsync()")
    else:
        stop music_crossfade # fadeout 1.0

    "Пришло время вытащить наушник." with dissolve

    announcement "Уважаемые дамы и господа, добро пожаловать в Москву, международный аэропорт Домодедово." with dissolve

    announcement "Местное время четырнадцать часов двадцать минут. Погода в Москве ясная, температура воздуха плюс двадцать градусов тепла." with dissolve

    announcement "Пожалуйста, оставайтесь на своих местах с пристегнутыми ремнями безопасности до выключения светового табло \"пристегните ремни\"." with dissolve

    announcement "От имени авиакомпании благодарим вас за полёт и будем рады новой встрече!" with dissolve

    #show cg_screen_phone_time_day3_afternoon_airplane as cg_screen_phone with dissolve

    show right_hand phone_day day3_afternoon_airplane as cg_screen_phone zorder 5 with dissolve

    "Я достал телефон и выключил авиарежим." with dissolve

    $ hidePhone()

    show aliya_sit_side no_emotion_layer special_airplane_phone as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    show aliya_sit_side no_earphones eyes_open_neutral as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Алия посмотрела на меня." with dissolve

    show aliya_sit_side no_earphones eyes_open_sad_worried_question as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Мне тоже выключить?" with dissolve

    me "Лучше пока не надо." with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_phone as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Ладно." with dissolve

    show aliya_sit_side no_earphones eyes_open_watching_phone as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    "Алия убрала телефон." with dissolve

    show aliya_sit_side no_earphones eyes_open_neutral as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Мы от аэропорта долго будем ехать?" with dissolve

    me "Да, 40 минут примерно." with dissolve

    me "Мы возьмем аэроэкспресс до Москвы, он отправляется в 15:00." with dissolve

    me "И мы приедем на Павелецкий вокзал примерно в 15:40. Оттуда нужно будет поехать на метро." with dissolve

    show aliya_sit_side no_earphones eyes_open_sad_worried_question as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    aliya "Ты не забыл, что нам нужно будет купить коврик и одежду?" with dissolve

    me "Да, конечно." with dissolve

    show aliya_sit_side no_earphones eyes_open_neutral as Aliya at any_center_pos zorder 3 with dissolve:
        zoom SCALE

    scene black with dissolve

    $ renpy.pause(1.0)

    scene airplane_day with dissolve

    $ savegame_picture = "savegame_airplane_day"

    #$ renpy.stop_predict("images/sprites/Aliya/Sitting2/bench/*.*")
    #$ renpy.stop_predict("images/sprites/Aliya/Sitting2/airplane/*.*")

    #$ renpy.start_predict("images/sprites/Aliya/Pose1/*.*")
    #$ renpy.start_predict("images/sprites/Aliya/Pose1/mask1/*.*")
    #$ renpy.start_predict("images/sprites/Aliya/Pose2/*.*")
    #$ renpy.start_predict("images/sprites/Aliya/Pose2/mask2/*.*")

    "Наконец самолёт остановился." with dissolve

    announcement "Бортпроводникам приготовиться к переводу селекторов в положение Disarmed." with dissolve

    announcement "Бортпроводникам перевести селекторы в положение Disarmed." with dissolve

    if renpy.emscripten:
        $ import emscripten
        $ emscripten.run_script("play_sound_seatbelt()")
    else:
        play sound "sound/seatbelt.ogg"


    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("stopAllMusic()")
            $ emscripten.run_script("play_audio_ambience_airplane_3after_landing_loop()")

    $ last_playing_music = "play_audio_ambience_airplane_stopped_loop"

    "Прозвучал звук выключения индикатора \"пристегните ремни\"." with dissolve


    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("play_audio_ambience_airplane_stopped_loop()")
    else:

        play music "ambience/airplane_stopped_loop.ogg"

    scene airplane_day2 with dissolve

    "Пассажиры вставали со своих кресел, собирали сумки и чемоданы, а затем пошли к выходу из самолёта." with dissolve

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("music_stage_preload = \"music_airplane2_Runaway08\"")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracks(stopAllMusic, play_audio_ambience_airplane_stopped_loop)")

    $ last_playing_music = "playRunaway08"

    "Я с Алией тоже встали, забрали вещи и пошли к выходу." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    scene domodedovo_luggage with dissolve

    $ savegame_picture = "savegame_domodedovo_luggage"

    $ music_stage_preload = "music_Runaway08_train"

    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("playRunaway08()")
            $ emscripten.run_script("music_stage_preload = \"music_Runaway08_train\"")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracksAsync()")
    else:

        play music "music/Runaway_08 (Loop).ogg" # fadein 3.0

        queue music "music/Runaway_08 (Loop).ogg"

    "Мы прошли через телетрап и вышли в зону выдачи багажа." with dissolve

    show Aliya_stand_half_turned jacket_armsdown eyes_open_sad_smile as Aliya at any_center_pos with dissolve:
        zoom 1.0

    aliya "Здесь мы должны забрать наш багаж?" with dissolve

    me "Да. Но мы не сдавали сумки в багаж, так что можем сразу идти на выход." with dissolve

    show Aliya_stand_half_turned jacket_armsdown eyes_open_sad_worried_open_mouth as Aliya at any_center_pos with dissolve:
        zoom 1.0

    aliya "Тогда можно я в туалет схожу?" with dissolve

    me "Да, хорошо. Он должен быть где-то справа." with dissolve

    me "Я пока что куплю билеты на аэроэкспресс." with dissolve

    show Aliya_stand_half_turned eyes_open_smile as Aliya at any_center_pos with dissolve:
        zoom 1.0

    aliya "Хорошо. Я быстро!" with dissolve

    hide Aliya with dissolve

    #show cg_screen_phone_aeroexpress1 as cg_screen_phone with dissolve

    show right_hand phone_day day_aeroexpress1 as cg_screen_phone with dissolve


    "Алия ушла, а я зашел в приложение Аэроэкспресса." with dissolve

    "С недавних пор приложение требует вводить паспортные данные пассажира." with dissolve

    "Очередной бред от спецслужб, наверное. Всё равно никто не контролирует правильность этих данных." with dissolve

    "Я просто куплю оба наши билета на свой паспорт." with dissolve

    #show cg_screen_phone_aeroexpress2 as cg_screen_phone with dissolve

    show right_hand phone_day day_aeroexpress2 as cg_screen_phone with dissolve

    "Так, тут требуется вводить номер карты." with dissolve

    #show semen_room_table_night_foreground_card_hands zorder 2 with dissolve

    show left_hand hand_card_day zorder 2 with dissolve

    "Я достал свою кредитную карту-выручалочку и ввёл данные." with dissolve

    #hide semen_room_table_night_foreground_card_hands with dissolve

    hide left_hand with dissolve

    #show cg_screen_phone_aeroexpress3 as cg_screen_phone with dissolve

    show right_hand phone_day day_aeroexpress3 as cg_screen_phone with dissolve

    "Пришло СМС-уведомление об успешной покупке." with dissolve

    #show cg_screen_phone_aeroexpress4 as cg_screen_phone with dissolve

    show right_hand phone_day day_aeroexpress4 as cg_screen_phone with dissolve

    "Я смахнул его в сторону не глядя. Мне уже страшно проверять баланс карты." with dissolve

    "Тем временем подошла Алия." with dissolve

    show Aliya_stand_straight eyes_open_smile as Aliya at any_center_pos with dissolve:
        zoom 1.0

    aliya "Мы готовы?" with dissolve

    me "Я тебе отправлю QR-код в мессенджере." with dissolve

    me "Отключи авиарежим на телефоне ненадолго, чтобы получить сообщение с кодом." with dissolve

    me "Когда мы будем проходить на аэроэкспресс, ты должна поднести телефон с кодом к сканеру." with dissolve

    $ switchMessengerToPhone()

    $ changeDialogToAliya()

    $ showMessengerPhone(is_night=False, force_no_transition=True)

    show Aliya_stand_half_turned jacket_armsdown eyes_open_happy as Aliya at any_center_pos with dissolve:
        zoom 1.0

    aliya "Хорошо." with dissolve

    show Aliya_stand_half_turned jacket_armsdown eyes_open_watching_phone extra_stand_half_turned2_phone as Aliya at any_center_pos with dissolve:
        zoom 1.0

    $ addSentMessageQr()

    "Я сделал скриншот и отправил Алие." with dissolve

    $ clearDisplayMessages()

    $ hidePhone()

    me "Пошли?" with dissolve

    show Aliya_stand_straight eyes_open_smile as Aliya at any_center_pos with dissolve:
        zoom 1.0

    aliya "Пошли." with dissolve

    scene black with dissolve


    #$ renpy.stop_predict("images/sprites/Aliya/Pose1/*.*")
    #$ renpy.stop_predict("images/sprites/Aliya/Pose1/mask1/*.*")
    #$ renpy.stop_predict("images/sprites/Aliya/Pose2/*.*")
    #$ renpy.stop_predict("images/sprites/Aliya/Pose2/mask2/*.*")

    #$ renpy.start_predict("images/sprites/Aliya/Sitting1/*.*")
    #$ renpy.start_predict("images/sprites/Aliya/Sitting1/alt/*.*")

    "Мы отправились к аэроэкспрессу..." with dissolve

    jump day3_aeroexpress



label day3_aeroexpress:

    scene aeroexpress with dissolve

    $ savegame_picture = "savegame_aeroexpress"

    show aliya_sit_front_hands_aside eyes_open_neutral as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    "Мы успешно прошли к вагонам аэроэкспресса и заняли места на первом этаже." with dissolve

    "Здесь было тихо, других пассажиров, кроме нас, в вагоне не было." with dissolve

    announcement "Уважаемые пассажиры, просим вас занять свои места. Аэроэкспресс отправляется через десять минут!" with dissolve

    "Я попытался подключиться к вайфаю, но здесь он был очень медленный." with dissolve

    "Так что мне пришлось использовать мобильный интернет." with dissolve

    me "Говоришь, тебе нужен коврик для намаза?" with dissolve

    show aliya_sit_front_hands_aside eyes_closed_sad as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Да и платье." with dissolve

    me "Есть идеи, где это можно купить?" with dissolve

    show aliya_sit_front_hands_together eyes_open_sad_worried_open_mouth as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "На рынке точно продаётся." with dissolve

    show aliya_sit_front_hands_together eyes_open_sad_worried as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    me "Это Москва. Здесь с рынками не очень." with dissolve

    me "Я поищу какие-нибудь магазины с мусульманскими товарами." with dissolve

    show aliya_sit_front_hands_together eyes_open_thinking_hands_inside as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Хорошо." with dissolve

    #show cg_screen_phone_map1 as cg_screen_phone with dissolve
    show right_hand phone_day map_taganskaya1 as cg_screen_phone with dissolve

    "Я открыл приложение с картой и начал искать." with dissolve

    me "Вот тут на Таганской есть несколько магазинов." with dissolve

    me "Скорее всего там же и одежду продают." with dissolve

    show aliya_sit_front_hands_together eyes_open_sad_smile as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Это хорошо." with dissolve

    me "Плохо что они закрываются в шесть часов вечера." with dissolve

    show aliya_sit_front_hands_together eyes_open_sad_worried as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "А во сколько мы сможем туда добраться?" with dissolve

    show aliya_sit_front_hands_together eyes_open_sad_worried as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    #show cg_screen_phone_metro_map as cg_screen_phone with dissolve

    show right_hand phone_day map_metro as cg_screen_phone with dissolve

    "Я посмотрел карту метро Москвы." with dissolve

    me "Аэроэкспресс привезет нас в 15:40 на станцию метро Павелецкая." with dissolve

    me "Это кольцевая линия метро." with dissolve

    me "Там мы спустимся в метро, сделаем тебе карту Тройка," with dissolve

    me "проедем одну станцию, затем выйдем на Таганской и немного пройдёмся пешком." with dissolve

    show aliya_sit_front_hands_together eyes_open_sad_worried_question as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Карту Тройка?" with dissolve

    $ hidePhone()

    me "Ну это карточка для оплаты проезда в Москве. Кладёшь на неё деньги и затем оплачиваешь проезд." with dissolve

    me "Работает в метро, автобусах, троллейбусах и трамваях." with dissolve

    show aliya_sit_front_hands_aside eyes_open_neutral as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "И сколько мы будем ехать туда?" with dissolve

    me "На метро быстро, но нам ещё придётся идти пешком. Минут 20-30 займёт." with dissolve

    aliya "Я поняла." with dissolve

    me "Если мы не найдём ничего подходящего в мусульманском магазине, скорее всего придётся искать другой магазин." with dissolve

    me "Думаю, мы сегодня немало на метро поездим." with dissolve

    aliya "Хорошо." with dissolve

    show aliya_sit_front_hands_together eyes_open_sad_worried_question as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Что нам ещё нужно будет купить?" with dissolve

    me "Будет уже поздно. Я думаю, мы ещё сделаем тебе новую сим-карту." with dissolve

    me "Больше ничего сегодня не успеем сделать." with dissolve

    me "Всё остальное оставим на завтра." with dissolve

    aliya "А где мы будем ночевать?" with dissolve

    "Вообще-то я до сих пор не забронировал жильё." with dissolve

    me "Пока не знаю. Думаю, самое время искать сейчас." with dissolve

    show aliya_sit_front_hands_aside eyes_open_thinking_hands_outside as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Хорошо!" with dissolve

    #show cg_screen_phone_booking as cg_screen_phone with dissolve

    show right_hand phone_day day_booking as cg_screen_phone with dissolve


    "Я начал смотреть приложения для бронирования." with dissolve

    "В какой-то момент я понял, что совершенно не знаю, где можно арендовать жильё не показывая паспорт." with dissolve

    #show cg_screen_phone_booking_new_message as cg_screen_phone with dissolve

    show right_hand phone_day day_booking_new_message as cg_screen_phone with dissolve

    messenger "Новое сообщение"

    $ changeDialogToCoach()

    $ showMessengerPhone(is_night=False, force_no_transition=True)

    $ addReceivedMessage(2)

    coach "Привет, Семён! Как дела?" with dissolve

    $ addSentMessage(3)

    me "Мы уже в Москве, сели на Аэроэкспресс." with dissolve

    $ addSentMessage(5)

    me "Правда у нас есть небольшая проблема. Нам нужно найти жильё, где не спрашивают паспорт" with dissolve

    $ addReceivedMessage(3)

    coach "В Москве много квартир сдаются посуточно." with dissolve

    $ addReceivedMessage(2)

    coach "На любом столбе есть объявления." with dissolve

    $ addReceivedMessage(3)

    coach "Ты из тех людей, которые не любят звонить по телефону?" with dissolve

    $ addSentMessage(2)

    me "Ну вообще-то да..." with dissolve

    $ addReceivedMessage(0)

    coach ":)" with dissolve

    $ addReceivedMessage(2)

    coach "Давай я забронирую тебе жильё." with dissolve

    $ addReceivedMessage(5)

    coach "Напиши примерный район где вы будете жить, я начну искать." with dissolve

    $ addSentMessage(4)

    me "В районе недалеко от станции метро Таганская. Квартиру на неделю." with dissolve

    $ addReceivedMessage(5)

    coach "Хорошо. Прямо возле метро не обещаю, но постараюсь найти в том районе." with dissolve

    $ addReceivedMessage(3)

    coach "Есть какие-то дополнительные пожелания?" with dissolve

    $ addSentMessage(4)

    me "Чистая квартира с ремонтом, раздельные кровати." with dissolve

    $ addSentMessage(1)

    me "Больше ничего." with dissolve

    $ addReceivedMessage(4)

    coach "Хорошо, начну искать. Напишу, когда забронирую." with dissolve

    $ addSentMessage(0)

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("stopAllMusic()")
            $ emscripten.run_script("playRunaway08()")

    $ last_playing_music = ""

    me "Спасибо!" with dissolve

    $ clearDisplayMessages()

    $ hidePhone()

    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("stopAllMusic()")
    else:

        stop music # fadeout 2.0

    "Я убрал телефон." with dissolve

    "Прошло немного времени..." with dissolve

    if renpy.emscripten:
        $ import emscripten
        $ emscripten.run_script("play_sound_aeroexpress()")
    else:

        play sound "sound/aeroexpress.ogg"


    announcement "Уважаемые пассажиры, аэроэкспресс в Москву отправляется сейчас! Длительность поездки составит сорок минут." with dissolve

    announcement "Осторожно, двери закрываются! Следующая станция - Павелецкий вокзал." with dissolve

    "Двери вагона тихо закрылись." with dissolve

    "Вагон тронулся, затем начал медленно разгоняться." with dissolve

    show aliya_sit_front_hands_together eyes_open_thinking_hands_inside as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("music_stage_preload = \"music_Runaway08_train\"")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracks(stopAllMusic)")

    $ last_playing_music = "play_audio_ambience_train"

    "Алия начала смотреть в окно." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    $ music_stage_preload = "music_train_metro"

    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("play_audio_ambience_train()")
            $ emscripten.run_script("music_stage_preload = \"music_train_metro\"")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracksAsync()")
    else:

        play music "ambience/440611__florianreichelt__train-ambience.ogg" # fadein 1.0 # fadeout 1.0

    scene aeroexpress with dissolve

    show aliya_sit_front_hands_together eyes_open_thinking_hands_inside as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    "Мы уже въехали в Москву и неторопливо ехали к Павелецкому вокзалу." with dissolve

    "Я решил прервать молчание." with dissolve

    me "Ты в порядке?" with dissolve

    show aliya_sit_front_hands_together eyes_open_sad_worried_question as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    "Алия посмотрела на меня." with dissolve

    aliya "Да." with dissolve

    me "Есть хочешь?" with dissolve

    aliya "Нет." with dissolve

    "Надо поговорить о чём-нибудь, но о чём?" with dissolve

    me "Расскажи, где ты хочешь учиться?" with dissolve

    me "Ты хочешь учиться в колледже на медика?" with dissolve

    show aliya_sit_front_hands_aside eyes_closed_neutral as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Нет." with dissolve

    show aliya_sit_front_hands_aside eyes_open_neutral as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Я вообще не хочу быть медиком." with dissolve

    aliya "Я туда поступила потому, что отец обещал мне, если я буду хорошо учиться, потом смогу пойти в университет." with dissolve

    aliya "Но потом он отказался от своих слов." with dissolve

    aliya "Мне тогда было 16. Родители сказали, что не смогут после колледжа отдать меня в университет." with dissolve

    aliya "Мне было очень плохо. Я полностью забила на учёбу." with dissolve

    aliya "Я даже пыталась порезать вены в туалете своего коллежда." with dissolve

    aliya "Мне было уже всё равно. Мне не хотелось жить." with dissolve

    aliya "Теперь мой отец хочет, чтобы я вышла замуж." with dissolve

    aliya "У него не хватает денег, чтобы оплатить мою учебу." with dissolve

    me "Если бы у тебя были деньги, куда бы ты хотела поступить учиться?" with dissolve

    show aliya_sit_front_hands_aside eyes_open_smile as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    "Алия улыбнулась." with dissolve

    aliya "В МГИМО." with dissolve

    me "Хороший выбор." with dissolve

    "Надо будет загуглить, сколько там стоит обучение." with dissolve

    me "Может быть когда-нибудь ты сможешь поступить туда." with dissolve

    show aliya_sit_front_hands_aside eyes_closed_smile as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Возможно." with dissolve

    me "А кем ты вообще хочешь быть в жизни?" with dissolve

    show aliya_sit_front_hands_together eyes_open_sad_worried as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Не знаю." with dissolve

    me "Что тебе нравится делать?" with dissolve

    show aliya_sit_front_hands_together eyes_open_happy as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Смотреть аниме, дорамы и читать стихи. Ещё я готовить люблю." with dissolve

    me "Может тебе стоит стать поваром?" with dissolve

    me "В будущем станешь крутым шеф-поваром, откроешь свой ресторан." with dissolve

    show aliya_sit_front_hands_together eyes_closed_grin as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    "Алия улыбнулась ещё больше." with dissolve

    show aliya_sit_front_hands_aside eyes_open_playful as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Я думала открыть свой ресторан, да." with dissolve

    aliya "Мечтала в каком месте он будет, какое там будет меню, интерьер." with dissolve

    show aliya_sit_front_hands_aside eyes_open_neutral as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Но потом как-то передумала." with dissolve

    me "Понятно." with dissolve

    show aliya_sit_front_hands_aside eyes_closed_neutral as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "У меня в этом году брат ЕГЭ сдает. Ему нужно поступить в универ." with dissolve

    aliya "Поэтому сейчас плохо с деньгами." with dissolve

    show aliya_sit_front_hands_aside eyes_open_neutral as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Моему отцу как-то не до меня, он тратит деньги на моего брата." with dissolve

    me "Понимаю." with dissolve

    me "Если у тебя брат спортсмен, он может и так поступить, бесплатно." with dissolve

    aliya "Нет, он не спортсмен. Он обычный." with dissolve

    me "Ясно." with dissolve

    me "Кроме брата у тебя ещё сестра есть?" with dissolve

    aliya "Да." with dissolve

    aliya "Она очень послушная и всё время меня поучает." with dissolve

    show aliya_sit_front_hands_aside eyes_closed_annoyed as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Всё время мне лекции читает, говорит типа:\"Вот я же говорила\"." with dissolve

    me "Да. Это бесит." with dissolve

    show aliya_sit_front_hands_aside eyes_open_angry as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE


    aliya "Конечно." with dissolve

    aliya "Она не смотрит аниме или корейские сериалы." with dissolve

    show aliya_sit_front_hands_together eyes_closed_sad_worried_open_mouth as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Иногда это удобно. Если я плачу, она может спросить у меня, что случилось." with dissolve

    show aliya_sit_front_hands_together eyes_open_sad_worried as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    aliya "Я отвечаю, что вспомнила грустный момент в какой-нибудь дораме." with dissolve

    aliya "Она этого всё равно не понимает." with dissolve

    aliya "Только говорит:\"Опять ты со своими корейцами\"." with dissolve

    me "Хорошая идея валить всё на сериалы." with dissolve

    show aliya_sit_front_hands_together eyes_open_sad_smile as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE


    aliya "Да." with dissolve

    show aliya_sit_front_hands_together eyes_open_thinking_hands_inside as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE


    if renpy.emscripten:
        $ import emscripten
        $ emscripten.run_script("play_sound_aeroexpress()")
    else:
        play sound "sound/aeroexpress.ogg"

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("stopAllMusic()")
            $ emscripten.run_script("play_audio_ambience_train()")

    $ last_playing_music = ""

    announcement "Уважаемые пассажиры, аэроэкспресс прибывает на конечную станцию Павелецкий вокзал." with dissolve

    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("stopAllMusic()")
    else:
        stop music # fadeout 1.0

    "Поезд медленно остановился." with dissolve

    "Двери тихо открылись." with dissolve

    me "Пойдём!" with dissolve

    show aliya_sit_front_hands_together eyes_open_sad_smile as Aliya with dissolve:
        xalign 0.5
        yalign 1.0
        zoom SCALE

    $ last_playing_music = "play_ambience_metro_station"

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("music_stage_preload = \"music_train_metro\"")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracks(stopAllMusic)")


    aliya "Пойдём." with dissolve

    scene black with dissolve

    #$ renpy.stop_predict("images/sprites/Aliya/Sitting1/*.*")
    #$ renpy.stop_predict("images/sprites/Aliya/Sitting1/alt/*.*")

    #$ renpy.start_predict("images/sprites/Aliya/Pose1/*.*")
    #$ renpy.start_predict("images/sprites/Aliya/Pose1/mask1/*.*")
    #$ renpy.start_predict("images/sprites/Aliya/Pose2/*.*")
    #$ renpy.start_predict("images/sprites/Aliya/Pose2/mask2/*.*")


    $ renpy.pause(1.0)

    jump day3_metro
