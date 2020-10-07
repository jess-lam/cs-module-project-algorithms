'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    non_zeros = []
    zeros = []
    for i in range(0, len(arr)):
        if arr[i] != 0:
            non_zeros.append(arr[i])
        else:
            zeros.append(arr[i])
    return non_zeros + zeros

            


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")