import collections
def solution(arr):
    
    d = collections.defaultdict(int)

    for v in arr:
        d[v] = d.get(v,0)+1

    ret = []
    for v in d: 
        if v == d[v]:
            ret.append(v)
    
    if len(ret) == 0 :
        return -1

    

arr = [1,1,2,3,3]
print(solution(arr))

arr = [0]
print([int(x) for x in arr])