class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            l = i + 1
            while l < n  and nums[l] - nums[i] < diff:
                l += 1
            if l < n and nums[l] - nums[i] == diff:
                
                r = l + 1
                while r < n and nums[r] - nums[l] < diff:
                    r += 1
                if r < n and nums[r] - nums[l] == diff:

                    count += 1
        return count
            
        
                    
                

