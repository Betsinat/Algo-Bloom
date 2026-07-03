class Solution:
    def repeatedCharacter(self, s: str) -> str:
   
       h = {}
       for c in s:
        if c in h:
            h[c] += 1
            return c
        else:
            h[c] = 1
       
        
        

         

       
       

            
            
            
        
        
        