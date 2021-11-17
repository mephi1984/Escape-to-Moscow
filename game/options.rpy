## Данный файл содержит настройки, способные изменить вашу игру.
##
## Строки, начинающиеся  с двух '#' — комментарии, и вы не должны их
## раскомментировать. Строки, начинающиеся с одной '#' — комментированный код,
## который вы можете раскомментировать, если посчитаете это нужным.


## Основное ####################################################################

## Читаемое название игры. Используется при установке стандартного заголовка
## окна, показывается в интерфейсе и отчётах об ошибках.
##
## Символы "_()", окружающие название, отмечают его как пригодное для перевода.

define config.name = _("Побег в Москву")


## Определяет, показывать ли заголовок, данный выше, на экране главного меню.
## Установите на False, чтобы спрятать заголовок.

define gui.show_name = True


## Версия игры.

define config.version = "1.5.0"


## Текст, помещённый в экран "Об игре". Поместите текст между тройными скобками.
## Для отделения абзацев оставляйте между ними пустую строку.


define credits_text1_line1 = Text(_("{color=#FFD800}Продюсер:{/color}\nВладислав Хорев"), size=int(50*SCALE))
define credits_text1_line2 = Text(_("{color=#FFD800}Разработчик:{/color}\nВладислав Хорев"), size=int(50*SCALE))
define credits_text1_line3 = Text(_("{color=#FFD800}Автор сценария:{/color}\nВладислав Хорев"), size=int(50*SCALE))
define credits_text1_line4 = Text(_("{color=#FFD800}Тексты:{/color}\nВладислав Хорев\nЯна \"Samadreal\" Однорог, Таша Фам, Вячеслав \"saBBar\" Левин"), size=int(50*SCALE))

define credits_text1_line5 = Text(_("{color=#FFD800}Спрайты персонажей:{/color}\nДарья \"miZaria\" Фролова\nSsurikin\nMarys (Маша Свиридова)\nТатьяна \"Akinago\" Аверина"), size=int(50*SCALE))


define credits_text1_line61 = Text(_("{color=#FFD800}Фоны:{/color}\nQuandial\nАнонимный художник"), size=int(50*SCALE))

define credits_text1_line62 = Text(_("{color=#FFD800}Прочие изображения:{/color}\nДарья \"miZaria\" Фролова\nЕлизавета \"Lyss\" Попкова\nАнонимный художник"), size=int(50*SCALE))


define credits_text1_line7 = Text(_("{color=#FFD800}Музыка:{/color}\nRomull"), size=int(50*SCALE))

define credits_text1_line8 = Text(_("{color=#FFD800}Звуки и амбиент:{/color}\nВладислав Хорев\nflorianreichelt (freesound.org)"), size=int(50*SCALE))


define credits_text1_line9 = Text(_("{color=#FFD800}Моушн-дизайн:{/color}\nДмитрий Журавский (night_xevf)"), size=int(50*SCALE))


define gui.about = ("""
Наша группа: {u}https://vk.com/escapetomoscow{/u}

{color=#FFD800}Продюсер:{/color} Владислав Хорев
{color=#FFD800}Разработчик:{/color} Владислав Хорев
{color=#FFD800}Автор сценария:{/color} Владислав Хорев
{color=#FFD800}Тексты:{/color} Владислав Хорев, Яна "Samadreal" Однорог, Таша Фам, Вячеслав "saBBar" Левин
{color=#FFD800}Спрайты персонажей:{/color} Дарья "miZaria" Фролова, Ssurikin, Marys (Маша Свиридова), Татьяна "Akinago" Аверина
{color=#FFD800}Фоны:{/color} Quandial, Анонимный художник
{color=#FFD800}Прочие изображения:{/color} Дарья "miZaria" Фролова, Елизавета "Lyss" Попкова, Анонимный художник
{color=#FFD800}Музыка:{/color} Romull
{color=#FFD800}Звуки и амбиент:{/color} Владислав Хорев, florianreichelt (freesound.org)
{color=#FFD800}Моушн-дизайн:{/color} Дмитрий Журавский (night_xevf)

Сделано с помощью Ren'Py
""")


## Короткое название игры, используемое для исполняемых файлов и директорий при
## постройке дистрибутивов. Оно должно содержать текст формата ASCII и не должно
## содержать пробелы, двоеточия и точки с запятой.

define build.name = "EscapeToMoscow"


## Звуки и музыка ##############################################################

## Эти три переменные контролируют соответствующие микшеры громкости в
## настройках, которые игрок может настраивать по умолчанию. Изменив один из
## параметров на False, скроется соответствующий микшер.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## Чтобы разрешить игроку тестировать громкость на звуковом или голосовом
## каналах, раскомментируйте строчку и настройте пример звука для прослушивания.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Раскомментируйте следующую строчку, чтобы настроить аудиофайл, который будет
## проигрываться в главном меню. Этот файл продолжит проигрываться во время
## игры, если не будет остановлен, или не начнёт проигрываться другой аудиофайл.

#define config.main_menu_music = "music/Runaway_01 (Main).ogg"


## Переходы ####################################################################
##
## Эти переменные задают переходы, используемые в различных событиях. Каждая
## переменная должна задавать переход или None, чтобы указать на то, что переход
## не должен использоваться.

## Вход и выход в игровое меню.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Переход между экранами игрового меню.

define config.intra_transition = dissolve


## Переход, используемый после загрузки слота сохранения.

define config.after_load_transition = None


## Используется при входе в главное меню после того, как игра закончится.

define config.end_game_transition = dissolve


## Переменная, устанавливающая переход, когда старт игры не существует. Вместо
## неё используйте функцию with после показа начальной сценки.


## Управление окнами ###########################################################
##
## Эта строка контролирует, когда появляется диалоговое окно. Если "show" — оно
## всегда показано. Если "hide" — оно показывается, только когда представлен
## диалог. Если "auto" — окно скрыто до появления оператора scene и показывается
## при появлении диалога.
##
## После начала игры этот параметр можно изменить с помощью "window show",
## "window hide" и "window auto".

define config.window = "auto"

define config.predict_statements = 2


## Переходы, используемые при показе и скрытии диалогового окна

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

#define config.debug_image_cache = True
#define config.image_cache_size = 10
define config.image_cache_size_mb = 200

## Стандартные настройки #######################################################

## Контролирует стандартную скорость текста. По умолчанию, это 0 — мгновенно,
## в то время как любая другая цифра — это количество символов, печатаемых в
## секунду.

default preferences.text_cps = 0


## Стандартная задержка авточтения. Большие значения означают долгие ожидания, а
## от 0 до 30 — вполне допустимый диапазон.

default preferences.afm_time = 15


## Директория сохранений #######################################################
##
## Контролирует зависимое от платформы место, куда Ren'Py будет складывать файлы
## сохранения этой игры. Файлы сохранений будут храниться в:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## Этот параметр обычно не должен изменяться, а если и изменился, должен быть
## текстовой строчкой, а не выражением.

define config.save_directory = "Runaway-1558914204"


## Иконка ######################################################################
##
## Иконка, показываемая на панели задач или на dock.

define config.window_icon = "gui/window_icon.png"




define config.autosave_on_choice = False

define config.autosave_on_quit = False

define config.has_autosave = False

## Настройка Дистрибутива ######################################################
##
## Эта секция контролирует, как Ren'Py строит дистрибутивные файлы из вашего
## проекта.

init python:

    ## Следующие функции берут образцы файлов. Образцы файлов не учитывают
    ## регистр и соответствующе зависят от директории проекта (base), с или без
    ## учёта /, задающей директорию. Если обнаруживается множество одноимённых
    ## файлов, то используется только первый.
    ##
    ## Инструкция:
    ##
    ## / — разделитель директорий.
    ##
    ## * включает в себя все символы, исключая разделитель директорий.
    ##
    ## ** включает в себя все символы, включая разделитель директорий.
    ##
    ## Например, "*.txt" берёт все файлы формата txt из директории base, "game/
    ## **.ogg" берёт все файлы ogg из директории game и всех поддиректорий, а
    ## "**.psd" берёт все файлы psd из любого места проекта.

    ## Классифицируйте файлы как None, чтобы исключить их из дистрибутивов.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## Чтобы архивировать файлы, классифицируйте их, например, как 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Файлы, соответствующие образцам документации, дублируются в приложениях
    ## Mac, чтобы они появлялись и в приложении, и в zip архиве.

    build.documentation('*.html')
    build.documentation('*.txt')

## Эта строка отвечает за подписывание игры на Mac с помощью вашего Apple ID.
## Подписывайте только со своего Apple Developer ID.

# define build.mac_identity = "Developer ID Application: Guy Shy (XHTE5H7Z42)"


## Лицензионный ключ Google Play требуется для загрузки файлов расширений и
## поддержки внутриигровых покупок. Он может быть найден на странице "Services &
## APIs" консоли разработчика Google Play.

define build.google_play_key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv3JnsHstHYwtZx7I9/VYXiAygGciiga1gIe9haRutNrBPgEU/MXvZGVIDmni1wl/gJJOTaTRliAJDNYMsB5qx84mxtCQFHp//nagcRbtSOyPrsEXnjMe7hcW0FVjhe9gzHI4zDY9RSyXwH1poyqX1c6T/KL3Bm8zXjTn5LEB25/IG3W/Ac8JpdEo3HyPB03bbRfld7D6fmReBXZXincLgx/NhvzWDzs9fPpQUwH/kHHOSK8oVP3nW0Tc7gDmCEIdbXci7Ca6OJu5tdTGFNTzUud+QkebwvEcOW0UteBE1+9WCpQPVaVI/3aLXPYP7OoQjJZTN67Mh/wlrf6ub5wnjQIDAQAB"


## Имя пользователя и название проекта, ассоциированные с проектом на itch.io,
## разделённые дробью.

define build.itch_project = "mephi1984/escape-to-moscow"

define config.default_fullscreen = True


default persistent.difficulty = 0 # 0 = easy; 1 = normal
