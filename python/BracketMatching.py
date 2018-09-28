#Solution

class Stack:
	def __init__(self):
		self.data = []
	def push(self, value):
		self.data.append(value)
	
	def pop(self):
		if len(self.data) > 0:
			return self.data.pop()
		else:
			return None
	
	def __len__(self):
		return len(self.data)


def test_brackets(junk):
	s = Stack()
	openers = ['(', '[', '{']
	closers = [')', ']', '}']
	for c in junk:
		if c in openers:
			s.push(c)
		elif c in closers:
			hold = s.pop()
			if not hold or openers.index(hold) != closers.index(c):
				return False
	if len(s)>0:
		return False
	else:
		return True



print(test_brackets('abc(123)'))
print(test_brackets('abc(123'))
print(test_brackets('a[bc(123)]'))
print(test_brackets('a[bc(12]3)'))
print(test_brackets('a{b}{c(1[2]3)}'))
print(test_brackets('a{b}{c(1}[2]3)'))
print(test_brackets('()'))
print(test_brackets('[]]'))
print(test_brackets('abc123yay'))

# from collections import deque

# class Stack:
# 	def __init__(self):
# 		self.data = []
# 	def push(self, value):
# 		self.data.append(value)
	
# 	def pop(self):
# 		if len(self.data) > 0:
# 			return self.data.pop()
# 		else:
# 			return None
	
# 	def __len__(self):
# 		return len(self.data)

# def BracketMatching(str):
# 	myStack = Stack()
# 	for i in str:
# 		if (i == '{') or (i =='}') or (i == '[') or (i ==']') or (i =='(') or (i ==')'):
# 			if (myStack.data[:-1] == i):
# 				myStack.pop()
# 			else:
# 				myStack.push(i)
# 	print('arr= ', myStack.data)
# 	print('length of arr= ', len(myStack.data))
# 	if len(myStack.data) % 2 != 0:
# 		return False
# 	if len(myStack.data) == 0:
# 		return True
	
# 	print('first element of arr= ',myStack.data[0])
# 	print('last element of arr= ',myStack.data[-1])
	
# 	if (myStack.data[0] == '[' or myStack.data[-1] != ']'):
# 		return False
# 	if (myStack.data[0] == '(' or myStack.data[-1] != ')'):
# 		return False
# 	if ([myStack.data[0] == '{' or myStack.data[-1]] !='}'):
# 		return False 
# 	return True




# print(BracketMatching('abc(123)'))
# print('---------------')
# print(BracketMatching('abc(123'))
# print('---------------')
# print(BracketMatching('a[bc(123)]'))
# print('---------------')
# print(BracketMatching('a[bc(12]3)'))
# print('---------------')
# print(BracketMatching('a{b}{c(1[2]3)}'))
# print('---------------')
# print(BracketMatching('a{b}{c(1}[2]3)'))
# print('---------------')
# print(BracketMatching('()'))
# print('---------------')
# print(BracketMatching('[]]'))
# print('---------------')
# print(BracketMatching('abc123yay'))

