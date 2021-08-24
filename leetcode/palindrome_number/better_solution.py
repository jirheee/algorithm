class Solution():
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        elif x==0: return True

        original_x = x
        reversed_num = 0
        while x > 0:
            reversed_num = reversed_num * 10 + x%10
            x//=10
        
        return reversed_num == original_x
        