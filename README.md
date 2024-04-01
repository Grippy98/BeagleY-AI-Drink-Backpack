# BeagleY-AI-Drink-Backpack

``` git clone https://github.com/Grippy98/BeagleY-AI-Drink-Backpack ```
 
 Docker file exists but is behind times. Stock Beagle install or binary in this repo recommended. 

Code Bits - All code in BeagleY_voice_backpack folder

* PCA9685.py - Motor Driver Library, modified to work with this setup of 2 boards.
* test_microphone.py - Voice Recognition Test, does not engage the pumps
* GUI_only.py - GUI Test, does not engage the pumps
* stop.py - Stops all pumps in case where voice recognition glitches
* combined_test.py - Actual Application Code - voice recognition + pumps


# Accesories:

1. USB Audio Adapter + 3.5mm Microphone - Tested with Logitech C920 Webcam
2. Screen - Waveshare 7.9 in Cap Touch 400x1280 HDMI - https://www.amazon.com/gp/product/B087CNJYB4/ref=ppx_yo_dt_b_search_asin_image?ie=UTF8&psc=1 
3. Adafruit Motor Driver HAT x2, configured for 0x60 and 0x70 I2C adresses respectively 
https://www.adafruit.com/product/2348  


## Important Notes:

* Copy "k3-j722s-evm-mcu-i2c0.dtbo" from the DTBO folder in this repo to /boot/firmware/overlays$  

Then edit /boot/firmware/extlinux/extlinux.conf to load it (last entry only)

* export DISPLAY=:0.0

* sudo apt-get update && sudo apt-get install nano wget python3 python3-pip portaudio19-dev libasound2-dev alsa-utils i2c-tools python3-smbus -y

* sudo pip3 install -r requirements.txt -vvv --break-system-packages 

Create a Folder called:

To find the sound card
* cat /proc/asound/cards

Then create:
/etc/asound.conf 

In it:

``` defaults.pcm.card 1
defaults.ctl.card 1 ```

Where 1 is your sound device number, 0 will be HDMI on BeagleY
