'''
Created on Feb 29, 2017

@author: Hannie Ngo
'''

    
# You are given an array of positive and negative integers. If a number n at an index is positive, then move forward n steps. Conversely, if it's negative (-n), move backward n steps. Assume the first element of the array is forward next to the last element, and the last element is backward next to the first element. Determine if there is a loop in this array. A loop starts and ends at a particular index with more than 1 element along the loop. The loop must be "forward" or "backward'.
# 
# Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.
# 
# Example 2: Given the array [-1, 2], there is no loop.
# 
# Note: The given array is guaranteed to contain no element "0".
# 
# Can you do it in O(n) time complexity and O(1) space complexity?

def hasLoop(nums):
    
    i = 0
    if len(nums) == 0:
        return False
#     hasLoop = False
    
    isForward = True if nums[i] >= 0 else False
    
        
    while True:

        print(i)
        #continue the circular array 
        if i >= len(nums):
            i = i % len(nums)

#         isForward_Current = False if nums[index] < 0 else True
        if nums[i] >= 0:
            current = True
        else: 
            current = False
        if isForward is not current:
            print("Against the original direction")
            return False

        #check if the next step comes into the index that is already queried
        # 
        if nums[i] == 0:
            return True
        
        tmpValue = nums[i]
        nums[i] = 0
        i = i+ tmpValue

        
    return

    

# print(hasLoop([2,-1,1,8,8]))
# print(hasLoop([1,2,3,-1]))
# print(hasLoop([2, -1, 1, 2, 2]))
# print(hasLoop([1,2,3,-1,4,3,2,1]))
print(hasLoop([2,2,2,2,-1,2,2,2]))