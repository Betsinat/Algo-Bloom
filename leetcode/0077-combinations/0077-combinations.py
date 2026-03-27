class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]
        used = set()
        temp = []
        ans = []

        def back(i):
            if len(temp) == k:
                ans.append(temp[:])
                return
            for j in range(i + 1, len(nums)):
                temp.append(nums[j])
                back(j)
                temp.pop()
        for i in range(n):
            temp.append(nums[i])
            back(i)
            temp.pop()
        return ans