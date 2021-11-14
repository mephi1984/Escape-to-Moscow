
label day4_intro:

    scene black with dissolve

    $ savegame_picture = "savegame_black"

    "Вокруг была темнота." with dissolve

    if isMobileWeb:
        show perlin_mobile_web as perlin with dissolve
    else:
        show perlin at credits_perlin_pos zorder 2 with dissolve:
            xpos 0.0
            linear 120.0 xpos -2.0

    "И не просто темнота, а словно густой туман." with dissolve

    "Я всматривался в туман, пытаясь что-то увидеть." with dissolve

    "Перед моими глазами плыли странные образы, силуэты, тени." with dissolve

    if not isMobileWeb:
        show perlin as perlin2 at credits_perlin_pos zorder 4 with dissolve:
            xpos -1.0
            linear 80.0 xpos -2.0

    show Aliya_stand_straight eyes_open_cry_sad2 as Aliya at any_center_pos zorder 1 with dissolve:
        zoom 1.0

    "И вот наконец мои глаза смогли сфокусироваться на одном знакомом образе." with dissolve

    show Aliya_stand_straight eyes_open_cry_sad2 as Aliya at any_center_pos zorder 3 with dissolve:
        zoom 1.0

    aliya "Ты жалеешь, что помог мне?" with dissolve

    me "С чего такой неожиданный вопрос?" with dissolve

    aliya "Не знаю. Ты просто какой-то мрачный. Наверное, сожалеешь, что вызвался помогать незнакомой девушке." with dissolve

    me "Нет, я даже рад." with dissolve

    show Aliya_stand_straight eyes_open_sad_worried_open_mouth as Aliya at any_center_pos zorder 3 with dissolve:
        zoom 1.0

    aliya "Рад?" with dissolve

    me "Да, на самом деле за последние пару дней я очень оживленно провел время." with dissolve

    aliya "И ты не беспокоишься, о том, что будет завтра?" with dissolve

    me "Хотел бы я сказать, что нет, но... Конечно же я волнуюсь. Даже очень." with dissolve

    aliya "Тогда, почему?" with dissolve

    me "Почему, что?" with dissolve

    aliya "Почему поехал со мной? Почему не остался там возле дома?" with dissolve

    me "Я бы не смог." with dissolve

    show Aliya_stand_straight eyes_closed_sad as Aliya at any_center_pos zorder 3 with dissolve:
        zoom 1.0

    "Алия ничего не ответила." with dissolve

    show Aliya_stand_straight eyes_closed_sad as Aliya at any_center_pos zorder 1 with dissolve:
        zoom 1.0

    "Ее фигура снова начала пропадать в тумане." with dissolve

    me "Постой! Подожди!" with dissolve

    hide Aliya with dissolve

    "Она исчезла." with dissolve

    "Я протянул руки вперед, но там было уже пусто." with dissolve

    if not isMobileWeb:
        hide perlin2 with dissolve

    "Меня снова окружил бесконечный туман." with dissolve

    hide perlin with dissolve

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("music_stage_preload = \"music_Runaway03_Runaway12\"")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracks(stopAllMusic, playRunaway03)")

    $ last_playing_music = "playRunaway12"



    "И бесконечная пустота..." with dissolve

    $ renpy.pause(1.0)

    scene imran_house_bedroom with dissolve

    $ savegame_picture = "savegame_imran_house_bedroom"

    $ music_stage_preload = "music_Runaway12_Runaway13"

    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("playRunaway12()")
            $ emscripten.run_script("music_stage_preload = \"music_Runaway12_Runaway13\"")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracksAsync()")
    else:
        play music "music/Runaway_12 (Loop).ogg" # fadein 3.0

        queue music "music/Runaway_12 (Loop).ogg"

    "Я проснулся ранним утром." with dissolve

    "И сразу вспомнил, где я и что я тут делаю." with dissolve

    #show cg_screen_phone_time_day4_morning_imran_home as cg_screen_phone with dissolve
    show right_hand phone_day day4_morning1 as cg_screen_phone with dissolve

    "Сон как рукой сняло. Я достал телефон и посмотрел на часы." with dissolve

    "8:47 утра. Судя по тишине в доме, родители еще не приехали, а Имран и Алия спят." with dissolve

    $ changeDialogToAliya()

    $ showMessengerPhone(is_night=False, force_no_transition=True)

    "Я открыл мессенджер и решил написать Алие." with dissolve

    $ addSentMessage(1)

    me "Привет, спишь?" with dissolve

    "Вчера Алия была очень неразговорчивая." with dissolve

    "Это было немного странно, но я думаю, она просто очень устала." with dissolve

    $ clearDisplayMessages()

    $ hidePhone()

    "Внезапно раздался тихий стук в дверь." with dissolve

    scene imran_house_doorway with dissolve

    $ savegame_picture = "savegame_imran_house_doorway"

    show Aliya_stand_straight tshirt eyes_open_neutral as Aliya at aliya_imran_room_pos with dissolve:
        zoom 1.0

    "Я подошел и открыл дверь. За дверью стояла Алия." with dissolve

    "Она выглядела еще серьезнее, чем в момент нашей встречи в аэропорту Минеральные Воды." with dissolve

    aliya "Мой отец прочитал нашу переписку в мессенджере." with dissolve

    me "В смысле, он взломал твой аккаунт?" with dissolve

    aliya "Да, похоже на то." with dissolve

    aliya "Поэтому не пиши мне больше." with dissolve

    "Ох черт. Я попробовал вспомнить, что такого важного я успел написать в мессенджере." with dissolve

    "Ну ладно, мессенджер скомпрометирован, уже ничего не поделаешь. Минус один способ связи." with dissolve

    me "Тогда я удалю то последнее сообщение, и больше не буду тебе писать." with dissolve

    "Всю переписку целиком уже поздно удалять, так мы только спалимся." with dissolve

    show Aliya_stand_straight tshirt eyes_open_neutral as Aliya at aliya_imran_room_pos with dissolve:
        zoom 1.0

    aliya "И много не говори, Имран может нас подслушивать." with dissolve

    aliya "Родители приедут примерно в 11 часов утра." with dissolve

    "Кажется, самое время поговорить о плане повторного побега." with dissolve

    me "Да, насчет этого, я хочу поговорить." with dissolve

    me "Твоя мама обманула меня, и я бы хотел ей это напомнить..." with dissolve

    show Aliya_stand_straight tshirt eyes_open_sad_worried as Aliya at aliya_imran_room_pos with dissolve:
        zoom 1.0

    aliya "Давай лучше не в этот раз. Прибереги это на будущее." with dissolve

    me "Хорошо, как скажешь. Я к тому, что если потребуется, то мы соврём твоим родителям, и чтоб тебя не мучала совесть." with dissolve

    aliya "Это хорошо, но я надеюсь это не понадобится." with dissolve

    me "Ты больше не хочешь сбегать?" with dissolve

    aliya "Давай сначала поговорим с моими родителями." with dissolve

    me "Ты хочешь с ними договориться?" with dissolve

    me "Они обманули меня вот только что, вчера." with dissolve

    me "Ты и сама рассказывала, как несколько лет назад твой отец не выполнил свое обещание перед тобой." with dissolve

    show Aliya_stand_straight tshirt eyes_closed_neutral as Aliya at aliya_imran_room_pos with dissolve:
        zoom 1.0

    "Алия вздохнула." with dissolve

    aliya "Я знаю..." with dissolve

    "Пока я думал, что еще сказать, внизу раздался шорох." with dissolve

    show Aliya_stand_straight tshirt eyes_open_sad_worried_question as Aliya at aliya_imran_room_pos with dissolve:
        zoom 1.0

    "Алия посмотрела на меня в последний раз." with dissolve

    hide Aliya with dissolve

    "Затем быстро ушла в свою комнату." with dissolve

    "Я стоял в дверном проеме, и слышал, как внизу на первом этаже ходил Имран." with dissolve

    scene imran_house_bedroom with dissolve

    $ savegame_picture = "savegame_imran_house_bedroom"

    "Я закрыл дверь и вернулся в комнату." with dissolve

    "Теперь перед мной и Алией встала еще и проблема связи." with dissolve

    "Если говорить голосом, то нас может подслушивать Имран." with dissolve

    "А если писать сообщения в мессенджере, то сообщения могут прочитать родители Алии." with dissolve

    "Как черт возьми они взломали мессенджер? Допускаю что у отца Алии есть друзья в ФСБ." with dissolve

    "Но ведь мессенджер начали блокировать как раз, потому что не могли его взломать." with dissolve

    "Мой внутренний параноик убеждает меня, что теперь весь телефон Алии сейчас скомпрометирован." with dissolve

    "Странно, почему родители Алии до сих пор не узнали мой номер телефона и не позвонили." with dissolve

    "Хотя с другой стороны, Алия тоже не знает мой номер телефона. И я ее старый номер тоже не знаю." with dissolve

    "Как-то так получилось, что мы все время общаемся через мессенджер..." with dissolve

    scene black with dissolve

    "Прошло еще немного времени..." with dissolve

    scene imran_house_bedroom with dissolve

    messenger "Новое сообщение" with dissolve # with hpunch

    #show cg_screen_phone_new_message_day4_morning_imran_home as cg_screen_phone with dissolve
    show right_hand phone_day day4_morning2 as cg_screen_phone with dissolve

    "Я отвлекся от мыслей и достал телефон." with dissolve

    $ changeDialogToCoach()

    $ showMessengerPhone(is_night=False, force_no_transition=True)

    $ addReceivedMessage(1)

    coach "Привет! Не спишь?" with dissolve

    $ addSentMessage(1)

    me "Нет, я уже проснулся" with dissolve

    $ addReceivedMessage(3)

    coach "Отлично! Насчет побега, у меня есть идея" with dissolve

    $ addReceivedMessage(5)

    coach "Я думаю, что если Алия сбежит с поезда или с автобуса, родители могут ее легко догнать и остановить" with dissolve

    $ addReceivedMessage(3)

    coach "Поэтому я думаю, нужно сбежать через аэропорт" with dissolve

    $ addReceivedMessage(5)

    coach "У меня есть план. Он немного безумный и запутанный, но все же кажется мне наиболее надежным" with dissolve

    $ addSentMessage(1)

    me "Рассказывай" with dissolve

    $ addReceivedMessage(5)

    coach "Для выполнения плана нужно чтобы Алия возвращалась домой на самолете, через аэропорт Домодедово" with dissolve

    $ addReceivedMessage(5)

    coach "Это обязательное условие. Ну и естественно, нужно чтобы Алия была готова сбежать снова" with dissolve

    $ addSentMessage(3)

    me "Интересно. А в чем суть плана?" with dissolve

    $ addReceivedMessage(3)

    coach "Ты часто бываешь в аэропорту Домодедово?" with dissolve

    $ addSentMessage(4)

    me "Вчера я там побывал дважды. Но вообще, редко, да" with dissolve

    $ addReceivedMessage(4)

    coach "Я часто вылетаю оттуда, и знаю этот аэропорт очень хорошо" with dissolve

    $ addReceivedMessage(4)

    coach "Совсем недавно там завершили реновацию в терминале" with dissolve

    $ addReceivedMessage(3)

    coach "В частности, в зоне вылета" with dissolve

    $ addReceivedMessage(5)

    coach "Раньше пассажиры международных рейсов сначала проходили границу, а затем досмотр. Теперь наоборот" with dissolve

    $ addReceivedMessage(5)

    coach "Зона досмотра теперь общая для пассажиров внутренних и международных рейсов" with dissolve

    $ addSentMessage(1)

    me "Зона досмотра?" with dissolve

    $ addReceivedMessage(5)

    coach "Там ты снимаешь верхнюю одежду, обувь, проходишь через рамки металлодетекторов, пропускаешь багаж через рентген" with dissolve

    $ addSentMessage(2)

    me "Да, помню такое" with dissolve

    $ addReceivedMessage(5)

    coach "В Домодедово, после того как ты прошел досмотр, ты утыкаешься в панорамное окно, в котором видно летное поле" with dissolve

    $ addReceivedMessage(5)

    coach "Оттуда можно уже выбирать куда пойти - на внутренние рейсы или на международные" with dissolve

    $ addReceivedMessage(5)

    coach "Если пойти в международный терминал, то там у тебя снова проверят паспорт, посадочный талон" with dissolve

    $ addReceivedMessage(4)

    coach "И дальше нужно будет переходить границу, таможню и т.д." with dissolve

    $ addReceivedMessage(3)

    coach "Уже понимаешь к чему я клоню?" with dissolve

    $ addSentMessage(4)

    me "Не понимаю. Причем тут международные рейсы?" with dissolve

    $ addReceivedMessage(5)

    coach "Если Алия попадет в зону международных рейсов, ее родители туда уже не могут проникнуть!" with dissolve

    $ addSentMessage(5)

    me "А как Алия попадет в зону международных рейсов? Для этого нужно иметь посадочный талон в другую страну!" with dissolve

    $ addReceivedMessage(4)

    coach "Ты купишь ей и себе билеты, и зарегистрируешь на рейс" with dissolve

    $ addSentMessage(4)

    me "Купить билеты на международный рейс? Ты предлагаешь нам бежать заграницу?" with dissolve

    $ addReceivedMessage(0)

    coach "Да!" with dissolve

    $ addSentMessage(4)

    me "Но куда Алия может улететь? У нее нет загранпаспорта" with dissolve

    $ addReceivedMessage(5)

    coach "По Российскому паспорту можно улететь в Казахстан, Беларусь, Киргизию и Армению" with dissolve

    $ addReceivedMessage(5)

    coach "В расписании аэропорта Домодедово есть рейсы в Алматы, Бишкек, Ош, которые вылетают примерно в то же время что и рейсы в Махачкалу и Минеральные Воды" with dissolve

    $ addReceivedMessage(4)

    coach "Узнай, каким рейсом родители Алии увозят ее домой" with dissolve

    $ addReceivedMessage(5)

    coach "У тебя есть ее паспортные данные. Купи себе и ей билеты например в Алматы" with dissolve

    "Ох, плакала моя кредитная карта!" with dissolve

    $ addReceivedMessage(3)

    coach "В нужный момент передай ей посадочный талон" with dissolve

    $ addReceivedMessage(4)

    coach "Переходите границу в аэропорту Домодедово, и вы в безопасности" with dissolve

    $ addReceivedMessage(4)

    coach "Ее родителей туда не пустят, так как у них нет посадочного талона на международный рейс" with dissolve

    $ addReceivedMessage(5)

    coach "А пока ее отец будет поднимать все свои связи в спецслужбах, вы уже успеете улететь" with dissolve

    $ addSentMessage(5)

    me "... Честно, это один из самых сложных планов побега, который я когда либо слышал!" with dissolve

    $ addReceivedMessage(0)

    coach "Спасибо))" with dissolve

    $ addSentMessage(5)

    me "Итак, первый шаг - я должен предупредить Алию что у меня есть план побега за границу. Да?" with dissolve

    $ addReceivedMessage(4)

    coach "Да. Убедись, что она точно готова последовать за тобой" with dissolve

    $ addSentMessage(5)

    me "Второй шаг. Я должен убедить родителей Алии, чтобы они улетали именно через аэропорт Домодедово" with dissolve

    $ addReceivedMessage(5)

    coach "Да. Как угодно, но сделай это. Предложи им, типа ты поможешь заказать билеты по интернету, например. Ты же айтишник" with dissolve

    $ addSentMessage(3)

    me "Ясно. Я думаю, я это легко сделаю" with dissolve

    $ addSentMessage(5)

    me "Затем я должен буду купить билеты на международный рейс в Казахстан или в Киргизию, который вылетает примерно в то же время" with dissolve

    $ addReceivedMessage(4)

    coach "Да. Лучше будет даже, чтобы рейс вылетал немного пораньше" with dissolve

    $ addReceivedMessage(4)

    coach "Чтобы после перехода границы вы сразу могли сесть на самолет" with dissolve

    $ addSentMessage(5)

    me "Затем я должен буду приехать в аэропорт, распечатать посадочный талон для Алии, и незаметно передать ей" with dissolve

    $ addSentMessage(4)

    me "Как мне это сделать, чтобы меня не запалили? Родители же будут всюду с ней" with dissolve

    $ addReceivedMessage(5)

    coach "Если у тебя есть знакомые девушки в Москве, которым ты можешь доверять, попроси чтобы кто-то из них передал билеты Алие" with dissolve

    $ addSentMessage(1)

    me "Именно девушки?" with dissolve

    $ addReceivedMessage(5)

    coach "Да. Чтобы передать в женском туалете. Или можно там же в туалете сделать закладку с билетом" with dissolve

    $ addSentMessage(4)

    me "К сожалению, у меня нет друзей-девушек в Москве" with dissolve

    "Тем более таких, которым я мог бы довериться." with dissolve

    $ addReceivedMessage(0)

    coach "Ладно..." with dissolve

    $ addReceivedMessage(5)

    coach "Смотри. Ты знаешь, как пройти в туалет в аэропорту Домодедово, в \"грязной\" зоне, до регистрации на рейс?" with dissolve

    $ addSentMessage(2)

    me "Нет, я не помню" with dissolve

    $ addReceivedMessage(4)

    coach "Посмотришь по карте потом. Там туалет единственный. И находится он где-то в подвале" with dissolve

    $ addReceivedMessage(4)

    coach "Чтобы туда пройти, нужно спуститься по лестнице. Лестница довольно узкая" with dissolve

    $ addReceivedMessage(4)

    coach "Когда лестница заканчивается, там будет узкий проход к туалетам" with dissolve

    $ addReceivedMessage(5)

    coach "В назначенное время ты встаешь с краю и держишь в руках посадочный талон Алии" with dissolve

    $ addReceivedMessage(2)

    coach "Она попросится в туалет" with dissolve

    $ addReceivedMessage(5)

    coach "Когда она будет проходить мимо тебя, она быстро и незаметно забирает посадочный талон из твоих рук" with dissolve

    $ addSentMessage(3)

    me "Комбинация прямо как в шпионских фильмах" with dissolve

    $ addSentMessage(2)

    me "Другого способа нет?" with dissolve

    $ addReceivedMessage(5)

    coach "Не знаю. Кажется, туалеты в Домодедово наиболее удобны чтобы незаметно что-то передать" with dissolve

    $ addReceivedMessage(4)

    coach "Там очень узкий проход, и там всегда много людей" with dissolve

    $ addReceivedMessage(5)

    coach "В любом другом месте аэропорта, если Алия что-то попытается получить от незнакомца или подобрать, родители это заметят" with dissolve

    $ addSentMessage(1)

    me "Ладно, согласен" with dissolve

    $ addSentMessage(5)

    me "Итак, допустим я передал посадочный талон Алие. Что нужно делать дальше?" with dissolve

    $ addReceivedMessage(4)

    coach "Ты проходи через рамки досмотра первый, и жди Алию" with dissolve

    $ addReceivedMessage(5)

    coach "В центре зала находится эскалатор и лифт. Ты их узнаешь, рядом с ними стоит указатель \"Рейсы в Армению, Беларусь, Казахстан, Киргизию\"" with dissolve

    $ addReceivedMessage(3)

    coach "Тебе нужно будет ждать там Алию" with dissolve

    $ addSentMessage(1)

    me "А что будет делать Алия?" with dissolve

    $ addReceivedMessage(5)

    coach "Алия должна пройти через досмотр. Я думаю, она пойдет туда вместе с родителями" with dissolve

    $ addReceivedMessage(5)

    coach "Она не должна выпускать паспорт и посадочный талон из рук" with dissolve

    $ addReceivedMessage(5)

    coach "При проходе через досмотр, Алия должна сложить все остальные вещи в корзину и отправить на ленту" with dissolve

    $ addReceivedMessage(5)

    coach "Это телефон, ключи, монеты, ремень и т.д. Кроме паспорта и посадочного талона" with dissolve

    $ addReceivedMessage(5)

    coach "Затем Алия должна пройти через металлодетектор. Она должна пройти через него самой первой, раньше родителей" with dissolve

    $ addReceivedMessage(5)

    coach "Паспорт и посадочный талон при этом нужно держать в руках. Не нужно их класть в корзину! Выпускать из рук вообще нельзя" with dissolve

    $ addSentMessage(0)

    me "Я запомню это" with dissolve

    $ addReceivedMessage(5)

    coach "После того как Алия пройдет рамки металлоискателей, она должна немедленно БЕЖАТЬ" with dissolve

    $ addReceivedMessage(5)

    coach "Просто бросить все и резко кабанчиком рвануть в сторону эскалатора и лифта" with dissolve

    $ addReceivedMessage(5)

    coach "Ей конечно же придется оставить все вещи прямо там, в зоне досмотра. Я имею в виду сумку, телефон, ключи, и т. д." with dissolve

    $ addReceivedMessage(5)

    coach "Она должна бежать налегке, только с паспортом и посадочным талоном в руках" with dissolve

    $ addReceivedMessage(5)

    coach "Пока родители будут проходить через рамки, Алия успеет добежать до тебя. Примерно там же ты ее встретишь" with dissolve

    $ addReceivedMessage(4)

    coach "Вы вдвоем должны будете бежать по эскалатору вниз" with dissolve

    $ addReceivedMessage(5)

    coach "Внизу вас встретят турникеты. Нужно приложить посадочный талон к сканеру, и вас пропустят к международным рейсам" with dissolve

    $ addReceivedMessage(5)

    coach "Затем нужно пройти таможенный контроль. Проходите через зеленый коридор, после него будет выход к погранпереходу" with dissolve

    $ addReceivedMessage(4)

    coach "Там можете немного расслабиться, ее родителей туда уже не пустят" with dissolve

    $ addReceivedMessage(5)

    coach "Но я все равно рекомендую вам побыстрее пройти границу и выйти в чистую зону" with dissolve

    $ addReceivedMessage(5)

    coach "Если на границе будет очередь, то найди офицера, который ходит по залу" with dissolve

    $ addReceivedMessage(5)

    coach "Скажи ему что вы опаздываете на рейс, и попросите вас пропустить без очереди" with dissolve

    $ addReceivedMessage(4)

    coach "Естественно, пусти вперед Алию, а затем уже переходи границу сам" with dissolve

    $ addSentMessage(5)

    me "Ага, ясно. Дальше мы находим наш выход на посадку, садимся в самолет и улетаем в Казахстан" with dissolve

    $ addReceivedMessage(2)

    coach "Да, именно так" with dissolve

    $ addSentMessage(5)

    me "Есть один вопрос. А зачем заранее передавать Алие посадочный талон, если мы все равно будем переходить границу вместе?" with dissolve

    $ addReceivedMessage(2)

    coach "Ах да, точно" with dissolve

    $ addReceivedMessage(2)

    coach "Это важный момент" with dissolve

    $ addReceivedMessage(5)

    coach "При входе в зону досмотра сотрудники аэропорта смотрят посадочный талон и ставят на него печать" with dissolve

    $ addReceivedMessage(4)

    coach "Потом эту печать смотрят пограничники на погранпереходе" with dissolve

    $ addReceivedMessage(4)

    coach "Если им дать посадочный талон без печати, у них будут вопросы" with dissolve

    $ addReceivedMessage(5)

    coach "Когда-нибудь в Домодедово сделают полностью электронную регистрацию на зарубежные рейсы. Но пока что вот так" with dissolve

    $ addSentMessage(0)

    me "Понятно" with dissolve

    $ addSentMessage(4)

    me "Хорошо. План довольно сложный, как я уже сказал" with dissolve

    $ addReceivedMessage(4)

    coach "Это самое надежное, что получилось придумать" with dissolve

    $ addReceivedMessage(5)

    coach "Если бы Алия сбежала с поезда или с автобуса, родители бы догнали ее рано или поздно" with dissolve

    $ addReceivedMessage(4)

    coach "А тут погранпереход в аэропорту, они не смогут туда так просто попасть" with dissolve

    $ addReceivedMessage(5)

    coach "Аэропорт Домодедово в этом плане удобен тем, что проход через рамки задержит их, и даст время Алие убежать к границе" with dissolve

    $ addSentMessage(5)

    me "Не будет ли вызывать подозрение быстро бегущий человек в аэропорту?" with dissolve

    $ addReceivedMessage(5)

    coach "Это же аэропорт))) Тут многие опаздывают на свой рейс и бегут с чемоданами через весь терминал" with dissolve

    $ addSentMessage(2)

    me "А, ну да, точно" with dissolve

    $ addReceivedMessage(3)

    coach "Вот такой у меня план))) Теперь все зависит от тебя" with dissolve

    $ addSentMessage(1)

    me "Спасибо большое" with dissolve

    $ addReceivedMessage(2)

    coach "Удачи! Напиши мне когда будете в Казахстане!" with dissolve

    $ addSentMessage(2)

    me "Очень оптимистично! Конечно я напишу" with dissolve

    $ clearDisplayMessages()

    $ hidePhone()

    "Я убрал телефон и задумался." with dissolve

    "План, придуманный Напарником, довольно неплох." with dissolve

    "Однако мне предстоит донести его до Алии." with dissolve

    "Написать ей в мессенджере или в СМС я не могу, так как родители могут прочитать сообщения и узнать весь план." with dissolve

    "Обсудить голосом с ней этот план я тоже не могу. Если я буду сейчас что-то с ней обсуждать, я привлеку внимание Имрана." with dissolve

    "Что же делать? Как незаметно и подробно рассказать ей о плане и о том, что она должна сделать?.." with dissolve

    "Я осмотрел комнату." with dissolve

    "Кровать, окно, телевизор, какие-то картины, комод возле двери." with dissolve

    scene imran_house_bedroom_open_closet with dissolve

    "Я открыл комод. Там лежали какие-то провода, отвертки, детали от жалюзи, болты, и..." with dissolve

    "Ручка! Обычная синяя шариковая ручка." with dissolve

    "Я поковырялся в карманах и достал несколько чековых лент из магазинов." with dissolve

    "У меня есть привычка брать чеки в магазине вместе с сдачей." with dissolve

    "Я расписал ручку на одном из чеков - да, она пишет." with dissolve

    "Отлично, проблема решена. Я просто напишу записку Алие и незаметно от родителей передам ей." with dissolve

    "Чековая лента не очень длинная, поэтому мне нужно подумать, как уместить весь план на ней." with dissolve

    #show cg_screen_phone_food_notes_empty as cg_screen_phone with dissolve
    show right_hand phone_day notes1 as cg_screen_phone with dissolve

    "Почесав затылок, я достал телефон и начал в заметках составлять текст записки." with dissolve

    #show cg_screen_phone_food_notes_fill as cg_screen_phone with dissolve
    show right_hand phone_day notes2 as cg_screen_phone with dissolve

    "Я по-быстрому написал записку. Это было легко, хмм..." with dissolve

    "Но слишком длинно. Теперь нужно выкинуть ненужное, и готовый текст написать на чековой ленте." with dissolve

    scene black with dissolve

    "И я начал думать над текстом..." with dissolve

    jump day4_parents_intro



label day4_parents_intro:

    scene imran_house_bedroom with dissolve

    "Мне казалось, это заняло целую вечность." with dissolve

    "Я наконец-таки закончил писать." with dissolve

    "Как же я давно не брал в руки ручку. У меня аж рука заболела от письма." with dissolve

    #show cg_screen_phone_new_message_day4_morning_after_note_imran_home as cg_screen_phone with dissolve
    show right_hand phone_day day4_morning3 as cg_screen_phone with dissolve

    "Я проверил телефон. Время уже приближалось к 11-ти часам." with dissolve

    $ hidePhone()

    "Когда родители приедут, я и Алия спустимся вниз. По пути я передам ей записку." with dissolve

    "Дальше предстоит разговор с родителями. Нужно будет вести себя естественно." with dissolve

    "В который раз ловлю себя на мысли - я даже не знаю как обычный человек может вести себя \"естественно\" в такой ситуации." with dissolve

    "Как бы то ни было, диалог будет очень сложный." with dissolve

    "Если я слишком буду поддерживать Алию и защищать ее перед родителями, ее родители не будут мне доверять." with dissolve

    "И тогда не получится уговорить их купить билеты с вылетом из Домодедово." with dissolve

    "Если я быстро встану на сторону родителей, Алия может решить, что я ее предал." with dissolve

    "Она может не догадаться, что я блефую. Обидится на меня, выкинет записку и улетит с родителями." with dissolve

    "И я не смогу во время разговора связаться с Напарником, естественно. Мне предстоит самостоятельно решить, что говорить и как говорить." with dissolve

    "...Я и не заметил, сколько времени провел в раздумьях." with dissolve

    "Тем временем, из окна послышался звук приближающегося автомобиля." with dissolve

    "Я посмотрел в окно и увидел такси, которое подъезжало к воротам дома Имрана." with dissolve

    "Затем я услышал, как Имран вышел из дома встречать родителей Алии." with dissolve

    scene black with dissolve

    "Я открыл дверь и вышел из комнаты." with dissolve

    scene imran_house_2nd_floor with dissolve

    $ savegame_picture = "savegame_imran_house_2nd_floor"

    "Рядом с моей комнатой была комната Алии. Я постучал в дверь." with dissolve

    "Я услышал, как Алия встала с кровати и начала собираться." with dissolve

    scene imran_house_2nd_floor_open_door with dissolve

    show Aliya_stand_straight tshirt eyes_open_sad_worried as Aliya at any_center_pos with dissolve:
        zoom 1.0

    "Спустя несколько минут дверь открылась, и она вышла из комнаты." with dissolve

    me "Твои родители приехали." with dissolve

    aliya "Да." with dissolve

    show Aliya special_note as Aliya at any_center_pos with dissolve:
        zoom 1.0

    "Я передал ей записку." with dissolve

    aliya "Что это?" with dissolve

    me "На случай если решишь сбежать, новый план побега записан там." with dissolve

    aliya "Ясно." with dissolve

    show Aliya special_pocket as Aliya at any_center_pos with dissolve:
        zoom 1.0

    "Алия положила записку в карман." with dissolve

    show Aliya_stand_straight tshirt eyes_open_neutral as Aliya at any_center_pos with dissolve:
        zoom 1.0

    "Я услышал, как дверь на первом этаже открылась, и родители вошли в дом." with dissolve

    "У меня очень мало времени." with dissolve

    me "Запомни пожалуйста. Чтобы я сейчас не сказал твоим родителям - на самом деле я всегда на твоей стороне." with dissolve

    show Aliya_stand_straight tshirt eyes_open_sad_worried_open_mouth as Aliya at any_center_pos with dissolve:
        zoom 1.0

    "Алия посмотрела на меня недоверчиво и непонимающе." with dissolve

    me "Возможно я буду блефовать и лгать твоим родителям, но это только чтобы вытащить тебя." with dissolve

    show Aliya_stand_straight tshirt eyes_open_neutral as Aliya at any_center_pos with dissolve:
        zoom 1.0

    aliya "Это не нужно," with dissolve

    aliya "Нам пора идти вниз." with dissolve

    if renpy.emscripten:
        if renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("music_stage_preload = \"music_Runaway12_Runaway13\"")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracks(stopAllMusic, playRunaway12)")

    $ last_playing_music = "playRunaway13"

    me "Хорошо, пошли." with dissolve

    $ music_stage_preload = "music_Runaway13_Runaway14"

    if renpy.emscripten:
        if not renpy.in_rollback():
            $ import emscripten
            $ emscripten.run_script("playRunaway13()")
            $ emscripten.run_script("music_stage_preload = \"music_Runaway13_Runaway14\"")
            $ emscripten.run_script("clearAllMusicExceptPreload()")
            $ emscripten.run_script("PreloadRequiredTracksAsync()")
    else:

        play music "music/Runaway_13 (Loop).ogg" # fadein 3.0

        queue music "music/Runaway_13 (Loop).ogg"

    scene black with dissolve

    "Мы спустились по лестнице вниз на первый этаж." with dissolve

    "Алия вошла в гостиную, и за ней вошел я." with dissolve

    scene imran_house_living_room with dissolve

    $ savegame_picture = "savegame_imran_house_living_room"

    show imran neutral at imran_house_pos1 with dissolve:
        zoom 1.0

    "В гостиной был Имран, которого я уже видел." with dissolve

    show Aliya_stand_straight tshirt eyes_open_sad_worried as Aliya at imran_house_pos2 with dissolve:
        zoom 1.0*0.9

    "Рядом была Алия." with dissolve

    show aslan neutral at imran_house_pos3 with dissolve:
        zoom 1.0

    "С другой стороны находился лысоватый и гладко выбритый пожилой мужчина. Его лицо было невероятно уставшим." with dissolve

    show fatima neutral at imran_house_pos4 with dissolve:
        zoom 1.0

    "Кроме него в гостиной на диване сидела женщина лет сорока, в платье и платке. Лицо ее выражало тревогу." with dissolve

    "Мы разместились в гостиной, и приготовились к разговору..." with dissolve

    scene black with dissolve

    $ renpy.pause(1.0)

    scene imran_house_living_room with dissolve

    show imran watching at imran_house_pos1:
        zoom 1.0
        alpha 0.0
        linear 0.5 alpha 1.0
        alpha 1.0

    show Aliya_stand_straight tshirt eyes_open_sad_worried as Aliya at imran_house_pos2:
        zoom 1.0*0.9
        alpha 0.0
        linear 0.5 alpha 1.0
        alpha 1.0

    show aslan watching_aliya at imran_house_pos3:
        zoom 1.0
        alpha 0.0
        linear 0.5 alpha 1.0
        alpha 1.0

    show fatima neutral at imran_house_pos4:
        zoom 1.0
        alpha 0.0
        linear 0.5 alpha 1.0
        alpha 1.0

    "Аслан вздохнул и начал говорить." with dissolve

    show aslan watching_aliya_open_mouth at imran_house_pos3 with dissolve:
        zoom 1.0
        alpha 1.0

    aslan "Алия, дочь моя, я твой отец." with dissolve

    aslan "Я растил тебя и заботился о тебе, а ты мне как отвечаешь?" with dissolve

    aslan "Ты как ребенок поступила, убежала из дома вот так." with dissolve

    aslan "Ты своих родителей позоришь, меня позоришь, мать свою позоришь." with dissolve

    aslan "Из-за тебя мы поставили на уши всю полицию Пятигорска." with dissolve

    aslan "Я вообще сначала подумал что тебя в Сирию увезли, на войну." with dissolve

    aslan "Мне плохо стало, маме твоей плохо стало." with dissolve

    aslan "Ты зачем так поступила? Ты зачем своих родителей не ценишь, не уважаешь?" with dissolve

    show aslan watching_aliya at imran_house_pos3 with dissolve:
        zoom 1.0
        alpha 1.0

    show Aliya_stand_straight tshirt eyes_open_angry as Aliya at imran_house_pos2 with dissolve:
        zoom 1.0*0.9
        alpha 1.0

    "Алия набралась смелости, строго посмотрела на отца и начала говорить." with dissolve

    show Aliya_stand_straight tshirt eyes_open_angry_open_mouth as Aliya at imran_house_pos2 with dissolve:
        zoom 1.0*0.9
        alpha 1.0

    aliya "Мам, пап, я действительно не хочу выходить замуж." with dissolve

    aliya "Я вам говорила много раз. Вы никогда не спрашиваете меня чего я хочу. Вам вообще безразлично." with dissolve

    show Aliya_stand_straight tshirt eyes_open_angry as Aliya at imran_house_pos2 with dissolve:
        zoom 1.0*0.9
        alpha 1.0

    aslan "В наше время мы вообще не выбирали!" with dissolve

    aslan "Вот родители меня женили на твоей матери - и все у нас нормально." with dissolve

    aslan "И вообще, в наше время если бы девушка убежала, ее бы догнали и прирезали там же." with dissolve

    aslan "Вместе с похитителем! И закопали там же." with dissolve

    show Aliya_stand_straight tshirt eyes_closed_annoyed as Aliya at imran_house_pos2 with dissolve:
        zoom 1.0*0.9
        alpha 1.0

    "В разговор вмешался Имран. Видимо он был старше всех присутствующих." with dissolve

    show aslan watching_imran at imran_house_pos3 with dissolve:
        zoom 1.0
        alpha 1.0

    show imran watching_open_mouth at imran_house_pos1 with dissolve:
        zoom 1.0
        alpha 1.0

    imran "Аслан, послушай что я тебе скажу." with dissolve

    imran "Я вот дольше тебя живу уже, я в Москве живу двадцать лет, я много повидал, я с разными людьми общался." with dissolve

    imran "Так вот, пойми - сейчас уже времена другие пришли." with dissolve

    imran "В наше время было так, я согласен. А сейчас вся вот эта честь гор - уже всем наплевать." with dissolve

    imran "Ты понимаешь, в твое время жили так, а молодежь уже живет по-другому," with dissolve

    imran "И давай лучше не будем мешать им жить, сейчас уже их время, а не наше." with dissolve

    "Аслан хотел возразить, но не стал перебивать Имрана." with dissolve

    imran "И это все-таки твоя родная дочь." with dissolve

    imran "Я же знаю, ты желаешь для нее самого лучшего, и ты не станешь делать ей плохо." with dissolve

    imran "Прислушайся к ней, она же тебе говорит чего она хочет!" with dissolve

    show Aliya_stand_straight tshirt eyes_open_sad_worried as Aliya at imran_house_pos2 with dissolve:
        zoom 1.0*0.9
        alpha 1.0

    show imran watching at imran_house_pos1 with dissolve:
        zoom 1.0
        alpha 1.0

    "Имран не так уж и плох, надо заметить." with dissolve

    show aslan watching_imran_open_mouth at imran_house_pos3 with dissolve:
        zoom 1.0
        alpha 1.0

    aslan "Мне уже безразлично. Моя дочь убежала от меня. Пусть теперь делает что хочет." with dissolve

    aslan "Но я скажу вот что. Сейчас в полиции Пятигорска уже возбуждено уголовное дело о похищении." with dissolve

    show aslan neutral at imran_house_pos3 with dissolve:
        zoom 1.0
        alpha 1.0

    aslan "Так что вот этот вот молодой человек - Семен, кажется? - рискует попасть в тюрьму." with dissolve

    show aslan watching_aliya_open_mouth at imran_house_pos3 with dissolve:
        zoom 1.0
        alpha 1.0

    aslan "Если хочешь ему помочь - вернись в Пятигорск, покажись полицейским и напиши заявление, что не имеешь претензии." with dissolve

    aslan "Но мне наплевать, поедешь ты или не поедешь - поступай как хочешь." with dissolve

    show aslan watching_aliya at imran_house_pos3 with dissolve:
        zoom 1.0
        alpha 1.0

    "Повисла тишина." with dissolve

    "Возможно Аслан блефует, или хочет как-то вызвать у Алии чувство вины?" with dissolve

    "Тишину прервала мать Алии." with dissolve

    show fatima watching_open_mouth at imran_house_pos4 with dissolve:
        zoom 1.0
        alpha 1.0

    fatima "Алия, тебе вообще очень повезло что тебе попался вот такой порядочный молодой человек." with dissolve

    fatima "Другой бы тебя увез и изнасиловал бы, или продал в рабство или на органы." with dissolve

    fatima "Ты с незнакомым мужчиной уехала, ты ведь не знаешь его намерений." with dissolve

    show fatima watching at imran_house_pos4 with dissolve:
        zoom 1.0
        alpha 1.0

    "Мать Алии обратилась ко мне." with dissolve

    show fatima sad at imran_house_pos4 with dissolve:
        zoom 1.0
        alpha 1.0

    fatima "Семен, спасибо вам большое, что позаботились об Алие." with dissolve

    fatima "Но почему вы вообще помогли ей бежать? Вы ее знаете два дня, она для вас чужой человек." with dissolve

    fatima "Почему, Семен?" with dissolve

    show fatima neutral at imran_house_pos4 with dissolve:
        zoom 1.0
        alpha 1.0

    show aslan neutral at imran_house_pos3 with dissolve:
        zoom 1.0
        alpha 1.0

    show imran neutral at imran_house_pos1 with dissolve:
        zoom 1.0
        alpha 1.0

    "Все присутствующие посмотрели на меня, и стали ждать ответа." with dissolve

    "Я могу сказать, как есть. Я поддержу Алию, но тогда родители Алии навряд ли будут мне доверять." with dissolve

    "Или я могу блефовать, чтобы завоевать доверие родителей Алии. Но Алия может подумать, что я ее предал." with dissolve

    #

    # By beginning of this dialog, parents_trust_points = 0, and aliya_trust_points = 0 (we don't count aliya_trust_points_hard yet)

    # This dialog has 3 options, each choice can add +1 to parents_trust_points or to aliya_trust_points

    "Что же мне ответить?" with dissolve

    menu:

        "Что ответить?"

        "Принять сторону Алии - сказать, как есть":
            jump day4_parents_part0_choice_for_aliya

        "Принять сторону родителей - блефовать":
            jump day4_parents_part0_choice_for_parents



label day4_parents_part0_choice_for_aliya:

    $ aliya_trust_points = aliya_trust_points + 1

    me "Аслан, Фатима, а Вы разве сами не догадываетесь? Что ж, думаю уже нет смысла сглаживать то, что я хочу сказать." with dissolve

    me "Уважаемый Имран был прав когда говорил, что сейчас уже другие времена, но вот Вы этого видимо не понимаете." with dissolve

    me "Ваша дочка невероятно удивительная юная девушка. Она живой человек со своими желаниями." with dissolve

    me "За то короткое время, что я её знаю я успел убедиться в том, что она вопреки Вашему о ней мнению серьёзно обдумывала данное решение." with dissolve

    me "Давайте будем до конца честны, ведь именно Вы её к этому подтолкнули." with dissolve

    me "Вы поставили её перед фактом замужества, при этом спросили ли Вы у неё хочет ли она этого? Нет." with dissolve

    me "Вы продолжали на неё давить, повторяя раз за разом, что она должна, что у неё нет других вариантов." with dissolve

    me "А хоть раз Вы спросили, готова ли она? Хочет ли этого? Спросили в конце концов, чего она сама бы хотела?" with dissolve

    me "Нет, Вы ни разу и не подумали, о таком. Знаете, мне вот даже интересно насколько Вы знаете Вашу же дочку? Её мечты, желание, чего она бы хотела?" with dissolve

    me "Знаете, если бы Вы хоть попробовали, то может мы бы здесь не сидели." with dissolve

    me "Хоть я и знаю её несколько дней, но... Алия показала мне, что в даже в столь юной девушки может быть стальная воля, могут быть прекрасные мечты." with dissolve

    me "И что не у каждого человека есть, смелость идти к тому, чего ты хочешь." with dissolve

    me "Я помог ей потому, что хотел. Хотел, чтобы она получила желаемое, чтобы смогла достичь поставленных целей." with dissolve

    me "И знаете, что? Я не жалею, что так поступил." with dissolve

    "Повисла тишина." with dissolve

    show Aliya_stand_straight tshirt eyes_closed_sad at imran_house_pos2 with dissolve:
        zoom 1.0*0.9
        alpha 1.0

    "Я посмотрел на Алию. Она отвела взгляд, но кажется, ей пришлось по душе все что я сказал." with dissolve

    jump day4_parents_part1_choice_relationship


label day4_parents_part0_choice_for_parents:

    $ parents_trust_points = parents_trust_points + 1

    me "Уважаемые, а разве мог я, как порядочный человек, поступить иначе?" with dissolve

    me "Разве мог я позволить юной и такой наивной девочке, как Ваша дочка самой сбегать из дома?" with dissolve

    me "Конечно, понимаю, что мне нужно было пресечь её глупую затею пойти против семьи, но она была так серьёзно настроена, что я не рискнул." with dissolve

    me "Честно говоря, я просто заволновался, что она продолжит искать пути побега и обратиться ни к тому человеку." with dissolve

    me "Я взрослый мужчина и успел за свою жизнь многое повидать, поэтому я прекрасно понимал, насколько опасно может быть подобная затея, для юной девушки." with dissolve

    me "Начиная с того, что её могли просто обмануть и ограбить, и заканчивая куда более ужасными вещами." with dissolve

    me "Учитывая, что она ведь и ко мне не первому обратилась, сперва она с моим знакомым общалась. А он уже обратился ко мне." with dissolve

    me "Было вполне логично предположить, что она продолжит искать пути побега." with dissolve

    me "Так, что я решил вызваться помочь, так я по крайней мере мог убедиться, что она будет в порядке и не встрянет в какую-то опасную историю." with dissolve

    if day3_address_told:
        me "И именно поэтому, когда Вы позвонили я и сказал Вам адрес, я был рад, что уважаемый Имран приехал за Алией и теперь она сможет вернуться к семье." with dissolve
    else:
        me "И именно поэтому я был рад, что уважаемый Имран приехал за Алией и теперь она сможет вернуться к семье." with dissolve

    me "Да, хоть местами мои действия и могут показаться спорными, но как видите намерения у меня были самые честные." with dissolve

    "Повисла тишина." with dissolve

    show Aliya_stand_straight tshirt eyes_closed_sad as Aliya at imran_house_pos2 with dissolve:
        zoom 1.0*0.9
        alpha 1.0

    "Я посмотрел на Алию. Алия смотрела в пол." with dissolve

    jump day4_parents_part1_choice_relationship


label day4_parents_part1_choice_relationship:

    "Через некоторое время Фатима нарушила молчание." with dissolve

    fatima "Семен, скажите, как вы относитесь к Алие? Между вами точно ничего нет?" with dissolve

    menu:

        "Что ответить?"

        "Да, просто знакомая":
            jump day4_parents_part2_choice2_just_friends

        "Нет, она мне нравится":
            jump day4_parents_part2_choice1_like_her

label day4_parents_part2_choice1_like_her:

    $ aliya_trust_points = aliya_trust_points + 1

    me "Между нами, ещё ничего не было, но к Вашей дочери я и правда пытаю чувства." with dissolve

    me "За то недолгое время, что я её знаю я успел понять, что она просто невероятная юная девушка." with dissolve

    me "И чем больше я с ней общался, тем сильнее в неё влюблялся." with dissolve

    me "Так, что да. Я люблю Вашу дочь, хотя и понимаю, что это весьма странно учитывая сколько мы знакомы." with dissolve

    "...Повисла тишина." with dissolve

    show Aliya_stand_straight tshirt eyes_open_neutral as Aliya at imran_house_pos2 with dissolve:
        zoom 1.0*0.9
        alpha 1.0

    "Алия внимательно смотрела на меня." with dissolve

    jump day4_parents_part3


label day4_parents_part2_choice2_just_friends:


    $ parents_trust_points = parents_trust_points + 1

    show Aliya_stand_straight tshirt eyes_open_neutral as Aliya at imran_house_pos2 with dissolve:
        zoom 1.0*0.9
        alpha 1.0

    me "Уважаемая, к Вашей дочери у меня слегка отеческие чувства." with dissolve

    me "Она столь юная и непосредственна, что не может не располагать к ней, при всём этом разве мог я не волноваться за неё?" with dissolve

    me "Ваша дочь для меня знакомая, за судьбу которой я волновался, что и подтолкнуло меня вызваться ей помочь." with dissolve

    me "Так, что мои намерения были чисты в высшем понимании этого слова." with dissolve

    "Фатима понимающе кивнула несколько раз." with dissolve

    fatima "Понимаю." with dissolve

    jump day4_parents_part3


label day4_parents_part3:

    fatima "А если Алия будет жить в Москве, вы будете ей помогать?" with dissolve

    menu:

        "Что ответить?"

        "Помогу первое время":
            jump day4_parents_part5_choice1_first_time_help

        "Буду помогать всегда":
            jump day4_parents_part5_choice2_always_help


label day4_parents_part5_choice1_first_time_help:

    $ parents_trust_points = parents_trust_points + 1

    me "Я сниму ей квартиру на первое время. Когда она будет работать и получать зарплату, я помогу ей снять комнату." with dissolve

    me "Я научу ее жить самостоятельно, и когда я увижу что все в порядке, я оставлю ее в покое." with dissolve

    fatima "Ясно." with dissolve

    jump day4_parents_part6



label day4_parents_part5_choice2_always_help:

    $ aliya_trust_points = aliya_trust_points + 1

    me "Я буду поддерживать её столько сколько это понадобиться чтобы она стала на ноги." with dissolve

    me "Так же даже после этого я всегда буду готов помочь ей, если такая необходимость возникнет." with dissolve

    me "Так, что в Вашей дочери всегда будет, ещё как минимум один человек к которому она сможет обратиться за помощью, помимо Вас и уважаемого Имрана." with dissolve

    fatima "Я поняла." with dissolve

    jump day4_parents_part6

label day4_parents_part6:

    scene black with dissolve

    "Повисла пауза..." with dissolve

    scene imran_house_living_room with dissolve

    show imran watching at imran_house_pos1:
        zoom 1.0
        alpha 0.0
        linear 0.5 alpha 1.0
        alpha 1.0

    show Aliya_stand_straight tshirt eyes_open_sad_worried as Aliya at imran_house_pos2:
        zoom 1.0*0.9
        alpha 0.0
        linear 0.5 alpha 1.0
        alpha 1.0

    show aslan watching_aliya at imran_house_pos3:
        zoom 1.0
        alpha 0.0
        linear 0.5 alpha 1.0
        alpha 1.0

    show fatima watching_open_mouth at imran_house_pos4:
        zoom 1.0
        alpha 0.0
        linear 0.5 alpha 1.0
        alpha 1.0

    "Наконец Фатима заговорила." with dissolve

    fatima "Ладно, Алия, решай что ты хочешь сделать сейчас." with dissolve

    fatima "Хочешь остаться, или уехать с нами домой - решай." with dissolve

    show fatima watching at imran_house_pos4 with dissolve:
        zoom 1.0
        alpha 1.0

    "Я посмотрел на Алию. Алия посмотрела на меня, и по очереди на всех присутствующих." with dissolve

    show Aliya_stand_straight tshirt eyes_closed_sad_worried_open_mouth as Aliya at imran_house_pos2 with dissolve:
        zoom 1.0*0.9
        alpha 1.0


    aliya "Я вернусь с вами домой." with dissolve

    show Aliya_stand_straight tshirt eyes_open_sad_worried as Aliya at imran_house_pos2 with dissolve:
        zoom 1.0*0.9
        alpha 1.0

    "Что? Это же ловушка!" with dissolve

    show Aliya_stand_straight tshirt eyes_open_sad_worried_open_mouth as Aliya at imran_house_pos2 with dissolve:
        zoom 1.0*0.9
        alpha 1.0

    aliya "Я вернусь в Пятигорск и продолжу учиться в колледже." with dissolve

    show Aliya_stand_straight tshirt eyes_open_sad_worried as Aliya at imran_house_pos2 with dissolve:
        zoom 1.0*0.9
        alpha 1.0

    "Нет, только не это! Как только ты окажешься наедине с родителями, они заставят тебя поступить по-своему!" with dissolve

    show fatima watching_open_mouth at imran_house_pos4 with dissolve:
        zoom 1.0
        alpha 1.0

    fatima "Хорошо, Алия." with dissolve

    fatima "Надо будет посмотреть билеты на сегодня, и расписание автобусов." with dissolve

    show fatima watching at imran_house_pos4 with dissolve:
        zoom 1.0
        alpha 1.0

    "Кажется, настал мой выход." with dissolve

    me "Я могу поискать вам в интернете авиабилеты на самолет в Минеральные Воды." with dissolve

    me "Мне это не трудно. Давайте я куплю вам удобные билеты, прямо с телефона." with dissolve

    "Учитывая, как я общался с родителями Алии... интересно, доверяют ли они мне?" with dissolve

    scene black with dissolve

    "Я замер в ожидании..." with dissolve

    # As for now, range might be following (parents / aliya)
    # p a
    # 3 0
    # 2 1
    # 1 2
    # 0 3

    # We let pass if parents_trust_points is 2 or higher

    if debug_mode==True:

        menu:

            "Какую ветку запустить?"

            "Родители Алии доверяют Семену":
                jump day4_parents_part6_parent_persuade_success

            "Родители Алии не доверяют Семену":
                jump day4_parents_part6_parent_persuade_fail

    else:
        if parents_trust_points >= 2:
            jump day4_parents_part6_parent_persuade_success
        else:
            jump day4_parents_part6_parent_persuade_fail
