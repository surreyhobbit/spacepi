# spacepi
space console project

Raspberry PI generation 1 with GPIO to produce sounds when buttons are pressed.
Power supply is via USB 5V (together with Arduino LEDs).

## Connectivity
Using the WiPi dongle the raspberry Pi is connected to WLAN with a fix local IP address (192.168.0.207).
It is also reachable using ssh via spacepi.local

## Source for soundfiles

Youtube Sound Response:
* https://www.youtube.com/channel/UC2FLOcV3S6LspWhJdEaflwQ

Download to mp3:
https://ytmp3.cc/uu6cc/

Convert to wav or ogg:
https://convertio.co/download/0c0870ae67efb4cbc606224847ac488517ef05/


## Shutdown :
1. shutdown with a button together with playing sounds using pygame mixer

for rescue restart of the rapsberry, add systemd.unit=rescue.target at the end of the cmdline.txt file on the boot SD card.
https://raspberrypi.stackexchange.com/questions/61638/how-do-i-start-up-in-safemode

brilliant article her: https://github.com/TonyLHansen/raspberry-pi-safe-off-switch


## Open issue
Might want a graceful way to shutdown even without pressing the button.
and about scheduling with crontab:
https://www.raspberrypi.org/documentation/linux/usage/cron.md




