import random as r



def students_intake(centres):

    students_allowed=0

    for i in range(len(centres)):
        centre=centres[i]
        centre_intake = r.randint(0, 20)
        students_allowed+=centre_intake

    return students_allowed


def new_students(time):  # total new students in time (months)
    new_student_count=0
    for month in range(time):
        number_new_students = r.randint(20, 30)
        new_student_count+=number_new_students





def go_through_centres(centres,waiting_list):
    students_allowed=0



def sim(time,centre_init):

    centres = [0]*(centre_init)

    waiting_list=0

    for month in range(time):
        if month%2!=0:
            centres.append(0)

        number_new_students = r.randint(20, 30)
        centres,waiting_list= go_through_centres(centres,waiting_list)




        if waiting_list==0:
            waiting_list+=number_new_students
            go_through_centres(centres,waiting_list)
        else:
            waiting_list+=number_new_students

    centre_count_tot = len(centres)
    n_full=centres.count(100)
    t_t =sum(centres)

    print('Number of centres:'+ str(centre_count_tot))
    print('Number of full centres:' + str(n_full))
    print(centres)
    print('Number of trainees in training:' + str(t_t))
    print('Number of trainees on waiting list:' + str(waiting_list))


time=int(input('time:'))

centre_init=int(input('Number of initial centres:'))

sim(time,centre_init)