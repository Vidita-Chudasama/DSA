"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
Please implement encode and decode
Example 1:
    Input: ["lint","code","love","you"]
    Output: ["lint","code","love","you"]
    Explanation: One possible encode method is: "lint:;code:;love:;you"
Example 2:
    Input: ["we", "say", ":", "yes"]
    Output: ["we", "say", ":", "yes"]
    Explanation: One possible encode method is: "we:;say:;:::;yes"
"""
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        encoded_str = ""
        for index_s in range(len(strs)):
            s = strs[index_s]
            if "--" in s:
                for index_c in range(len(s)):
                    if s[index_c] == "-" and s[index_c+1] == "-":
                        encoded_str = encoded_str + "//--"
                    else:
                        encoded_str = encoded_str + s[index_c]
            elif index_s == 0:
                encoded_str = encoded_str + s
            else:
                encoded_str = encoded_str + "--" + s
        return encoded_str


    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        decoded_str = []
        is_word = False
        s = ""
        index_c = 0
        while index_c < len(str):
            if str[index_c] == "/" and str[index_c+1] == "/" and str[index_c+2] == "-" and str[index_c+3] == "-":
                s = s + "--"
                index_c += 3
            elif str[index_c] == "-" and str[index_c+1] == "-":
                index_c = index_c + 1
                is_word = True
            else:
                s = s + str[index_c]
            if is_word:
                decoded_str.append(s)
                s = ""
                is_word = False
            index_c = index_c + 1
        decoded_str.append(s)
        return decoded_str