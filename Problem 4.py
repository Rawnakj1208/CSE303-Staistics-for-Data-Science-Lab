def Series_Sum(n):
    if(n == 0):
        return 0
    else:
        num = (n * n) + Series_Sum(n - 1)
        return num

a = int(input("Enter any integer:" ))

Res = Series_Sum(a)

print("The sum of the series is: ", Res)