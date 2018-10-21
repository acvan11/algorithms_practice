'''
Given a text file file.txt, transpose its content.

You may assume that each row has the same number of columns and each field is separated by the ' ' character.

Example:

If file.txt has the following content:

name age
alice 21
ryan 30
Output the following:

name alice ryan
age 21 30
'''

result1 = []
result2 = []
result3 = []

with open('file194.txt', 'r') as f:
	for line in f:
		result1.append(line.split())
size = len(result1[0])
for i in range(size):
	result2.append([])
for i in result1:
	for j in range(len(i)):
		result2[j].append(i[j])
for i in result2:
	str = ""
	for j in i:
		str += j + " "
	result3.append(str)
for i in result3:
	print(i)
