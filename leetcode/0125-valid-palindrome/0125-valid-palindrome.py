class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = "".join([ch for ch in s if ch.isalnum()])
        stl = st.lower()
        left = 0
        right = len(stl) - 1
        print(stl)
        while left <= right:
            if stl[left] != stl[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
