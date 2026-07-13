class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        arr = set()
        nums.sort()
        for i in range(len(nums)):
             left = i + 1
             right = len(nums) - 1
             while left < right:
                curr = nums[left] + nums[right] + nums[i]
                if curr == 0:
                    arr.add((nums[left] , nums[right] , nums[i]))
                    left += 1
                    right -= 1
                elif curr  > 0:
                    right -= 1
                else:
                    left += 1
        return [list(a) for a in arr] 


        
        