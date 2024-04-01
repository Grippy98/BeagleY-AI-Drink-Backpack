# BeagleY-AI-Drink-Backpack
 

## Important Notes:
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
