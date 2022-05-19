
def on_forever():
    basic.show_icon(IconNames.HEART)
    basic.pause(500)
    basic.clear_screen()
    basic.show_string("GG")
basic.forever(on_forever)
