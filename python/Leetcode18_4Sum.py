def sum4(arr, target):
	result = []
	for i in range(len(arr) - 3): 
		for j in range(i+1, len(arr) -2):
			for k in range(j+1, len(arr) -1):
				for l in range(k+1, len(arr)):
					if arr[i] + arr[j] + arr[k] + arr[l] == target:
						result2 = [arr[i], arr[j], arr[k], arr[l]]
						if not checkDuplicate(result, result2):
							result.append(result2)
	print(result)

def checkDuplicate(bigarr, smallarr):
	result = False
	for i in bigarr:
		if i[0] in smallarr and i[1] in smallarr and i[2] in smallarr and i[3] in smallarr:
			result = True
	return result

sum4([1, 0, -1, 0, -2, 2],0)