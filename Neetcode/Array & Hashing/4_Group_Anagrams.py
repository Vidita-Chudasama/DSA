"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:
    Input: strs = [""]
    Output: [[""]]
Example 3:
    Input: strs = ["a"]
    Output: [["a"]]
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = collections.defaultdict(list)
        strs_sorted = [0] * len(strs)
        for index in range(len(strs)):
            strs_sorted[index] = tuple(sorted(strs[index]))
        for index in range(len(strs)):
            strs_dict[strs_sorted[index]].append(strs[index])
        return strs_dict.values()