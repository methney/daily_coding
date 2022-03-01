
import collections 
def solution(str1,str2):
    d = collections.defaultdict(list)
    for v in str1:
        d[v] = d.get(v,0)+1
    for v in str2:
        d[v] = d.get(v,0)-1
    
    ret = ''
    for v in d:
        if d[v] < 0:
            ret += v
    
    print(ret)

str1 = 'abcd'
str2 = 'cbdae'

solution(str1,str2)