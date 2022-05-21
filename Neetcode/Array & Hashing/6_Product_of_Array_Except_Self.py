"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]
Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]
Constraints:
    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul_from_start = [0]*len(nums)
        mul_from_end = [0]*len(nums)
        nums_ans = [0]*len(nums)

        mul_from_start[0] = nums[0]
        index = 1
        while index != len(nums):
            mul_from_start[index] = mul_from_start[index-1] * nums[index]
            index += 1

        mul_from_end[len(nums)-1] = nums[len(nums)-1]
        index = len(nums)-2
        while index != -1:
            mul_from_end[index] = mul_from_end[index+1] * nums[index]
            index -= 1
            
        nums_ans[0] = mul_from_end[1]
        nums_ans[len(nums)-1] = mul_from_start[len(nums)-2]
        for index in range(1, len(nums)-1):
            nums_ans[index] = mul_from_start[index-1] * mul_from_end[index+1]
            
        return nums_ans