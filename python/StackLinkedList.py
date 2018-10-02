class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class StackLinkedList:
	def __init__(self):
		self.top = None
		self.size = 0


	def push(self, data):
		lastNode = Node(data)
		if self.size == 0:
			lastNode.next = None
			self.top = lastNode
		else:
			lastNode.next = self.top
			self.top = lastNode
		self.size += 1

	def peek(self):
		return self.top.data

	def pop(self):
		if self.size <= 0:
			return None
		if self.size == 1:
			self.top = None
			self.size -= 1
		else:
			self.top = self.top.next
			self.size -= 1

	def printStack(self):
		result = []
		current = self.top
		while current != None:
			result.append(current.data)
			current = current.next
		print(result)

class QueueLinkedList:
	def __init__(self):
		self.first = None
		self.size = 0

	def enqueue(self,data):
		newNode = Node(data)
		if self.size == 0:
			self.first = newNode
			newNode.next = None
		else:
			current = self.first
			while current.next != None:
				current = current.next
			current.next = newNode
		self.size += 1

	def dequeue(self):
		if self.size <= 0:
			return None
		if self.size == 1:
			self.first = None
		else:
			self.first = self.first.next
		self.size -= 1

	def peek(self):
		current = self.first
		while current.next != None:
			return current.data

	def printQueue(self):
		result = []
		current = self.first
		while current != None:
			result.append(current.data)
			current = current.next
		print(result)

myQueue = QueueLinkedList()
myQueue.enqueue(4)
myQueue.printQueue()
myQueue.enqueue(3)
myQueue.printQueue()
myQueue.enqueue(6)
myQueue.printQueue()
myQueue.enqueue(8)
myQueue.printQueue()
myQueue.enqueue(7)
myQueue.printQueue()
myQueue.enqueue(1)
myQueue.printQueue()
myQueue.enqueue(9)
myQueue.printQueue()
myQueue.dequeue()
myQueue.printQueue()
