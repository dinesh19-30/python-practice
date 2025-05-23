from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res,count=0,0
        for i in nums:
            if count==0:
                res=i
            count+=(1 if res==i else -1)    
        return res    

if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 3]
    print(solution.majorityElement(nums))  
