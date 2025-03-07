def my_decorator(func):
    def wrapper(a, b):  # Accepts two arguments
        print(f"Adding {a} and {b}...")  # Extra feature
        result = func(a, b)  # Call the original function
        print(f"Result is {result}")  # Extra feature
        return result  # Return the result
    return wrapper

@my_decorator  # Apply the decorator
def add_numbers(x, y):
    return x + y

# Call the function
sum_result = add_numbers(5, 3)
print(f"Final Output: {sum_result}")
