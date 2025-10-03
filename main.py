def on_forever():
    if input.button_is_pressed(Button.A):
        for index in range(10):
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                """)
basic.forever(on_forever)

def on_forever2():
    basic.show_leds("""
        . . . . .
        . . # . .
        . . # . .
        # # # # #
        # # # # #
        """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . # . .
        # # # # #
        """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . # . .
        . . # . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . # . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(50)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . # . # .
        """)
    basic.pause(50)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . # . # .
        . . . . .
        """)
    basic.pause(50)
    basic.show_leds("""
        . . . . .
        . . . . .
        . # . # .
        . . . . .
        . . . . .
        """)
    basic.pause(50)
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(50)
    basic.show_leds("""
        . . # . .
        # . # . #
        . # . # .
        # . # . #
        . . # . .
        """)
    basic.pause(50)
    basic.show_leds("""
        # . # . #
        # . . . #
        . . . . .
        # . . . #
        # . # . #
        """)
    basic.pause(50)
    basic.show_leds("""
        # . . . #
        . . . . .
        . . . . .
        . . . . .
        # . . . #
        """)
    basic.pause(50)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(50)
    basic.show_leds("""
        . . . . .
        # # . . .
        . . . # #
        . . . . .
        . . . . .
        """)
    basic.pause(50)
    basic.show_leds("""
        . . . . .
        # . . . .
        . . # # .
        . . . . .
        . . . . .
        """)
    basic.pause(50)
    basic.show_leds("""
        . . . . .
        . . . . #
        . # # . .
        . . . . .
        . . . . .
        """)
    basic.pause(50)
    basic.show_leds("""
        . . . . .
        . . . # #
        # # . . .
        . . . . .
        . . . . .
        """)
    basic.pause(50)
    basic.show_leds("""
        . . . . .
        . . # # .
        # . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(50)
    basic.show_leds("""
        . . . . .
        . # # . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(50)
    basic.show_leds("""
        . . . . .
        # # . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(50)
    basic.show_leds("""
        . . . . .
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(50)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(50)
basic.forever(on_forever2)
