def Find_Fibonacci(n):
    F0 = 0
    F1 = 1
    if n < 0:
        print("Negative number")

    elif n ==0:
        return 1
    elif n == 1:
        return F1
    else:
        for i in range(1,n):
            F2 = F0 + F1
            F0 = F1
            F1 = F2

        return F1

a = int(input("Enter any number: " ))
result = Find_Fibonacci(a)
print("The Fibonacci Number is ",result)