from stepMotor import stepMotor
import time

horizontal_pins = [7,11,13,15]
vertical_pins = [31,33,35,37]

horizontalMotor = stepMotor(horizontal_pins)
verticalMotor = stepMotor(vertical_pins)

horizontalMotor.rotate(40)  # move cursor 40 units right
horizontalMotor.rotate(-40) # move cursor 40 units left
verticalMotor.rotate(40)  # move cursor 40 units up
verticalMotor.rotate(-40) # move cursor 40 units down

horizontalMotor.close()
verticalMotor.close()

## Create a diagonal line
# alternate instructions to the horizontal and vertical motors
for step in range(40):
	horizontalMotor.rotate(1)
	verticalMotor.rotate(1)


## calibration
def calibrate(iters = 20):
    leftMotor = stepMotor([7,11,13,15])
    rightMotor = stepMotor([31,33,35,37])
    step = 512
    for i in range(iters):
        leftMotor.rotate(step)
        rightMotor.rotate(step)
        leftMotor.rotate(-step)
        rightMotor.rotate(-step)
