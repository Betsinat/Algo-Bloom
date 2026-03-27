class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def recur(string):
            if len(string) <= 1:
                return ""
            
            quick = set(string)
            for i in range(len(string)):
                if string[i].swapcase() not in quick:
                    l = recur(string[:i])
                    r = recur(string[i + 1:])
                    if len(l) >= len(r):
                        return l
                    return r
            return string
        return recur(s)
