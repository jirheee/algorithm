from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        l = [0, 1]
        for i in range(1, n):
            l += [2**i + j for j in l[::-1]]
        return l