list1 = [59,50,70,100,27,25,90]
list2 = [69,88,84,60,34,22,95]

list3 =[]

for i in list1:
    if (i % 2!=0):
        list3.append(i)

for i in list2:
    if(i%2==0):
        list3.append(i)

print("The new list is", list3)