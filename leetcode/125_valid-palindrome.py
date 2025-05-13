class Solution:
    def isPalindrome(self, s: str) -> bool:
        listt=[]
        for i in s:#fix data
            if ord(i)>=ord('A') and ord('Z')>=ord(i) :
                i=i.lower()
                listt.append(i)

            elif ord(i)>=ord('a') and ord('z')>=ord(i) :
                
                listt.append(i)

            elif ord(i)>=ord('0') and ord(i)<=ord('9'):
                listt.append(i)

        for j in range((len(listt)//2)):
            if listt[j] != listt[-1-j]:
                return False

        return True
