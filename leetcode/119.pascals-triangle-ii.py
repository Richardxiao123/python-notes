class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        pascal=[[1]]
        for i in range(1,rowIndex+1):
            prev=pascal[-1]
            temp=[1]
            for j in range(len(prev)-1):
                temp.append(prev[j]+prev[j+1])
            temp.append(1)
            pascal.append(temp)
            
        return pascal[-1]
