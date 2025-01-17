'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    new_arr = []
    for i in range(0, len(nums)):
        if i+k > len(arr):
            break
        sub_array = arr[i:k+i]
        print(sub_array)
        new_arr.append(max(sub_array))


    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
