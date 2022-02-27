Given_list = [10,20, 30,40, 50, 60, 70, 80, 90, 100, 110]
n = 11

def second_largest_number_2019_1_60_134(list):
    largest = Given_list[0]
    second_largest = Given_list[1]
    for i in range(1, n):
        if largest < Given_list[i]:
            largest = Given_list[i]
            if largest < Given_list[i]:
                second_largest = Given_list[i]

    return second_largest

print("The second Largest element is :",second_largest_number_2019_1_60_134(Given_list) )