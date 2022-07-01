"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
Example 1:
    Input: s = "()"
    Output: true
Example 2:
    Input: s = "()[]{}"
    Output: true
Example 3:
    Input: s = "(]"
    Output: false
Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        mapped_parenthesis = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for c in s:
            if c in mapped_parenthesis.values():
                stack.append(c)
                continue
            if len(stack) != 0 and stack[-1] == mapped_parenthesis[c]:
                    stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False