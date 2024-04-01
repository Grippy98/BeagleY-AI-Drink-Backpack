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
                print ("1")
                pwm.setLevel(self.AIN1, 0)
                pwm.setLevel(self.AIN2, 1)
            else:
                print ("2")
                pwm.setLevel(self.AIN1, 1)
                pwm.setLevel(self.AIN2, 0)
        if(motor == 1):
            pwm.setDutycycle(self.PWMB, speed)
            if(index == Dir[0]):
                print ("3")
                pwm.setLevel(self.BIN1, 0)
                pwm.setLevel(self.BIN1, 1)
            else:
                print ("4")
                pwm.setLevel(self.BIN1_2, 1)
                pwm.setLevel(self.BIN2_2, 0)
        if(motor == 2):
            pwm.setDutycycle(self.PWMA_2, speed)
            if(index == Dir[0]):
                print ("5")
                pwm.setLevel(self.AIN1_2, 0)
                pwm.setLevel(self.AIN2_2, 1)
            else:
                print ("6")
                pwm.setLevel(self.AIN1_2, 1)
                pwm.setLevel(self.AIN2_2, 0)
        if(motor == 3):
            pwm.setDutycycle(self.PWMB_2, speed)
            if(index == Dir[0]):
                print ("5")
                pwm.setLevel(self.BIN1_2, 0)
                pwm.setLevel(self.BIN2_2, 1)
            else:
                print ("6")
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
                print ("1")
                pwm2.setLevel(self.AIN1, 0)
                pwm2.setLevel(self.AIN2, 1)
            else:
                print ("2")
                pwm2.setLevel(self.AIN1, 1)
                pwm2.setLevel(self.AIN2, 0)
        if(motor == 1):
            pwm2.setDutycycle(self.PWMB, speed)
            if(index == Dir[0]):
                print ("3")
                pwm2.setLevel(self.BIN1, 0)
                pwm2.setLevel(self.BIN1, 1)
            else:
                print ("4")
                pwm2.setLevel(self.BIN1_2, 1)
                pwm2.setLevel(self.BIN2_2, 0)
        if(motor == 2):
            pwm2.setDutycycle(self.PWMA_2, speed)
            if(index == Dir[0]):
                print ("5")
                pwm2.setLevel(self.AIN1_2, 0)
                pwm2.setLevel(self.AIN2_2, 1)
            else:
                print ("6")
                pwm2.setLevel(self.AIN1_2, 1)
                pwm2.setLevel(self.AIN2_2, 0)
        if(motor == 3):
            pwm2.setDutycycle(self.PWMB_2, speed)
            if(index == Dir[0]):
                print ("5")
                pwm2.setLevel(self.BIN1_2, 0)
                pwm2.setLevel(self.BIN2_2, 1)
            else:
                print ("6")
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

Motor.MotorStop(0)
Motor.MotorStop(1)
Motor.MotorStop(2)
Motor.MotorStop(3)
Motor2.MotorStop(0)
Motor2.MotorStop(1)