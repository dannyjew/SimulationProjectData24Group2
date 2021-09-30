import random as r


accum_students = 0

def go_through_centres(centres,waiting_list,accum_students_in_training):

    acc_spaces_per_month=0

    for i in range(len(centres)):
        # print('\n')
        # print('No of centres:' + str(len(centres)))
        # print('waiting list:' + str(waiting_list))

        if centres[i] == 100:
            pass
        else:
            centre_intake = r.randint(0,20)
            acc_spaces_per_month+=centre_intake
            # print('intake:'+ str(centre_intake))

            if centres[i] + centre_intake > 100:
                x = 100 - centres[i]

                if x > waiting_list:
                    centres[i] += waiting_list
                    #print('1')
                    waiting_list=0

                elif x <= waiting_list:
                    centres[i] += x
                    #print('2')
                    waiting_list -= x

            elif centres[i] + centre_intake <= 100:

                if centre_intake > waiting_list:
                    centres[i] += waiting_list
                    #print('3')
                    waiting_list = 0

                elif centre_intake <= waiting_list:
                    #print('4')
                    centres[i] += centre_intake
                    # print(centres[i])
                    # print(centres)

                    waiting_list -= centre_intake


            centre_intake = 10#centre intake
        # print('centre:'+str(i+1))
        # print(centres)
    accum_students_in_training.append(sum(centres))
    return centres,waiting_list,accum_students_in_training



# print(go_through_centres([10,0,0],114))

# def sim(time,centre_init):
#
#     centres = [0]*(centre_init)
#
#     waiting_list=0
#
#     total_students=[]
#
#     for month in range(time):
#         print('\n')
#         #print('Month:'+str(month))
#         if month%2!=0:
#             centres.append(0)
#         number_new_students = r.randint(20, 30) #new students per month
#         # print('waiting list pre assign:'+ str(waiting_list))
#         waiting_list+=number_new_students
#         total_students.append(number_new_students)
#
#         centres,waiting_list = go_through_centres(centres,waiting_list)
#
#
#     centre_count_tot = len(centres)
#     n_full=centres.count(100)
#     t_t =sum(centres)
#     display(centre_count_tot, n_full, t_t, waiting_list,month)
#
#




def display(centre_count_tot,n_full,t_t,waiting_list,month):

    # print('Month:' + str(month))
    # print('No of centres:'+ str(centre_count_tot))
    # print('No of full centres:' + str(n_full))
    # #print(f'No of students per centre:{centres}')
    # print('No of trainees in training:' + str(t_t))
    # print('No of trainees on waiting list:' + str(waiting_list))

    return 'Month:'+ str(month+1) + '\n' + 'No of centres:'+ str(centre_count_tot) + '\n' + 'No of full centres:' + str(n_full) + '\n' + 'No of trainees in training:' + str(t_t) + '\n' + 'No of trainees on waiting list:' + str(waiting_list)






# time=int(input('How many months would you like the simulation to run (please insert a number):'))
#
# centre_init=int(input('What is the number of initial centres (please insert a number):'))
#
# sim(time,centre_init)
# #
#
#
#
#








