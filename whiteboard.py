# Find Middle Number
# Given a number (n) and an array of numbers (num_list) as input to a function, 
# return True if the number is greater than the middle number of the array. 
# Return False if the number is less than the middle number of the array.
# If the array has an even amout of indexes you must decide how to handle that.

# Example Input: n = 4, array = [3,5,8, 10]
# Example Output: False: 
array = [10,30,44,22,100]
# Example Output: True
numbers = [3, 5, 8, 10]
#get length of array indexes
#determine half of total indexes (use round to round up if not even)
#compare n to value at middle index
others = [7, 4, 3, 8]
other2 = [60, 25, 15, 56, 77]


def middle(nums, n):
    x = len(nums)
    mid = round(x/2)
    if nums[mid] < n:
        return True
    else:
        return False


print(middle(others, 2))
