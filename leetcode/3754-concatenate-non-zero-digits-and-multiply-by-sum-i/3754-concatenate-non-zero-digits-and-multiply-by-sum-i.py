class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)
        num = ""
        for i in range(len(s)):
            if s[i] != "0":
                num += s[i]
        if len(num) == 0:
            return 0
        su = 0
        for s in num:
            su += int(s)
        return su * int(num)
        