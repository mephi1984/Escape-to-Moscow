


label dagestan_exposition:

    $ addReceivedMessage(4)

    $ coach_exposition_general_asked = True

    coach "Она из Дагестана. Ты много знаешь об этой республике?" with dissolve

    menu:

        "Что ответить?"

        "\"Почти ничего не знаю.\"":
            jump day1_ask_coach_dagestan

        "\"Да, я знаю о Дагестане и о традициях его жителей.\"":
            jump day1_ask_coach_knowall


label day1_ask_coach_dagestan:

    $ addSentMessage(3)

    me "Почти ничего не знаю." with dissolve

    $ addReceivedMessage(5)

    coach "Хорошо, с чего бы начать... Дагестан это национальная республика, которая находится на Северном Кавказе." with dissolve

    $ addReceivedMessage(5)

    coach "Хотя Дагестан находится в составе России, жизнь в нём сильно отличается от жизни в средней российской глубинке." with dissolve

    $ addReceivedMessage(5)

    coach "Ну вообще, все республики на Кавказе - особенные, но Дагестан, наверное, по-своему особенная республика." with dissolve

    $ addSentMessage(3)

    me "Чем Дагестан выделяется?" with dissolve

    $ addReceivedMessage(5)

    coach "Во-первых, Дагестан самый населённый - три миллиона жителей - первое место среди всех субъектов Северного Кавказа." with dissolve

    $ addReceivedMessage(5)

    coach "Во-вторых, это очень многонациональная республика." with dissolve

    $ addReceivedMessage(5)

    coach "Если в Чечне преимущественно живут чеченцы, в Ингушетии - ингуши и так далее, то в Дагестане вместе проживают более полутора десятка национальностей." with dissolve

    $ addReceivedMessage(5)

    coach "Поэтому говорить про дагестанца, что \"он по национальности дагестанец\" - неверно." with dissolve

    $ addReceivedMessage(5)

    coach "\"Дагестанец\" может быть по национальности аварцем, даргинцем, лезгином, лакцем или даже русским." with dissolve

    $ addReceivedMessage(5)

    coach "У каждого из народов республики Дагестан свой язык, который не похож на другие." with dissolve

    $ addReceivedMessage(5)

    coach "Может быть и так, что выходцы из одного села в Дагестане не будут понимать язык жителей другого села." with dissolve

    $ addReceivedMessage(5)

    coach "Особенно сильно это различие в языках проявляется в Махачкале, где все народы плотно перемешались и живут вместе." with dissolve

    $ addReceivedMessage(5)

    coach "В этом случае дагестанцы, чтобы понимать друг друга, переходят на русский язык. Он становится языком межнационального общения." with dissolve

    $ addReceivedMessage(5)

    coach "Поэтому средний дагестанец достаточно хорошо знает русский язык, а если взять жителя Махачкалы, то и использует его в ежедневном общений." with dissolve

    $ addReceivedMessage(5)

    coach "Ещё одна особенность: по сравнению с остальным Кавказом, в Махачкале достаточно либеральные нравы." with dissolve

    $ addReceivedMessage(5)

    coach "Девушки могут ходить в чём хотят: кто-то, конечно, закрывает волосы платком, но немало из них носит джинсы и юбки." with dissolve

    $ addReceivedMessage(5)

    coach "Представить что-то подобное в Грозном, например, просто немыслимо." with dissolve

    $ addReceivedMessage(5)

    coach "Более того, в Махачкале проходит ежегодный фестиваль аниме-культуры, где встречаются косплееры, фанаты аниме и видеоигр." with dissolve

    $ addReceivedMessage(5)

    coach "Если сравнить, например, с Чечней или с Ингушетией - разница значительная." with dissolve

    $ addSentMessage(2)

    me "Интересно, спасибо!" with dissolve

    $ addReceivedMessage(5)

    coach "Спрашивай, если тебя интересует какая-то конкретная тема. Я расскажу более подробно." with dissolve

    jump day1_ask_coach_menu1

label day1_ask_coach_menu1:

    if (coach_exposition_danger_asked == True) and (coach_exposition_religion_asked == True) and (coach_exposition_tradition_asked == True) and (coach_exposition_woman_love_asked == True) and (coach_exposition_woman_decline_marry_asked == True) and (coach_exposition_woman_honor_killing_asked == True) and (coach_exposition_woman_kidnapping_asked == True):
        jump day1_ask_coach_learnedall

    menu:

        "Что спросить?"

        "\"В Дагестане опасно?\"" if coach_exposition_danger_asked == False:
            jump day1_ask_coach_danger

        "Религия в Дагестане." if coach_exposition_religion_asked == False:
            jump day1_ask_coach_religion

        "Традиции Дагестана." if coach_exposition_tradition_asked == False:
            jump day1_ask_coach_tradition

        "Положение женщины в обществе Дагестана." if (coach_exposition_woman_love_asked == False) or (coach_exposition_woman_decline_marry_asked == False) or (coach_exposition_woman_honor_killing_asked == False) or (coach_exposition_woman_kidnapping_asked == False):
            jump day1_ask_coach_woman1

        "\"Спасибо, я узнал всё, что нужно.\"":
            jump day1_ask_coach_learnedall


label day1_ask_coach_danger:

    $ coach_exposition_danger_asked = True

    $ addSentMessage(2)

    me "В Дагестане опасно?" with dissolve

    $ addReceivedMessage(5)

    coach "Нет, там безопасно как и в других регионах Северного Кавказа." with dissolve

    $ addReceivedMessage(5)

    coach "Уровень насильственных преступлений очень низкий по сравнению с другими регионами России." with dissolve

    $ addReceivedMessage(5)

    coach "По улицам можно ходить ночью не опасаясь, что тебя ограбят или убьют." with dissolve

    $ addSentMessage(4)

    me "А что насчёт террористической угрозы?" with dissolve

    $ addReceivedMessage(5)

    coach "Террористическая угроза существовала в нулевых годах. Было время, боевики спускались с гор и нападали на блокпосты." with dissolve

    $ addReceivedMessage(5)

    coach "Однако, примерно с 2012 года, радикально настроенные экстремисты начали уезжать воевать в Сирию." with dissolve

    $ addReceivedMessage(5)

    coach "На текущий момент в горах Дагестана больше нет никаких бандформирований." with dissolve

    $ addReceivedMessage(5)

    coach "Сейчас самое спокойное время в Дагестане, можно сказать, за всю его современную историю." with dissolve

    $ addSentMessage(0)

    me "Понял." with dissolve

    jump day1_ask_coach_menu1


label day1_ask_coach_religion:

    $ coach_exposition_religion_asked = True

    $ addSentMessage(3)

    me "Расскажи про религию в Дагестане." with dissolve

    $ addReceivedMessage(4)

    coach "В Дагестане большинство населения - мусульмане-сунниты." with dissolve

    $ addReceivedMessage(5)

    coach "Если ты не различаешь суннитов и шиитов, то для тебя это не существенно. Можешь не запоминать." with dissolve

    $ addReceivedMessage(5)

    coach "Несмотря на то, что большинство населения исповедует ислам, в Дагестане не принято быть очень уж религиозным." with dissolve

    $ addReceivedMessage(5)

    coach "Когда дагестанец молится и соблюдает запреты шариата это нормально." with dissolve

    $ addReceivedMessage(5)

    coach "Но стоит ему начать учить арабский язык, изучать какие-то тексты, литературу - на него начинают косо смотреть и подозревать в экстремизме." with dissolve

    $ addReceivedMessage(5)

    coach "Это в какой-то мере идет ещё с советских времен и особенно характерно для силовиков или просто госслужащих." with dissolve

    $ addReceivedMessage(5)

    coach "Доходит до того, что дагестанцы стараются быть чисто выбритыми, чтобы не быть похожими на бородачей-террористов." with dissolve

    $ addReceivedMessage(5)

    coach "Это относится больше к взрослому поколению, в особенности тех, кто ещё застал Советский Союз." with dissolve

    $ addReceivedMessage(5)

    coach "Современная молодёжь в Дагестане в среднем намного более религиозна, чем их родители." with dissolve

    $ addReceivedMessage(5)

    coach "Но опять же, все дагестанцы разные и нельзя сказать что-то однозначное. Кто-то более религиозен, кто-то менее." with dissolve

    $ addSentMessage(0)

    me "Понятно." with dissolve

    jump day1_ask_coach_menu1

label day1_ask_coach_tradition:

    $ coach_exposition_tradition_asked = True

    $ addSentMessage(4)

    me "Расскажи про традиции в Дагестане." with dissolve

    $ addReceivedMessage(5)

    coach "Как и на всём Северном Кавказе, в Дагестане сильны традиции гостеприимства." with dissolve

    $ addReceivedMessage(5)

    coach "В мелких городах и сёлах почти нет гостиниц, потому что они не нужны." with dissolve

    $ addReceivedMessage(5)

    coach "Если ты приехал издалека, можешь просто подойти к любому дому, постучаться и попроситься переночевать. Тебя пустят, накормят и дадут ночлег." with dissolve

    $ addReceivedMessage(5)

    coach "В Дагестане принято уважать старших. Им нужно уступать места и слушаться." with dissolve

    $ addReceivedMessage(5)

    coach "Особенно сильно это проявляется в семье. Ослушаться отца — немыслимое дело!" with dissolve

    $ addReceivedMessage(5)

    coach "Дагестанец может не бояться ни драки, ни полиции, единственное чего он боится — потерять уважение своего отца." with dissolve

    $ addReceivedMessage(5)

    coach "Ещё в Дагестане достаточно трепетное отношение к своим женщинам." with dissolve

    $ addReceivedMessage(5)

    coach "Женщина в Дагестане находится под защитой всех своих родственников." with dissolve

    $ addReceivedMessage(5)

    coach "Не стоит обижать дагестанку. Она пожалуется, например, своему брату, который вызовет обидчика на разговор." with dissolve

    $ addReceivedMessage(5)

    coach "По этой же причине в Дагестане не принято делать замечание посторонней девушке." with dissolve

    $ addReceivedMessage(5)

    coach "Это будет невежливо, оскорбительно и тому, кто сделал замечание, может непоздоровиться." with dissolve

    $ addReceivedMessage(5)

    coach "Если дагестанец видит, что девушка ведёт себя неподобающе, он скорее всего промолчит, максимум - скажет об этом её родственнику-мужчине." with dissolve

    $ addSentMessage(0)

    me "Ага..." with dissolve

    jump day1_ask_coach_menu1


label day1_ask_coach_woman1:

    if coach_exposition_woman1_asked == True:
        jump day1_ask_coach_menu_woman

    $ coach_exposition_woman1_asked = True

    $ addSentMessage(5)

    me "Расскажи про положение женщины в обществе Дагестана." with dissolve

    $ addReceivedMessage(5)

    coach "Если смотреть в целом на государственном уровне - всё выглядит прилично." with dissolve

    $ addReceivedMessage(5)

    coach "Декларируется равноправие: никаких ограничений нет, женщины учатся в колледжах и университетах." with dissolve

    $ addReceivedMessage(5)

    coach "Также они получают профессию и работают наравне с мужчинами." with dissolve

    $ addReceivedMessage(5)

    coach "Тем не менее, общество в Дагестане патриархальное. Женщина зачастую воспринимается не как самостоятельная личность, а как принадлежащая своему мужу или отцу." with dissolve

    $ addReceivedMessage(5)

    coach "Тут всё зависит уже от семьи. Если родители девушки либеральные, они не будут ограничивать свою дочь." with dissolve

    $ addReceivedMessage(5)

    coach "Они позволят ей учиться там, где она пожелает и разрешат выйти замуж за кого она хочет." with dissolve

    $ addReceivedMessage(5)

    coach "Но если девушка выросла где-нибудь в селе, то скорее всего родители не будут считаться с её мнением." with dissolve

    $ addReceivedMessage(5)

    coach "Девушка будет вынуждена выйти замуж за того, кого родители посчитают достойным женихом." with dissolve

    $ addReceivedMessage(5)

    coach "И в дальнейшем она будет вынуждена жить с мужем и слушаться его." with dissolve

    $ addReceivedMessage(5)

    coach "Дагестан меняется со временем. Но и сейчас по-прежнему существуют убийства чести и свадьбы по принуждению." with dissolve

    $ addReceivedMessage(5)

    coach "В общем, тема обширная. Что именно ты хочешь узнать?" with dissolve

    jump day1_ask_coach_menu_woman


label day1_ask_coach_menu_woman:

    if (coach_exposition_woman_love_asked == True) and (coach_exposition_woman_decline_marry_asked == True) and (coach_exposition_woman_honor_killing_asked == True) and (coach_exposition_woman_kidnapping_asked == True):
        jump day1_ask_coach_menu1

    menu:

        "Что спросить?"

        "\"Что будет, если девушка откажется выходить замуж?\"" if coach_exposition_woman_decline_marry_asked == False:
            jump day1_ask_coach_woman_decline_marry

        "\"Что делать, если девушка полюбила парня?\"" if coach_exposition_woman_love_asked == False:
            jump day1_ask_coach_woman_love

        "\"Что такое убийство чести?\"" if coach_exposition_woman_honor_killing_asked == False:
            jump day1_ask_coach_woman_honor_killing

        "Похищение невесты." if coach_exposition_woman_kidnapping_asked == False:
            jump day1_ask_coach_woman_kidnapping

        "Вернуться назад.":
            jump day1_ask_coach_menu1


label day1_ask_coach_woman_decline_marry:

    $ coach_exposition_woman_decline_marry_asked = True

    $ addSentMessage(5)

    me "Что будет, если девушка откажется выходить замуж?" with dissolve

    $ addReceivedMessage(4)

    coach "Если девушка живёт в селе, особо выбора-то и нет." with dissolve

    $ addReceivedMessage(5)

    coach "Она так же, как и односельчане, живёт по заведённым традициям и не представляет, что может быть иначе." with dissolve

    $ addReceivedMessage(5)

    coach "Если девушке прямо совсем неприятен мужчина, за которого она выходит замуж, то выбор невелик:" with dissolve

    $ addReceivedMessage(5)

    coach "она может сбежать из дома или совершить самоубийство. И то и другое сложно сделать, как ты понимаешь." with dissolve

    $ addReceivedMessage(5)

    coach "Если же дагестанка, допустим, училась в Махачкале, вкусила городской жизни, имеет широкий круг друзей и интересов," with dissolve

    $ addReceivedMessage(5)

    coach "получила диплом, собирается устроиться на работу и тут её вдруг родители хотят вернуть в село и выдать замуж за односельчанина - " with dissolve

    $ addReceivedMessage(4)

    coach "вот тут уже не всё так однозначно." with dissolve

    $ addReceivedMessage(5)

    coach "Может быть, девушка сумеет отстоять свою независимость и переубедить родителей." with dissolve

    $ addReceivedMessage(5)

    coach "А может, договориться с родителями не удастся и тогда возможен любой исход, вплоть до убийства чести." with dissolve

    $ addSentMessage(0)

    me "Да уж." with dissolve

    jump day1_ask_coach_menu_woman


label day1_ask_coach_woman_love:

    $ coach_exposition_woman_love_asked = True

    $ addSentMessage(4)

    me "Что делать, если девушка полюбила парня?" with dissolve

    $ addReceivedMessage(5)

    coach "По правилам парень и девушка не должны \"встречаться\", в том смысле как это происходит у русских." with dissolve

    $ addReceivedMessage(5)

    coach "Если парню понравилась девушка, он должен посвататься: просить руки и сердца у её родителей." with dissolve

    $ addReceivedMessage(5)

    coach "Если родители дают одобрение, парень сможет взять девушку в жёны." with dissolve

    $ addReceivedMessage(5)

    coach "Если вместо этого девушка будет ходить на свидания с парнем, она будет считаться распутной." with dissolve

    $ addReceivedMessage(5)

    coach "Разумеется, конкретные рамки допустимого могут варьироваться. В Махачкале студентка ДГУ может без проблем общаться со своими одногруппниками." with dissolve

    $ addReceivedMessage(5)

    coach "В то время как где-нибудь в селе девушка не осмелится даже заговорить с незнакомым мужчиной." with dissolve

    $ addReceivedMessage(5)

    coach "Однозначно существует лишь запрет на ночевку в доме с чужим мужчиной. Всё остальное по ситуации." with dissolve

    $ addSentMessage(0)

    me "Интересно." with dissolve

    jump day1_ask_coach_menu_woman


label day1_ask_coach_woman_honor_killing:

    $ coach_exposition_woman_honor_killing_asked = True

    $ addSentMessage(3)

    me "Что такое убийство чести?" with dissolve

    $ addReceivedMessage(5)

    coach "На Кавказе, конечно, это так не называют, там говорят \"смыть позор\"." with dissolve

    $ addReceivedMessage(5)

    coach "Если девушка ведёт себя неподобающе, считается что она таким образом позорит весь свой род." with dissolve

    $ addReceivedMessage(5)

    coach "Кто-то из родственников-мужчин может в таком случае решить убить её, чтобы решить проблему." with dissolve

    $ addReceivedMessage(5)

    coach "Обычно у родителей и братьев рука не поднимется убить свою дочь, сестру. Однако это может сделать кто-то из более дальних родственников." with dissolve

    $ addReceivedMessage(4)

    coach "Чаще всего убивают за измену, блуд, отказ выходить замуж. Реже - за слухи." with dissolve

    $ addReceivedMessage(4)

    coach "Настоящие убийства чести — всё же редкое явление и служат скорее \"пугалом\"." with dissolve

    $ addReceivedMessage(5)

    coach "Истории об убийствах чести циркулируют в обществе в виде тем, которые люди обсуждают или в виде слухов." with dissolve

    $ addReceivedMessage(4)

    coach "В реальной жизни обычно такие вопросы решаются без крови." with dissolve

    $ addSentMessage(0)

    me "Понятно." with dissolve

    jump day1_ask_coach_menu_woman


label day1_ask_coach_woman_kidnapping:

    $ coach_exposition_woman_kidnapping_asked = True

    $ addSentMessage(4)

    me "Расскажи про традицию похищения невесты." with dissolve

    $ addReceivedMessage(4)

    coach "Похищение невесты в Дагестане осуждается." with dissolve

    $ addReceivedMessage(5)

    coach "Если парню понравилась девушка, будет правильнее всего идти к её родителям просить руки и сердца." with dissolve

    $ addReceivedMessage(5)

    coach "Похищение имеет смысл лишь в том случае, если не удаётся договориться нормально." with dissolve

    $ addReceivedMessage(5)

    coach "Это может быть когда парень и девушка любят друг друга, но родители против свадьбы." with dissolve

    $ addReceivedMessage(5)

    coach "Второй вариант похуже: парень хочет взять девушку в жёны, но она против и родители её поддерживают." with dissolve

    $ addReceivedMessage(5)

    coach "В первом случае парень и девушка заранее договариваются о похищении и это происходит скорее для вида." with dissolve

    $ addReceivedMessage(5)

    coach "Но может быть, что девушка реально не хочет выходить за парня, родители также против, но жених очень хочет жениться именно на ней." with dissolve

    $ addReceivedMessage(5)

    coach "Тогда он действительно может организовать похищение, и довольно жестокое." with dissolve

    $ addReceivedMessage(5)

    coach "Девушку завернут в бурку, кинут в автомобиль и отвезут в дом жениха." with dissolve

    $ addReceivedMessage(5)

    coach "Дальше, если девушка провела ночь в доме мужчины, родителям приходится согласиться выдать дочь за него замуж под давлением общественного мнения." with dissolve

    $ addSentMessage(0)

    me "Ясно." with dissolve

    jump day1_ask_coach_menu_woman



label day1_ask_coach_knowall:

    $ addSentMessage(4)

    me "Да, я знаю о Дагестане и о традициях его жителей." with dissolve

    jump day1_ask_coach_finish


label day1_ask_coach_learnedall:

    $ addSentMessage(4)

    me "Спасибо, я узнал всё, что мне нужно." with dissolve

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
