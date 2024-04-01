import tkinter as tk

from PCA9685 import PCA9685
import time

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

root = tk.Tk()

Motor = MotorDriver()
Motor2 = MotorDriver2()

# creating tkinter window 
root.geometry("1280x400")  
root.attributes('-fullscreen', True)
root.title("Drink Backpack")

# Adding widgets to the root window 
topL = tk.Label(root, text = 'Available Ingredients', font =('Helvetica', 30)).pack(side = tk.TOP, pady = 10) 

# Creating a photoimage object to use image 
drink1 = tk.PhotoImage(file = r"drinks/drink1.png")  
drink2 = tk.PhotoImage(file = r"drinks/drink2.png")  
drink3 = tk.PhotoImage(file = r"drinks/drink3.png")  
drink4 = tk.PhotoImage(file = r"drinks/drink4.png")  
drink5 = tk.PhotoImage(file = r"drinks/drink5.png")  
drink6 = tk.PhotoImage(file = r"drinks/drink6.png")  
# here, image option is used
# set image on button 

def pourDrink1():
    Motor.MotorRun(0, 'forward', 100)
    time.sleep(5)
    Motor.MotorStop(0)

def pourDrink2():
    Motor.MotorRun(1, 'forward', 100)
    time.sleep(5)
    Motor.MotorStop(1)

def pourDrink3():
    Motor.MotorRun(2, 'forward', 100)
    time.sleep(5)
    Motor.MotorStop(2)

def pourDrink4():
    Motor.MotorRun(3, 'forward', 100)
    time.sleep(5)
    Motor.MotorStop(3)

def pourDrink5():
    Motor2.MotorRun(0, 'forward', 100)
    time.sleep(5)
    Motor2.MotorStop(0)

def pourDrink6():
    Motor2.MotorRun(1, 'forward', 100)
    time.sleep(5)
    Motor2.MotorStop(1)

b1 = tk.Button(root, text = 'Drink', image = drink1, command = pourDrink1) 
b2 = tk.Button(root, text = 'Drink', image = drink2, command = pourDrink2) 
b3 = tk.Button(root, text = 'Drink', image = drink3, command = pourDrink3) 
b4 = tk.Button(root, text = 'Drink', image = drink4, command = pourDrink4)
b5 = tk.Button(root, text = 'Drink', image = drink5, command = pourDrink5) 
b6 = tk.Button(root, text = 'Drink', image = drink6, command = pourDrink6)

b1.pack(side=tk.LEFT, padx = (25,0)) 
b2.pack(side=tk.LEFT) 
b3.pack(side=tk.LEFT) 
b4.pack(side=tk.LEFT) 
b5.pack(side=tk.LEFT) 
b6.pack(side=tk.LEFT) 

root.mainloop() 
