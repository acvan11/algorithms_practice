'''
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
def sum3(arr):
	result = []
	for i in range(0,len(arr)-2):
		for j in range(i+1, len(arr)-1):
			for k in range(i+2, len(arr)):
				if arr[i] + arr[j] + arr[k] == 0:
					arr1 = [arr[i], arr[j], arr[k]]
					if not checkDuplicate(result, arr1):
						result.append(arr1)
	print(result)

def checkDuplicate(arrBig, arrSmall):
	value = False
	for i in arrBig:
		if i[0] in arrSmall and i[1] in arrSmall and i[2] in arrSmall:
			value = True
	return value

sum3([-1,0,1,2,-1,-4])


