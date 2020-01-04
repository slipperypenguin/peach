from time import sleep
import RPi.GPIO as GPIO

DIR = 20   # Direction GPIO Pin color: yellow
STEP = 21  # Step GPIO Pin color: green
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
#SPR = 48   # Steps per Revolution (360 / 7.5)
SPR = 168   # Steps per Revolution (360 / 7.5)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

step_count = SPR
#delay = .0209
delay = .0015
#delay = .0059

for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

sleep(.5)
GPIO.output(DIR, CCW)
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

GPIO.cleanup()
