Given_list = [10,20,30,40,50,60,70,80,90,100,110]

def Sum_of_List(List):
    Sum = 0
    for i in List:
        Sum = Sum + i
    return Sum

print("Sum of the List is", Sum_of_List(Given_list))