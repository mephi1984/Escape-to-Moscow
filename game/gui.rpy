################################################################################
## Инициализация
################################################################################

## Оператор init offset повышает приоритет инициализации в этом файле над
## другими файлами, из-за чего инициализация здесь запускается первее.
init offset = -2


#Change here for settning scale 1920x1080 to 1280x720
#define SCALE = 0.66667
define SCALE = 1.0

#define config.language = "english"
#define config.language = None



## Вызываю gui.init, чтобы сбросить стили, чувствительные к стандартным
## значениям, и задать высоту и ширину окна игры.
init python:
    #Change here for settning scale 1920x1080 to 1280x720
    #gui.init(1280, 720)
    gui.init(1920, 1080)



################################################################################
## Конфигурируемые Переменные GUI
################################################################################


## Цвета #######################################################################
##
## Цвета текста в интерфейсе.

## Акцентный цвет используется в заголовках и подчёркнутых текстах.
define gui.accent_color = '#4D7BBE'

## Цвет, используемый в текстовой кнопке, когда она не выбрана и не наведена.
define gui.idle_color = '#7E8696'

## Small_color используется в маленьком тексте, который должен быть ярче/темнее,
## для того, чтобы выделяться.
define gui.idle_small_color = '#7E8696'

## Цвет, используемых в кнопках и панелях, когда они наведены.
define gui.hover_color = '#86CAFF'

## Цвет, используемый текстовой кнопкой, когда она выбрана, но не наведена.
## Кнопка может быть выбрана, если это текущий экран или текущее значение
## настройки.
define gui.selected_color = '#E2F3FF'

## Цвет, используемый текстовой кнопкой, когда она не может быть выбрана.
define gui.insensitive_color = '#7E86967f'

## Цвета, используемые для частей панелей, которые не заполняются. Они
## используются не напрямую, а только при воссоздании файлов изображений.
define gui.muted_color = '#1A3156'
define gui.hover_muted_color = '#2B518C'

## Цвета, используемые в тексте диалогов и выборов.
define gui.text_color = '#E2F3FF'
define gui.interface_text_color = '#E2F3FF'


## Шрифты и их размеры #########################################################

## Шрифт, используемый внутриигровым текстом.
define gui.text_font = "fonts/Manrope-Medium.ttf"

## Шрифт, используемый именами персонажей.
define gui.name_text_font = "fonts/Manrope-Medium.ttf"

## Шрифт, используемый текстом вне игры.
define gui.interface_text_font = "fonts/Manrope-Medium.ttf"

## Размер нормального текста диалога.
define gui.text_size = 33 * SCALE

## Размер имён персонажей.
define gui.name_text_size = 45*SCALE

## Размер текста в пользовательском интерфейсе.
define gui.interface_text_size = 33*SCALE

## Размер заголовков в пользовательском интерфейсе.
define gui.label_text_size = 36*SCALE

## Размер текста на экране уведомлений.
define gui.notify_text_size = 24*SCALE

## Размер заголовка игры.
define gui.title_text_size = 75*SCALE


## Главное и игровое меню. #####################################################

## Изображения, используемые в главном и игровом меню.
define gui.main_menu_background = im.FactorScale("gui/main_menu.png", SCALE)
define gui.main_menu_background_aliya_locked = im.FactorScale("gui/main_menu_aliya_locked.png", SCALE)
define gui.main_menu_background_aliya_unlocked = im.FactorScale("gui/main_menu_aliya_unlocked.png", SCALE)

define gui.main_menu_background_semyon_locked = im.FactorScale("gui/main_menu_semyon_locked.png", SCALE)
define gui.main_menu_background_semyon_unlocked = im.FactorScale("gui/main_menu_semyon_unlocked.png", SCALE)

define gui.main_menu_logo = im.FactorScale("gui/logo.png", SCALE)

define gui.main_menu_overlay = im.FactorScale("gui/overlay/main_menu.png", SCALE)
define gui.game_menu_overlay = im.FactorScale("gui/overlay/game_menu.png", SCALE)

define gui.confirm_overlay = im.FactorScale("gui/overlay/confirm.png", SCALE)


define gui.confirm_frame = im.FactorScale("gui/confirm_frame.png", SCALE)

define gui.frame = im.FactorScale("gui/frame.png", SCALE)
define gui.skip = im.FactorScale("gui/skip.png", SCALE)

define gui.nvl = im.FactorScale("gui/nvl.png", SCALE)

define gui.textbox = im.FactorScale("gui/textbox.png", SCALE)

define gui.namebox = im.FactorScale("gui/namebox.png", SCALE)
define gui.notify = im.FactorScale("gui/notify.png", SCALE)

define gui.bar_top = im.FactorScale("gui/bar/top.png", SCALE)
define gui.bar_bottom = im.FactorScale("gui/bar/bottom.png", SCALE)
define gui.bar_left = im.FactorScale("gui/bar/left.png", SCALE)
define gui.bar_right = im.FactorScale("gui/bar/right.png", SCALE)


define gui.language_overlay = im.FactorScale("gui/overlay/language.png", SCALE)

## Диалог ######################################################################
##
## Эти переменные контролируют, как диалог появляется на отдельной строчке.

## Высота текстового окна, содержащего диалог.
define gui.textbox_height = int(277.5*SCALE)

## Местоположение текстового окна по вертикали экрана. 0.0 — верх, 0.5 — центр и
## 1.0 — низ.
define gui.textbox_yalign = 1.0


## Местоположение имени говорящего персонажа по отношению к текстовому окну.
## Это могут быть целые значения в пикселях слева и сверху от начала окна или
## процентное отношение, например, 0.5 для центрирования.
define gui.name_xpos = int(360*SCALE)
define gui.name_ypos = 0

## Горизонтальное выравнивание имени персонажа. Это может быть 0.0 для
## левоориентированного, 0.5 для центрированного и 1.0 для правоориентированного
## выравнивания.
define gui.name_xalign = 0.0

## Ширина, высота и границы окна, содержащего имя персонажа или None, для
## автоматической размерки.
define gui.namebox_width = None
define gui.namebox_height = None

## Границы окна, содержащего имя персонажа слева, сверху, справа и снизу по
## порядку.
define gui.namebox_borders = Borders(int(8*SCALE), int(8*SCALE), int(8*SCALE), int(8*SCALE))

## Если True, фон текстового окна будет моститься (расширяться по эффекту
## плитки). Если False, фон текстового окна будет фиксированным.
define gui.namebox_tile = False


## Размещение диалога по отношению к текстовому окну. Это могут быть целые
## значения в пикселях слева и сверху от текстового окна или процентное
## отношение, например, 0.5 для центрирования.
define gui.dialogue_xpos = int(402*SCALE)
define gui.dialogue_ypos = int(75*SCALE)

## Максимальная ширина текста диалога в пикселях.
define gui.dialogue_width = int(1116*SCALE)

## Горизонтальное выравнивание текста диалога. Это может быть 0.0 для
## левоориентированного, 0.5 для центрированного и 1.0 для правоориентированного
## выравнивания.
define gui.dialogue_text_xalign = 0.0


## Кнопки ######################################################################
##
## Эти переменные, вместе с файлами изображений в gui/button, контролируют
## аспекты того, как отображаются кнопки.

## Ширина и высота кнопки в пикселях. Если None, Ren'Py самостоятельно
## рассчитает размер.
define gui.button_width = None
define gui.button_height = None

## Границы каждой стороны кнопки в порядке слева, сверху, справа, снизу.
define gui.button_borders = Borders(int(6*SCALE), int(6*SCALE), int(6*SCALE), int(6*SCALE))

## Если True, фон изображения будет моститься. Если False, фон изображения будет
## линейно масштабирован.
define gui.button_tile = False

## Шрифт, используемый кнопкой.
define gui.button_text_font = gui.interface_text_font

## Размер текста, используемый кнопкой.
define gui.button_text_size = gui.interface_text_size

## Цвет текста в кнопке в различных состояниях.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## Горизонтальное выравнивание текста в кнопке. (0.0 — лево, 0.5 — по центру,
## 1.0 — право).
define gui.button_text_xalign = 0.0


## Эти переменные переписывают настройки различных видов кнопок. Пожалуйста,
## посмотрите документацию по gui для просмотра всех вариаций кнопок и для чего
## каждая из них нужна.
##
## Эти настройки используются стандартным интерфейсом:

define gui.radio_button_borders = Borders(int(27*SCALE), int(6*SCALE), int(6*SCALE), int(6*SCALE))

define gui.check_button_borders = Borders(int(27*SCALE), int(6*SCALE), int(6*SCALE), int(6*SCALE))

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(int(15*SCALE), int(6*SCALE), int(15*SCALE), int(6*SCALE))

define gui.quick_button_borders = Borders(int(15*SCALE), int(6*SCALE), int(15*SCALE), 0)
define gui.quick_button_text_size = int(21*SCALE)
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Вы также можете добавить собственные настройки, добавляя правильно
## именованные переменные. Например, вы можете раскомментировать следующую
## строчку, чтобы установить ширину кнопок навигации.

# define gui.navigation_button_width = 250


## Кнопки Выбора ###############################################################
##
## Кнопки выбора используются во внутриигровых меню.

define gui.choice_button_width = int(1185*SCALE)
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(int(150*SCALE), int(8*SCALE), int(150*SCALE), int(8*SCALE))
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = "#444444"


## Кнопки Слотов ###############################################################
##
## Кнопка слотов — особый вид кнопки. Она содержит миниатюру и текст,
## описывающий слот сохранения. Слот сохранения использует файлы из gui/button,
## как и другие виды кнопок.

## Кнопка слота сохранения.
define gui.slot_button_width = int(414*SCALE)
define gui.slot_button_height = int(309*SCALE)
define gui.slot_button_borders = Borders(int(15*SCALE), int(15*SCALE), int(15*SCALE), int(15*SCALE))
define gui.slot_button_text_size = int(21*SCALE)
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## Ширина и высота миниатюры, используемой слотом сохранения.
define config.thumbnail_width = int(384*SCALE)
define config.thumbnail_height = int(216*SCALE)

## Количество колонок и рядов в таблице слотов.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Позиционирование и Интервалы ################################################
##
## Эти переменные контролируют позиционирование и интервалы различных элементов
## пользовательского интерфейса.

## Местоположение левого края навигационных кнопок по отношению к левому краю
## экрана.
define gui.navigation_xpos = int(60*SCALE)

## Вертикальная позиция индикатора пропуска.
define gui.skip_ypos = int(15*SCALE)

## Вертикальная позиция экрана уведомлений.
define gui.notify_ypos = int(67.5*SCALE)

## Интервал между выборами в меню.
define gui.choice_spacing = int(33*SCALE)

## Кнопки в секции навигации главного и игрового меню.
define gui.navigation_spacing = int(6*SCALE)

## Контролирует интервал между настройками.
define gui.pref_spacing = int(15*SCALE)

## Контролирует интервал между кнопками настройки.
define gui.pref_button_spacing = 0

## Интервал между кнопками страниц.
define gui.page_spacing = 0

## Интервал между слотами.
define gui.slot_spacing = int(15*SCALE)

## Интервал между слотами.
define gui.slot_spacing_gallery = int(40*SCALE)

## Позиция текста главного меню.
define gui.main_menu_text_xalign = 1.0


## Рамки #######################################################################
##
## Эти переменные контролируют вид рамок, содержащих компоненты
## пользовательского интерфейса, когда наложения или окна не представлены.

## Генерируем рамки.
define gui.frame_borders = Borders(int(6*SCALE), int(6*SCALE), int(6*SCALE), int(6*SCALE))

## Рамки, используемые в частях экрана подтверждения.
define gui.confirm_frame_borders = Borders(int(60*SCALE), int(60*SCALE), int(60*SCALE), int(60*SCALE))

## Рамки, используемые в частях экрана пропуска.
define gui.skip_frame_borders = Borders(int(24*SCALE), int(8*SCALE), int(75*SCALE), int(8*SCALE))

## Рамки, используемые в частях экрана уведомлений.
define gui.notify_frame_borders = Borders(int(24*SCALE), int(8*SCALE), int(60*SCALE), int(8*SCALE))

## Должны ли фоны рамок моститься?
define gui.frame_tile = False


## Панели, Полосы прокрутки и Ползунки #########################################
##
## Эти настройки контролируют вид и размер панелей, полос прокрутки и ползунков.
##
## Стандартный GUI использует только ползунки и вертикальные полосы прокрутки.
## Все остальные полосы используются только в новосозданных экранах.

## Высота горизонтальных панелей, полос прокрутки и ползунков. Ширина
## вертикальных панелей, полос прокрутки и ползунков.
define gui.bar_size = int(37.5*SCALE)
define gui.scrollbar_size = int(18*SCALE)
define gui.slider_size = int(37.5*SCALE)

## True, если изображения панелей должны моститься. False, если они должны быть
## линейно масштабированы.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Горизонтальные границы.
define gui.bar_borders = Borders(int(6*SCALE), int(6*SCALE), int(6*SCALE), int(6*SCALE))
define gui.scrollbar_borders = Borders(int(6*SCALE), int(6*SCALE), int(6*SCALE), int(6*SCALE))
define gui.slider_borders = Borders(int(6*SCALE), int(6*SCALE), int(6*SCALE), int(6*SCALE))

## Вертикальные границы.
define gui.vbar_borders = Borders(int(6*SCALE), int(6*SCALE), int(6*SCALE), int(6*SCALE))
define gui.vscrollbar_borders = Borders(int(6*SCALE), int(6*SCALE), int(6*SCALE), int(6*SCALE))
define gui.vslider_borders = Borders(int(6*SCALE), int(6*SCALE), int(6*SCALE), int(6*SCALE))

## Что делать с непрокручиваемыми полосами прокрутки в интерфейсе. "hide" прячет
## их, а None их показывает.
define gui.unscrollable = "hide"


## История #####################################################################
##
## Экран истории показывает диалог, который игрок уже прошёл.

## Количество диалоговых блоков истории, которые Ren'Py будет хранить.
define config.history_length = int(375*SCALE)

## Высота доступных записей на экране истории, или None, чтобы задать высоту в
## зависимости от производительности.
define gui.history_height = int(210*SCALE)

## Местоположение, ширина и выравнивание заголовка, показывающего имя говорящего
## персонажа.
define gui.history_name_xpos = int(232.5*SCALE)
define gui.history_name_ypos = 0
define gui.history_name_width = int(232.5*SCALE)
define gui.history_name_xalign = 1.0

## Местоположение, ширина и выравнивание диалогового текста.
define gui.history_text_xpos = int(255*SCALE)
define gui.history_text_ypos = int(3*SCALE)
define gui.history_text_width = int(1110*SCALE)
define gui.history_text_xalign = 0.0


## Режим NVL ###################################################################
##
## Экран режима NVL показывает диалог NVL персонажей.

## Границы фона окна NVL.
define gui.nvl_borders = Borders(0, int(15*SCALE), 0, int(30*SCALE))

## Максимальное число показываемых строк в режиме NVL. Когда количество строчек
## начинает превышать это значение, старые строчки очищаются.
define gui.nvl_list_length = 6

## Высота доступных строчек в режиме NVL. Установите на None, чтобы строчки
## динамически регулировали свою высоту.
define gui.nvl_height = int(172.5*SCALE)

## Интервал между строчками в режиме NVL, если gui.nvl_height имеет значение
## None, а также между строчками и меню режима NVL.
define gui.nvl_spacing = int(15*SCALE)

## Местоположение, ширина и выравнивание заголовка, показывающего имя говорящего
## персонажа.
define gui.nvl_name_xpos = int(645*SCALE)
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = int(225*SCALE)
define gui.nvl_name_xalign = 1.0

## Местоположение, ширина и выравнивание диалогового текста.
define gui.nvl_text_xpos = int(675*SCALE)
define gui.nvl_text_ypos = 8
define gui.nvl_text_width = int(885*SCALE)
define gui.nvl_text_xalign = 0.0

## Местоположение, ширина и выравнивание текста nvl_thought (текст от лица
## персонажа nvl_narrator).
define gui.nvl_thought_xpos = int(360*SCALE)
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = int(1170*SCALE)
define gui.nvl_thought_xalign = 0.0

## Местоположение кнопок меню NVL.
define gui.nvl_button_xpos = int(675*SCALE)
define gui.nvl_button_xalign = 0.0

## Локализация #################################################################

## Эта настройка контролирует доступ к разрыву линий. Стандартная настройка
## подходит для большинства языков. Список доступных значений можно найти на
## https://www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## Мобильные устройства
################################################################################

init python:

    ## Этот параметр увеличивает размер быстрых кнопок, чтобы сделать их
    ## доступнее для нажатия на планшетах и телефонах.
    if renpy.variant("touch"):

        gui.quick_button_borders = Borders(int(60*SCALE), int(21*SCALE), int(60*SCALE), 0)

    ## Это изменяет размеры и интервалы различных элементов GUI, чтобы
    ## убедиться, что они будут лучше видны на телефонах.
    if renpy.variant("small"):

        ## Размеры шрифтов.
        gui.text_size = int(45*SCALE)
        gui.name_text_size = int(54*SCALE)
        gui.notify_text_size = int(37.5*SCALE)
        gui.interface_text_size = int(45*SCALE)
        gui.button_text_size = int(45*SCALE)
        gui.label_text_size = int(51*SCALE)

        ## Регулирует местоположение текстового окна.
        gui.textbox_height = int(360*SCALE)
        gui.name_xpos = int(120*SCALE)
        gui.text_xpos = int(135*SCALE)
        gui.text_width = int(1650*SCALE)

        ## Изменяет размеры и интервалы различных объектов.
        gui.slider_size = int(54*SCALE)

        gui.choice_button_width = int(1860*SCALE)

        gui.navigation_spacing = int(30*SCALE)
        gui.pref_button_spacing = int(15*SCALE)

        gui.history_height = int(285*SCALE)
        gui.history_text_width = int(1035*SCALE)

        gui.quick_button_text_size = int(30*SCALE)

        ## Местоположение кнопок слотов.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## Режим NVL.
        gui.nvl_height = int(255*SCALE)

        gui.nvl_name_width = int(457.5*SCALE)
        gui.nvl_name_xpos = int(487.5*SCALE)

        gui.nvl_text_width = int(1372.5*SCALE)
        gui.nvl_text_xpos = int(517.5*SCALE)
        gui.nvl_text_ypos = int(7.5*SCALE)

        gui.nvl_thought_width = int(1860*SCALE)
        gui.nvl_thought_xpos = int(30*SCALE)

        gui.nvl_button_width = int(1860*SCALE)
        gui.nvl_button_xpos = int(30*SCALE)
