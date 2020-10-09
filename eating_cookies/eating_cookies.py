'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    eaten = 0
    # base case
    if eaten > n:
        return 0
    elif eaten == n:
        return 1
    else:
        # eat more cookies
        return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

    # base case
    # if n < 0:
    #     return 0
    # if n == 0:
    #     return 1
    # if n in cache:
    #     return cache[n]

    # cache[n] = eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)
    # return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
