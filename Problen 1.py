
print("Enter any two integers:")
a = int(input("First number: "))
b= int(input("Second number: "))

result = a*b;

if(result<1000):

   print("The product of two number is: ",result)

elif(result>1000):
    result1 = a + b;
    print("The sum is: ", result1)

else:
    print("Invalid")