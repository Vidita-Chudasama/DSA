"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.
Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.
Constraints:
    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        check_str = ""
        for c in s:
            if ord(c) >= 65 and ord(c) <= 90:
                c = chr(ord(c)+32)
                check_str = check_str + c
            elif (ord(c) >= 97 and ord(c) <= 122) or (ord(c) >= 48 and ord(c) <= 57):
                check_str = check_str + c
        left_index = 0
        right_index = len(check_str)-1
        while left_index < right_index:
            print(check_str[left_index], check_str[right_index])
            if check_str[left_index] != check_str[right_index]:
                return False
            left_index += 1
            right_index -=1
        return True
        