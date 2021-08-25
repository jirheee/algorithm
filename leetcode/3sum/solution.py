from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ptr1 = 0
        ptr2 = len(nums) - 1

        l = []
        
        while ptr1 != ptr2:
            searched = self.binary_search(nums, ptr1 + 1, ptr2 - 1, -nums[ptr1]-nums[ptr2])
            sum = nums[searched]+nums[ptr1]+nums[ptr2]
            print(sum, l)
            print(ptr1, ptr2, searched)
            if sum==0:
                if not [nums[ptr1], nums[searched], nums[ptr2]] in l:
                    l.append([nums[ptr1], nums[searched], nums[ptr2]])
                ptr1 += 1
            elif sum > 0:
                ptr2 -= 1
            else:
                ptr1 += 1
        
        return l

    def binary_search(
        self, 
        nums: List[int], 
        start: int, 
        end: int, 
        target: int
        ) -> int:

        if start - end == 1:
            return (start + end)//2
        hi = end
        lo = start
        
        while hi != lo:
            mid = (hi + lo)//2
            print(hi, lo, mid, nums[mid], target)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return hi

if __name__ == "__main__":
    sol = Solution()
    assert sol.binary_search([0], 0, 0, 0) == 0

    l = [0, 4, 5, 9, 10, 11]
    assert sol.binary_search(l, 0, 6, 0) == 0
    assert sol.binary_search(l, 0, 6, 4) == 1
    assert sol.binary_search(l, 0, 6, 5) == 2
    assert sol.binary_search(l, 0, 6, 9) == 3
    assert sol.binary_search(l, 0, 6, 2) == 0

    print(sol.threeSum([-1,0,1,2,-1,-4]))