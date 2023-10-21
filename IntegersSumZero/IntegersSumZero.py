# Function to generate an array of N unique integers that sum up to zero
def sumZero(N):  # Function to generate an array of N unique integers that sum up to zero
    ArrayRes = [0] * N  # Initialize an array of size N with all elements set to 0
    init = -(N // 2)  # Initialize the starting value to ensure the sum is zero

    # Populate the array with unique values that sum up to zero
    for i in range(N):
        ArrayRes[i] = init  # Assign the current value to the array
        init += 1  # Increment the value for the next iteration

    return ArrayRes  # Return the generated array


# Example usage
N = 5  # Define the value of N
ArrayRes = sumZero(N)  # Generate an array of N unique integers that sum up to zero
print(ArrayRes)  # Print the generated array
