class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        n=len(strs)
        idx=len(strs[0]) # 切到第幾個
        
        for i  in range(n):
            while prefix != strs[i][:idx]:
                idx=idx-1
                prefix=prefix[:idx]

          
        return prefix[:idx]         
            
