class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic={}
        out=[]
        for ind , cha in enumerate(s):#紀錄最後出現位置
            dic[cha]=ind

        start=end=0
        for ind, cha in enumerate(s):
            if end < dic[cha]:
                end=dic[cha]
            elif end==ind:
                out.append(end-start+1)
                start=end+1
                end+=1
                
        return out
