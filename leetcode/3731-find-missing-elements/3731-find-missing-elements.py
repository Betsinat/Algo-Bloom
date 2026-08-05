class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        r = max(nums)
        m = min(nums)
        arr = []
        for i in range(m , r + 1):
            if i not in nums:
                arr.append(i)
        return arr


        