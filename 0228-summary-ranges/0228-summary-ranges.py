class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        arr = []
        start = 0
        if not nums:
            return []
        for i in range(1 ,len(nums)):
            if nums[i] -  nums[i-1] != 1:
                if nums[start] == nums[i-1]:
                    arr.append(str(nums[start]))
                else:
                    arr.append(f"{nums[start]}->{nums[i-1]}")
                start = i
        if nums[start] == nums[-1]:
            arr.append(str(nums[start]))
        else:
             arr.append(f"{nums[start]}->{nums[-1]}")  
        return arr


                



        