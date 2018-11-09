import RPi.GPIO as GPIO
import time

class stepMotor(object):
    def __init__(self, control_pins):
        GPIO.setmode(GPIO.BOARD)
        self.control_pins = control_pins
        self.prev = 0
        self.halfstep_seq = [
            [1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,1,1],
            [0,0,0,1],
            [1,0,0,1]
          ]

         for pin in self.control_pins:
             GPIO.setup(pin, GPIO.OUT)
             GPIO.output(pin, 0)

    def rotate(self, n):
        int(n)
        ## need to write this still


    def close(self):
        GPIO.cleanup
