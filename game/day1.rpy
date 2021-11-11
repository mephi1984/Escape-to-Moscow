
label day1_intro:

    # Will stop predicting them at the end of day 2
    #$ renpy.start_predict("images/cg_screen/*.*")
    #$ renpy.start_predict("images/CG_messenger_desktop/*.*")
    #$ renpy.start_predict("images/semen_room*.*")
    #$ renpy.start_predict("images/CG_hands/Card.png")


    $ last_playing_music = "playRunaway01()"

    if renpy.emscripten:

        $ import emscripten
        $ emscripten.run_script("playRunaway01()")

    else:
        play music "music/Runaway_01 (Main).ogg" # fadein 2.0

        queue music "music/Runaway_01 (Loop).ogg"

    scene black

    $ renpy.pause(0.2)

    show text Text(_("Все персонажи и произошедшие в игре события вымышлены."), size=int(36*SCALE)) as credits_text10_line1 at credits_text10_line1_pos zorder 10 with dissolve

    $ renpy.pause(2)

    show text Text(_("Любые совпадения с реальными личностями и событиями случайны."), size=int(36*SCALE)) as credits_text10_line2 at credits_text10_line2_pos zorder 10 with dissolve

    $ renpy.pause(2)

    show text Text(_("Сюжет игры был создан под впечатлением от событий, описанных в СМИ и в блогах."), size=int(36*SCALE)) as credits_text10_line3 at credits_text10_line3_pos zorder 10 with dissolve

    $ renpy.pause(4)

    scene black with dissolve

    scene semen_room_night with dissolve

    $ savegame_picture = "savegame_semen_room_night"

    "За окном густая ночь." with dissolve

    "Все приличные люди давно уже спят в этот час." with dissolve

    "А я до сих пор ещё не лёг." with dissolve

    "Меня тянет в сон, но какая-то неведомая сила заставляет продолжать смотреть в дисплей ноутбука." with dissolve

    "Словно бы я таким образом могу задержать наступление следующего дня." with dissolve

    "Конечно, я понимаю - следующий день настанет в любом случае." with dissolve

    "Но мой мозг будто говорит: \"Не хочу идти в завтра! Давай останемся в сегодня ещё хоть на пять минуточек?\"" with dissolve

    "Как бы мне хотелось остановить время, задержать наступление завтрашнего дня." with dissolve

    "Хотя бы ненадолго получить возможность ничего не делать." with dissolve

    "Вырваться из бесконечного бега по кругу, который называется жизнь." with dissolve

    "Да, кстати, я фрилансер. Я работаю в ИТ-индустрии." with dissolve

    "Иронично. Когда-то для меня фриланс выглядел как спасение из вечной суеты жизни." with dissolve

    "Типичный образ фрилансера - с ноутбуком на пляже, работает, когда хочет." with dissolve

    "Конечно же, когда я стал фрилансером, то понял - всё совсем не так." with dissolve

    "Нужно покупать еду, платить за интернет, за съемную квартиру, за то, за это." with dissolve

    "А чтобы платить за всё это, нужно зарабатывать деньги. Постоянно." with dissolve

    "Стоит только остановиться, отдохнуть - всё, бюджет не сходится. Приходится переходить на доширак." with dissolve

    "Такое ощущение, будто я тону вниз. Постоянно тону." with dissolve

    "И чтобы не утонуть, мне нужно постоянно толкать себя вверх." with dissolve

    "Остановиться страшно, остановишься - утонешь." with dissolve

    "Но у меня уже нет сил плыть." with dissolve

    "Поэтому я сейчас здесь. Сижу в своей комнате перед дисплеем ноутбука и смотрю тупые видео в интернете." with dissolve

    show black with dissolve

    $ renpy.pause(1.0)

    jump day1_coach_pre_meeting


label day1_coach_pre_meeting:

    scene semen_room_table_night

    $ savegame_picture = "savegame_semen_room_table_night"

    show black zorder 20

    show semen_room_table_night_foreground_phone zorder 1

    show semen_room_table_night_foreground_card zorder 2

    show cg_screen_youtube

    hide black with dissolve

    "Впрочем, нельзя сказать, что я совсем никак не пытаюсь исправить своё положение." with dissolve

    "То с чем я столкнулся, называется профессиональным выгоранием." with dissolve

    "Я гуглил об этом, читал статьи на разных сайтах." with dissolve

    "Там предлагают разные способы борьбы с ним." with dissolve

    "Я перепробовал уже всё, кажется. Ничего не помогает." with dissolve

    "Судя по всему, мне нужно в отпуск." with dissolve

    "Но, как я уже сказал, я никак не могу накопить денег, чтобы отдохнуть от работы пару недель." with dissolve

    "Возможно, мне стоит сходить к психологу?" with dissolve

    "Нет! Я конечно устаю, но я же не псих." with dissolve

    "Мне просто нужно немного отдохнуть и разобраться в себе..." with dissolve

    "Такие мысли крутились у меня в голове в последнее время." with dissolve

    "И как специально - несколько дней назад мне попалась на глаза реклама: эксклюзивная акция от банка." with dissolve

    "При оформлении кредитной карты, я получаю сертификат на участие в клубе психологической взаимопомощи \"Зона понимания\"." with dissolve

    "Как было написано в рекламе, это клуб людей, которые совместно участвуют в социально-психологических играх." with dissolve

    "Участники клуба обсуждают свои проблемы в парах и группах, а также выполняют задания, самостоятельно или совместно." with dissolve

    "Кажется, участие в клубе помогает повысить продуктивность, победить прокрастинацию, установить какие-то цели в жизни." with dissolve

    "Вообще, я думаю, все эти клубы предназначены главным образом для зарабатывания денег на участниках." with dissolve

    "Однако в данном случае я получаю сертификат на участие бесплатно." with dissolve

    "Если оформлю кредитную карту, конечно же." with dissolve

    "Это заинтересовало меня. Кредитной карты у меня ещё ни разу не было, но от лишних денег я бы сейчас не отказался." with dissolve

    "С кредитной картой мне не нужно будет судорожно браться за первый попавшийся заказ, чтобы срочно заработать денег." with dissolve

    "Я смогу позволить себе немного расслабиться." with dissolve

    "А психологическая помощь в дополнение к карте - вообще отлично!" with dissolve

    "Так что я записался, встретился с курьером, подписал документы, получил банковскую карту." with dissolve

    hide semen_room_table_night_foreground_card with dissolve

    show semen_room_table_night_foreground_card_hands zorder 2 with dissolve

    "Вот моя новая кредитная карта." with dissolve

    hide semen_room_table_night_foreground_card_hands with dissolve

    show semen_room_table_night_foreground_card zorder 2 with dissolve

    "Меня записали в клуб и познакомили с его программой." with dissolve

    "Мне был назначен человек из моего города, с которым я должен буду познакомиться." with dissolve

    "Это более опытный участник клуба, который должен будет помочь мне разобраться в себе." with dissolve

    "Я ещё не знаю кто это." with dissolve

    "Мне говорили, что он мне напишет сегодня." with dissolve

    "Никто мне так и не написал, но я все еще жду." with dissolve

    "Для меня это еще один повод не ложиться спать." with dissolve

    show black zorder 20 with dissolve

    "Прошло некоторое время..." with dissolve

    jump day1_coach_meeting_alt



label day1_coach_meeting_alt:

    hide black with dissolve

    show semen_room_table_night_foreground_phone_day1_coach as semen_room_table_night_foreground_phone zorder 1 with dissolve

    show cg_screen_new_message_coach

    messenger "Новое сообщение"  with dissolve

    hide cg_screen_new_message_coach

    show semen_room_table_night_foreground_phone as semen_room_table_night_foreground_phone zorder 1 with dissolve

    $ changeDialogToCoach()

    $ showMessengerWithRightOrder()

    $ addReceivedMessage(2)

    coach "Приветствую! Вы Семён, да?" with dissolve

    $ addSentMessage(1)

    me "Привет, да!" with dissolve

    $ addReceivedMessage(4)

    coach "Отлично! Я буду вашим напарником в клубе." with dissolve

    $ addSentMessage(3)

    me "Можно на \"ты\"?" with dissolve

    $ addReceivedMessage(0)

    coach "Конечно))" with dissolve

    $ addReceivedMessage(4)

    coach "Моя задача - помочь тебе в определении твоих целей." with dissolve

    $ addReceivedMessage(5)

    coach "Также я отвечаю на твои вопросы и могу дать советы по их достижению." with dissolve

    $ addSentMessage(3)

    me "Спасибо, но я пока ещё не придумал себе цели." with dissolve

    $ addReceivedMessage(4)

    coach "Всё в порядке. Сначала расставь приоритеты в своей жизни." with dissolve

    $ addReceivedMessage(4)

    coach "Карьера, здоровье, любовь, учёба - всё что угодно." with dissolve

    $ addReceivedMessage(5)

    coach "Я помогу тебе разобраться в том, что тебе действительно важно и вместе мы назначим цели для тебя." with dissolve

    $ addSentMessage(3)

    me "Я могу тебе писать в любое время?" with dissolve

    $ addReceivedMessage(5)

    coach ":D Я не смогу постоянно быть онлайн, но ты пиши мне в любое время. Я отвечу, когда будет возможность." with dissolve

    $ addSentMessage(0)

    me "Хорошо." with dissolve

    $ addSentMessage(2)

    me "Сейчас у меня вопросов нет." with dissolve

    $ addSentMessage(4)

    me "Но спасибо за поддержку. Я напишу тебе, когда мне потребуется помощь или совет." with dissolve

    $ addReceivedMessage(4)

    coach "Окей! Если тебя что-то беспокоит - пиши! Я буду онлайн." with dissolve

    show black zorder 20 with dissolve

    hide cg_screen_messenger_window
    hide cg_screen_messenger_window_top

    $ changeDialogToMinjun()

    #$ renpy.force_autosave(take_screenshot=False, block=True)

    "И я снова погрузился в прокрастинацию..." with dissolve

    jump day1_aliya_meeting



label day1_aliya_meeting:

    hide black with dissolve



    "...Прошло ещё немного времени бесцельного блуждания по интернету." with dissolve

    show semen_room_table_night_foreground_phone_day1_pak as semen_room_table_night_foreground_phone zorder 1 with dissolve

    show cg_screen_new_message_minjun

    if renpy.emscripten:
        $ import emscripten
        if renpy.in_rollback():
            $ emscripten.run_script("stopAllMusic()")
            $ emscripten.run_script("playRunaway01()")

    $ last_playing_music = "playRunaway02()"

    messenger "Новое сообщение"  with dissolve # with hpunch

    #$ switchToSong()

    show semen_room_table_night_foreground_phone as semen_room_table_night_foreground_phone zorder 1 with dissolve

    hide cg_screen_new_message_minjun

    $ showMessengerWithRightOrder()

    $ addReceivedMessage(2)

    if renpy.emscripten:
        $ import emscripten
        if not renpy.in_rollback():
            $ emscripten.run_script("playRunaway02()")

    minjun "Привет, Семён! Ты не занят сейчас?" with dissolve

    "Это же Мин Чжун Пак, мой знакомый кореец из Сеула." with dissolve

    "Он учит русский язык и иногда пишет мне с вопросами." with dissolve

    $ addSentMessage(2)

    me "Нет, я не занят. Что случилось?" with dissolve

    $ addReceivedMessage(2)

    minjun "Есть одно дело, в общем." with dissolve

    $ addReceivedMessage(4)

    minjun "Я установил приложение для языкового обмена и там познакомился с девушкой из России." with dissolve

    $ addReceivedMessage(4)

    minjun "Она не говорит по-английски, она знает только русский язык." with dissolve

    $ addReceivedMessage(3)

    minjun "Ты не подумай, я не хочу найти себе подружку из России." with dissolve

    $ addReceivedMessage(5)

    minjun "Просто она хочет уехать жить в Корею, а ты единственный мой русский друг." with dissolve

    $ addReceivedMessage(4)

    minjun "Ты можешь помочь? Расскажи ей как можно попасть в Корею для русских." with dissolve

    $ addSentMessage(1)

    me "Да без проблем." with dissolve

    $ addReceivedMessage(3)

    minjun "Отлично! Тогда я дам ей твои контакты?" with dissolve

    $ addSentMessage(0)

    me "Конечно." with dissolve

    $ addReceivedMessage(0)

    minjun "Окей!" with dissolve

    "Ну что же, теперь у меня есть законный повод не спать ещё некоторое время." with dissolve

    show cg_screen_you_were_added_aliya

    messenger "Вас добавили: Миса Амане"

    hide cg_screen_you_were_added_aliya

    hide cg_screen_messenger_window
    hide cg_screen_messenger_window_top

    $ changeDialogToAliya()

    $ showMessengerWithRightOrder()

    $ addSentMessage(0)

    me "Привет!" with dissolve

    $ addReceivedMessage(1)

    aliya_mobile "Привет, Семён!" with dissolve

    $ addSentMessage(4)

    me "Пак мне сказал, что ты хочешь уехать в Корею. Правильно?" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Да. Но я не знаю корейский." with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "И английский тоже." with dissolve

    "Да, типичный случай. Я знаю много таких фанаток Кореи." with dissolve

    $ addSentMessage(4)

    me "Тогда лучше всего - немного выучи английский язык и езжай учиться в Корею." with dissolve

    $ addSentMessage(4)

    me "Выучишь корейский язык, получишь диплом, потом будешь там работать." with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Если я сменю свои документы, проблемы какие-нибудь возникнут?" with dissolve

    $ addSentMessage(1)

    me "Какие документы?" with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Паспорт, полис, СНИЛС и т.д." with dissolve

    "Зачем менять документы? Она что, была в Корее нелегалом?" with dissolve

    $ addSentMessage(4)

    me "При въезде в Корею проверяют отпечатки пальцев." with dissolve

    $ addSentMessage(5)

    me "Даже если ты сменишь документы, тебя вычислят по совпадению отпечатков." with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Я не была в Корее ни разу." with dissolve

    "А вот теперь я запутался." with dissolve

    $ addSentMessage(5)

    me "Тогда зачем менять документы? Можешь сделать загранпаспорт и просто приехать." with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Чтобы меня не нашли." with dissolve

    $ addSentMessage(1)

    me "Кто нашёл?" with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Родители." with dissolve

    "Ничего себе расклады." with dissolve

    $ addSentMessage(3)

    me "А тебе сколько лет?" with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "18." with dissolve

    $ addSentMessage(3)

    me "Тебе нужно сбежать в другую страну от родителей?" with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Да." with dissolve

    $ addSentMessage(5)

    me "Тебе нужно сбежать именно в Корею или любая страна подойдёт?" with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Любая страна подойдёт, но, раз уж я решаюсь на такой шаг, почему бы не в страну, которую давно хочу посетить?" with dissolve

    $ addSentMessage(4)

    me "В Корее дорогая жизнь и работу найти сложно." with dissolve

    $ addSentMessage(5)

    me "Сейчас там много русских работает нелегально на стройках или на рыбных заводах." with dissolve

    $ addSentMessage(5)

    me "Также есть риск, что тебя пригласят работать в Go-Go барах или в KTV, а это довольно неприятная работа." with dissolve

    $ addSentMessage(4)

    me "Ты далеко от Кореи живёшь? В каком ты городе?" with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Пятигорск." with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Это город Ставропольского края." with dissolve

    "Ставропольский край. Северо-Кавказский федеральный округ. Неужели..." with dissolve

    $ addSentMessage(1)

    me "Ты русская?" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Я не русская, но хорошо знаю русский." with dissolve

    "Стало понятнее. Не русская девушка хочет сбежать от родителей в Корею." with dissolve

    "Уже из ошибок в ее сообщениях понятно, что русский язык для нее не родной." with dissolve

    "Ну ладно, я не буду придираться к ее грамотности." with dissolve

    $ addSentMessage(3)

    me "А загранпаспорт у тебя есть?" with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Нет, но собираюсь сделать." with dissolve

    $ addSentMessage(3)

    me "Не понимаю тогда, зачем тебе в Корею?" with dissolve

    $ addSentMessage(4)

    me "Можно, например, уехать работать в Москву, в Питер." with dissolve

    $ addSentMessage(4)

    me "Или в любой другой большой город, там затеряться легко." with dissolve

    $ addSentMessage(4)

    me "Там можно работать без прописки и снимать квартиру с друзьями." with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Нет, в Москве полно моих родственников." with dissolve

    $ addSentMessage(3)

    me "Как они о тебе узнают?" with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Родители ведь будут меня искать и они наверняка им сообщат, ну мало ли." with dissolve

    $ addSentMessage(5)

    me "Если ты живешь без регистрации и не указываешь свой адрес нигде, то вычислить тебя нереально." with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Хм..." with dissolve

    $ addSentMessage(5)

    me "Просто если ты сразу уедешь в другую страну без денег, без языка - можешь легко попасть в неприятности." with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Тоже мысль верная." with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Но я думала, если и совершать преступление, то по-крупному." with dissolve

    $ addSentMessage(5)

    me "Сбежать из дома не преступление. Тебе 18, можешь делать что хочешь." with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Понимаешь, ситуация более запутанная и сложная, чем кажется на первый взгляд." with dissolve

    $ addSentMessage(0)

    me "Расскажи." with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Я из Дагестана, а по нашим обычаям и традициям, сбежать из дома, да ещё и перед своей свадьбой, это большое преступление!" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Если меня поймают, прощать никто не станет." with dissolve

    $ addSentMessage(4)

    me "Тебя хотят выдать замуж, а ты этого не хочешь?" with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Эх, долгая история." with dissolve

    $ addSentMessage(1)

    me "Я понимаю." with dissolve

    "Кажется, диалог остановился." with dissolve

    "Что же делать?" with dissolve

    jump day1_aliya_advice1_question


label day1_aliya_advice1_question:

    menu:

        "Что же делать?"

        "Посоветоваться с Напарником." if day1_advice_asked == False:
            jump day1_ask_coach

        "Посочувствовать ей.":
            jump day1_aliya_sympathize

        "Предложить помощь." if (day1_advice_asked == False) and (day1_first_help_offered == False):
            jump day1_aliya_offer

        "\"Извини, мне это не интересно\"":
            jump day1_aliya_decline

label day1_aliya_sympathize:

    "Наверное, наилучший вариант — показать ей, что я понимаю её проблемы." with dissolve

    $ addSentMessage(2)

    me "Я понимаю твою ситуацию." with dissolve

    $ addSentMessage(5)

    me "Ты росла в дагестанской семье и вокруг тебя были люди с соответствующим менталитетом." with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Ага." with dissolve

    $ addSentMessage(5)

    me "Они тебе говорят:\"Всё! Если сбежишь - ты преступница, тебе позор и всё такое\"." with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Да! Это ужасно." with dissolve

    $ addSentMessage(4)

    me "Они тебе много раз говорили такое, поэтому ты запомнила." with dissolve

    $ addReceivedMessage(1)

    aliya_mobile "Всю жизнь." with dissolve

    $ addSentMessage(5)

    me "Но на самом деле, твои родители не всесильные. Их главное оружие - твой страх." with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Мой папа бывший следователь, у него очень-очень много знакомых работающих в этой сфере." with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Они меня найдут." with dissolve

    $ addSentMessage(3)

    me "Ну это мы ещё посмотрим." with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Знаешь, на деле проверять не хочется..." with dissolve

    $ addSentMessage(4)

    me "Возможно, если ты сбежишь, они просто от тебя откажутся?" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Разве это не самое худшее наказание?" with dissolve

    $ addSentMessage(5)

    me "Но ведь тогда они тебя и искать не будут. Как будто ты пропала, исчезла." with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Вообще, я думала подстроить свою смерть и со спокойной душой сбежать." with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "они бы 100\% меня искать не стали и им бы не пришлось врать, а я жила бы своей жизнью." with dissolve

    $ addSentMessage(5)

    me "Если твои родители от тебя откажутся, будет очень печально." with dissolve

    $ addSentMessage(5)

    me "Но если выйдешь замуж против своей воли, твоя жизнь будет намного печальнее." with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Да, я знаю." with dissolve

    $ addSentMessage(4)

    me "Я слышал, на кавказе мужья часто бьют жен." with dissolve

    $ addSentMessage(4)

    me "Конечно, если ты имеешь братьев, они тебя защитят." with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Этот человек не плохой." with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Да и брат у меня есть, но он младше того, за кого меня выдают." with dissolve

    "Кажется, мне удалось разговорить её." with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "В общем, дело в том, что меня родители хотят выдать замуж." with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Ему 32, он хороший, состоятельный и прочее... минус только в возрасте и в том, что у него есть дети от бывшей жены." with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "А я не хочу замуж, я просто не хочу, он мне вообще никак не нравится." with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Все, вообще все хотят, чтобы мы поженились." with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "А я хочу после колледжа не замуж выйти, а дальше пойти учиться." with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Но проблема в том, что у родителей нет возможности, в этом году брат поступает на вышку, а денег нет..." with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "На моё обучение тоже нет, поэтому они хотят так сделать." with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Вот вся история вкратце." with dissolve

    $ addSentMessage(5)

    me "Если нет денег на обучение, можно получить грант и учиться бесплатно." with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Они не хотят, чтобы я дальше училась." with dissolve

    $ addSentMessage(5)

    me "А есть причина, почему отец хочет выдать тебя замуж именно за этого человека? Может другого жениха найти?" with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Он богат: есть дом, машина, хороший человек, религиозный. В общем мечта." with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Из других возможных женихов только мой кузен, бывший одноклассник и друг брата." with dissolve

    $ addSentMessage(4)

    me "Звучит как будто твои родители продают тебя." with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Да." with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Я замуж тупо не хочу, они это знают, но упускать такую возможность не хотят." with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Ты же знаешь, что в Дагестане нет такого понятия \"любовь\" и по любви свадьбы не играют у нас." with dissolve

    $ addSentMessage(2)

    me "Да уж, сложная ситуация." with dissolve

    jump day1_aliya_advice2_question


label day1_aliya_advice2_question:

    menu:

        "Что посоветовать?"

        "Предложить помощь.":
            jump day1_aliya_offer_help #day1_aliya_offer_go_to_moscow

        "\"А как насчет того, чтобы сымитировать похищение?\"" if day1_kidnap_imitate_offered == False:
            jump day1_aliya_offer_steal

        "\"Предложи своему жениху отказаться от свадьбы.\"" if day1_cancel_wedding_offered == False:
            jump day1_aliya_offer_postpone_wedding

        "\"Извини, мне это не интересно.\"":
            jump day1_aliya_decline



label day1_aliya_offer_steal:

    $ day1_kidnap_imitate_offered = True

    $ addSentMessage(5)

    me "Я слышал, если парень и девушка сильно любят друг друга, они могут договориться о похищении." with dissolve

    $ addSentMessage(4)

    me "Тогда родителям придётся согласиться на их свадьбу." with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Это то да, но я никого не люблю... поэтому этот вариант тоже отпадает." with dissolve

    jump day1_aliya_advice2_question




label day1_aliya_offer_postpone_wedding:

    $ day1_cancel_wedding_offered = True

    $ addSentMessage(5)

    me "Ты можешь написать своему жениху и попросить его отказаться от свадьбы?" with dissolve

    $ addSentMessage(4)

    me "Может быть, он скажет твоему отцу что он передумал?" with dissolve

    $ addSentMessage(5)

    me "Это даст тебе немного времени. Может быть, отец потом другого жениха найдет." with dissolve

    $ addSentMessage(5)

    me "Но пока он ищет другого жениха, ты будешь свободна и можешь готовиться - учить английский язык, например." with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Плохая идея, это позор на всю жизнь, меня потом замуж точно никто не возьмёт." with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "А родители знаешь, лучше не знать что сделают со мной..." with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Все, абсолютно все уже знают о предстоящей свадьбе." with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "И как, по-твоему, будет выглядеть то, что он отказывается на мне жениться?" with dissolve

    jump day1_aliya_advice2_question



label day1_aliya_offer_help:

    $ addSentMessage(4)

    me "Да, это сложная ситуация, где нужно выбирать решение." with dissolve

    $ addSentMessage(5)

    me "Если ты уйдешь от родителей, то по сути начнёшь самостоятельную жизнь." with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Я никогда не жила отдельно от родителей." with dissolve

    $ addSentMessage(5)

    me "Я могу примерно описать твою жизнь, если родители откажутся от тебя." with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "И какой же она будет?" with dissolve

    $ addSentMessage(5)

    me "Сначала будет одиноко. Станет лучше, если ты поступишь в университет и заселишься в общежитие." with dissolve

    $ addSentMessage(5)

    me "Там у тебя появятся новые друзья и знакомые, которых ты раньше не знала. Но также появятся и проблемы с деньгами." with dissolve

    $ addSentMessage(5)

    me "Нужно будет следить за своими расходами, покупать продукты питания," with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "найти работу." with dissolve

    $ addSentMessage(5)

    me "Тебе нужно будет самостоятельно решать возникающие проблемы. Как будто у тебя над головой висит туча, постоянно." with dissolve

    $ addSentMessage(5)

    me "Нужно сходить в банк открыть карту, сделать курсовую, записаться на курсы, купить методичку." with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Я в меде учусь. Думаю, с учёбой проблем не так уж много будет." with dissolve

    $ addSentMessage(3)

    me "Ты умеешь ездить на велосипеде?" with dissolve

    $ addReceivedMessage(1)

    aliya_mobile "Да, немного." with dissolve

    $ addSentMessage(3)

    me "Жизнь похожа на езду на велосипеде." with dissolve

    $ addSentMessage(3)

    me "Чтобы не упасть, нужно постоянно двигаться вперёд." with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Да." with dissolve

    $ addSentMessage(3)

    me "Вот такая у тебя будет жизнь. Понимаешь?" with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Понимаю." with dissolve

    $ addSentMessage(5)

    me "Я думаю, что ты смелая девушка. В любом случае, ты должна жить своей жизнью, а не так как сказали родители." with dissolve

    $ addReceivedMessage(1)

    aliya_mobile "Смелая, говоришь?" with dissolve

    $ addSentMessage(0)

    me "Да." with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Знаешь как мне сейчас тяжело и страшно об этом даже думать?" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Я ведь понимаю, что назад пути уже не будет." with dissolve

    $ addSentMessage(1)

    me "Да, догадываюсь." with dissolve

    $ addSentMessage(5)

    me "Я попробую тебе помочь." with dissolve

    $ addReceivedMessage(1)

    aliya_mobile "Чем помочь?" with dissolve

    $ addSentMessage(4)

    me "Разобраться с тем куда ехать, найти авиабилеты, загранпаспорт, визу если потребуется." with dissolve

    $ addSentMessage(4)

    me "Затем найти жильё, работу, подать документы в универ и т.д." with dissolve

    $ addReceivedMessage(1)

    aliya_mobile "Спасибо большое." with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Но для начала нужно поменять паспорт и документы, по которым меня могут найти." with dissolve

    $ addSentMessage(3)

    me "Может прямо в Москве поменять паспорт?" with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Нет." with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "До Москвы ещё добраться нужно, меня на посту могут остановить и сообщить родителям." with dissolve

    $ addSentMessage(3)

    me "Не остановят, если уедешь неожиданно." with dissolve

    $ addSentMessage(4)

    me "Просто в Пятигорске у твоего отца много связей." with dissolve

    $ addSentMessage(3)

    me "Он узнает если ты будешь паспорт менять." with dissolve

    $ addSentMessage(4)

    me "А допустим в Москве, кому какое дело до следователя из Пятигорска?" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Он следователь в отставке из Дагестана." with dissolve

    $ addSentMessage(0)

    me "Хмм, ладно." with dissolve

    $ addSentMessage(5)

    me "Решение принимать тебе. Если ты решишь остаться, это твоё дело. А если ты решишь сбежать, я постараюсь чем-нибудь помочь." with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "В общем, у меня есть время до лета, чтоб денег поднакопить и принять окончательное решение." with dissolve

    $ addSentMessage(1)

    me "Когда свадьба?" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Летом. Но точной даты ещё нет." with dissolve

    $ addSentMessage(2)

    me "А где ты учишься?" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "В Пятигорском мед колледже." with dissolve

    $ addSentMessage(3)

    me "Когда выпускаешься?" with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "В следующем году." with dissolve

    $ addSentMessage(5)

    me "Может перевестись в другой город учиться? Или ты будешь бросать учёбу?" with dissolve

    $ addReceivedMessage(1)

    aliya_mobile "Наверное брошу." with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Тогда и документы нужны, чтоб в другое место поступить." with dissolve

    $ addSentMessage(4)

    me "Да, из колледжа нужно забрать аттестат." with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Кстати, номер тоже менять надо будет." with dissolve

    $ addSentMessage(3)

    me "Номер легко поменять." with dissolve

    $ addSentMessage(4)

    me "Можешь взять с собой друга и оформить на его паспорт." with dissolve

    $ addSentMessage(3)

    me "Тогда точно не найдут." with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Хм, а это идея." with dissolve

    show black zorder 20 with dissolve


    $ renpy.pause(1.0)

    jump day1_aliya_meeting_after_success



label day1_aliya_meeting_after_success:

    hide black zorder 10 with dissolve

    show semen_room_table_night_foreground_phone zorder 1

    show semen_room_table_night_foreground_card zorder 2

    $ addReceivedMessage(4)

    aliya_mobile "Ладно, уже поздно, мне пора спать." with dissolve

    $ addSentMessage(0)

    me "Ладно." with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Я напишу тебе потом!" with dissolve

    $ addSentMessage(0)

    me "Конечно!" with dissolve

    $ addSentMessage(3)

    me "Кстати, забыл спросить. Как тебя зовут?" with dissolve

    $ addReceivedMessage(0)

    aliya_mobile ":)" with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Алия." with dissolve

    $ addSentMessage(3)

    me "Окей. Спокойной ночи, Алия!" with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Спокойной ночи, Семён!" with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    jump day1_over_success

label day1_over_success:


    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("stopAllMusic()")
            $ emscripten.run_script("playRunaway02()")

    $ last_playing_music = "playRunaway01()"

    "Что же, время действительно позднее." with dissolve

    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("playRunaway01()")
    else:
        play music "music/Runaway_01 (Main).ogg" # fadein 2.0

        queue music "music/Runaway_01 (Loop).ogg"

    scene semen_room_night with dissolve

    $ savegame_picture = "savegame_semen_room_night"

    "Утомлённый разговором, я лёг спать." with dissolve

    "В голове крутились разные мысли." with dissolve

    "Все мои проблемы казались теперь незначительными." with dissolve

    "У меня хотя бы есть какая-никакая работа, доходы, съёмная квартира." with dissolve

    "А тут девочке 18 лет и её родители выдают замуж." with dissolve

    "И ей настолько страшен и противен этот человек, что она готова сбежать из дома." with dissolve

    "Даже странно представить, что подобное всё ещё происходит где-то в России." with dissolve

    "И я вызвался ей помочь." with dissolve

    "Возможно, ей и не понадобится моя помощь. До лета ещё далеко, может проблема будет решена как-то по-другому." with dissolve

    "Может быть, Алия передумает сбегать или придумает какой-нибудь другой план." with dissolve

    "Кажется, впереди достаточно времени, чтобы придумать какое-нибудь решение этой проблемы." with dissolve

    "А теперь пора спать." with dissolve

    scene black with dissolve

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("stopAllMusic()")
            $ emscripten.run_script("playRunaway01()")


    $ last_playing_music = "playRunaway08()"

    "С этими мыслями я погрузился в сон..." with dissolve

    jump day2_intro


label day1_ask_coach:

    $ day1_advice_asked = True

    hide cg_screen_messenger_window
    hide cg_screen_messenger_window_top

    $ changeDialogToCoach()

    $ showMessengerWithRightOrder()

    "Я открыл диалог с Напарником и начал строчить." with dissolve

    $ addSentMessage(2)

    me "Привет, мне нужен твой совет." with dissolve

    $ addReceivedMessage(1)

    coach "Привет, слушаю)" with dissolve

    $ addSentMessage(4)

    me "У меня тут есть сложный случай. Я познакомился с девушкой в интернете." with dissolve

    $ addReceivedMessage(1)

    coach "Хорошее начало)" with dissolve

    $ addSentMessage(3)

    me "Она мне рассказывает о своих проблемах." with dissolve

    $ addSentMessage(4)

    me "Я бы хотел понять, как мне строить с ней диалог." with dissolve

    $ addReceivedMessage(0)

    coach "Хмм..." with dissolve

    $ addReceivedMessage(3)

    coach "Пришли мне переписку, я почитаю." with dissolve

    $ addSentMessageHistory()

    "Я скопировал переписку и отправил Напарнику." with dissolve

    $ addReceivedMessage(0)

    coach "Хмм..." with dissolve

    $ addReceivedMessage(3)

    coach "Ужасная ситуация, конечно. Надеюсь, она найдёт решение." with dissolve

    $ addSentMessage(2)

    me "Возможно, я смогу ей чем-то помочь?" with dissolve

    $ addReceivedMessage(3)

    coach "Я думаю, эта девушка очень недоверчивая и скрытная." with dissolve

    $ addReceivedMessage(4)

    coach "Если ты серьезно хочешь ей помочь, тебе нужно войти в доверие." with dissolve

    $ addReceivedMessage(4)

    coach "Сначала тебе стоит войти в её положение, показать, что ты её понимаешь." with dissolve

    $ addReceivedMessage(5)

    coach "И только потом, когда будешь с ней на одной волне, ты уже можешь что-то предлагать." with dissolve

    $ addReceivedMessage(4)

    coach "Если ты сходу предложишь ей помощь, она заподозрит неладное и просто откажется." with dissolve

    $ addSentMessage(1)

    me "Так... ладно." with dissolve

    $ coach_exposition_return_step = 0

    jump dagestan_exposition

label day1_ask_coach_after_exposition:

    $ addSentMessage(2)

    me "Окей. Спасибо за помощь." with dissolve

    $ addReceivedMessage(2)

    coach "^^ Удачи тебе!" with dissolve

    hide cg_screen_messenger_window
    hide cg_screen_messenger_window_top

    $ changeDialogToAliya()

    $ showMessengerWithRightOrder()

    "Я переключился обратно на диалог с моей новой знакомой. Итак, что теперь делать?" with dissolve

    jump day1_aliya_advice1_question


label day1_aliya_offer:

    $ day1_first_help_offered = True

    $ addSentMessage(2)

    me "Хочешь я помогу тебе?" with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Как?" with dissolve

    $ addSentMessage(3)

    me "Я куплю тебе билеты, помогу сбежать в Москву или куда захочешь." with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Спасибо, не надо." with dissolve

    $ addSentMessage(0)

    me "Почему?" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Ты меня не знаешь, я тебя не знаю." with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Не стоит." with dissolve

    "Кажется, диалог не клеится. Что же делать?" with dissolve

    jump day1_aliya_advice1_question





label day1_aliya_decline:

    $ addSentMessage(3)

    me "Извини, мне это не интересно." with dissolve

    $ addSentMessage(5)

    me "Я конечно поддерживаю тебя, но у меня сейчас и своих проблем по горло." with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Поняла." with dissolve

    $ addSentMessage(3)

    me "Желаю тебе удачи и всё такое." with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Спасибо." with dissolve

    "Наступило молчание" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "В таком случае прости, что побеспокоила." with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Я пожалуй пойду." with dissolve

    $ aliya_banned = True

    $ showMessengerWithRightOrder()

    "Пока я думал, что ответить - аватарка Миса Амане пропала." with dissolve

    $ clearMessagesAfterBan()

    "Вслед за аватаркой пропали все сообщения." with dissolve


    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("stopAllMusic()")
            $ emscripten.run_script("playRunaway02()")

    $ last_playing_music = "playRunaway01()"

    "\"Миса Амане - был(а) в сети давно\"." with dissolve

    #if isMobileWeb:
    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("playRunaway01()")
    else:
        play music "music/Runaway_01 (Main).ogg" # fadein 2.0

        queue music "music/Runaway_01 (Loop).ogg"

    "Кажется, она добавила меня в чёрный список." with dissolve

    "Да уж." with dissolve

    "Жалко её, конечно, но я действительно не могу ничем помочь." with dissolve

    "Максимум, что я мог бы сделать - дать телефоны и адреса каких-нибудь женских правозащитных организаций." with dissolve

    "Но у меня среди знакомых нет никого с кем я бы мог посоветоваться." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    scene semen_room_night with dissolve

    $ savegame_picture = "savegame_semen_room_night"

    "Она отправила меня в ЧС, поэтому сейчас я уже ничем не могу помочь ей." with dissolve

    "Ладно пожалуй пойду спать." with dissolve

    "Мне же ещё нужно завтра заставить себя работать." with dissolve

    "Нужно очистить свои мысли от ненужных беспокойств..." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    return

    #"THE END, спасибо что поиграли! Концовка 1 - \"Первый день, Семён слился\"" with dissolve
