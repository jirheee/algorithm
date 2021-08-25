from typing import List

class Solution:
    def get_distance(self, x: int, e: int) -> int:
        return x - e if x >= e else e - x

    def findClosestElements(self, arr:List[int], k:int, x: int) -> List[int]:
        total_dist = sum([self.get_distance(x, e) for e in arr[0:k]])
        dists = [0 for _ in range(len(arr)-k+1)]
        dists[0] = total_dist
        max_idx = 0
        
        for i in range(0, len(arr)-k):
            new_dist = total_dist - self.get_distance(x, arr[i]) + self.get_distance(x, arr[i+k])
            dists[i+1] = new_dist
            if total_dist > new_dist:
                max_idx = i+1
            total_dist = new_dist

        return arr[max_idx:max_idx+k]

if __name__ == "__main__":
    arr = [1,1,1,10,10,10]
    k = 1
    x = 9
    answer = Solution().findClosestElements(arr, k, x)
    print(answer)