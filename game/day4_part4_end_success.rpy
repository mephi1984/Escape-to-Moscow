label day4_end_success:

    scene black with dissolve

    "И вот наконец мы в самолете..." with dissolve

    show black zorder 10

    play music "ambience/kazakhstan_airplane_before_takeoff_ambience.ogg" fadein 1.0

    show airplane_day_side as airplane_scene

    show airplane_window_landing11 as airplane_window

    hide black with dissolve

    show aliya_sit_side no_emotion_layer special_airplane_window as Aliya at any_center_pos:
        zoom SCALE

    "Как только мы сели на свои места, бортпроводники объявили о завершении посадки." with dissolve

    "Я немного отдышался, затем посмотрел на Алию." with dissolve

    me "Спасибо, что доверяешь мне." with dissolve

    show aliya_sit_side no_earphones eyes_open_sad_worried_open_mouth as Aliya at any_center_pos:
        zoom SCALE

    aliya "Куда мы летим?" with dissolve

    show aliya_sit_side no_earphones eyes_open_neutral as Aliya at any_center_pos:
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

    show aliya_sit_side no_emotion_layer special_airplane_window as Aliya at any_center_pos:
        zoom SCALE

    aliya "Поняла..." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    show airplane_day_kz at airplane_scene_pos with dissolve:
        ypos 0.525
        xpos 0.5
        zoom 1.15

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

    play sound "sound/seatbelt.ogg"

    announcement "Уважаемые пассажиры, мы готовимся к взлету." with dissolve

    announcement "Пожалуйста, пристегните ремни, приведите спинки кресел в горизонтальное положение, уберите откидные столики и откройте шторки на иллюминаторах." with dissolve

    play music "ambience/takeoff_kazakhstan.ogg"

    queue music "ambience/kazakhstan_after_takeoff_ambience.ogg"

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

    "Я включил музыку и отдал один наушник Алие." with dissolve

    play music_crossfade "music/Runaway_07 (Main_Theme).ogg" fadein 1.0
    queue music_crossfade "music/Runaway_07 (Main_Theme_Loop).ogg"

    "В наушниках заиграли знакомые мотивы." with dissolve

    scene black with dissolve

    "Я откинулся на кресло и закрыл глаза." with dissolve

    stop music fadeout 5.0

    "Это только начало большого пути." with dissolve

    "Впереди нас ждут удивительные приключения." with dissolve

    "Но это уже совсем другая история..." with dissolve

    jump credits
