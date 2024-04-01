import tkinter as tk

root = tk.Tk()

# creating tkinter window 
root.geometry("1280x400")  
root.attributes('-fullscreen', True)
root.title("Drink Backpack")

# Adding widgets to the root window 
topL = tk.Label(root, text = 'Available Ingredients', font =('Helvetica', 30)).pack(side = tk.TOP, pady = 10) 

# Creating a photoimage object to use image 
drink1 = tk.PhotoImage(file = r"/home/debian/BeagleY_voice_backpack/drinks/drink1.png")  
drink2 = tk.PhotoImage(file = r"/home/debian/BeagleY_voice_backpack/drinks/drink2.png")  
drink3 = tk.PhotoImage(file = r"/home/debian/BeagleY_voice_backpack/drinks/drink3.png")  
drink4 = tk.PhotoImage(file = r"/home/debian/BeagleY_voice_backpack/drinks/drink4.png")  
drink5 = tk.PhotoImage(file = r"/home/debian/BeagleY_voice_backpack/drinks/drink5.png")  
drink6 = tk.PhotoImage(file = r"/home/debian/BeagleY_voice_backpack/drinks/drink6.png")  
# here, image option is used
# set image on button 

b1 = tk.Button(root, text = 'Drink', image = drink1) 
b2 = tk.Button(root, text = 'Drink', image = drink2) 
b3 = tk.Button(root, text = 'Drink', image = drink3) 
b4 = tk.Button(root, text = 'Drink', image = drink4)
b5 = tk.Button(root, text = 'Drink', image = drink5) 
b6 = tk.Button(root, text = 'Drink', image = drink6)

b1.pack(side=tk.LEFT, padx = (25,0)) 
b2.pack(side=tk.LEFT) 
b3.pack(side=tk.LEFT) 
b4.pack(side=tk.LEFT) 
b5.pack(side=tk.LEFT) 
b6.pack(side=tk.LEFT) 

root.mainloop() 
