# Considering an array A of N integers, we need to return the smallest positive integer (that has to be greater than 0) and that it is not present in A.

# For example, considering A = [1, 5, 4, 1, 2], the function should return 3.

# For A = [1, 2, 3], the function has to return 4.

# For A = [−1, −2], the function has to return 1.

# N is an integer within the range [1..100,000];
# And each element of the array A is an integer within the range [−1,000,000..1,000,000].

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    arr = [0] * 1000001
    for a in A:
        if a > 0:
            arr[a] = 1
    for i in range(1, 1000000+1):
        if arr[i] == 0:
            return i
    pass

