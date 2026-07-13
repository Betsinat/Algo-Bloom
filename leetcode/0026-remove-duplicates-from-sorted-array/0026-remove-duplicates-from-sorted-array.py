class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seek = 0
        holder = 0
        while seek < len(nums):
            if nums[seek] != nums[holder]:
                nums[seek] , nums[holder + 1] = nums[holder + 1] , nums[seek]
                holder += 1
            seek += 1
        return holder + 1

