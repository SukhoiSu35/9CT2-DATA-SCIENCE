# Create a calculator function
# The function should accept three parameters:
# first_number: a numeric value for the math operation
# second_number: a numeric value for the math operation
# operation: the word 'add' or 'subtract'
# the function should return the result of the two numbers added or subtracted
# based on the value passed in for the operator

def calculator(first, second, operation):
    if operation == '+': 
        result = first + second
        return result
    elif operation == '-':
        result = first - second
        return result
    elif operation == '/':
        result = first / second
        return result
    else:
        print("error values are invalid")
    

# Test your function with the values 6,4, add 
# Should return 10
print(calculator(6, 4, '+'))

# Test your function with the values 6,4, subtract 
# Should return 2
print(calculator(6,4,'-'))
 
# BONUS: Test your function with the values 6, 4 and divide 
# Have your function return an error message when invalid values are received

print(calculator(6,4,''))

