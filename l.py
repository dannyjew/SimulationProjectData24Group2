def centre(time,centre_init):
    centre_count=0+centre_init
    for i in range(time//2):
        centre_count+=1
    return centre_count

myList = ["one", "two", 37, "four", 51];
for i in range(len(myList)):
    if myList[i]==37:
        myList[i]=48


print(myList);