# Define a function to check whether a number is a power of two
def is_power_of_two(n):
    # Keep dividing the number by 2 as long as the number is even and greater than 1
    while n % 2 == 0 and n > 1:
        n = n / 2
    # If the number becomes 1, it is a power of 2
    if n == 1:
        return True
    else:
        return False

# Test the function
number = int(input("Enter a number: "))  # Take an integer input from the user
if is_power_of_two(number):  # Check if the number is a power of 2 using the defined function
    print(f"{number} is a power of 2.")  # Print a message indicating that the number is a power of 2
else:
    print(f"{number} is not a power of 2.")  # Print a message indicating that the number is not a power of 2
