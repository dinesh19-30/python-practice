from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for n in nums:
            res=res^n
        return res    
if __name__ == "__main__":
    solution = Solution()
    nums = [4, 1, 2, 1, 2]
    print(solution.singleNumber(nums))  
