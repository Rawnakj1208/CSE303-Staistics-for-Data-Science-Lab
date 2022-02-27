Given_list = [10,20,30,40,50,60,70,80,90,100,110]
n = 11
def Summation(list):
    sum = 0
    for i in range(len(Given_list)):
         if i % 2 == 0:
           sum = Given_list[i] + sum
    return sum

print("The summation of even indexed element is :", Summation(Given_list))