'''
/*
We are working on a security system for a badged-access room in our company's building.
We want to find employees who badged into our secured room unusually often. We have an unordered list of names and access times over a single day. Access times are given as numbers up to four-digits in length using 24-hour time, such as "800" or "2250".
Write a function that finds anyone who badged into the room 3 or more times in a 1-hour period, and returns each time that they badged in during that period. (If there are multiple 1-hour periods where this was true, just return the first one.)
badge_times = [
  ["Paul",     1355],
  ["Jennifer", 1910],
  ["John",      830],
  ["Paul",     1315],
  ["John",      835],
  ["Paul",     1405],
  ["Paul",     1630],
  ["John",      855],
  ["John",      930],
  ["John",      915],
  ["John",      730],
  ["Jennifer", 1335],
  ["Jennifer",  730],
  ["John",     1630],
]
Expected output:
  John:  830  835  855  915  930
  Paul: 1315 1355 1405
*/
'''
import math
def security(arr):
	dic = {}
	for i in arr:
		if i[0] not in dic.keys():
			dic[i[0]] = [i[1]]
		else:
			dic[i[0]].append(i[1])
	for key in dic:
		dic[key].sort()	
		if len(threeTimes1hour(dic[key])) >=3:
			s = key + " : "
			for i in threeTimes1hour(dic[key]):
				s += str(i) + " " 
			print(s)		

def threeTimes1hour(arr):
	result = []
	arr2 = []
	for i in range(len(arr)-1):
		if len(arr2) == 0:
			arr2 = [arr[i]]
		if arr[i+1]-arr[i] < 100:
			arr2 += [arr[i+1]]
		elif len(arr2) >=3:
			result += arr2 
			arr2 = []
		else:
			arr2 = []
	return result


arr = [
  ["Paul",     1355],
  ["Jennifer", 1910],
  ["John",      830],
  ["Paul",     1315],
  ["John",      835],
  ["Paul",     1405],
  ["Paul",     1630],
  ["John",      855],
  ["John",      930],
  ["John",      915],
  ["John",      730],
  ["Jennifer", 1335],
  ["Jennifer",  730],
  ["John",     1630],
]
security(arr)
