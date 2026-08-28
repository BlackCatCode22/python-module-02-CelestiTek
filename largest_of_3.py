first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))
third = int(input("Enter the third integer: "))

if first >= second:
    if first >= third:
        largest = first
    else:
        largest = third
else:
    if second >= third:
        largest = second
    else:
        largest = third

print("The largest integer is:", largest)
