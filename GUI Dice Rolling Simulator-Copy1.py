#!/usr/bin/env python
# coding: utf-8

# In[20]:


# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random
x=6
for i in range(x):
 print(i)

# Generates a random number 
# Between 1 and 6 (including 
# both 1 and 6 )
 no = random.randint(1,6)

if no == 1:
 print("[-----]")
print("[   ]")
print("[ 0 ]")
print("[   ]")
print("[-----]")
if no == 2:
 print("[----]")
print("[  0   ]")
print("[     ]")
print("[   0 ]")
print("[-----]")
if no == 3:
 print("[-----]")
print("[     ]")
print("[0 0 0]")
print("[     ]")
print("[-----]")
if no == 4:
 print("[-----]")
print("[0   0]")
print("[     ]")
print("[0   0]")
print("[-----]")
if no == 5:
 print("[-----]")
print("[0   0]")
print("[  0  ]")
print("[0   0]")
print("[-----]")
if no == 6:
 print("[-----]")
print("[0 0 0]")
print("[     ]")
print("[0 0 0]")
print("[-----]")
         
x=input("press y to roll again and n to exit:")
print("\n")

import random
while True:
  print('''1.roll the dice    2.To exit ''')
  user = input("what you want to do\n")
  if user==1:
    number = random.randint(1,6)
    print(number)
  else:
    break

#Importing tkinter and random modules
from tkinter import *
import random

# Creating a window
window= Tk()

#Setting background colour of the window
window.configure(bg="black")

#Setting geometry of the window
window.geometry("550*350")

# In[51]:


# Importing tkinter and random modules
from tkinter import *
import random
  
# Creating a window
window = Tk()
  
# Setting background colour of the window
window.configure(bg="black")
  
# Setting geometry of the window
window.geometry("550x350")
  
# Setting title of the window
window.title("Rolling The Dices Game")
  
# Preventing maximizing of the window
window.resizable(0, 0)
  
# Creating function to roll the dices
def roll_dices():
     # These values indicate dots on the dices.
     # For eg: \u2680 corresponds to 1 dot,
     # \u2681 corresponds to 2 dots etc.
    dice_dots = ['\u2680', '\u2681',
                 '\u2682', '\u2683',
                 '\u2684', '\u2685']
    # Generating random dots on the dices
    label.configure(
        text=f'{random.choice(dice_dots)}{random.choice(dice_dots)}')
    label.pack()
  
  
# Adding button to roll the dices
roll_button = Button(window, text="Roll!",
                     width=10, height=2,
                     font=15, bg="aqua",
                     bd=2, command=roll_dices)
# Setting the position of the button
roll_button.pack(padx=10, pady=15)  
  
# Adding Label
label = Label(window, font=("times", 250),
              bg="black", fg="yellow")
  
window.mainloop()


# In[ ]:




