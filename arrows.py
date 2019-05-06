from pynput import keyboard
from consts import leftMotor, rightMotor
from stepMotor import stepMotor
from threading import Thread
import os

horizontal = stepMotor(leftMotor)
vertical = stepMotor(rightMotor)

horizontalChannel = Thread(target=horizontal.turnOn, args=())
horizontalChannel.start()

verticalChannel = Thread(target=vertical.turnOn, args=())
verticalChannel.start()


def on_press(key):
    if key == keyboard.Key.left:
        horizontal.clockwise = True
        horizontal.on = True
    if key == keyboard.Key.right:
        horizontal.clockwise = False
        horizontal.on = True
    if key == keyboard.Key.up:
        vertical.clockwise = True
        vertical.on = True
    if key == keyboard.Key.down:
        vertical.clockwise = False
        vertical.on = True


def on_release(key):
    if key == keyboard.Key.left:
        horizontal.on = False
    if key == keyboard.Key.right:
        horizontal.on = False
    if key == keyboard.Key.up:
        vertical.on = False
    if key == keyboard.Key.down:
        vertical.on = False
    

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()






