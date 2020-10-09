'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # base case
    if len(arr) == 0:
        return

    elif len(arr) == 1:
        return arr[0]

    for i in range(len(arr)):
        # use count method to count the number of elements
        if arr.count(arr[i]) == 1:
            return arr[i]

    return arr[i]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")