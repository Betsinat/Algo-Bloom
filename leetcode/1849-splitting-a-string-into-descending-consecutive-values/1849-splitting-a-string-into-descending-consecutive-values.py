class Solution:
    def splitString(self, s: str) -> bool:
        ans = []
        temp = []

        def back(i):
            if i == len(s):
                return True
            curr = ""
            for j in range(i, len(s)):
                curr += s[j]
                if int(curr) - int(temp[-1]) == -1:
                    temp.append(curr)
                    if back(j + 1):
                        return True
                    temp.pop()
            return False

        for i in range(len(s) - 1):
            c = s[:i+1]
            temp.append(c)
            if back(i + 1):
                return True
            temp.pop()

        return False