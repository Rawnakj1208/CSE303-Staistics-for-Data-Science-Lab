def Prime_Find_2019_1_60_134(n):
    if n > 1:
        for i in range(2,n):
          if (n % i) == 0:
              print("It is not a Prime number.")
              break
        else:
            print("It is a Prime Number")

    else:
        print("The number is negative.")


n = int(input("Enter any integer : "))

result = Prime_Find_2019_1_60_134(n)
print(result)