#!/usr/bin/python

from PCA9685 import PCA9685
import time

pumpDuration = 3
purgeTime = 6

import argparse
import queue
import sys
import sounddevice as sd

import json

from vosk import Model, KaldiRecognizer

acceptedWords = '["stop", "prime", "red", "green", "blue", "orange", "purple", "yellow", "[unk]"]'


Dir = [
    'forward',
    'backward',
]
pwm = PCA9685(0x60, debug=False)
pwm.setPWMFreq(50)

pwm2 = PCA9685(0x61, debug=False)
pwm2.setPWMFreq(50) 

class MotorDriver():
    def __init__(self):

        #Adafruit TB6612FNG #1
        self.PWMA = 8
        self.AIN1 = 10
        self.AIN2 = 9
        self.PWMB = 13
        self.BIN1 = 11
        self.BIN2 = 12

        #Adafruit TB6612FNG #2

        self.PWMA_2 = 2
        self.AIN1_2 = 4
        self.AIN2_2 = 3
        self.PWMB_2 = 7
        self.BIN1_2 = 5
        self.BIN2_2 = 6

    def MotorRun(self, motor, index, speed):
        if speed > 100:
            return
        if(motor == 0):
            pwm.setDutycycle(self.PWMA, speed)
            if(index == Dir[0]):
                pwm.setLevel(self.AIN1, 0)
                pwm.setLevel(self.AIN2, 1)
            else:
                pwm.setLevel(self.AIN1, 1)
                pwm.setLevel(self.AIN2, 0)
        if(motor == 1):
            pwm.setDutycycle(self.PWMB, speed)
            if(index == Dir[0]):
                pwm.setLevel(self.BIN1, 0)
                pwm.setLevel(self.BIN1, 1)
            else:
                pwm.setLevel(self.BIN1_2, 1)
                pwm.setLevel(self.BIN2_2, 0)
        if(motor == 2):
            pwm.setDutycycle(self.PWMA_2, speed)
            if(index == Dir[0]):
                pwm.setLevel(self.AIN1_2, 0)
                pwm.setLevel(self.AIN2_2, 1)
            else:
                pwm.setLevel(self.AIN1_2, 1)
                pwm.setLevel(self.AIN2_2, 0)
        if(motor == 3):
            pwm.setDutycycle(self.PWMB_2, speed)
            if(index == Dir[0]):
                pwm.setLevel(self.BIN1_2, 0)
                pwm.setLevel(self.BIN2_2, 1)
            else:
                pwm.setLevel(self.BIN1_2, 1)
                pwm.setLevel(self.BIN2_2, 0)
        

    def MotorStop(self, motor):
        if (motor == 0):
            pwm.setDutycycle(self.PWMA, 0)
        elif (motor == 1):
            pwm.setDutycycle(self.PWMB, 0)
        elif (motor == 2):
            pwm.setDutycycle(self.PWMA_2, 0)
        elif (motor == 3):
            pwm.setDutycycle(self.PWMB_2, 0)

            
class MotorDriver2():
    def __init__(self):

        #Adafruit TB6612FNG #1
        self.PWMA = 8
        self.AIN1 = 10
        self.AIN2 = 9
        self.PWMB = 13
        self.BIN1 = 11
        self.BIN2 = 12

        #Adafruit TB6612FNG #2

        self.PWMA_2 = 2
        self.AIN1_2 = 4
        self.AIN2_2 = 3
        self.PWMB_2 = 7
        self.BIN1_2 = 5
        self.BIN2_2 = 6

    def MotorRun(self, motor, index, speed):
        if speed > 100:
            return
        if(motor == 0):
            pwm2.setDutycycle(self.PWMA, speed)
            if(index == Dir[0]):
                pwm2.setLevel(self.AIN1, 0)
                pwm2.setLevel(self.AIN2, 1)
            else:
                pwm2.setLevel(self.AIN1, 1)
                pwm2.setLevel(self.AIN2, 0)
        if(motor == 1):
            pwm2.setDutycycle(self.PWMB, speed)
            if(index == Dir[0]):
                pwm2.setLevel(self.BIN1, 0)
                pwm2.setLevel(self.BIN1, 1)
            else:
                pwm2.setLevel(self.BIN1_2, 1)
                pwm2.setLevel(self.BIN2_2, 0)
        if(motor == 2):
            pwm2.setDutycycle(self.PWMA_2, speed)
            if(index == Dir[0]):
                pwm2.setLevel(self.AIN1_2, 0)
                pwm2.setLevel(self.AIN2_2, 1)
            else:
                pwm2.setLevel(self.AIN1_2, 1)
                pwm2.setLevel(self.AIN2_2, 0)
        if(motor == 3):
            pwm2.setDutycycle(self.PWMB_2, speed)
            if(index == Dir[0]):
                pwm2.setLevel(self.BIN1_2, 0)
                pwm2.setLevel(self.BIN2_2, 1)
            else:
                pwm2.setLevel(self.BIN1_2, 1)
                pwm2.setLevel(self.BIN2_2, 0)
        

    def MotorStop(self, motor):
        if (motor == 0):
            pwm2.setDutycycle(self.PWMA, 0)
        elif (motor == 1):
            pwm2.setDutycycle(self.PWMB, 0)
        elif (motor == 2):
            pwm2.setDutycycle(self.PWMA_2, 0)
        elif (motor == 3):
            pwm2.setDutycycle(self.PWMB_2, 0)

print("this is a motor driver test code")
Motor = MotorDriver()
Motor2 = MotorDriver2()
#sd.default.device = 1

q = queue.Queue()

def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    "-l", "--list-devices", action="store_true",
    help="show list of audio devices and exit")
args, remaining = parser.parse_known_args()
if args.list_devices:
    print(sd.query_devices())
    parser.exit(0)
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser])
parser.add_argument(
    "-f", "--filename", type=str, metavar="FILENAME",
    help="audio file to store recording to")
parser.add_argument(
    "-d", "--device", type=int_or_str,
    help="input device (numeric ID or substring)")
parser.add_argument(
    "-r", "--samplerate", type=int, help="sampling rate")
parser.add_argument(
    "-m", "--model", type=str, help="language model; e.g. en-us, fr, nl; default is en-us")
args = parser.parse_args(remaining)

try:
    if args.samplerate is None:
        device_info = sd.query_devices(args.device, "input")
        # soundfile expects an int, sounddevice provides a float:
        args.samplerate = int(device_info["default_samplerate"])
        
    if args.model is None:
        model = Model(lang="en-us")
    else:
        model = Model(lang=args.model)

    if args.filename:
        dump_fn = open(args.filename, "wb")
    else:
        dump_fn = None

    with sd.RawInputStream(samplerate=args.samplerate, blocksize = 200, device=args.device,
            dtype="int16", channels=1, callback=callback):
        print("#" * 80)
        print("Press Ctrl+C to stop the recording")
        print("#" * 80)

        rec = KaldiRecognizer(model, args.samplerate, acceptedWords)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                textRead = json.loads(rec.Result())['text']
                print(textRead)
                if("red" in textRead):
                    Motor.MotorRun(0, 'forward', 100)
                    time.sleep(pumpDuration)
                    Motor.MotorStop(0)
                    #print("backward 2 s")
                    #Motor.MotorRun(0, 'backward', 100)
                    #Motor.MotorRun(1, 'backward', 100) 
                elif("blue" in textRead):
                    Motor.MotorRun(1, 'forward', 100)
                    time.sleep(pumpDuration)
                    Motor.MotorStop(1)
                elif("green" in textRead): #MOTOR .MOTOR2 BACKWARDS
                    Motor.MotorRun(2, 'backward', 100)
                    time.sleep(pumpDuration)
                    Motor.MotorStop(2)
                elif("purple" in textRead):
                    Motor.MotorRun(3, 'backward', 100) #MOTOR.Motor3 BACKWARDS
                    time.sleep(pumpDuration)
                    Motor.MotorStop(3)
                elif("yellow" in textRead):
                    Motor2.MotorRun(0, 'forward', 100)
                    time.sleep(pumpDuration)
                    Motor2.MotorStop(0)
                elif("orange" in textRead):
                    Motor2.MotorRun(1, 'forward', 100)
                    time.sleep(pumpDuration)
                    Motor2.MotorStop(1)
                elif("prime" in textRead):
                    Motor.MotorRun(0, 'forward', 100)
                    time.sleep(purgeTime)
                    Motor.MotorStop(0)
                    Motor.MotorRun(1, 'forward', 100)
                    time.sleep(purgeTime)
                    Motor.MotorStop(1)
                    Motor.MotorRun(2, 'backward', 100)
                    time.sleep(purgeTime)
                    Motor.MotorStop(2)
                    Motor.MotorRun(3, 'backward', 100)
                    time.sleep(purgeTime)
                    Motor.MotorStop(3) 
                    Motor2.MotorRun(0, 'forward', 100)
                    time.sleep(purgeTime)  
                    Motor2.MotorStop(0)
                    Motor2.MotorRun(1, 'forward', 100)
                    time.sleep(purgeTime)    
                    Motor2.MotorStop(1)
                elif("stop" in textRead):
                    Motor.MotorStop(0)
                    Motor.MotorStop(1)
                    Motor.MotorStop(2)
                    Motor.MotorStop(3)
                    Motor2.MotorStop(0)
                    Motor2.MotorStop(1)
                textRead = ""
            #else:
                #print(rec.PartialResult())
            if dump_fn is not None:
                dump_fn.write(data)

except KeyboardInterrupt:
    print("\nDone")
    parser.exit(0)
except Exception as e:
    parser.exit(type(e).__name__ + ": " + str(e))
