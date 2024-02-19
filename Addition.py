def add_numbers(a, b):
    result = a + b
    return result

num1 = float(input('Enter value of number : '))
num2 = float(input('Enter value of number : '))

sum_result = add_numbers(num1, num2)

print(f"The sum of {num1} and {num2} is: {sum_result}")