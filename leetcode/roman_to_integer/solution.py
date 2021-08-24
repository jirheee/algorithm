from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I": 1, 
            "V": 5, 
            "X":10, 
            "L": 50, 
            "C":100, 
            "D":500, 
            "M":1000, 
            "IV":4, 
            "IX":9, 
            "XL":40, 
            "XC":90, 
            "CD":400, 
            "CM":900
        }

        parsed = self.parse(s)
        return sum([mapping[e] for e in parsed])

    def parse(self, s:str) -> List[str]:
        l = []
        while s != "":
            if s[:2] in {"IV", "IX", "XL", "XC", "CD", "CM"} :
                l.append(s[:2])
                s = s[2:]
            else: 
                l.append(s[0])
                s = s[1:]
        
        return l

print(Solution().romanToInt("MCMXCIV"))