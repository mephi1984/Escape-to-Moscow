
label day2_intro:

    play music "music/Runaway_08 (Pre_Loop).ogg" fadein 1.0

    queue music "music/Runaway_08 (Loop).ogg"

    scene semen_room_day with dissolve

    "Наступил новый день."

    "Я проснулся, и нехотя потянулся в теплой постели." with dissolve

    "В работе фрилансера есть и хорошая сторона." with dissolve

    "Мне не нужно вставать рано утром и идти на работу." with dissolve

    "Я могу спать сколько мне захочется. И я проснулся только тогда, когда полностью выспался." with dissolve

    show black with dissolve

    "Начался новый трудовой день фрилансера..." with dissolve

    jump day2_before_choice


label day2_before_choice:

    scene semen_room_table_day

    show black zorder 20

    show semen_room_table_day_foreground_phone zorder 1

    show semen_room_table_day_foreground_card zorder 2

    show cg_screen_youtube

    $ changeDialogToAliya()

    $ showMessengerWithRightOrder()

    hide black with dissolve

    "Я умылся, наскоро позавтракал, и сел за ноутбук." with dissolve

    "Мой взгляд задержался на мессенджере." with dissolve

    "Новых сообщений от заказчиков нет. В самом верху контакт-листа были два новых контакта - Алия (с ником Миса Амане) и Напарник. Оба в сети." with dissolve

    "Итак, с чего бы начать день?" with dissolve

    jump day2_what_to_do


label day2_what_to_do:


    if (day2_coach_talked == True) and (day2_aliya_talked == True):
        jump day2_do_own_business

    "Чем заняться?" with dissolve

    menu:

        "Чем заняться?"

        "Посоветоваться с Напарником" if day2_coach_talked == False:

            jump day2_talk_coach

        "Пообщаться с Алией" if day2_aliya_talked == False:

            jump day2_talk_aliya

        "Заняться своими делами":

            jump day2_do_own_business

label day2_talk_coach:

    $ day2_coach_talked = True

    hide cg_screen_messenger_window
    hide cg_screen_messenger_window_top

    $ changeDialogToCoach()

    $ showMessengerWithRightOrder()

    "Я открыл диалог с Напарником и начал писать." with dissolve

    if day1_advice_asked:
        jump day2_talk_coach_day1_talked
    else:
        jump day2_talk_coach_day1_not_talked



label day2_talk_coach_day1_talked:

    $ addSentMessage(3)

    me "Привет! Спасибо за вчерашние советы!" with dissolve

    $ addReceivedMessage(0)

    coach "Привет)" with dissolve

    $ addReceivedMessage(2)

    coach "Как все прошло?" with dissolve

    $ addSentMessage(2)

    me "Вроде нормально поговорили" with dissolve

    $ addReceivedMessage(2)

    coach "Отправь мне переписку)" with dissolve

    $ addSentMessageHistory()

    "Я скопировал переписку с Алией и отправил Напарнику." with dissolve

    $ addReceivedMessage(0)

    coach "Хмм..." with dissolve

    if day2_aliya_talked == False:
        jump day2_talk_coach_part2_before_talked_to_aliya
    else:
        jump day2_talk_coach_part2_after_talked_to_aliya




label day2_talk_coach_day1_not_talked:

    $ addSentMessage(4)

    me "Привет! Я вчера познакомился с девушкой в интернете" with dissolve

    $ addReceivedMessage(1)

    coach "Привет! Отлично)" with dissolve

    $ addSentMessage(4)

    me "Она мне рассказала про свои проблемы, и мы поговорили" with dissolve

    $ addReceivedMessage(3)

    coach "Что там у нее случилось?" with dissolve

    $ addSentMessage(2)

    me "Долго рассказывать, хмм" with dissolve

    $ addReceivedMessage(3)

    coach "Пришли мне переписку, я почитаю" with dissolve

    $ addSentMessageHistory()

    "Я скопировал переписку с Алией и отправил Напарнику." with dissolve

    $ addReceivedMessage(0)

    coach "Хмм..." with dissolve

    $ addReceivedMessage(4)

    coach "Дочитываю сейчас ваш вчерашний ночной диалог" with dissolve

    $ addReceivedMessage(4)

    coach "Ужасная ситуация, конечно. Надеюсь, она найдет решение" with dissolve

    $ addReceivedMessage(5)

    coach "Я думаю, ты все правильно сделал, и молодец что предложил ей помочь" with dissolve

    $ addSentMessage(4)

    me "Возможно я смогу ей чем-то помочь" with dissolve

    $ coach_exposition_return_step = 1

    jump dagestan_exposition


label day2_talk_coach_day1_not_talked_after_exposition:

    if day2_aliya_talked == False:
        jump day2_talk_coach_part2_before_talked_to_aliya
    else:
        jump day2_talk_coach_part2_after_talked_to_aliya



label day2_talk_coach_part2_before_talked_to_aliya:

    $ addReceivedMessage(4)

    coach "В-общем я считаю, вчера вы неплохо поговорили" with dissolve

    $ addReceivedMessage(4)

    coach "Кажется, она стала больше доверять тебе" with dissolve

    $ addReceivedMessage(4)

    coach "Но все равно, соблюдай дистанцию" with dissolve

    $ addReceivedMessage(5)

    coach "Пообщайся с ней немного, узнай больше о ней. Расскажи о себе, найди общие интересы" with dissolve

    $ addReceivedMessage(4)

    coach "Если у тебя будет время сегодня, конечно" with dissolve

    $ addSentMessage(2)

    me "Спасибо за совет!" with dissolve

    $ addReceivedMessage(2)

    coach "Не за что)" with dissolve

    $ addReceivedMessage(5)

    coach "Мне нужно будет отвлечься на дела. Я буду на связи вечером! Пиши если что" with dissolve

    $ addSentMessage(0)

    me "Окей" with dissolve

    jump day2_what_to_do


label day2_talk_coach_part2_after_talked_to_aliya:

    $ addReceivedMessage(4)

    coach "Вижу вы и сегодня успели наговорить много)" with dissolve

    $ addReceivedMessage(4)

    coach "Сейчас я прочитаю ваш сегодняшний диалог тоже" with dissolve

    $ addReceivedMessage(0)

    coach "Хмм..." with dissolve

    # At this point, aliya_trust_points could be 0, 1, 2 or 3
    if aliya_trust_points_hard == 0:

        $ addReceivedMessage(4)

        coach "Кажется, ты не очень то разговорчив с ней" with dissolve

        $ addReceivedMessage(4)

        coach "Я думаю, она тоже к тебе сейчас относится настороженно" with dissolve

    elif aliya_trust_points_hard == 1:

        $ addReceivedMessage(4)

        coach "Вы неплохо поговорили. Кажется, она доверяет тебе больше" with dissolve

        $ addReceivedMessage(4)

        coach "Главное, в будущем не ляпни чего-нибудь не подумав" with dissolve

        $ addReceivedMessage(4)

        coach "А в остальном все окей, ты неплохо справляешься" with dissolve

    elif aliya_trust_points_hard >= 2:

        $ addReceivedMessage(4)

        coach "Кажется, ты хорошо поладил с ней" with dissolve

        $ addReceivedMessage(4)

        coach "Я думаю она тебе доверяет намного больше" with dissolve

        $ addReceivedMessage(3)

        coach "Продолжай в том же духе!" with dissolve


    $ addSentMessage(4)

    me "Хорошо, буду иметь в виду, спасибо" with dissolve

    $ addReceivedMessage(2)

    coach "Не за что)" with dissolve

    $ addReceivedMessage(5)

    coach "Мне нужно будет отвлечься на дела. Я буду на связи вечером! Пиши если что" with dissolve

    $ addSentMessage(0)

    me "Окей" with dissolve

    jump day2_what_to_do


label day2_talk_aliya:

    if day2_coach_talked:
        hide cg_screen_messenger_window
        hide cg_screen_messenger_window_top

        $ changeDialogToAliya()

        $ showMessengerWithRightOrder()

    $ day2_aliya_talked = True

    $ aliya_trust_points_hard = aliya_trust_points_hard + 1

    $ addSentMessage(1)

    me "Привет, Алия!" with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Привет" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Я хочу тебя предупредить кое о чем" with dissolve

    $ addSentMessage(1)

    me "Да, слушаю!" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Я из Дагестана, и у нас есть такое понятие, как честь девушки" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Имей в виду, если ты с мной что-то сделаешь" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Ты смотрел фильм Ворошиловский стрелок?" with dissolve

    "Алия намекает на последствия, если я буду приставать к ней." with dissolve

    $ addSentMessage(2)

    me "Да. Я понимаю, о чем ты говоришь" with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Хорошо что ты это понимаешь" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "У нас был в Дагестане случай, лет 10 назад" with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Мама и дочь сидели дома, каждый занимался своим делом. Был уже поздний вечер" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "В дверь постучали. Дочь пошла посмотреть, кто там, и не вернулась" with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Мама подумала что она там со знакомым вышла пообщаться. Но прошел час, она не вернулась" with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Так эта девушка пропала" with dissolve

    $ addSentMessage(1)

    me "Ее похитили?" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Потом выяснилось, что она убежала с женихом, и все такое" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Она вернулась через несколько лет" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Но это уже был позор на всю оставшуюся жизнь" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Так как она развелась уже, с ребенком на руках была" with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Родители пожалели ее, но такого отношения как раньше уже не было" with dissolve

    $ addSentMessage(1)

    me "Интересная история" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Я не хочу так. Это будет позор на всю жизнь" with dissolve

    show black zorder 20 with dissolve

    $ renpy.pause(1.0)

    jump day2_talk_aliya_part2



label day2_talk_aliya_part2:

    hide black with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Если я собираюсь сбежать за границу, мне точно нужен загранпаспорт?" with dissolve

    $ addSentMessage(1)

    me "Да, нужен" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Ты не знаешь сколько по времени может занять оформление загранпаспорта?" with dissolve

    $ addSentMessage(5)

    me "Знаю, недавно помогал другу с оформлением. Заняло где-то в районе 3-х месяцев" with dissolve

    $ addReceivedMessage(1)

    aliya_mobile "Так долго?" with dissolve

    $ addSentMessage(4)

    me "Там мы просто не по месту прописки оформляли, вот и дольше" with dissolve

    $ addSentMessage(2)

    me "А так до одного месяца" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Ясно, а без загранпаспорта в Корею никак нельзя?" with dissolve

    $ addSentMessage(1)

    me "Увы, но нет" with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Плохо" with dissolve

    $ addSentMessage(3)

    me "Да и загранпаспорт это только полдела" with dissolve

    $ addReceivedMessage(1)

    aliya_mobile "Ты о чём?" with dissolve

    $ addSentMessage(4)

    me "Россиянам для въезда в Корею на 60 дней, конечно, не нужна виза" with dissolve

    $ addSentMessage(3)

    me "Но будут нужны и другие документы" with dissolve

    $ addReceivedMessage(1)

    aliya_mobile "Это какие?" with dissolve

    $ addSentMessage(4)

    me "Ну кроме загранпаспорта, нужно будет иметь билеты обратно, или в третью страну" with dissolve

    $ addSentMessage(5)

    me "Подтверждение платежеспособности, тоже. Деньги, выписка из банка о состоянии счета, оплаченная бронь отеля" with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Зачем?" with dissolve

    $ addSentMessage(4)

    me "Много русских остались в Корее работать нелегалами" with dissolve

    $ addSentMessage(2)

    me "Корейцам это надоело" with dissolve

    $ addSentMessage(4)

    me "Поэтому сейчас всех пассажиров из России тщательно проверяют" with dissolve

    $ addSentMessage(5)

    me "Если корейские пограничники подозревают, что ты едешь работать нелегально - тебя разворачивают на границе" with dissolve

    $ addReceivedMessage(1)

    aliya_mobile "Это плохо" with dissolve

    $ addSentMessage(3)

    me "Вообще это все решаемый вопрос" with dissolve

    $ addSentMessage(4)

    me "Просто нужно будет побольше документов приготовить" with dissolve

    $ addSentMessage(5)

    me "Этим можно заняться перед поездкой. Забронировать отель, подготовить билеты, обменять валюту, купить дорожные чеки" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Это наверное очень дорого будет стоить" with dissolve

    $ addSentMessage(1)

    me "Да, это точно" with dissolve

    $ addSentMessage(5)

    me "Но только так корейцы будут уверены, что ты едешь в Корею тратить деньги" with dissolve

    $ addSentMessage(2)

    me "А не зарабатывать их" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "А если поехать туда учиться?" with dissolve

    $ addSentMessage(4)

    me "Как ты будешь учиться, не зная корейского или английского" with dissolve

    $ addSentMessage(4)

    me "Надо заработать деньги на обучение, выучить язык, подготовиться" with dissolve

    $ addReceivedMessage(1)

    aliya_mobile "И то верно" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Ладно. А сколько стоит загранпаспорт сделать?" with dissolve

    $ addSentMessage(4)

    me "Кажется, 2500 рублей. Но я могу и ошибаться" with dissolve

    $ addReceivedMessage(1)

    aliya_mobile "Ох, ладно" with dissolve

    $ addSentMessage(2)

    me "А ты зарабатываешь деньги?" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Нет. Обычно родители мне дают немного карманных денег" with dissolve

    $ addSentMessage(4)

    me "Ты думала о том, чтобы найти подработку?" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Однажды мне и моим подругам предложили поработать на Пасху" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Нужно было на точке продавать освященные куличи" with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Но я же мусульманка" with dissolve

    $ addReceivedMessage(1)

    aliya_mobile "Это неправильно" with dissolve

    $ addSentMessage(4)

    me "Я думаю, в исламе запрещено поклоняться другим религиям" with dissolve

    $ addSentMessage(4)

    me "Но продавать куличи, скорее всего не запрещено" with dissolve

    $ addSentMessage(4)

    me "Ты же в куличи не веришь, ты их просто продаешь" with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Наверное, ты прав" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Мне точно нужно будет заработать немного денег к лету" with dissolve

    $ addSentMessage(3)

    me "Что ты еще можешь делать?" with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Я думаю также научиться накручивать аккаунты в соцсетях, за деньги" with dissolve

    $ addSentMessage(4)

    me "Да, тоже вариант... но этому учиться нужно" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Как еще можно заработать?" with dissolve

    $ addSentMessage(4)

    me "Вообще, в небольших городах с работой сложно" with dissolve

    $ addSentMessage(3)

    me "В Москве перспектив намного больше" with dissolve

    $ addSentMessage(4)

    me "Поживешь там, поработаешь, накопишь деньги" with dissolve

    $ addSentMessage(2)

    me "Потом в Корею" with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Если честно, я боюсь, что в Москве меня смогут найти" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Если уж уезжать, то в другую страну" with dissolve

    $ addSentMessage(0)

    me "Ладно" with dissolve

    "Разговор сходит на нет." with dissolve

    "Что делать дальше?" with dissolve

    menu:

        "Что делать дальше?"

        "Узнать больше про Алию":

            jump day2_talk_aliya_part3

        "Завершить разговор":

            jump day2_talk_aliya_end





label day2_talk_aliya_part3:

    $ aliya_trust_points_hard = aliya_trust_points_hard + 1

    $ addSentMessage(4)

    me "Я хочу узнать побольше о тебе" with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Например?" with dissolve

    $ addSentMessage(3)

    me "Что ты делаешь сейчас?" with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Только что пообедала" with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "У нас на обед курзе" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Я бы поделилась, если бы могла передать еду через интернет)" with dissolve

    $ addSentMessage(2)

    me "Спасибо, мне приятно" with dissolve

    $ addSentMessage(3)

    me "Как у тебя день прошел?" with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Если честно, не очень" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "С утра к стоматологу ходила" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Два часа после этого не могла есть ничего" with dissolve

    $ addSentMessage(3)

    me "Не любишь лечить зубы?" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "В прошлом году я лечила зуб" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "И стоматолог повредил его" with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "С тех пор приходится с этим зубом ходить к стоматологу регулярно" with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Ненавижу" with dissolve

    $ addSentMessage(0)

    me "Понимаю" with dissolve

    $ addSentMessage(3)

    me "Стоматология была в Дагестане?" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Нет, здесь, в Пятигорске" with dissolve

    $ addSentMessage(4)

    me "Ты получается все время живешь в Пятигорске?" with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Я здесь учусь" with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Отец снимает коттедж" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "И мы все вместе с ним живем - я, брат, сестра" with dissolve

    $ addSentMessage(3)

    me "А мама у тебя где?" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Мама живет в Дагестане" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Иногда мы к ней приезжаем на выходные" with dissolve

    if coach_exposition_general_asked == True:
        jump day2_talk_aliya_part4
    else:
        "Разговор потихонечку иссякает." with dissolve

        jump day2_talk_aliya_end




label day2_talk_aliya_part4:

    $ addSentMessage(4)

    me "А ваша семья по национальности кто?" with dissolve

    $ addReceivedMessage(1)

    aliya_mobile "Мы аварцы)" with dissolve

    $ addSentMessage(3)

    me "Ты хорошо знаешь родной язык?" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Да, я знаю аварский язык" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Еще чуть-чуть понимаю даргинский и лезгинский языки" with dissolve

    $ addSentMessage(0)

    me "Интересно!" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Но я хорошо разговариваю по-русски" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Я же живу и учусь в Пятигорске" with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "И если честно, я по аварски разговариваю только в своей семье" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Или когда приезжаю в родное село в Дагестан" with dissolve

    $ addSentMessage(0)

    me "Понятно" with dissolve

    "Разговор потихонечку иссякает." with dissolve

    jump day2_talk_aliya_end





label day2_talk_aliya_end:

    $ addSentMessage(3)

    me "Ладно, мне пора возвращаться к делам" with dissolve

    $ addSentMessage(3)

    me "Было приятно с тобой пообщаться!" with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Спасибо за советы!" with dissolve

    if aliya_trust_points_hard >= 2:

        $ addReceivedMessage(4)

        aliya_mobile "Мне тоже было интересно поговорить)" with dissolve
    else:
        $ addReceivedMessage(0)

        aliya_mobile "Пока!" with dissolve

    "Ладно, я поговорил с Алией. Теперь нужно решить, что делать дальше..." with dissolve

    jump day2_what_to_do


label day2_do_own_business:

    "Я решил пока не тратить время на разговоры." with dissolve

    "У меня сейчас немало заказов висят, их нужно успеть сделать." with dissolve

    "Я приступил к работе..." with dissolve

    show black zorder 20 with dissolve

    "Я настолько увлекся работой, что не заметил, как быстро пролетело время..." with dissolve

    jump day2_evening


label day2_evening:

    play music "music/Runaway_01 (Pre_Loop).ogg" fadein 1.0

    queue music "music/Runaway_01 (Loop).ogg"

    scene semen_room_table_night

    show black zorder 20

    show semen_room_table_night_foreground_phone zorder 1

    show semen_room_table_night_foreground_card zorder 2

    show cg_screen_youtube

    hide cg_screen_messenger_window
    hide cg_screen_messenger_window_top

    hide black with dissolve

    "Наступил вечер." with dissolve

    "Я уже успел поужинать, и был в весьма хорошем настроении." with dissolve

    show cg_screen_new_message_aliya

    $ renpy.show('semen_room_table_night_foreground_phone_day2_aliya', tag='semen_room_table_night_foreground_phone', zorder=1)

    messenger "Новое сообщение" with dissolve # with hpunch

    hide cg_screen_new_message_aliya

    $ renpy.show('semen_room_table_night_foreground_phone', tag='semen_room_table_night_foreground_phone', zorder=1)

    $ changeDialogToAliya()

    $ showMessengerWithRightOrder()

    play music "music/Runaway_03 (Pre_Loop).ogg" fadein 1.0

    queue music "music/Runaway_03 (Loop).ogg"

    $ addReceivedMessage(0)

    aliya_mobile "Привет" with dissolve

    $ addReceivedMessage(1)

    aliya_mobile "Можешь говорить?" with dissolve

    $ addSentMessage(3)

    me "Привет, да. Что случилось?" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "У меня есть новости" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Мои родители назначили свадьбу на 8 июня" with dissolve

    $ addSentMessage(3)

    me "Ого. Это очень скоро" with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Да. Мне страшно" with dissolve

    $ addReceivedMessage(1)

    aliya_mobile "Что же делать?" with dissolve

    $ addSentMessage(5)

    me "До 8 июня чуть больше месяца, может быть ты успеешь сделать загранпаспорт?" with dissolve

    $ addReceivedMessage(2)

    aliya_mobile "Нет, не успею" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Я уже в мае вернусь в Дагестан" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Оттуда я не смогу сбежать" with dissolve

    $ addSentMessage(3)

    me "Да уж. Придется сбежать в мае" with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "В начале мая начинается Рамадан. И он продлится до 5 июня" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Во время Рамадана нельзя совершать грех" with dissolve

    $ addSentMessage(0)

    me "Ладно..." with dissolve

    $ addSentMessage(2)

    me "И что нам остается?" with dissolve

    $ addReceivedMessage(1)

    aliya_mobile "Не знаю" with dissolve

    "Действительно, выбор сильно сокращается." with dissolve

    "Отвертеться не получится. Теперь мне нужно принять серьезное решение." with dissolve

    menu:

        "Итак, что теперь делать?"

        "Предложить сбежать в ближайшее время":

            jump day2_escape_now

        "Отказаться от плана побега":

            jump day2_cancel

label day2_escape_now:

    "Я прямо почувствовал, как у меня в крови появился адреналин, и участился пульс." with dissolve

    $ addSentMessage(3)

    me "Ты знаешь, что нужно делать" with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "что?" with dissolve

    $ addSentMessage(4)

    me "Признай. Единственное решение - сбежать сейчас" with dissolve

    $ addReceivedMessage(0)

    aliya_mobile ":'(" with dissolve

    $ addSentMessage(4)

    me "Сейчас твои родители не ожидают, что ты сбежишь" with dissolve

    $ addSentMessage(5)

    me "Ближе к свадьбе, будет труднее уйти от контроля родителей" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Ладно. Что мне делать?" with dissolve

    $ addSentMessage(4)

    me "Ты же находишься в Пятигорске, да?" with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Да" with dissolve

    $ addSentMessage(4)

    me "Тебе нужно будет как-то добраться до Москвы" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "До Москвы ехать на автобусе 20 часов" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Меня остановят на посту" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Или родители догонят меня" with dissolve

    $ addSentMessage(3)

    me "Ты можешь прилететь в Москву на самолете" with dissolve

    $ addSentMessage(4)

    me "Рядом с Пятигорском есть аэропорт Минеральные Воды" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Я никогда не летала на самолете" with dissolve

    "Это может быть проблемой. Какой сделать выбор?" with dissolve

    menu:

        "Какой сделать выбор?"

        "Посоветоваться с Напарником":

            jump day2_escape_now_coach

        "Предложить прилететь к ней":

            jump day2_escape_now2

        "Предложить купить для нее билет на самолет":

            jump day2_escape_now2_fail

        "Отказаться от плана побега":

            jump day2_cancel

label day2_escape_now_coach:

    hide cg_screen_messenger_window
    hide cg_screen_messenger_window_top

    $ changeDialogToCoach()

    $ showMessengerWithRightOrder()

    "Я открыл вкладку диалога с Напарником и начал быстро строчить." with dissolve

    if day2_coach_talked or day1_advice_asked:
        jump day2_escape_now_coach_ever_talked
    else:
        jump day2_escape_now_coach_not_talked

label day2_escape_now_coach_not_talked:

    $ day2_coach_advice_asked = True

    $ addSentMessage(5)

    me "Привет! Вчера я познакомился с девушкой по интернету, и сейчас мне нужен совет" with dissolve

    $ addReceivedMessage(2)

    coach "Привет! Отличное начало)" with dissolve

    $ addReceivedMessage(2)

    coach "Что ты хочешь спросить?" with dissolve

    $ addSentMessage(2)

    me "Эээ, долго рассказывать" with dissolve

    $ addReceivedMessage(4)

    coach "Пришли мне свою переписку с ней, я почитаю" with dissolve

    $ addSentMessageHistory()

    "Я скопировал переписку с Алией и отправил Напарнику." with dissolve

    "Прошло достаточно много времени, но наконец-то Напарник начал писать ответ." with dissolve

    $ addReceivedMessage(3)

    coach "Я офигеваю от сложившейся ситуации" with dissolve

    $ addReceivedMessage(4)

    coach "Ты молодец что хочешь помочь, но вариантов тут мало" with dissolve

    $ addReceivedMessage(4)

    coach "Но прежде чем это обсуждать, я хочу кое-что уточнить у тебя" with dissolve

    $ coach_exposition_return_step = 2

    jump dagestan_exposition


label day2_escape_now_coach_not_talked_after_exposition:

    $ addReceivedMessage(3)

    coach "Теперь, возвращаемся к текущей ситуации" with dissolve

    jump day2_escape_now_coach_continue




label day2_escape_now_coach_ever_talked:

    $ day2_coach_advice_asked = True

    $ addSentMessage(5)

    me "Привет, мне срочно нужен совет. Насчет Алии, девушки из Дагестана, с которой я познакомился" with dissolve

    $ addReceivedMessage(3)

    coach "Привет! Пришли переписку, я прочитаю" with dissolve

    $ addSentMessageHistory()

    "Я скопировал переписку и отправил Напарнику." with dissolve

    $ addReceivedMessage(4)

    coach "Хмм, она права, тут очень мало пространства для маневра" with dissolve

    jump day2_escape_now_coach_continue


label day2_escape_now_coach_continue:

    $ addSentMessage(3)

    me "Можешь что-нибудь посоветовать?" with dissolve

    $ addReceivedMessage(5)

    coach "Ты с этой девушкой знаком всего два дня. Нормальный человек посоветовал бы тебе не ввязываться в этот блудняк" with dissolve

    $ addReceivedMessage(4)

    coach "Но если она чем-то тебя зацепила, и ты хочешь ей помочь, то" with dissolve

    $ addReceivedMessage(4)

    coach "НЕ ТУПИ, прилети сам в Пятигорск или куда там, и встреть ее на месте" with dissolve

    $ addReceivedMessage(3)

    coach "Затем уже оттуда вы вдвоем улетите в Москву" with dissolve

    $ addSentMessage(4)

    me "Ох, это же получается я потрачу немало денег на билеты туда-обратно для себя самого" with dissolve

    $ addSentMessage(4)

    me "Почему нельзя только купить один билет, для Алии до Москвы?" with dissolve

    $ addReceivedMessage(4)

    coach "Она не согласится лететь одна непонятно куда непонятно к кому" with dissolve

    $ addReceivedMessage(5)

    coach "И потом, если ты беспокоишься за деньги, то не ввязывайся в эту историю вообще" with dissolve

    hide cg_screen_messenger_window
    hide cg_screen_messenger_window_top

    $ changeDialogToAliya()

    $ showMessengerWithRightOrder()

    "Ох, ладно. Я переключился на диалог с Алией." with dissolve

    "Какой сделать выбор?" with dissolve

    menu:

        "Какой сделать выбор?"

        "Предложить прилететь к ней":

            jump day2_escape_now2

        "Отказаться от плана побега":

            jump day2_cancel


label day2_escape_now2_fail:

    $ addSentMessage(4)

    me "Я могу купить тебе билеты до Москвы" with dissolve

    $ addSentMessage(5)

    me "Тебе нужно будет приехать в аэропорт, зарегистрироваться на рейс и улететь в Москву" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Не знаю. Мне страшно" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Я ни разу не летала на самолетах" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Я даже не знаю как зарегистрироваться на рейс" with dissolve

    $ addSentMessage(3)

    me "Это не сложно, я могу объяснить" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Нет, это не вариант, совсем" with dissolve

    $ addSentMessage(0)

    me "Ладно" with dissolve

    "Кажется, не стоило этого предлагать. Что же тогда делать?" with dissolve

    menu:

        "Какой сделать выбор?"

        "Посоветоваться с Напарником":

            jump day2_escape_now_coach

        "Предложить прилететь к ней":

            jump day2_escape_now2

        "Отказаться от плана побега":

            jump day2_cancel



label day2_escape_now2:

    $ addSentMessage(2)

    me "Давай сделаем так" with dissolve

    $ addSentMessage(3)

    me "Я прилечу к тебе в Минеральные Воды" with dissolve

    $ addSentMessage(3)

    me "Встречу тебя в аэропорту" with dissolve

    $ addSentMessage(3)

    me "И мы вместе полетим в Москву" with dissolve

    $ addReceivedMessage(0)

    aliya_mobile "Хмм" with dissolve

    $ addReceivedMessage(4)

    aliya_mobile "Хороший план. Как будто ты меня похищаешь" with dissolve

    $ addSentMessage(0)

    me "Да" with dissolve

    $ addSentMessage(5)

    me "Когда твои родители заподозрят неладное, ты уже будешь далеко от дома" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "У меня нет денег на билеты" with dissolve

    $ addSentMessage(4)

    me "Не переживай, я куплю тебе билеты" with dissolve

    $ addReceivedMessage(1)

    aliya_mobile "Спасибо большое" with dissolve

    $ addSentMessage(3)

    me "Я на твоей стороне, и я хочу помочь тебе" with dissolve

    "Это были простые слова, однако же мне было нелегко их написать и отправить." with dissolve

    $ addReceivedMessage(0)

    aliya_mobile ":)" with dissolve

    $ addSentMessage(4)

    me "Мы сделаем так. Я прилетаю к тебе в Минеральные Воды, и я встречаю тебя в аэропорту" with dissolve

    $ addSentMessage(5)

    me "Ты утром пойдешь как будто бы в колледж. Но на самом деле ты должна сесть на автобус до аэропорта" with dissolve

    $ addSentMessage(4)

    me "Я куплю билеты так чтобы мы улетели сразу же, тем же утром" with dissolve

    $ addSentMessage(4)

    me "И когда твои родители заподозрят что-то неладное, мы уже будем в Москве" with dissolve

    $ addReceivedMessage(3)

    aliya_mobile "Я боюсь. Я тебя совсем не знаю" with dissolve

    $ addSentMessage(4)

    me "Мы встретимся в аэропорту Минеральные Воды. Там мы познакомимся и поговорим" with dissolve

    $ addSentMessage(4)

    me "Там тебе нужно будет окончательно решить, готова ли ты сбежать со мной или нет" with dissolve

    $ addReceivedMessage(5)

    aliya_mobile "Самое страшное, чего я больше всего боюсь - это то что я передумаю в самый последний момент" with dissolve

    $ addSentMessage(5)

    me "Пока ты не улетишь, ты можешь передумать, вернуться домой и притвориться, что была в колледже" with dissolve

    $ addSentMessage(4)

    me "После того как мы сядем в самолет, ты уже не сможешь передумать" with dissolve

    $ addReceivedMessage(1)

    aliya_mobile "Я поняла. Ладно..." with dissolve

    # Проверка на доверие

    show black zorder 20 with dissolve

    $ renpy.pause(1.0)

    if debug_mode==True:
        menu:

            "Семен набрал достаточно плюсиков, чтобы Алия ему доверяла?"

            "Да - запустить ветку сюжета, где Алия доверяет Семену":

                jump day2_escape_now_success

            "Нет - запустить ветку сюжета, где Алия не доверяет Семену":

                jump day2_escape_now_fail
    else:
        if (persistent.difficulty == 0): # Normal
            jump day2_escape_now_success
        else:
            if aliya_trust_points_hard >= 2:           #At this point aliya_trust_points_hard: max = 2, min = 0
                jump day2_escape_now_success
            else:
                jump day2_escape_now_fail
