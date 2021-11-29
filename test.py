import pygame.mixer
from pygame.mixer import Sound
from gpiozero import Button
from signal import pause
import time, os

pygame.mixer.pre_init(16000, -16, 2, 2048)

pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)

laser = Sound("/home/pi/space/wavs/w_laser1.wav")
power = Sound("/home/pi/space/wavs/w_power.wav") 
rpg = Sound("/home/pi/space/wavs/w_rpg.wav")
missile = Sound("/home/pi/space/wavs/w_missile.wav")
#melting = Sound("/home/pi/space/wavs/w1_self_destruct.ogg")
nohome = Sound("/home/pi/space/wavs/w1_system_shut_down.ogg")
# new sounds 2021 - w1 prefix
#weapons = Sound("/home/pi/space/wavs/w1_sci_fi_weapons.ogg")
#binary = Sound("/home/pi/space/wavs/w1_binary_code.ogg")
shields = Sound("/home/pi/space/wavs/w1_shield_up_red_alert.wav")

# holdTime = 6 - this worked with the ImMelting sound, the self destruct sequence is longer, might have to be cut
# holdTime = 73 - this keeps the proportion, but is too long as it is also used to set the time for "when_held"
holdTime = 6
offGPIO = 3

def shutdown():
    # play some shutdown sound
    #melting.stop()
    nohome.play()
    # give it a chance to play for one second
    time.sleep(1)
    # shutdown for real
    #os.system("sudo poweroff")
    os.system("sudo shutdown -h now")

def off_pressed():
    # start playing
    # melting.play(loops=holdTime/melting.get_length())
    #melting.play(loops=3)

def off_released():
    # stop playing if released early
    #melting.stop()

def press_laser():
    # start playing
    laser.play()

def press_power():
    # start playing - used as slower throttle sound
    power.play()

def press_rpg():
    rpg.play()

def press_missile():
    missile.play()

# new functions 2021
def press_weapons():
    #weapons.play()

def press_binary():
    #binary.play()

def press_shields():
    shields.play()

btn1 = Button(11)
btn2 = Button(2)
btn3 = Button(23)
btn4 = Button(24)
# New button: Big red fire button
#btn5 = Button(00)
btnOff = Button(offGPIO, hold_time=holdTime)

#btn1 = when_pressed = press_binary
#btn1.when_pressed = press_laser
btn2.when_pressed = press_shields
#btn2.when_pressed = press_power
btn3.when_pressed = press_rpg
btn4.when_pressed = press_missile
#btn5.when_pressed = press_rpg
btnOff.when_pressed = off_pressed
btnOff.when_released = off_released
btnOff.when_held = shutdown

pause()



