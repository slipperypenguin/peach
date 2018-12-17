import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
control_pins = [7,11,13,15,31,33,35,37]
leftMotor = [7,11,13,15]
rightMotor = [31,33,35,37]
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
halfstep_seq = [
  [1,0,0,1],
  [0,0,0,1],
  [0,0,1,1],
  [0,0,1,0],
  [0,1,1,0],
  [0,1,0,0],
  [1,1,0,0],
  [1,0,0,0]
]
for i in range(512):
  for halfstep in range(8):
    for pin in range(4):
      GPIO.output(leftMotor[pin], halfstep_seq[halfstep][pin])
      GPIO.output(rightMotor[pin], halfstep_seq[halfstep][pin])
    time.sleep(0.001)
GPIO.cleanup()