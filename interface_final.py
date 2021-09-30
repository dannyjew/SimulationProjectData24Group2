from Simulation_final import *
import matplotlib.pyplot as plt
import seaborn as sb
import tkinter as tk
import numpy as np
from tkinter import font
from Simulation import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

'''
function for creating the existing number of centres, the random number of new students every two months
'''



def sim(time,centre_init):

    centres = [0]*(centre_init)

    waiting_list=0

    total_students=[]

    total_students_list=[]

    accum_students_in_training = []

    waiting_list_list=[]

    for month in range(time):
        print('\n')
        #print('Month:'+str(month))
        if month%2!=0:
            centres.append(0)
        number_new_students = r.randint(20, 30) #new students per month
        # print('waiting list pre assign:'+ str(waiting_list))
        waiting_list+=number_new_students

        total_students_list.append(number_new_students)
        total_students.append(sum(total_students_list))

        centres,waiting_list,accum_students_in_training = go_through_centres(centres,waiting_list,accum_students_in_training)
        waiting_list_list.append(waiting_list)



    centre_count_tot = len(centres)
    n_full=centres.count(100)
    t_t =sum(centres)

    # display(centre_count_tot, n_full, t_t, waiting_list, month)
    label['text']= display(centre_count_tot, n_full, t_t, waiting_list,len(range(time)))
    graphs(total_students,accum_students_in_training,waiting_list_list)


#Creating the graphs
def graphs(total_students,accum_students_in_training,waiting_list_list):
    time=list(range(len(waiting_list_list)))
    time=[x+1 for x in time]
    fig = plt.figure(figsize=(6.5, 2.85), dpi=80)

    plt.ion()  #Plot for simulation
    x=time
    y=waiting_list_list
    plt.title('Number of Waiting Students over time in Months')
    # plt.xlabel('Time in Months')
    plt.ylabel('# of Students')
    plt.plot(x, y)


    graph = FigureCanvasTkAgg(fig, master=graph_label)  #Inserting Graph into GUI

    plot_widget = graph.get_tk_widget()

    plot_widget.grid(row=0, column=0)



HEIGHT=800
WIDTH=700

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)  # Size of the default window
canvas.pack()

background_image = tk.PhotoImage(file='Untitled.png')
background_label=tk.Label(root, image=background_image)
background_label.place(relwidth=1,relheight=1)


frame = tk.Frame(root, bg='#dc143c',bd=5)  # Top Frame inside window with properties
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75 , relheight = 0.2, anchor='n')

label_1 = tk.Label(frame, text='# of Months', font=('Calibri',20),fg='White',  bg = 'Black')
label_1.place( relwidth = 0.55, relheight = 0.475)

label_2 = tk.Label(frame, text='# of Initial Centres', font=('Calibri',20),fg='White',  bg = 'Black')
label_2.place(rely = 0.525, relwidth = 0.55, relheight = 0.475)

entry1 = tk.Entry(frame, font =('Calibri',20),fg='White',  bg = 'Black')
entry1.place(relx=0.565  ,relwidth = 0.1, relheight = 0.475)

entry2 = tk.Entry(frame, font =('Calibri',20),fg='White',  bg = 'Black')
entry2.place(relx=0.565, rely = 0.525, relwidth = 0.1, relheight = 0.475)

button1 = tk.Button(frame, text='Test',font =('Calibri',20),fg='White',  bg = 'Black', command =lambda: sim(int(entry1.get()),int(entry2.get())))  # Properties of the button(where it is passed to ~what its is stuck to)
button1.place(relx = 0.675, relwidth = 0.325, relheight = 0.975)


Low_frame = tk.Frame(root, bg='#dc143c',bd=10)  # Bottom Frame inside window with properties
Low_frame.place(relx = 0.5, rely = 0.325, relwidth = 0.75 , relheight = 0.6, anchor='n')

label = tk.Label(Low_frame, font=('Calibri',20),fg='White',  bg = 'Black')
label.place(relwidth = 1, relheight = 0.45)

graph_label = tk.Label(Low_frame, font=('Calibri',20),fg='White',  bg = 'Black')
graph_label.place(rely = 0.5,relwidth = 1, relheight = 0.5)


root.mainloop()



# time=int(input('How many months would you like the simulation to run (please insert a number):'))
#
# centre_init=int(input('What is the number of initial centres (please insert a number):'))
#
# sim(time,centre_init)