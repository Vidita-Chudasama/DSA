"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true
Example 2:
    Input: s = "rat", t = "car"
    Output: false
Constraints:
    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.       
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = {}
        dict_t = {}
        for index in range(len(s)):
            # for s
            character = s[index]
            if character in dict_s.keys():
                dict_s[character] += 1
            else:
                dict_s[character] = 1
            # for t
            character = t[index]
            if character in dict_t.keys():
                dict_t[character] += 1
            else:
                dict_t[character] = 1
        if dict_s == dict_t:
            return True
        else:
            return False