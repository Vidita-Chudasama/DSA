"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
Example 2:
    Input: nums = []
    Output: []
Example 3:
    Input: nums = [0]
    Output: []
Constraints:
    0 <= nums.length <= 3000
    -105 <= nums[i] <= 105
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        triplets = []
        for index, num in enumerate(nums):
            left_index = index+1
            right_index = len(nums)-1
            while left_index < right_index:
                triplet = [num, nums[left_index], nums[right_index]]
                triplet_sum = sum(triplet)
                if triplet_sum < 0:
                    left_index += 1
                elif triplet_sum > 0:
                    right_index -= 1
                else:
                    if triplet not in triplets:
                        triplets.append(triplet)
                    left_index += 1
        return triplets