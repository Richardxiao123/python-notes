class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:return False   
        x=str(x)
        
        n=len(x)//2
        for i in range(n):
            if x[i]!= x[-1-i]:
                return False    
        return True
