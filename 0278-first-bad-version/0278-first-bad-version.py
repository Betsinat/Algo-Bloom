# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l , h = 0 , n
        while l < h:
            mid = (l + h) // 2
            if isBadVersion(mid):
                h = mid
            else:
                l = mid + 1
        return l

        