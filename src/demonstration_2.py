"""
Given a list of integers, your function should return `True` if any value
appears at least two times in the array. Your function should return `False` if
every element is unique.

Example:

Input: [1,3,3,2,1]
Output: True

Example:

Input: [0,1,2,3]
Output: False

*Note: In your first solution, it is okay to use a simple linear search. What
is the time complexity of this approach? Other possible solutions will have
time complexities of `O(n log n)` or `O(n)`. Possible space complexities are
`O(1)` or `O(n)`. Try to come up with solutions with different time and space
complexities and think about the tradeoffs between the solutions.*
"""
def contains_duplicate(nums):
    # Time complexity: O(n)
    # Space complexity: O(1)
    # Your code here
    if len(nums) == len(set(nums)):
        return False
    else:
        return True
    print("Len of nums", len(nums))
    print("Len of set nums", len(set(nums)))
result = contains_duplicate([1])
print(result)


def prefixFreePhone(numbers):
    # What if we sort numbers first?
    # numbers is a list of strings, so it's going to sort alphabetically
    #sort

    #overall runtime is O(n log n)
    #iterate through
    #compare each element with the one right after it
    # if the second element starts with the first, return false
    #otherwise return True

    numbers.sort()

    for i in range(i, len(numbers) - 1):
        first = numbers[i]
        second = numbers[i + 1]
        if second.startswith(first):
            return False
    return True