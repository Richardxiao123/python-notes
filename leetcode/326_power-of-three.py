class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:return True
        list=[1]
        while list[-1] < n:
            list.append(list[-1]*3)
            if list[-1]==n:
                return True

        return False
