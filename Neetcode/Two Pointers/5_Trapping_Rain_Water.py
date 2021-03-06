"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Example 1:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:
    Input: height = [4,2,0,3,2,5]
    Output: 9
Constraints:
    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105
"""
class Solution:
    def trap(self, heights: List[int]) -> int:
        ans = 0
        left_index = 0
        right_index = len(heights) - 1
        left_max = heights[left_index]
        right_max = heights[right_index]
        while left_index < right_index:
            if left_max < right_max:
                if left_max - heights[left_index] > 0:
                    ans += (left_max - heights[left_index])
                left_index += 1
                left_max = max(left_max, heights[left_index])
            else:
                if right_max - heights[right_index] > 0:
                    ans += (right_max - heights[right_index])
                right_index -= 1
                right_max = max(right_max, heights[right_index])
        return ans