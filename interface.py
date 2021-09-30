import tkinter as tk
from tkinter import font
from Simulation import *



def sim(time,centre_init):

    centres = [0]*(centre_init)

    waiting_list=0

    total_students=[]

    accum_students_in_training = []

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


    centre_count_tot = len(centres)
    n_full=centres.count(100)
    t_t =sum(centres)
    # graphs(total_students,accum_students_in_training)
    # display(centre_count_tot, n_full, t_t, waiting_list, month)
    label['text']= display(centre_count_tot, n_full, t_t, waiting_list,month)


#Creating the graphs
def graphs(total_students,accum_students_in_training):
    time=list(range(len(total_students)))
    print(total_students)
    print(accum_students_in_training)



HEIGHT=800
WIDTH=700

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)  # Size of the default window
canvas.pack()

background_image = tk.PhotoImage(file='Untitled.png')
background_label=tk.Label(root, image=background_image)
background_label.place(relwidth=1,relheight=1)


frame = tk.Frame(root, bg='#c71585',bd=5)  # Frame inside window with properties
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75 , relheight = 0.2, anchor='n')

entry1 = tk.Entry(frame, font =('Calibri',20),fg='White',  bg = 'Black')
entry1.place( relwidth = 0.65, relheight = 0.475)

entry2 = tk.Entry(frame, font =('Calibri',20),fg='White',  bg = 'Black')
entry2.place( rely = 0.525, relwidth = 0.65, relheight = 0.45)

button1 = tk.Button(frame, text='Test',font =('Calibri',20),fg='White',  bg = 'Black', command =lambda: sim(int(entry1.get()),int(entry2.get())))  # Properties of the button(where it is passed to ~what its is stuck to)
button1.place(relx = 0.675, relwidth = 0.325, relheight = 0.975)


Low_frame = tk.Frame(root, bg='#c71585',bd=10)  # Frame inside window with properties
Low_frame.place(relx = 0.5, rely = 0.325, relwidth = 0.75 , relheight = 0.6, anchor='n')

label = tk.Label(Low_frame, font=('Calibri',20),fg='White',  bg = 'Black')
label.place(relwidth = 1, relheight = 1)



root.mainloop()



# time=int(input('How many months would you like the simulation to run (please insert a number):'))
#
# centre_init=int(input('What is the number of initial centres (please insert a number):'))
#
# sim(time,centre_init)