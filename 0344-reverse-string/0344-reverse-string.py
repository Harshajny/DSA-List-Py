class Solution:
    def reverseString(self, s: List[str]) -> None:
        t=''
        for i in range(int(len(s)/2)):
            t= s[(len(s)-1)-i]
            s[(len(s)-1)-i]=s[i]
            s[i]=t

        