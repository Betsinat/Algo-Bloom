class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        arr = set()
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                ta = nums[i] + nums[right] + nums[left]
                if ta == target:
                    return ta
                elif ta > target:
                    arr.add(ta)
                    right -= 1
                else:
                    arr.add(ta)
                    left += 1
        return min(arr, key=lambda x: abs(target - x))

