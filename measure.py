import os
import time
import math
import subprocess
from sense_hat import SenseHat
sense = SenseHat()

OFFSET_LEFT = 1
OFFSET_TOP = 2

NUMS =[1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,  # 0
       0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,  # 1
       1,1,1,0,0,1,0,1,0,1,0,0,1,1,1,  # 2
       1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,  # 3
       1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,  # 4
       1,1,1,1,0,0,1,1,1,0,0,1,1,1,1,  # 5
       1,1,1,1,0,0,1,1,1,1,0,1,1,1,1,  # 6
       1,1,1,0,0,1,0,1,0,1,0,0,1,0,0,  # 7
       1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,  # 8
       1,1,1,1,0,1,1,1,1,0,0,1,0,0,1]  # 9

# Displays a single digit (0-9)
def show_digit(val, xd, yd, r, g, b):
  offset = val * 15
  for p in range(offset, offset + 15):
    xt = p % 3
    yt = (p-offset) // 3
    sense.set_pixel(xt+xd, yt+yd, r*NUMS[p], g*NUMS[p], b*NUMS[p])

# Displays a two-digits positive number (0-99)
def show_number(val, r, g, b):
  abs_val = math.trunc(float(val))
  tens = abs_val // 10
  units = abs_val % 10
  if (abs_val > 9): show_digit(tens, OFFSET_LEFT, OFFSET_TOP, r, g, b)
  show_digit(units, OFFSET_LEFT+4, OFFSET_TOP, r, g, b)



sense.clear()
sense.load_image("img/balena.png")
time.sleep(2)
sense.clear()

count = 0

RED=[255,0,0]
GREEN=[0,255,0]
BLUE=[0,0,255]
ORANGE=[255,69,0]


def read_cpu_temperature():
    cpu_temp = subprocess.check_output("vcgencmd measure_temp", shell=True).decode('utf-8')
    temperature = float(cpu_temp.split("=")[1].split("'")[0])
    return float("{:.2f}".format(temperature))


def compute_temperature():
    cpu_temp = read_cpu_temperature()
    hat_temp = float(sense.temperature)
    print("CPU TEMP {} ".format(cpu_temp))
    print("HAT TEMP {}".format(hat_temp))
    humidity_temp = sense.get_temperature_from_humidity()
    print("PRESSURE TEMP {}".format(humidity_temp))

    FACTOR = 5.466
    temp_calibrated = hat_temp - ((cpu_temp - hat_temp)/FACTOR)
    print("TEMP {}".format(temp_calibrated))
    return temp_calibrated

while 1:
    temperature = compute_temperature()
    humidity = float(sense.humidity)
    pressure = float(sense.pressure)

    measurements = [
        {
            'measurement': 'temperature',
            'fields': {
                'value':  temperature
            }
        }
    ]

    measurements.extend([
        {
            'measurement': 'humidity',
            'fields': {
                'value': humidity
            }
        }
    ])

    measurements.extend([
        {
            'measurement': 'pressure',
            'fields': {
                'value': pressure
            }
        }
    ])

    #sense.show_message("{}".format(trunc(temperature)), text_colour=RED)
    #sense.show_message("{}".format(trunc(humidity)), text_colour=BLUE)
    #sense.show_message("{}".format(trunc(pressure)), text_colour=GREEN)
    show_number("{}".format(temperature), 255,0,0)
    time.sleep(5)
    show_number("{}".format(humidity),0,255,0)
    # show_number("{}".format(pressure), 0,0,255)
    time.sleep(3)



