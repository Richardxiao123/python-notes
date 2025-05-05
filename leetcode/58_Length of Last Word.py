class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idx=-1
        cnt=0
        while s[idx]==' ':
            cnt+=1
            idx-=1

      
        while s[idx] != ' ':          
            idx-=1
            if -idx > len(s):return len(s)-cnt

        return -idx-cnt-1
