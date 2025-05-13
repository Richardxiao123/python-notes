class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        l=columnTitle[::-1]
        cnt=0
        n=0

        for i in  l:
            cnt+=(26**n)*(ord(i)-ord('A')+1)
            n+=1

        return cnt
