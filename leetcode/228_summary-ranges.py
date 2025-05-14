class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:return []
        output=[]
        temp=str(nums[0])
        nums.append(-100000000)
        i=0
        for i in range(len(nums)-1):

            if  nums[i]+1 == nums[i+1]:               
                continue

            else:#不等於下一個
                if  nums[i-1]+1 != nums[i]:
                    output.append(temp)
                    temp=str(nums[i+1])
                else:
                    temp+='->'
                    temp+=str(nums[i])
                    output.append(temp)
                    temp=str(nums[i+1])
                
          
        return output
