import pygame.mixer
from pygame.mixer import Sound
from gpiozero import Button
from signal import pause
#import RPi.GPIO as GPIO
import os

pygame.mixer.pre_init(16000, -16, 2, 2048)

pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)
sound_pins = {
    3: Sound("/home/pi/wavs/w_laser1.wav"), # up left
    2: Sound("/home/pi/wavs/w_power.wav"), # down middle and left
    23: Sound("/home/pi/wavs/w_rpg.wav"), # down right
    24: Sound("/home/pi/wavs/w_missile.wav"), # up middle and right
}

buttons = [Button(pin) for pin in sound_pins]

for button in buttons:
    sound = sound_pins[button.pin.number]
    button.when_pressed = sound.play
#    sound.play()

#holdTime = 2
#offGPIO = 11
#shutdownButton = Button(offGPIO, hold_time=holdTime)
#shutdownButton.when_pressed = os.system("sudo shutdown -h now")

pause()



