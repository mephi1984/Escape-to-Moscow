



default var_day3_photo_made = False

default aliya_trust_points = 0

default aliya_trust_points_hard = 0

default parents_trust_points = 0

default savegame_picture = "savegame_black"

default savegame_text = ""

# See screens.rpy, when counter reaches 10, the debug_mode will be changed
default debug_mode_counter = 0
default debug_mode = False

default day1_advice_asked = False

default day1_first_help_offered = False


default coach_exposition_return_step = 0
# 0 - exposition told at day1 after Semyon asked advice from Coach - return to day1_ask_coach_after_exposition
# 1 - exposition told at day2 morning, after Semyon decided to talk with Coach - return to day2_talk_coach_day1_not_talked_after_exposition
# 2 - exposition told at day2 evening, when Aliya explained situation and Semyon asked advice from Coach - return to day2_escape_now_coach_not_talked_after_exposition
# 3 - exposition told at day2 evening, when Semyon is buying tickets and Coach finally talked to Semyon about Aliya - return to day2_escape_now_success_coach_not_talked_after_exposition

default coach_exposition_general_asked = False

default coach_exposition_danger_asked = False

default coach_exposition_religion_asked = False

default coach_exposition_tradition_asked = False

default coach_exposition_woman1_asked = False

default coach_exposition_woman_love_asked = False

default coach_exposition_woman_decline_marry_asked = False

default coach_exposition_woman_honor_killing_asked = False

default coach_exposition_woman_kidnapping_asked = False



default day1_kidnap_imitate_offered = False

default day1_cancel_wedding_offered = False

define day2_night_car_coach_talked = False

define day2_night_car_yarik_talked = False

default day2_coach_talked = False

default day2_coach_advice_asked = False

default day2_aliya_talked = False

default aliya_banned = False

default day3_address_told = False



define me = Character(_('Семён'), color="#f0f0f0")

define messenger = Character(_('Messenger'), color="#40A7E3")

define coach = Character(_('Напарник'), color="#007F46")

define minjun = Character(_('Minjun Park'), color="#7AA077")

define aliya_mobile = Character(_('Миса Амане'), color="#FFE297")

define aliya = Character(_('Алия'), color="#856F5D")

define yarik = Character(_('Ярик'), color="#687DC9")

define announcement = Character(_('Объявление'), color="#ff4040")

define flight_attendant = Character(_('Бортпроводница'), color="#4F92FF")

define saleswoman = Character(_('Продавщица'), color="#4C8C96")

define salesman_cellular = Character(_('Продавец-консультант'), color="#F5E438")

define landlady = Character(_('Хозяйка'), color="#FF6672")

define aslan = Character(_('Аслан'), color="#C45600")

define fatima = Character(_('Фатима'), color="#3BC600")

define police = Character(_('Участковый'), color="#0094FF")

define imran_unknown = Character(_('Мужчина'), color="#BFB99E")

define imran = Character(_('Имран'), color="#BFB99E")

define officer = Character(_('Пограничник'), color="#8FB5E4")



define apartment_kitchen_food_pos = Position(xpos = 0.3, xanchor=0.5, ypos=0.6, yanchor=0.5)

define apartment_kitchen_aliya_sit_pos = Position(xpos = 0.225, xanchor=0.5, ypos=0.55, yanchor=0.5)

define cafe_table_pos = Position(xpos = 0.5, xanchor=0.5, ypos=0.58, yanchor=0.5)

define any_center_pos = Position(xpos = 0.5, xanchor=0.5, ypos=1.0, yanchor=1.0)

define any_left_pos = Position(xpos = 0.33, xanchor=0.5, ypos=1.0, yanchor=1.0)

define any_right_pos = Position(xpos = 0.66, xanchor=0.5, ypos=1.0, yanchor=1.0)


define any_left_pos2 = Position(xpos = 0.25, xanchor=0.5, ypos=1.0, yanchor=1.0)

define any_right_pos2 = Position(xpos = 0.75, xanchor=0.5, ypos=1.0, yanchor=1.0)


define imran_house_pos1 = Position(xpos = 0.15, xanchor=0.5, ypos=1.0, yanchor=1.0)

define imran_house_pos2 = Position(xpos = 0.4, xanchor=0.5, ypos=1.0, yanchor=1.0)

define imran_house_pos3 = Position(xpos = 0.6, xanchor=0.5, ypos=1.0, yanchor=1.0)

define imran_house_pos4 = Position(xpos = 0.85, xanchor=0.5, ypos=1.0, yanchor=1.0)

define duty_free_aliya_pos = Position(xpos = 0.15, xanchor=0.5, ypos=1.0, yanchor=1.0)

define aliya_metro_buy_card_pos = Position(xpos = 0.4, xanchor=0.5, ypos=1.0, yanchor=1.0)
define aliya_metro_buy_card_straight_pos = Position(xpos = 0.435, xanchor=0.5, ypos=1.0, yanchor=1.0)

define aliya_imran_room_pos = Position(xpos = 0.45, xanchor=0.5, ypos=1.0, yanchor=1.0)

define aliya_cafe_pos = Position(xpos = 0.45, xanchor=0.5, ypos=0.6, yanchor=0.5)

define aliya_apartment_kitchen_stand_pos = Position(xpos = 0.85, xanchor=0.5, ypos=1.0, yanchor=1.0)


define aliya_hood_right_pos = Position(xpos = 0.75, xanchor=0.5, ypos=1.0, yanchor=1.0)


define isMobileWeb = True

image splash = "splash.png"

init python:
    renpy.music.register_channel("music_crossfade","music",loop=True,tight=True)
    #global webTestCall
    #def webTestCall():
    #    renpy.play('sound/seatbelt.ogg')


    if isMobileWeb:
        config.has_autosave = True
        config.autosave_frequency = 10
        config.autosave_on_choice = True


image splash = "splash.png"

label splashscreen:

    scene black
    with Pause(1)

    show splash with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    if not isMobileWeb:
        if not persistent.lang_chosen:
            $ persistent.lang_chosen = True
            call screen language_and_difficulty_menu_first_time

    return

# Игра начинается здесь:
label start:

    # Adding empty message for each dialog, to fill the area at pos (-1) right under the mess



    $ var_message_queue = {'coach' : [{'special': True, 'type': 0, 'phoneType' : 0}], 'minjun' : [{'special': True, 'type': 0, 'phoneType' : 0}], 'aliya' : [{'special': True, 'type': 0, 'phoneType' : 0}], 'yarik' : [{'special': True, 'type': 0, 'phoneType' : 0}]}

    $ var_current_dialog = 'coach'

    $ var_current_dialog_order = []

    $ var_message_count_coach = 1

    $ var_message_count_minjun = 1

    $ var_message_count_aliya = 1

    $ var_message_count_yarik = 1

    $ var_messenger_is_phone = False

    $ var_day3_photo_made = False

    $ savegame_picture = "savegame_black"

    jump day1_intro
