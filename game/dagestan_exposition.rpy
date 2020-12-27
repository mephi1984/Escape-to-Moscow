


label dagestan_exposition:

    $ addReceivedMessage(4)

    $ coach_exposition_general_asked = True

    coach "Она из Дагестана. Ты много знаешь про Дагестан?" with dissolve

    menu:

        "Что ответить?"

        "\"Почти ничего не знаю\"":
            jump day1_ask_coach_dagestan

        "\"Да, я знаю о Дагестане и о традициях Дагестана\"":
            jump day1_ask_coach_knowall


label day1_ask_coach_dagestan:

    $ addSentMessage(3)

    me "Почти ничего не знаю" with dissolve

    $ addReceivedMessage(5)

    coach "Хорошо, с чего бы начать... Дагестан это национальная республика в составе России. Дагестан находится на Северном Кавказе" with dissolve

    $ addReceivedMessage(4)

    coach "Столица - Махачкала. Население - три миллиона человек" with dissolve

    $ addReceivedMessage(5)

    coach "Хотя Дагестан находится в составе России, жизнь в Дагестане сильно отличается от жизни в средней российской глубинке" with dissolve

    $ addReceivedMessage(5)

    coach "Это же можно сказать и про другие республики Кавказа. В этом смысле они похожи" with dissolve

    $ addSentMessage(3)

    me "А чем Дагестан выделяется?" with dissolve

    $ addReceivedMessage(3)

    coach "Да, есть отличия, конечно же" with dissolve

    $ addReceivedMessage(5)

    coach "Во-первых, Дагестан самый населенный - три миллиона жителей, первое место среди всех субъектов на Северном Кавказе" with dissolve

    $ addReceivedMessage(5)

    coach "Во-вторых, Дагестан - очень многонациональная республика" with dissolve

    $ addReceivedMessage(5)

    coach "Если в Чечне преимущественно живут чеченцы, в Ингушетии - ингуши и так далее, то в Дагестане вместе проживают более полтора десятка национальностей" with dissolve

    $ addReceivedMessage(5)

    coach "Поэтому про дагестанца говорить, что \"он по национальности - дагестанец\", это неверно" with dissolve

    $ addReceivedMessage(5)

    coach "\"Дагестанец\" может быть по национальности аварцем, даргинцем, лезгином, лакцем или даже русским" with dissolve

    $ addReceivedMessage(5)

    coach "У каждого из народов Дагестана свой язык, непохожий на другие" with dissolve

    $ addReceivedMessage(5)

    coach "Может быть и так, что выходцы из одного села в Дагестане не будут понимать язык жителей другого села" with dissolve

    $ addReceivedMessage(5)

    coach "Особенно сильно это различие в языках проявляется в Махачкале, где все народы плотно перемешались и живут вместе" with dissolve

    $ addReceivedMessage(5)

    coach "В этом случае дагестанцы, чтобы понимать друг друга, переходят на русский язык. Русский язык становится языком межнационального общения" with dissolve

    $ addReceivedMessage(5)

    coach "Поэтому средний дагестанец достаточно хорошо знает русский язык, а если взять жителя Махачкалы - то и использует его в ежедневном общений" with dissolve

    $ addReceivedMessage(5)

    coach "Еще одна особенность - по сравнению с остальным Кавказом, в Махачкале достаточно либеральные нравы" with dissolve

    $ addReceivedMessage(5)

    coach "Девушки могут ходить в чем хотят. Кто-то конечно закрывает волосы платком, но немало девушек ходят джинсах и в юбках" with dissolve

    $ addReceivedMessage(5)

    coach "Представить что-то подобное в Грозном, например, просто немыслимо" with dissolve

    $ addReceivedMessage(5)

    coach "Более того, в Махачкале проходит ежегодный фестиваль аниме-культуры, где встречаются косплееры, фанаты аниме и видеоигр" with dissolve

    $ addReceivedMessage(5)

    coach "Правда, в прошлом году фестиваль был сорван толпой агрессивно настроенных молодых людей" with dissolve

    $ addReceivedMessage(5)

    coach "Но все равно, сам факт. Если сравнить например с Чечней, то разница значительная" with dissolve

    $ addSentMessage(2)

    me "Интересно, спасибо!" with dissolve

    $ addReceivedMessage(5)

    coach "Если тебя интересует какая-то конкретная тема, то спрашивай! Я расскажу более подробно" with dissolve

    jump day1_ask_coach_menu1

label day1_ask_coach_menu1:

    if (coach_exposition_danger_asked == True) and (coach_exposition_religion_asked == True) and (coach_exposition_tradition_asked == True) and (coach_exposition_woman_love_asked == True) and (coach_exposition_woman_decline_marry_asked == True) and (coach_exposition_woman_honor_killing_asked == True) and (coach_exposition_woman_kidnapping_asked == True):
        jump day1_ask_coach_learnedall

    menu:

        "Что спросить?"

        "\"В Дагестане опасно?\"" if coach_exposition_danger_asked == False:
            jump day1_ask_coach_danger

        "Религия в Дагестане" if coach_exposition_religion_asked == False:
            jump day1_ask_coach_religion

        "Традиции Дагестана" if coach_exposition_tradition_asked == False:
            jump day1_ask_coach_tradition

        "Положение женщины в обществе Дагестана" if (coach_exposition_woman_love_asked == False) or (coach_exposition_woman_decline_marry_asked == False) or (coach_exposition_woman_honor_killing_asked == False) or (coach_exposition_woman_kidnapping_asked == False):
            jump day1_ask_coach_woman1

        "\"Спасибо, я узнал все что мне нужно\"":
            jump day1_ask_coach_learnedall


label day1_ask_coach_danger:

    $ coach_exposition_danger_asked = True

    $ addSentMessage(2)

    me "В Дагестане опасно?" with dissolve

    $ addReceivedMessage(5)

    coach "Нет, там безопасно, как и в других регионах Северного Кавказа" with dissolve

    $ addReceivedMessage(5)

    coach "Уровень насильственных преступлений там очень низкий по сравнению с другими регионами России" with dissolve

    $ addReceivedMessage(5)

    coach "По улицам можно ходить ночью не опасаясь, что тебя ограбят или убьют" with dissolve

    $ addSentMessage(4)

    me "А что насчет террористической угрозы?" with dissolve

    $ addReceivedMessage(5)

    coach "Террористическая угроза существовала в нулевых годах. Было время, боевики спускались с гор и нападали на блокпосты" with dissolve

    $ addReceivedMessage(5)

    coach "Однако примерно с 2012 года, радикально настроенные экстремисты начали уезжать воевать в Сирию" with dissolve

    $ addReceivedMessage(5)

    coach "На текущий момент, в горах Дагестана больше нет никаких бандформирований" with dissolve

    $ addReceivedMessage(5)

    coach "Сейчас самое спокойное время в Дагестане, можно сказать, за всю его современную историю" with dissolve

    $ addSentMessage(0)

    me "Понял" with dissolve

    jump day1_ask_coach_menu1


label day1_ask_coach_religion:

    $ coach_exposition_religion_asked = True

    $ addSentMessage(3)

    me "Расскажи про религию в Дагестане" with dissolve

    $ addReceivedMessage(4)

    coach "В Дагестане большинство населения - мусульмане-сунниты" with dissolve

    $ addReceivedMessage(5)

    coach "Если ты не различаешь суннитов и шиитов, то для тебя это не существенно, можешь не запоминать" with dissolve

    $ addReceivedMessage(5)

    coach "Несмотря на то, что большинство населения исповедуют ислам, в Дагестане не принято быть очень уж религиозным" with dissolve

    $ addReceivedMessage(5)

    coach "Когда дагестанец молится и соблюдает запреты Шариата это нормально" with dissolve

    $ addReceivedMessage(5)

    coach "Но, если он начинает учить арабский язык, изучать какие-то тексты, литературу - на него начинают косо смотреть и подозревать в экстремизме" with dissolve

    $ addReceivedMessage(5)

    coach "Это в какой-то мере идет еще с советских времен. И это особенно характерно для силовиков, или просто госслужащих" with dissolve

    $ addReceivedMessage(5)

    coach "Доходит до того, что дагестанцы стараются быть чисто выбритыми, чтобы не быть похожими на бородачей-террористов" with dissolve

    $ addReceivedMessage(5)

    coach "Это относится больше к взрослому поколению, в особенности тех, кто еще застал Советский союз" with dissolve

    $ addReceivedMessage(5)

    coach "Современная молодежь в Дагестане в среднем намного более религиозна, чем их родители" with dissolve

    $ addReceivedMessage(5)

    coach "Но опять же, все дагестанцы разные, и поэтому нельзя что-то сказать однозначное. Кто-то более религиозен, а кто-то менее" with dissolve

    $ addSentMessage(0)

    me "Понятно" with dissolve

    jump day1_ask_coach_menu1

label day1_ask_coach_tradition:

    $ coach_exposition_tradition_asked = True

    $ addSentMessage(4)

    me "Расскажи про традиции в Дагестане" with dissolve

    $ addReceivedMessage(5)

    coach "Как и на всем Северном Кавказе, в Дагестане сильны традиции гостеприимства" with dissolve

    $ addReceivedMessage(5)

    coach "В мелких городах и селах там почти нет гостиниц, потому что гостиницы не нужны" with dissolve

    $ addReceivedMessage(5)

    coach "Если ты приехал издалека можешь просто подойти к любому дому, постучаться и попроситься переночевать. Тебя пустят, накормят и дадут ночлег" with dissolve

    $ addReceivedMessage(5)

    coach "В Дагестане принято уважение к старшим. Старшим нужно уступать места, старших нужно слушаться" with dissolve

    $ addReceivedMessage(5)

    coach "Особенно сильно это проявляется в семье. Ослушаться отца — это немыслимое дело!" with dissolve

    $ addReceivedMessage(5)

    coach "Дагестанец может не бояться ни драки, ни полиции, и единственное чего он боится — это потерять уважение своего отца" with dissolve

    $ addReceivedMessage(5)

    coach "Еще в Дагестане достаточно трепетное отношение к своим женщинам" with dissolve

    $ addReceivedMessage(5)

    coach "Женщина в Дагестане находится под защитой всех своих родственников" with dissolve

    $ addReceivedMessage(5)

    coach "Не стоит обижать дагестанку - она пожалуется, например, своему брату, который вызовет обидчика на разговор" with dissolve

    $ addReceivedMessage(5)

    coach "По этой же причине в Дагестане не принято даже делать замечание посторонней девушке" with dissolve

    $ addReceivedMessage(5)

    coach "Это будет невежливо, оскорбительно, и тот, кто сделал замечание, может получить последствия" with dissolve

    $ addReceivedMessage(5)

    coach "Если дагестанец видит, что девушка ведет себя неподобающе, он скорее всего промолчит, максимум - скажет об этом ее родственнику мужского пола" with dissolve

    $ addSentMessage(0)

    me "Ага" with dissolve

    jump day1_ask_coach_menu1


label day1_ask_coach_woman1:

    if coach_exposition_woman1_asked == True:
        jump day1_ask_coach_menu_woman

    $ coach_exposition_woman1_asked = True

    $ addSentMessage(5)

    me "Расскажи про положение женщины в обществе Дагестана" with dissolve

    $ addReceivedMessage(5)

    coach "Если смотреть в целом на государственном уровне, то все выглядит прилично" with dissolve

    $ addReceivedMessage(5)

    coach "Декларируется равноправие, никаких ограничений нет, женщины в Дагестане учатся в колледжах и в университетах" with dissolve

    $ addReceivedMessage(5)

    coach "Женщины получают профессию и работают наравне с мужчинами" with dissolve

    $ addReceivedMessage(5)

    coach "Тем не менее, общество в Дагестане - патриархальное. Женщина зачастую воспринимается не как самостоятельная личность, а как принадлежащая своему мужу или отцу" with dissolve

    $ addReceivedMessage(5)

    coach "И тут все зависит уже от семьи. Если родители девушки либеральные, они не будут ограничивать свою дочь" with dissolve

    $ addReceivedMessage(5)

    coach "Они позволят ей учиться там, где она хочет, позволят ей замуж за кого она хочет" with dissolve

    $ addReceivedMessage(5)

    coach "Но если девушка выросла где-нибудь в селе, то скорее всего родители не будут считаться с ее мнением" with dissolve

    $ addReceivedMessage(5)

    coach "Девушка будет вынуждена выйти замуж за того, кого родители посчитают достойным женихом" with dissolve

    $ addReceivedMessage(5)

    coach "И в дальнейшем девушка будет вынуждена жить с мужем и слушаться мужа" with dissolve

    $ addReceivedMessage(5)

    coach "Дагестан меняется со временем. Но и сейчас по-прежнему существуют убийства чести и свадьбы по принуждению" with dissolve

    $ addReceivedMessage(5)

    coach "В-общем, тема обширная. Что именно ты хочешь узнать?" with dissolve

    jump day1_ask_coach_menu_woman


label day1_ask_coach_menu_woman:

    if (coach_exposition_woman_love_asked == True) and (coach_exposition_woman_decline_marry_asked == True) and (coach_exposition_woman_honor_killing_asked == True) and (coach_exposition_woman_kidnapping_asked == True):
        jump day1_ask_coach_menu1

    menu:

        "Что спросить?"

        "\"Что будет если девушка откажется выходить замуж?\"" if coach_exposition_woman_decline_marry_asked == False:
            jump day1_ask_coach_woman_decline_marry

        "\"Что делать, если девушка полюбила парня?\"" if coach_exposition_woman_love_asked == False:
            jump day1_ask_coach_woman_love

        "\"Что такое убийство чести?\"" if coach_exposition_woman_honor_killing_asked == False:
            jump day1_ask_coach_woman_honor_killing

        "Похищение невесты" if coach_exposition_woman_kidnapping_asked == False:
            jump day1_ask_coach_woman_kidnapping

        "Вернуться назад":
            jump day1_ask_coach_menu1


label day1_ask_coach_woman_decline_marry:

    $ coach_exposition_woman_decline_marry_asked = True

    $ addSentMessage(5)

    me "Что будет если девушка откажется выходить замуж?" with dissolve

    $ addReceivedMessage(4)

    coach "Если девушка живет в селе, то особо выбора-то и нет" with dissolve

    $ addReceivedMessage(5)

    coach "Она живет в селе, и все односельчане живут по заведенным традициям, и она не представляет, как можно жить иначе" with dissolve

    $ addReceivedMessage(5)

    coach "Если девушке прямо совсем неприятен мужчина, за которого она выходит замуж, то выбор невелик" with dissolve

    $ addReceivedMessage(5)

    coach "Она может сбежать из дома или совершить самоубийство. И то, и другое сложно сделать, как ты понимаешь" with dissolve

    $ addReceivedMessage(5)

    coach "Если же дагестанка, допустим, училась в Махачкале, вкусила городской жизни, имеет широкий круг друзей и интересов" with dissolve

    $ addReceivedMessage(5)

    coach "Вот она получила диплом, собирается устроиться на работу, и тут ее вдруг родители хотят вернуть в село и выдать замуж за односельчанина" with dissolve

    $ addReceivedMessage(4)

    coach "Вот тут уже не все так однозначно" with dissolve

    $ addReceivedMessage(5)

    coach "Может быть, девушке удастся отстоять свою независимость и переубедить родителей" with dissolve

    $ addReceivedMessage(5)

    coach "А может быть, договориться с родителями не удастся, и тогда возможен любой исход, вплоть до убийства чести" with dissolve

    $ addSentMessage(0)

    me "Да уж" with dissolve

    jump day1_ask_coach_menu_woman


label day1_ask_coach_woman_love:

    $ coach_exposition_woman_love_asked = True

    $ addSentMessage(4)

    me "Что делать, если девушка полюбила парня?" with dissolve

    $ addReceivedMessage(5)

    coach "По правилам, парень и девушка не должны \"встречаться\", в том смысле как это происходит у русских" with dissolve

    $ addReceivedMessage(5)

    coach "Если парню понравилась девушка, он должен посвататься - просить руки и сердца у ее родителей" with dissolve

    $ addReceivedMessage(5)

    coach "Если родители одобрят, то парень сможет взять девушку в жены" with dissolve

    $ addReceivedMessage(5)

    coach "Если вместо этого девушка будет ходить на свидания с парнем, то она будет считаться распутной" with dissolve

    $ addReceivedMessage(5)

    coach "Разумеется, конкретные рамки допустимого могут варьироваться. В Махачкале студентка ДГУ может без проблем общаться со своими одногруппниками" with dissolve

    $ addReceivedMessage(5)

    coach "в то время как где-нибудь в селе девушка не осмелится даже заговорить с незнакомым мужчиной" with dissolve

    $ addReceivedMessage(5)

    coach "Однозначно существует лишь запрет на ночевку в доме с чужим мужчиной. Все остальное - по ситуации" with dissolve

    $ addSentMessage(0)

    me "Интересно" with dissolve

    jump day1_ask_coach_menu_woman


label day1_ask_coach_woman_honor_killing:

    $ coach_exposition_woman_honor_killing_asked = True

    $ addSentMessage(3)

    me "Что такое убийство чести?" with dissolve

    $ addReceivedMessage(5)

    coach "На Кавказе конечно так не говорят, там говорят \"смыть позор\"" with dissolve

    $ addReceivedMessage(5)

    coach "Если девушка ведет себя неподобающе, то считается что она таким образом позорит весь свой род" with dissolve

    $ addReceivedMessage(5)

    coach "Кто-то из родственников мужского пола может в таком случае решить убить ее, чтобы решить проблему" with dissolve

    $ addReceivedMessage(5)

    coach "Обычно у родителей и братьев рука не поднимется убить свою дочь, свою сестру, однако это может сделать кто-то из более дальних родственников" with dissolve

    $ addReceivedMessage(4)

    coach "Обычно убивают за измену, за блуд, за отказ выходить замуж. Реже - за слухи" with dissolve

    $ addReceivedMessage(4)

    coach "Настоящие убийства чести — это все же редкое явление и служат скорее \"пугалом\"" with dissolve

    $ addReceivedMessage(5)

    coach "Истории об убийствах чести циркулируют в обществе, в виде тем, которые люди обсуждают, или даже в виде слухов" with dissolve

    $ addReceivedMessage(4)

    coach "Но в реальной жизни обычно такие вопросы все-таки решаются без крови" with dissolve

    $ addSentMessage(0)

    me "Понятно" with dissolve

    jump day1_ask_coach_menu_woman


label day1_ask_coach_woman_kidnapping:

    $ coach_exposition_woman_kidnapping_asked = True

    $ addSentMessage(4)

    me "Расскажи про традицию похищения невесты" with dissolve

    $ addReceivedMessage(4)

    coach "Похищение невесты в Дагестане все-таки осуждается" with dissolve

    $ addReceivedMessage(5)

    coach "Если парню понравилась девушка, будет правильнее всего идти к ее родителям, просить руки и сердца" with dissolve

    $ addReceivedMessage(5)

    coach "Похищение имеет смысл лишь в том случае, если не удается договориться нормально" with dissolve

    $ addReceivedMessage(5)

    coach "Это может быть, когда парень и девушка любят друг друга, но родители против свадьбы" with dissolve

    $ addReceivedMessage(5)

    coach "Второй вариант, похуже - парень хочет взять девушку в жены, но девушка против, поэтому и родители против" with dissolve

    $ addReceivedMessage(5)

    coach "В первом случае, парень и девушка заранее договариваются о похищении, поэтому похищение проходит скорее для вида" with dissolve

    $ addReceivedMessage(5)

    coach "Но может быть, что девушка реально не хочет выходить за парня, родители также против, но жених очень хочет взять в жены именно ее" with dissolve

    $ addReceivedMessage(5)

    coach "Тогда жених действительно может организовать похищение, и довольно жестокое" with dissolve

    $ addReceivedMessage(5)

    coach "Девушку завернут в бурку, кинут в автомобиль и отвезут в дом жениха" with dissolve

    $ addReceivedMessage(5)

    coach "Дальше, если девушка провела ночь в доме мужчины, родителям приходится согласится выдать замуж девушку за этого мужчину, под давлением общественного мнения" with dissolve

    $ addSentMessage(0)

    me "Ясно" with dissolve

    jump day1_ask_coach_menu_woman



label day1_ask_coach_knowall:

    $ addSentMessage(4)

    me "Да, я знаю о Дагестане и о традициях Дагестана" with dissolve

    jump day1_ask_coach_finish


label day1_ask_coach_learnedall:

    $ addSentMessage(4)

    me "Спасибо, я узнал все что мне нужно" with dissolve

    jump day1_ask_coach_finish


label day1_ask_coach_finish:

    $ addReceivedMessage(0)

    coach "Отлично!" with dissolve

    if coach_exposition_return_step == 0:
        jump day1_ask_coach_after_exposition
    elif  coach_exposition_return_step == 1:
        jump day2_talk_coach_day1_not_talked_after_exposition
    elif  coach_exposition_return_step == 2:
        jump day2_escape_now_coach_not_talked_after_exposition
    else:
        jump day2_escape_now_success_coach_not_talked_after_exposition
