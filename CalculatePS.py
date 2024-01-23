# Set Variables
def multiply_or_sum(num1, num2):
    # If and Else Function
    if num1 * num2 <= 1000:
        return num1 * num2
    else:
        return num1 + num2


# Given number1 = 20 number2 = 30
result = multiply_or_sum(20, 30)
print("The result is", result)

# Given number1 = 40 number2 = 30
result = multiply_or_sum(40, 30)
print("The result is", result)
