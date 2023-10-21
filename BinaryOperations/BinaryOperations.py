"""
You are given a binary string representing a non-negative number. You need to perform two types of operations on the number until it becomes 0:

If the number is even, divide it by 2.
If the number is odd, subtract 1 from it.
Write a function solution(S) that takes a binary string S and returns the number of operations required to reach 0 from the given binary number.

The function should adhere to the following constraints:

The string S consists only of '0' and/or '1'.
The length of S is an integer within the range [1, 1,000,000].
The binary representation is big-endian (the first character corresponds to the most significant bit).
The binary representation may contain leading zeros.
"""

def solution(S):
    num_int = int(S, 2)  # Convert binary string to integer

    ops = 0  # Initialize a variable to count the number of operations

    # Loop until the number becomes 0
    while num_int > 0:
        if num_int % 2 == 0:  # If the number is even
            num_int //= 2  # Divide by 2
        else:  # If the number is odd
            num_int -= 1  # Subtract 1
        ops += 1  # Increment the count of operations

    return ops  # Return the total number of operations

# Examples
print(solution("011100"))  # 7
print(solution("111"))  # 5
print(solution("1111010101111"))  # 22
