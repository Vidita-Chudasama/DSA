"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
Example 1:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:
    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9
Constraints:
    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        seq_starting_nums = []
        for num in nums:
            if num-1 not in nums_set:
                seq_starting_nums.append(num)
        max_len = 0
        for num in seq_starting_nums:
            next_num = num + 1
            curr_len = 1
            while next_num in nums_set:
                curr_len = curr_len + 1
                next_num = next_num + 1
            if curr_len > max_len:
                max_len = curr_len
        return max_len