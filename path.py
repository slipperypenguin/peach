from consts import leftMotor, rightMotor
from stepMotor import stepMotor
from threading import Thread
from time import sleep

horizontal = stepMotor(leftMotor)
vertical = stepMotor(rightMotor)

horizontalChannel = Thread(target=horizontal.turnOn, args=())
horizontalChannel.start()

verticalChannel = Thread(target=vertical.turnOn, args=())
verticalChannel.start()

# path = [(0.0,1.0), (1.0,1.0), (1.0,0.0), (0.0,0.0)]
# path = [(-1.0,1.0), (1.0,1.0), (0.0,0.0), (-1.0,-1.0), (1.0, -1.0), (0.0,0.0)]
path = [(-6.0,1.0)]
# path = [(-1.0,0.0)]
# path = [(0.0,-1.0)]

r = 1

def drawPath(path):
    curPos = (0,0)
    for p in path:
        goTo(curPos, p)
        curPos = p

def goTo(a, b):
    dx = b[0] - a[0]
    dy = b[1] - a[1]

    sx = 1
    sy = 1

    magDx = abs(dx)
    magDy = abs(dy)

    if magDx == 0:
        d = magDy
    elif magDy == 0:
        d = magDx
    if magDx == magDy:
        d = magDx
    elif(magDx > magDy):
        d = magDx
        sy = magDy/magDx
    elif(magDx < magDy):
        d = magDy
        sx = magDx/magDy
    
    moveHorz = Thread(target=move, args=(d, -dx, sx, horizontal))
    moveHorz.start()

    moveVert = Thread(target=move, args=(d, dy, sy, vertical))
    moveVert.start()

    moveHorz.join()
    moveVert.join()

def move(a, d, s, motor):
    if d == 0:
        return
    if(d < 0):
        motor.clockwise = True
    else:
        motor.clockwise = False
    motor.setSpeed(s)
    motor.start()
    sleepTime = r * abs(a)
    print("s =", s)
    print("d =", d)
    print("sleepTime =", sleepTime)
    sleep(sleepTime)
    motor.stop()
    motor.reset()

if __name__ == "__main__":
    drawPath(path)
    horizontal.turnOff()
    vertical.turnOff()