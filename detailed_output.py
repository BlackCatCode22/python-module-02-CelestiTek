def build_detailed_message(num1, num2, num3, largest_value, largest_var_name):
    return (
        f'You entered three numbers, {num1}, {num2}, and {num3}. '
        f'The first whole number you entered was assigned to a variable named num1, '
        f'the second ({num2}) to num2, and finally the third ({num3}) was assigned to num3. '
        f'Your input was processed and the largest number you entered was {largest_value}, '
        f'which belonged to an integer variable named {largest_var_name}.'
    )


num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

if num1 >= num2:
    if num1 >= num3:
        largest = num1
        largest_name = "num1"
    else:
        largest = num3
        largest_name = "num3"
else:
    if num2 >= num3:
        largest = num2
        largest_name = "num2"
    else:
        largest = num3
        largest_name = "num3"

message = build_detailed_message(num1, num2, num3, largest, largest_name)
print('Message to User: "' + message + '"')
