Given_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
n = 11

def largest_number_2019_1_60_134(list):
    largest = Given_list[0]
    for i in range(1, n):
        if largest < Given_list[i]:
            largest = Given_list[i]

    return largest


def smallest_number_2019_1_60_134(list):
    smallest = Given_list[0]
    for i in range(1, n):
        if (smallest > Given_list[i]):
            smallest = Given_list[i]

    return smallest

print("The largest number in the list is: ",largest_number_2019_1_60_134(Given_list))

print("The smallest number in the list is: ",smallest_number_2019_1_60_134(Given_list))