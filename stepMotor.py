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

    def rotate(self, x):
        ## need to test
        x = int(x)
        if x < 0:
            step = -1
        elif x > 0:
            step = 1
        else:
            return
        if step != self.prev:
            print('re-aligning')
            x += 24*step
        for i in range(int(abs(x))):
          for halfstep in range(8):
            for pin in range(4):
              GPIO.output(self.control_pins[pin], self.halfstep_seq[::step][halfstep][pin])
            time.sleep(0.002)
        self.prev = step


    def close(self):
        GPIO.cleanup
