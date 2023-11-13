randNum = 0

def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global randNum
    randNum = randint(0, 2)
    if randNum == 0:
        basic.show_leds("""
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            """)
    elif randNum == 1:
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            """)
    else:
        basic.show_leds("""
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    basic.show_leds("""
        # # . . #
        # # . # .
        . . # . .
        # # . # .
        # # . . #
        """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        . # # # .
        . # # # .
        . # # # .
        . # # # .
        . # # # .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)
