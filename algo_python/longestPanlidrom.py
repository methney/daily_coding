
str = "BABAD"

class Solution() : 
    def longestPalindrome(self, s:str):

        def expand(left:int, right:int):
            while left >=0 and right < len(s) and s[left]==s[right]:
                # 이부분이 이해가 안간다. 보통의 투포인터는 left+=1, right-=1 로 진행하는데말이지..
                left -= 1
                right += 1
            
            print(left,right,s[left+1:right])
            return s[left+1:right]
        
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''

        for i in range(len(s)-1):
            result = max(result,
                            expand(i, i+1),
                            expand(i, i+2),
                            key=len
                )
        
        return result

aa = Solution()
print(aa.longestPalindrome(str))