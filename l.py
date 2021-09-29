def centre(time,centre_init):
    centre_count=0+centre_init
    for i in range(time//2):
        centre_count+=1
    return centre_count

myList = ["one", "two", 37, "four", 51]
#
# for i in myList:
#     if i == 37:
#         myList.replace(48)


#
# print(myList)

# centres = [0]*(10)
#
# print(type(centres[3]))


a_list = ["a", "b", "c"]

for i in range(len(a_list)):
    if a_list[i] == 'a':
        a_list[i] += a_list[i]



print(a_list)