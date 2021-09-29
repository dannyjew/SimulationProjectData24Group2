import random as r

accum_students = 0

def go_through_centres(centres,waiting_list):

    for i in range(len(centres)):
        print('\n')
        print('No of centres:' + str(len(centres)))
        print('waiting list:' + str(waiting_list))

        if centres[i] == 100:
            pass
        else:
            centre_intake = r.randint(0,20)
            print('intake:'+ str(centre_intake))

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
        print('centre:'+str(i+1))
        print(centres)

    return centres,waiting_list



# print(go_through_centres([10,0,0],114))

def sim(time,centre_init):

    centres = [0]*(centre_init)

    waiting_list=0

    for month in range(time):
        print('\n')
        print('month:'+str(month))
        if month%2!=0:
            centres.append(0)
        number_new_students = r.randint(20, 30) #new students per month
        print('waiting list pre assign:'+ str(waiting_list))
        waiting_list+=number_new_students
        centres,waiting_list = go_through_centres(centres,waiting_list)


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













