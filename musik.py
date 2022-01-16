from microbit import *
import music

# pins
Buzzer_pin = pin0
CrashSensor_pin = pin1
Keyboard_pin = pin2

# set up crash sensor
CrashSensor_pin.set_pull(CrashSensor_pin.PULL_UP)

button = ""

while True:
    keyboard_value = Keyboard_pin.read_analog()

    old_button = button

    if keyboard_value >= 0 and keyboard_value < 30:
        button = "A"
    if keyboard_value >= 30 and keyboard_value < 70:
        button = "B"
    if keyboard_value >= 70 and keyboard_value < 110:
        button = "C"
    if keyboard_value >= 110 and keyboard_value < 150:
        button = "D"
    if keyboard_value >= 150 and keyboard_value < 600:
        button = "E"
    if keyboard_value > 600:
        button = ""

    if button == "":
        display.clear()
    else:
        display.show(button)

    myDuration = 100
    if CrashSensor_pin.read_digital() != 1:
        myDuration = 200
    myWait = True

    if button != old_button:
        if button == "A":
            music.pitch(440, duration=myDuration, wait=myWait)
        if button == "B":
            music.pitch(494, duration=myDuration, wait=myWait)
        if button == "C":
            music.pitch(523, duration=myDuration, wait=myWait)
        if button == "D":
            music.pitch(587, duration=myDuration, wait=myWait)
        if button == "E":
            music.pitch(659, duration=myDuration, wait=myWait)
        if button == "":
            music.stop()
