from typing import List

class Solution:
    def findClosestElements(self, arr:List[int], k:int, x: int) -> List[int]:
        if x <= arr[0]: return arr[:k]
        if x >= arr[-1]: return arr[len(arr) - k:]

        l = []

        hi = len(arr) - 1
        lo = 0

        mid = -1
        while hi > lo :
            mid = (hi + lo)//2
            if arr[mid] == x:
                break
            elif arr[mid] > x:
                hi = mid - 1
            else:
                lo = mid + 1
        
        count = k
        odd = 0
        if mid - k//2 >0:
            return [arr]

