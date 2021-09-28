import random as r


def go_through_centres(centres,waiting_list):

    for i in range(len(centres)):
        centre=centres[i]
        centre_intake = r.randint(0, 20)

        if centre + centre_intake > 100:
            if (waiting_list - centre_intake) < 0:
                final_intake = centre_intake - waiting_list

                x = 100 - centre
                remainder = final_intake - x

                waiting_list += remainder - final_intake
                centres[i] += final_intake - remainder
        else:
            if (waiting_list - centre_intake) < 0:
                final_intake = centre_intake - waiting_list
                waiting_list += -final_intake
                centres[i] += final_intake
        # print (centre)
    return centres,waiting_list


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













