'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):

    new_arr = [0] * len(arr)
    print (new_arr)
    i = 0
    for x in arr:
        if x != 0:
            new_arr[i]  = x
            i += 1
    
    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")