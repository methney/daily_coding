# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# user_input = input()
# print ("Hello Goorm! Your input is " + user_input)
import math

d = dict()
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i,v in enumerate(alphabets):
		d[i] = v 

def solution(arr):
	# arr = input.split()	
	pick = 0
	ret = ''
	for i in range(len(arr[2])):
		# print(arr[2][i])			
		fix = math.pow(int(arr[1]),int(i)+1)
		ret += moveAlpha(arr[2][i],fix)
	print(ret)
		
def moveAlpha(cha,move):
	idx = alphabets.index(cha)
	return d[idx+move%26]

# 입력을 이렇게 받아야함...미친 진짜..미친쉑키들!!
inputArr = [x for x in input().split()]
inputArr.append(input())
solution(inputArr)

