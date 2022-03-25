
str = "BABAD"
str = "BABABD"

# i = 0, expand(0,1) >> s[0]==s[1]? False 
#        expand(0,2) >> s[0]==s[2]? True >> s[-1+1:3]==BAB
# i = 1, expand(1,2) >> s[1]==s[2]? False
#        expand(1,3) >> s[1]==s[3]? True >> s[0+1:4]==ABA
# i = 2, expand(2,3) >> s[2]==s[3]? False
#        expand(2,4) >> s[2]==s[4]? False
# i = 3, expand(3,4) >> s[3]==s[4]? False
#        expand(3,5) >> s[3]==s[5]???? 이게 말이되나? s[5]는 없는데? 
#        >> 에러가 나는게 맞고, 하지만 while 문안에서 right<len(s)에서 이미 해당부분이 짤리게되어 에러가 안나는거다.


# -------------- loop ---------------------------------
# 
#  arr[::-1] 완전히 뒤짚기 [5,4,3,2,1]
# 
# -----------------------------------------------------

class Solution() : 
    def longestPalindrome(self, s:str):
        def expand(left:int, right:int):
            while left >=0 and right < len(s) and s[left]==s[right]:
                # 이부분이 이해가 안간다. 보통의 투포인터는 left+=1, right-=1 로 진행하는데말이지..
                # 이건 거꾸로 하나씩 확장해나간다.
                left -= 1
                right += 1
            return s[left+1:right]
        
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''

        # 5-1 = 4 근데, 4를 포함하지않으니, 0,1,2,3 이거 4개만 도는거다.
        # expand(i,i+2)는 string길이상으로는 에러가 나야하는데.. 나지않는다. >> 위에서 설명 
        # expand(i,i+1)와 expand(i,i+2)가 짝홀수개념으로 늘려가면서 테스트를하게된다. 이것도 외우지 않으면 생각하기 어려운부분이다.
        for i in range(len(s)-1):
            print(result,'/',expand(i,i+1),'/',expand(i,i+2))
            result = max(result,
                            expand(i, i+1),
                            expand(i, i+2),
                            key=len)
        
        return result

aa = Solution()
print(aa.longestPalindrome(str))



