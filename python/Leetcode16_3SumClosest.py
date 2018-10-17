def sum3Closest(arr, target):
	result = []
	closest = max(arr) * 3
	temp = 0
	for i in range(len(arr)-2):
		for j in range(i+1, len(arr)-1):
			for k in range(j+1, len(arr)):
				temp = arr[i] + arr[j] + arr[k]
				if abs(temp - target) < closest:
					result = [arr[i], arr[j], arr[k]]
					closest = abs(temp - target)
	print(result)

sum3Closest([-1, 2, 1, -4], 1)