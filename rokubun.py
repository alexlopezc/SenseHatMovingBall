
def rokubun_logo(sense):
    sense.clear()
    sense.set_pixel(0, 1, 0, 0, 255)
    sense.set_pixel(1, 1, 0, 0, 255)
    sense.set_pixel(2, 1, 0, 0, 255)
    sense.set_pixel(0, 2, 0, 0, 255)
    sense.set_pixel(0, 3, 0, 0, 255)
    sense.set_pixel(0, 4, 0, 0, 255)
    sense.set_pixel(0, 5, 0, 0, 255)
    sense.set_pixel(0, 6, 0, 0, 255)
    sense.set_pixel(0, 6, 0, 0, 255)
    sense.set_pixel(1, 6, 0, 0, 255)
    sense.set_pixel(2, 6, 0, 0, 255)

    sense.set_pixel(5, 1, 0, 0, 255)
    sense.set_pixel(6, 1, 0, 0, 255)
    sense.set_pixel(7, 1, 0, 0, 255)
    sense.set_pixel(7, 2, 0, 0, 255)
    sense.set_pixel(7, 3, 0, 0, 255)
    sense.set_pixel(7, 4, 0, 0, 255)
    sense.set_pixel(7, 5, 0, 0, 255)
    sense.set_pixel(7, 6, 0, 0, 255)
    sense.set_pixel(5, 6, 0, 0, 255)
    sense.set_pixel(6, 6, 0, 0, 255)
    sense.set_pixel(7, 6, 0, 0, 255)

    sense.set_pixel(3, 3, 255,69,0)
    sense.set_pixel(3, 4, 255,69,0)
    sense.set_pixel(4, 3, 255,69,0)
    sense.set_pixel(4, 4, 255,69,0)

    sense.show_message("ROKUBUN")