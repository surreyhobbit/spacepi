import pygame.mixer
from pygame.mixer import Sound
from gpiozero import Button
from signal import pause
import time, os

pygame.mixer.pre_init(16000, -16, 2, 2048)

pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)

laser = Sound("/home/pi/wavs/w_laser1.wav")
power = Sound("/home/pi/wavs/w_power.wav") 
rpg = Sound("/home/pi/wavs/w_rpg.wav")
missile = Sound("/home/pi/wavs/w_missile.wav")

holdTime = 10
offGPIO = 11

def shutdown():
    # play some shutdown sound
    # to be added
    # give it a chance to play for one second
    time.sleep(1)
    # shutdown for real
    os.system("sudo poweroff")
    #os.system("sudo shutdown -h now")

def press_laser():
    # start playing
    laser.play()

def press_power():
    # start playing
    power.play()

def press_rpg():
    rpg.play()

def press_missile():
    missile.play()


btn3 = Button(3)
btn2 = Button(2)
btn23 = Button(23)
btn24 = Button(24)
btnOff = Button(offGPIO, hold_time=holdTime)

btn3.when_pressed = press_laser
btn2.when_pressed = press_power
btn23.when_pressed = press_rpg
btn24.when_pressed = press_missile
btnOff.when_held = shutdown

pause()



