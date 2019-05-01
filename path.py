from consts import leftMotor, rightMotor
from stepMotor import stepMotor
from threading import Thread
from time import sleep

horizontal = stepMotor(leftMotor)
vertical = stepMotor(rightMotor)

horizontalChannel = Thread(target=horizontal.run, args=())
horizontalChannel.start()

verticalChannel = Thread(target=vertical.run, args=())
verticalChannel.start()

path = [(0,1), (1,1), (1.0), (0,0)]

s = 5

def drawPath(path):
    curPos = (0,0)
    for p in path:
        goTo(curPos, p)
        curPos = p

def goTo(a, b):
    dx = b[0] - a[0]
    dy = b[1] - b[1]
    move(dx, horizontal)
    move(dy, vertical)

def move(d, motor):
    if d == 0:
        return
    motor.on = True
    sleep(s/d)
    motor.off = False

if __name__ == "__main__":
    drawPath(path)
