"""
Given a string s, find the length of the longest substring without repeating characters.
Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        left_index = 0
        max_len = 1
        last_occurance_index = {s[0]: 0}
        for right_index in range(1, len(s)):
            if s[right_index] in s[left_index:right_index]:
                left_index = last_occurance_index[s[right_index]] + 1
            else:
                substr = s[left_index:right_index+1]
                if len(substr) > max_len:
                    max_len = len(substr)
            last_occurance_index[s[right_index]] = right_index
        return max_len