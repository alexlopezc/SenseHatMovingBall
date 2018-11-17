from sense_hat import SenseHat, ACTION_RELEASED
import time
from Ball import Ball
from random import getrandbits
import sys

while True:
    for i in range(5):
        self.sense.load_image("img/heart8.png")
        time.sleep(0.5)
        self.sense.clear()
        time.sleep(0.5)
    self.sense.show_message("TE QUIERO")
    time.sleep(1)