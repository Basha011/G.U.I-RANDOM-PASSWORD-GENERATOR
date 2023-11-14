import checkbox_api
import random
from tkinter import *
import tkinter

#creating window

w=Tk()

#giving name to window

w.title("random password generator")

#size of window

w.geometry("900x600")

#adding label

Label(w, font=('times', 18), text='Generate a password by length given below').pack()

#convert length to string

length1 = tkinter.IntVar()
length2 = tkinter.IntVar()
length3 = tkinter.IntVar()
length4 = tkinter.IntVar()

#function to generate a random password

def password_generation(g):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_@#'
    password = ''.join(random.sample(letters, g))
    k = Label(w, text=password, font=('bold', 17)) #size and font of password
    k.place(x=370, y=120)

 #get length function calls the password generation function

def get_length():
     if length1.get() == 4:
         password_generation(4)
     elif length2.get() == 8:
         password_generation(8)
     elif length3.get() == 10:
         password_generation(10)
     else:
         password_generation(13)
#creating a button for generation of password

Button(w, text = 'Generate the password', font = ('normal',15), bg = 'blue', command = get_length).place(x=365, y=160)

#creating the checkboxes

Checkbutton(text = '4 characters', font=('normal',13), bg = 'green yellow', onvalue=4, offvalue=0, variable=length1).place(x=380, y=220)
Checkbutton(text = '8 characters', font=('normal',13), bg = 'cyan', onvalue=8, offvalue=0, variable=length2).place(x=380, y=260)
Checkbutton(text = '10 characters', font=('normal',13), bg = 'tomato', onvalue=10, offvalue=0, variable=length3).place(x=380, y=300)
Checkbutton(text = '13 characters', font=('normal',12), bg = 'cadet blue', onvalue=13, offvalue=0, variable=length4).place(x=380, y=340)

w.mainloop()