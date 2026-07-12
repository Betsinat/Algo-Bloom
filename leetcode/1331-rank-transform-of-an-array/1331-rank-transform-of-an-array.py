class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = sorted(list(set(arr)))
        m = {}
        for index, num in enumerate(a):
            m[num] = index + 1
        return [m[num] for num in arr]



           




        