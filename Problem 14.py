def palindrome_checker_2019_1_60_134(s):
    for i in range(0, int(len(s) / 2)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

a = input("Enter any word to find out Palindrome: ")
res = palindrome_checker_2019_1_60_134(a)

if (res):
    print("Palindrome")

else:
    print("Not Palindrome")