from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(enumerate(nums), key = lambda x: x[1])
        ptr1 = 0
        ptr2 = len(nums_sorted) - 1
        while ptr1 != ptr2:
            sum = nums_sorted[ptr1][1] + nums_sorted[ptr2][1]
            if sum == target:
                return [nums_sorted[ptr1][0], nums_sorted[ptr2][0]]
                break
            elif sum  > target:
                ptr2 -= 1
            else:
                ptr1 += 1
        

if __name__ == "__main__":
    sol = Solution().twoSum([2,7,11,15], 9)
    print(sol)