from typing import Tuple

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        longest = i = j = 0

        while i < len(s) and j <len(s):
            if s[j] in char_set:
                char_set.remove(s[i])
                i+=1
            else:
                char_set.add(s[j])
                j+=1
                longest = max(longest, len(char_set))
                
        return longest

if __name__ == "__main__":
    s = "dvdf"
    print(Solution().lengthOfLongestSubstring(s))