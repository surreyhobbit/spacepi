import pygame.mixer
from pygame.mixer import Sound
from gpiozero import Button
from signal import pause
import time, os

pygame.mixer.pre_init(44100, -16, 2, 2048)

pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)

laser = Sound("/home/pi/space/wavs/w_laser1.wav")
weapons = Sound("/home/pi/space/wavs/w2_weapons.ogg")
vector = Sound("/home/pi/space/wavs/w_vector.wav")
#power = Sound("/home/pi/space/wavs/w_power.wav") 
rpg = Sound("/home/pi/space/wavs/w_rpg.wav")
missile = Sound("/home/pi/space/wavs/w_missile.wav")
melting = Sound("/home/pi/space/wavs/w2_self_destruct_short.ogg")
nohome = Sound("/home/pi/space/wavs/w1_system_shut_down.ogg")
shields = Sound("/home/pi/space/wavs/w1_shields_up_red_alert.wav")

holdTime = 6
offGPIO = 3

def shutdown():
    # play some shutdown sound
    melting.stop()
    nohome.play()
    # give it a chance to play for one second
    time.sleep(1)
    # shutdown for real
    #os.system("sudo poweroff")
    os.system("sudo shutdown -h now")

def off_pressed():
    # start playing
    #melting.play(loops=holdTime/melting.get_length())
    melting.play(loops=3)

def off_released():
    # stop playing if released early
    melting.stop()

def press_laser():
    # start playing
    laser.play()

def press_weapon():
    weapons.play()

#def press_power():
    # start playing
#    power.play()

def press_shields():
    #start playing
    shields.play()

def press_rpg():
    rpg.play()

def press_missile():
    missile.play()

btn1 = Button(11)
btn2 = Button(2)
btn3 = Button(23)
btn4 = Button(24)
btnFire = Button(22)
btnOff = Button(offGPIO, hold_time=holdTime)

btn1.when_pressed = press_laser
btn2.when_pressed = press_shields
btn3.when_pressed = press_rpg
btn4.when_pressed = press_missile
btnFire.when_pressed = press_weapon
btnOff.when_pressed = off_pressed
btnOff.when_released = off_released
btnOff.when_held = shutdown

vector.play()

pause()



