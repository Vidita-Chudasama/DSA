"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.
Example 1:
    Input: s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:
    Input: s = "AABABBA", k = 1
    Output: 4
    Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    The substring "BBBB" has the longest repeating letters, which is 4.
Constraints:
    1 <= s.length <= 105
    s consists of only uppercase English letters.
    0 <= k <= s.length
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_len = 0
        left_index = 0
        for right_index in range(len(s)):
            count[s[right_index]] = count.get(s[right_index], 0) + 1
            window_len = right_index + 1 - left_index
            max_freq = max(count.values())            
            if window_len - max_freq > k:
                count[s[left_index]] -= 1
                left_index += 1
            window_len = right_index + 1 - left_index
            max_len = max(max_len, window_len)
        return max_len