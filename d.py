import matplotlib.pyplot as plt
import seaborn as sb
import tkinter as tk
import numpy as np
from tkinter import font
from Simulation import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

root = tk.Tk()

fig = plt.figure(1)
plt.ion()
t = np.arange(0.0,3.0,0.01)
s = np.sin(np.pi*t)
plt.plot(t,s)

canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()


s = np.cos(np.pi*t)
plt.plot(t,s)
    #d[0].set_ydata(s)
fig.canvas.draw()

plot_widget.grid(row=0, column=0)

root.mainloop()
