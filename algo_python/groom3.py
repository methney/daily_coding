
# ============================
# NOT YET SOLVED!!!!
# ============================

import sys
import collections

n = int(sys.stdin.readline())
data = [sys.stdin.readline().split() for i in range(n)]
d = collections.defaultdict(int)
data2 = [[y,z] for x,y,z in sorted(data, key=lambda x:x[1])]

def solution(data):
	# for i,v in enumerate(data2):
	# 	widen(int(v[0]),int(v[1]))
	
	for i,v in enumerate(data2):
		for j in range(i):
			print(v,data2[j])
		print('------')
		
			
		# d[v[1]] += 1
		# d[v[2]] -= 1
				
def widen(s,e):
	while s <= e:
		d[s]+=1
		s+=1

solution(data)