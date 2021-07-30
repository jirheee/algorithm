class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        if x == 0:
            return True

        l = []
        while x > 0:
            l.append(x%10)
            x//=10
        length = len(l)
        for i in range(length//2):
            if l[i] != l[length-1-i]:
                return False
        
        return True

if __name__ == "__main__":
    print(Solution().isPalindrome(11))