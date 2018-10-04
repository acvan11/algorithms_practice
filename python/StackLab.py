class Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next
	
	def __str__(self):
		return str(self.data)

class Stack:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def push(self, data):
		if self.size == 0:
			self.head = Node(data, None)
			self.tail = self.head
		elif self.size == 1:
			self.tail = Node(data, self.head)
		else:
			temp = self.tail
			self.tail = Node(data, temp)
		self.size += 1

	def pop(self):
		if self.size <= 0:
			return None
		elif self.size == 1:
			self.head = self.tail = None
		else:
			self.tail = self.tail.next
		self.size -= 1
	def print(self):
		result = []
		temp = self.tail
		while temp != None:
			result.append(temp.data)
			temp = temp.next
		print(result)
		

myStack = Stack()
myStack.print()
myStack.push(1)
myStack.print()
myStack.push(2)
myStack.print()
myStack.push(3)
myStack.print()
myStack.push(4)
myStack.print()
print('------')
myStack.pop()
myStack.print()
myStack.pop()
myStack.print()
myStack.pop()
myStack.print()
myStack.pop()
myStack.print()
myStack.pop()
myStack.print()


