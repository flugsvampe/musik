from microbit import *
import music

# pins
Buzzer_pin = pin0
CrashSensor_pin = pin1
Keyboard_pin = pin2

# set up crash sensor
CrashSensor_pin.set_pull(CrashSensor_pin.PULL_UP)

while True:
    # if crash sensor is pressed, play a note, if not stop the music
    if CrashSensor_pin.read_digital() == 1:
        display.set_pixel(0, 0, 0)
        music.stop()

    else:
        display.set_pixel(0, 0, 9)
        music.play("c4:3")

    keyboard_value = Keyboard_pin.read_analog()

    if keyboard_value >= 0 and keyboard_value < 30:
        print("A")
        music.pitch(440)

    if keyboard_value >= 30 and keyboard_value < 70:
        print("B")
        music.pitch(494)

    if keyboard_value >= 70 and keyboard_value < 110:
        print("C")
        music.pitch(523)

    if keyboard_value >= 110 and keyboard_value < 150:
        print("D")
        music.pitch(587)

    if keyboard_value >= 150 and keyboard_value < 600:
        print("E")
        music.pitch(659)

    if keyboard_value > 600:
        music.stop()
