"""
Given a sorted array `nums`, remove the duplicates from the array.

Example 1:

Given nums = [0, 1, 2, 3, 3, 3, 4]

Your function should return [0, 1, 2, 3, 4]

Example 2:

Given nums = [0, 1, 1, 2, 2, 2, 3, 4, 4, 5]

Your function should return [0, 1, 2, 3, 4, 5].

*Note: For your first-pass, an out-of-place solution is okay. However, after
solving out-of-place, try an in-place solution with a space complexity of O(1).
For that solution, you will need to return the length of the modified `nums`.
The length will tell the user where the end of the array is after removing all
of the duplicates.*
"""
def remove_duplicates(nums):
    # in place means we don't use extra space -- means we have to swap / move numbers around within 'nums'
    # we can run a for loop
    # Overall runtimeL O(n^2)
    # Space complexity: 0(1)

    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i+1]:
            nums.pop(i + 1)
        else:
            i = i + 1
    return nums
    # return list(dict.fromkeys(nums))
result = remove_duplicates([0, 1, 2, 3, 3, 3, 4])
print(result)


def remove_duplicates_in_place_linear(nums):
    # runtime: 0(n)
    # iterate through the list
    # keep one non_duplicate_index index pointing to the end of the part of the array w/no duplicates
    non_duplicate_index = 0
    # and another idx pointing to the "current" element in the array
    for current_index in range(1, len(nums)):
        # if current element is already in the nonduplicate part of the array
        if nums[current_index] == nums[non_duplicate_index - 1]:
            continue
            # skip it
        else:
            # otherwise, set nums[non_duplicate_index] to current element and increment idx
            nums[non_duplicate_index] = nums[current_index]
            non_duplicate_index += 1
    return nums, non_duplicate_index
print(remove_duplicates_in_place_linear([0, 1, 2, 3, 3, 3, 4]))

