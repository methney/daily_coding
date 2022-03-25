# ============================
# NOT YET SOLVED!!!!
# ============================

def solution(arr):
	k = int(arr[0]) # 가능점프횟수
	steps = list(map(int,arr[2].split()))
	psb = max(steps)//k
	ret = []
	for i in range(len(steps)):
		step = steps[i]
		diff = 0
		for j in range(i):
			diff = max(diff, step - int(steps[j])) # 계단간의 이동가능 점프력중 최대값
			diff = step - int(steps[j])
	
		ret.append(max(psb,diff))
	print(max(ret))


inputArr = [x for x in input().split()]
inputArr.append(input())
solution(inputArr)
