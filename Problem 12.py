def remove_element(a, b):
    return a[b:len(a)]


string_input = input("Enter any string: ")
b = int(input("Enter any number: "))

size_Input = len(string_input)
if (size_Input > b):
    print(remove_element(string_input, b))