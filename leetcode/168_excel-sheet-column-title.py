class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        string = ''
        while columnNumber > 0:
            columnNumber -= 1  
            n = chr(ord('A') + columnNumber % 26)
            string = n + string  
            columnNumber //= 26
        return string
