label day4_end_success:

    scene black with dissolve

    #$ renpy.stop_predict("images/sprites/Aliya/Pose4/*.*")

    #$ renpy.stop_predict("images/sprites/Aliya/Pose1/*.*")
    #$ renpy.stop_predict("images/sprites/Aliya/Pose1/mask1/*.*")
    #$ renpy.stop_predict("images/sprites/Aliya/Pose2/*.*")
    #$ renpy.stop_predict("images/sprites/Aliya/Pose2/mask2/*.*")

    #$ renpy.start_predict("images/sprites/Aliya/Sitting2/airplane/*.*")
    #$ renpy.start_predict("images/sprites/Aliya/Sitting2/bench/*.*")

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("music_stage_preload = \"music_Runaway15_airplane3\"")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracks(stopAllMusic, playRunaway15)")

    $ last_playing_music = "play_ambience_kazakhstan_airplane_before_takeoff_ambience"

    "И вот наконец мы в самолете..." with dissolve

    show black zorder 10

    $ music_stage_preload = "music_airplane3_Runaway07"

    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("play_ambience_kazakhstan_airplane_before_takeoff_ambience()")
            $ emscripten.run_script("music_stage_preload = \"music_airplane3_Runaway07\"")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracksAsync()")
    else:

        play music "ambience/kazakhstan_airplane_before_takeoff_ambience.ogg" # fadein 1.0

    if isMobileWeb:
        show airplane_day_side_mobile_web as airplane_scene at airplane_scene_pos zorder 2

        show cg_airplane_window4_mobile_web as cg_airplane_window_mobile_web at airplane_window_pos zorder 2
    else:
        show airplane_day_side as airplane_scene

    $ savegame_picture = "savegame_airplane_day_side"

    if not isMobileWeb:
        show cg_airplane_window4 as airplane_window

    hide black with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_window as Aliya at any_center_pos zorder 3:
        zoom SCALE

    "Как только мы сели на свои места, бортпроводники объявили о завершении посадки." with dissolve

    "Я немного отдышался, затем посмотрел на Алию." with dissolve

    me "Спасибо, что доверяешь мне." with dissolve

    show aliya_sit_side no_earphones eyes_open_sad_worried_open_mouth as Aliya at any_center_pos zorder 3:
        zoom SCALE

    aliya "Куда мы летим?" with dissolve

    show aliya_sit_side no_earphones eyes_open_neutral as Aliya at any_center_pos zorder 3:
        zoom SCALE

    me "Мы летим в Казахстан, в город Усть-Каменогорск." with dissolve

    aliya "Ты там был когда-нибудь?" with dissolve

    me "Нет, ни разу. Но у меня есть знакомая, которая живет там." with dissolve

    aliya "Какой у тебя план?" with dissolve

    me "Детального плана нет." with dissolve

    me "Я думаю, мы с тобой будем скрываться в Казахстане некоторое время." with dissolve

    me "Твой отец постарается организовать для меня уголовное дело в России." with dissolve

    me "Да и тебе туда лучше не возвращаться." with dissolve

    me "Нам нужно будет сделать себе другие документы, на другое имя. Возможно, придется сменить внешность." with dissolve

    me "А затем, когда-нибудь в будущем, мы сможем уехать в Южную Корею, как ты об этом мечтаешь." with dissolve

    me "Уже под другими именами, с другими документами, с другой внешностью..." with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_window as Aliya at any_center_pos zorder 3:
        zoom SCALE

    aliya "Поняла..." with dissolve

    scene black with dissolve

    #$ renpy.stop_predict("images/sprites/Aliya/Sitting2/airplane/*.*")
    #$ renpy.stop_predict("images/sprites/Aliya/Sitting2/bench/*.*")

    $ renpy.pause(1.0)

    show airplane_day_kz at airplane_scene_pos with dissolve:
        ypos 0.525
        xpos 0.5
        zoom 1.15

    $ savegame_picture = "savegame_airplane_day"

    "Минуты тянулись очень долго." with dissolve

    "Почему мы до сих пор не взлетаем?" with dissolve

    "Неужели нас обнаружили, и сейчас высадят из самолета?" with dissolve

    "Я нервничал, и пытался высмотреть что там происходит в окне, но я не видел ничего особенного." with dissolve

    show airplane_day_kz at airplane_scene_pos:
        zoom 1.15
        linear 0.1 xpos 0.501 ypos 0.526
        linear 0.1 xpos 0.499 ypos 0.524
        linear 0.1 xpos 0.501 ypos 0.524
        linear 0.1 xpos 0.499 ypos 0.526
        linear 0.1 xpos 0.499 ypos 0.524
        linear 0.1 xpos 0.501 ypos 0.526
        linear 0.1 xpos 0.499 ypos 0.524
        linear 0.1 xpos 0.501 ypos 0.526
        linear 0.1 xpos 0.501 ypos 0.526
        linear 0.1 xpos 0.499 ypos 0.524
        linear 0.1 xpos 0.501 ypos 0.524
        linear 0.1 xpos 0.499 ypos 0.526
        linear 0.1 xpos 0.499 ypos 0.524
        linear 0.1 xpos 0.501 ypos 0.526
        linear 0.1 xpos 0.499 ypos 0.524
        linear 0.1 xpos 0.501 ypos 0.526
        linear 0.1 xpos 0.501 ypos 0.526
        linear 0.1 xpos 0.499 ypos 0.524
        linear 0.1 xpos 0.501 ypos 0.524
        linear 0.1 xpos 0.499 ypos 0.526
        linear 0.1 xpos 0.499 ypos 0.524
        linear 0.1 xpos 0.501 ypos 0.526
        linear 0.1 xpos 0.499 ypos 0.524
        linear 0.1 xpos 0.501 ypos 0.526
        ypos 0.525
        xpos 0.5

    "Вот самолет дернулся, трогаясь с места, и поехал к взлетной полосе." with dissolve

    "Ох, как же он медленно едет... скорее, скорее!" with dissolve

    "Мне уже мерещились полицейские машины, выезжающие на летное поле и преследующие наш самолет." with dissolve

    "Наконец, самолет подъехал к самому началу взлетно-посадочной полосы, и остановился." with dissolve

    if renpy.emscripten:
        $ import emscripten
        $ emscripten.run_script("play_sound_seatbelt()")
    else:
        play sound "sound/seatbelt.ogg"

    announcement "Уважаемые пассажиры, мы готовимся к взлету." with dissolve

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("stopAllMusic()")
            $ emscripten.run_script("play_ambience_kazakhstan_airplane_before_takeoff_ambience()")

    $ last_playing_music = "play_ambience_kazakhstan_after_takeoff_ambience"

    announcement "Пожалуйста, пристегните ремни, приведите спинки кресел в вертикальное положение," with dissolve

    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("play_ambience_takeoff_kazakhstan()")
            $ emscripten.run_script("play_ambience_kazakhstan_after_takeoff_ambience(39.960-2.0)")
    else:
        play music "ambience/takeoff_kazakhstan.ogg"

        queue music "ambience/kazakhstan_after_takeoff_ambience.ogg"

    announcement "уберите откидные столики и откройте шторки на иллюминаторах." with dissolve

    show airplane_day_kz at airplane_scene_pos:
        ypos 0.525
        zoom 1.15
        linear 2.0 zoom 1.075
        linear 0.2 xpos 0.501 ypos 0.526
        linear 0.2 xpos 0.499 ypos 0.524
        linear 0.2 xpos 0.501 ypos 0.524
        linear 0.2 xpos 0.499 ypos 0.526
        linear 0.2 xpos 0.499 ypos 0.524
        linear 0.2 xpos 0.501 ypos 0.526
        linear 0.2 xpos 0.499 ypos 0.524
        linear 0.2 xpos 0.501 ypos 0.526
        linear 0.2 xpos 0.501 ypos 0.526
        linear 0.2 xpos 0.499 ypos 0.524
        linear 0.2 xpos 0.501 ypos 0.524
        linear 0.2 xpos 0.499 ypos 0.526
        linear 0.2 xpos 0.499 ypos 0.524
        linear 0.2 xpos 0.501 ypos 0.526
        linear 0.2 xpos 0.499 ypos 0.524
        linear 0.2 xpos 0.501 ypos 0.526

        linear 0.2 xpos 0.501 ypos 0.526
        linear 0.2 xpos 0.499 ypos 0.524
        linear 0.2 xpos 0.501 ypos 0.524
        linear 0.2 xpos 0.499 ypos 0.526
        linear 0.2 xpos 0.499 ypos 0.524
        linear 0.2 xpos 0.501 ypos 0.526
        linear 0.2 xpos 0.499 ypos 0.524
        linear 0.2 xpos 0.501 ypos 0.526
        linear 0.2 xpos 0.5 ypos 0.525
        linear 3.0 ypos 0.475
        linear 0.2 xpos 0.501 ypos 0.476
        linear 0.2 xpos 0.499 ypos 0.474
        linear 0.2 xpos 0.501 ypos 0.474
        linear 0.2 xpos 0.499 ypos 0.476
        linear 0.2 xpos 0.499 ypos 0.474
        linear 0.2 xpos 0.501 ypos 0.476
        linear 0.2 xpos 0.499 ypos 0.474
        linear 0.2 xpos 0.501 ypos 0.476
        linear 0.2 xpos 0.5 ypos 0.475

    "Раздался рев двигателей, я почувствовал, как меня вдавило в кресло. Самолет разогнался и начал взлет." with dissolve

    "Я почувствовал, как все мое тело расслабилось, позволяя силе инерции удерживать меня в кресле." with dissolve

    "Наконец, самолет оторвался от земли." with dissolve

    "Я почувствовал сильное облегчение, видя через окно как далеко позади остается земля, дома, дороги." with dissolve

    "Словно бы все мои страхи тоже остались только там, внизу." with dissolve

    "А впереди было только чистое небо, полное надежд." with dissolve

    "Второй побег прошел успешно." with dissolve

    "Здесь в небе нас уже никто не достанет." with dissolve

    "Алия повернулась ко мне." with dissolve

    aliya "Я хочу послушать музыку, но мой телефон остался там внизу." with dissolve

    me "Я записал себе на телефон ту песню которую ты мне дала послушать. Хочешь я включу ее?" with dissolve

    aliya "Давай." with dissolve

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("stopAllMusic()")
            $ emscripten.run_script("play_ambience_kazakhstan_after_takeoff_ambience()")

    $ last_playing_music = "play_ambience_kazakhstan_after_takeoff_ambience, playRunaway07"

    "Я включил музыку и отдал один наушник Алие." with dissolve

    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("playRunaway07()")
    else:
        play music_crossfade "music/Runaway_07 (Main_Theme).ogg" # fadein 1.0
        queue music_crossfade "music/Runaway_07 (Main_Theme_Loop).ogg"

    "В наушниках заиграли знакомые мотивы." with dissolve

    scene black with dissolve

    $ savegame_picture = "savegame_black"

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("stopAllMusic()")
            $ emscripten.run_script("play_ambience_kazakhstan_after_takeoff_ambience()")
            $ emscripten.run_script("playRunaway07()")

    $ last_playing_music = "playRunaway07"

    "Я откинулся на кресло и закрыл глаза." with dissolve

    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("stopAllMusicExceptRunaway07AndAirplane2Landed()")
    else:
        stop music # fadeout 5.0

    "Это только начало большого пути." with dissolve

    "Впереди нас ждут удивительные приключения." with dissolve

    "Но это уже совсем другая история..." with dissolve

    jump credits
