def divideTwo(dividend, divisor):
	dividend1 = abs(dividend)
	divisor1 = abs(divisor)
	count = 0
	while dividend1 >= divisor1:
		dividend1 -= divisor1
		count+=1
	if dividend > 0 and divisor > 0:
		return count
	elif dividend < 0 and divisor < 0:
		return count
	else:
		return -count

print(divideTwo(10,3))
print(divideTwo(7,-3))