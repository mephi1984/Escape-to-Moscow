image cg_screen_phone_day = im.FactorScale("CG_hands/new/cg_screen_phone_day.png", SCALE)

image cg_screen_phone_night = im.FactorScale("CG_hands/new/cg_screen_phone_night.png", SCALE)

define cg_screen_phone_pos = Position(xpos = 1.0, xanchor=1.0, ypos=1.0, yanchor=1.0)



image cg_screen_phone_messenger_top_aliya = im.FactorScale("CG_hands/new/messenger_top_aliya.jpg", SCALE)
image cg_screen_phone_messenger_top_aliya_banned = im.FactorScale("CG_hands/new/messenger_top_aliya_banned.jpg", SCALE)
image cg_screen_phone_messenger_top_coach = im.FactorScale("CG_hands/new/messenger_top_coach.jpg", SCALE)
image cg_screen_phone_messenger_top_yarik = im.FactorScale("CG_hands/new/messenger_top_yarik.jpg", SCALE)


image cg_screen_phone_shoot2 = im.FactorScale("CG_hands/new/shoot2.jpg", SCALE)
image cg_screen_phone_shoot3 = im.FactorScale("CG_hands/new/shoot3.jpg", SCALE)
image cg_screen_phone_shoot4 = im.FactorScale("CG_hands/new/shoot4.jpg", SCALE)
image cg_screen_phone_shoot5 = im.FactorScale("CG_hands/new/shoot5.jpg", SCALE)
image cg_screen_phone_shoot6 = im.FactorScale("CG_hands/new/shoot6.jpg", SCALE)

image cg_screen_phone_shoot_anim:
    "cg_screen_phone_shoot2"
    0.4
    "cg_screen_phone_shoot3"
    0.4
    "cg_screen_phone_shoot4"
    0.4
    "cg_screen_phone_shoot5"
    0.4
    "cg_screen_phone_shoot6"

define cg_screen_phone_content_pos = Position(xpos = 1.0, xanchor=1.0, ypos=1.0, yanchor=1.0)

layeredimage right_hand:
    xalign 0.0
    yalign 0.0

    group hand:
        #520x570
        pos (760, 150)
        attribute phone_day:
            "CG_hands/new/cg_screen_phone_day.png"
        attribute phone_night:
            "CG_hands/new/cg_screen_phone_night.png"
        attribute hand_money:
            "CG_hands/new/cg_hand_money.png"
        attribute hand_mask:
            "CG_hands/new/cg_hand_mask.png"
        attribute hand_cup1:
            "CG_hands/new/cg_hand_cup1.png"
        attribute hand_cup2:
            "CG_hands/new/cg_hand_cup2.png"

    group scr:
        pos (846, 224)
        #pos (60, 0)
        attribute day2_msg_yarik:
            #pos (60, 0)
            "CG_hands/new/day2_msg_yarik_night_22_26_new_message.jpg"
        attribute night_check_in1:
            "CG_hands/new/night_check_in1.jpg"
        attribute night_check_in2:
            "CG_hands/new/night_check_in2.jpg"
        attribute day2_msg_aliya:
            "CG_hands/new/day2_msg_aliya_night_23_08_new_message.jpg"

        attribute night_black_screen:
            "CG_hands/new/night_black_screen.jpg"
        attribute day_black_screen:
            "CG_hands/new/day_black_screen.jpg"

        attribute day3_airplane_morning:
            "CG_hands/new/day3_airplane_morning_night_9_30_airplane.jpg"
        attribute day3_airport_morning1:
            "CG_hands/new/day3_airport_morning1_day_9_56_airplane.jpg"
        attribute day3_airport_morning2:
            "CG_hands/new/day3_airport_morning2_9_56_new_message.jpg"
        attribute day3_airport_morning3:
            "CG_hands/new/day3_airport_morning3_day_10_04_new_message.jpg"
        attribute day_check_in1:
            "CG_hands/new/day_check_in1.jpg"
        attribute day_check_in2:
            "CG_hands/new/day_check_in2.jpg"

        attribute day3_afternoon_airplane:
            "CG_hands/new/day3_afternoon_airplane_day_14_20_airplane.jpg"

        attribute day_aeroexpress1:
            "CG_hands/new/day_aeroexpress1.jpg"
        attribute day_aeroexpress2:
            "CG_hands/new/day_aeroexpress2.jpg"
        attribute day_aeroexpress3:
            "CG_hands/new/day_aeroexpress3.jpg"
        attribute day_aeroexpress4:
            "CG_hands/new/day_aeroexpress4.jpg"

        attribute map_taganskaya1:
            "CG_hands/new/map_taganskaya1.jpg"

        attribute map_metro:
            "CG_hands/new/map_metro.jpg"

        attribute day_booking:
            "CG_hands/new/day_booking.jpg"

        attribute day_booking_new_message:
            "CG_hands/new/day_booking_new_message.jpg"

        attribute map_taganskaya2:
            "CG_hands/new/map_taganskaya1.jpg"

        attribute shoot1_time:
            "CG_hands/new/shoot1_time.jpg"
        attribute shoot2:
            "CG_hands/new/shoot2.jpg"
        attribute cg_screen_phone_shoot_anim:
            "cg_screen_phone_shoot_anim"

        attribute day_photo_aliya1:
            "CG_hands/new/day_photo_aliya1.jpg"
        attribute day_photo_aliya2:
            "CG_hands/new/day_photo_aliya2.jpg"

        attribute day3_muslim_store1:
            "CG_hands/new/day3_muslim_store1_day_16_18.jpg"
        attribute day3_muslim_store2:
            "CG_hands/new/day3_muslim_store2_day_16_18_new_message.jpg"

        attribute map_store:
            "CG_hands/new/map_store.jpg"

        attribute map_apartment:
            "CG_hands/new/map_apartment.jpg"

        attribute map_shaurma1:
            "CG_hands/new/map_shaurma1.jpg"
        attribute map_shaurma2:
            "CG_hands/new/map_shaurma2.jpg"

        attribute day3_evening_msg_before_rent_apartment:
            "CG_hands/new/day3_evening_msg_before_rent_apartment_day_18_23_new_message.jpg"

        attribute food_delivery:
            "CG_hands/new/food_delivery.jpg"

        attribute day3_evening_athome_alone:
            "CG_hands/new/day3_evening_athome_alone_day_22_54_new_message.jpg"

        attribute day4_morning1:
            "CG_hands/new/day4_morning1_day_8_47.jpg"
        attribute day4_morning2:
            "CG_hands/new/day4_morning2_day_9_04_new_msg.jpg"

        attribute notes1:
            "CG_hands/new/notes1.jpg"
        attribute notes2:
            "CG_hands/new/notes2.jpg"

        attribute day4_morning3:
            "CG_hands/new/day4_morning3_after_note_imran_day_10_49.jpg"

        attribute day4_evening_athome_alone:
            "CG_hands/new/day4_evening_athome_alone_day_23_12_new_message.jpg"

        attribute day_tickets_buy1:
            "CG_hands/new/day_tickets_buy1.jpg"
        attribute day_tickets_buy2:
            "CG_hands/new/day_tickets_buy2.jpg"
        attribute day_tickets_buy3:
            "CG_hands/new/day_tickets_buy3.jpg"
        attribute day_tickets_buy4:
            "CG_hands/new/day_tickets_buy4.jpg"
        attribute day_tickets_buy5:
            "CG_hands/new/day_tickets_buy5.jpg"

        attribute day4_afternoon_imran_home:
            "CG_hands/new/day4_afternoon_imran_home_12_37.jpg"

        attribute day4_afternoon_airport_duty_free:
            "CG_hands/new/day4_afternoon_airport_duty_free_day_16_12.jpg"

        attribute day_messenger_contacts:
            "CG_hands/new/day_messenger_contacts.jpg"

layeredimage left_hand:
    group hand:
        pos (-640, 180)
        attribute hand_card_day:
            "CG_hands/new/cg_hand_card_day.png"
        attribute hand_sandwich:
            "CG_hands/new/cg_left_hand_sandwich.png"
