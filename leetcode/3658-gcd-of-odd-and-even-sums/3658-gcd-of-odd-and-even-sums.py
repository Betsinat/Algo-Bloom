import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even = 0
        odd = 0
        for i in range(2*n):
            if i % 2 == 0:
                even += i
            else:
                odd += i

        return(math.gcd(even , odd))
        
