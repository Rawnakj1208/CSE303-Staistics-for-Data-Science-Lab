def compound_interest_2019_1_60_134(P, R, T):
    A = P * ((1 + R/100) ** T)
    return A

a = int(input("Enter your Principle Amount: "))
b = int(input("Enter your Interest rate(%) : "))
c = int(input("Enter your Estimated time (in years) :"))

res = compound_interest_2019_1_60_134(a,b, c)
print("Your Compound Interest is :", res)