class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []

        def back(i):
            ans.append(temp[:])

            for j in range(i, len(nums)):
                temp.append(nums[j])
                back(j + 1)
                temp.pop()
        back(0)
        return ans
