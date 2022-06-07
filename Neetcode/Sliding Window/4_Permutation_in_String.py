"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.
Example 1:
    Input: s1 = "ab", s2 = "eidbaooo"
    Output: true
    Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
    Input: s1 = "ab", s2 = "eidboaoo"
    Output: false
Constraints:
    1 <= s1.length, s2.length <= 104
    s1 and s2 consist of lowercase English letters.
"""
class Solution:
    def countFreq(self, s: str) -> dict:
        count = {}
        for index in range(len(s)):
            count[s[index]] = count.get(s[index], 0) + 1
        return count
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left_index = 0
        right_index = len(s1) - 1
        s1_freq = self.countFreq(s1)
        while right_index < len(s2):
            s2_freq = self.countFreq(s2[left_index:right_index+1])
            if s1_freq == s2_freq:
                return True
            right_index += 1
            left_index += 1
        return False