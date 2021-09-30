import tkinter as tk
from Simulation import *

HEIGHT=700
WIDTH=800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)  # Size of the default window
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff')  # Frame inside window with properties
frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8 , relheight = 0.5)

button = tk.Button(frame, text='Test',bg='gray')  # Properties of the button(where it is passed to ~what its is stuck to)
button.place(relx=0, rely=0, relwidth=0.25, relheight=0.25)
# button.pack(side = 'left', fill='x', expand = True)  #feed positions into it, fill space direction(x,y,both) of parent with item,expand button
# button.grid(row=0, column=0)#other way of positioning items on window without using pack

label = tk.Label(frame, text='This is a label', bg = 'Yellow')
label.place(relx = 0.3, rely = 0, relwidth = 0.45, relheight = 0.25)

entry = tk.Entry(frame, bg='green')
entry.place(relx = 0.8, rely = 0, relwidth = 0.2, relheight = 0.2)

root.mainloop()