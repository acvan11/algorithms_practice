class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.size = 0

	def insertFront(self,data):
		currentNode = self.head
		newNode = Node(data)
		self.head = newNode
		newNode.next = currentNode
		self.size += 1

	def insertEnd(self, data):
		newNode = Node(data)
		if self.head is None:
			self.head = newNode
		else:
			lastNode = self.head
			while True:
				if lastNode.next is None:
					break
				lastNode = lastNode.next
			lastNode.next = newNode
		self.size += 1

	def insertAt(self,data, pos):
		new_Node = Node(data)
		currentNode = self.head
		currentPosition = 0
		if pos < 0 or pos > self.size:
			return None 
		while True:
			if pos == 0:
				self.insertFront(data)
				break
			if currentPosition == pos:
				previousNode.next = new_Node
				new_Node.next = currentNode
				self.size += 1
				break
			previousNode = currentNode
			currentNode = currentNode.next
			currentPosition += 1
	
	def deleteLastNode(self):
		currentNode = self.head
		if self.size == 1:
			self.head = None
		else:
			while currentNode.next is not None:
				previousNode = currentNode
				currentNode = currentNode.next
			previousNode.next = None
		self.size -= 1

	def deleteFirstNode(self):
		currentNode = self.head
		if self.size == 1:
			self.head = None
		else:
			self.head = self.head.next
		self.size -= 1

	def deleteNodeAt(self, pos):
		if pos == 0:
			self.deleteFirstNode()
		elif pos == self.size - 1:
			self.deleteLastNode()
		else:
			currentNode = self.head
			position = 0
			while not position == pos:
				previousNode = currentNode
				currentNode = currentNode.next
				position += 1
			previousNode.next = currentNode.next
			self.size -= 1

	def printList(self):
		result = ''
		temp = self.head
		while temp.next != None:
			result += str(temp.data) + '->'
			temp = temp.next
		result += str(temp.data) 
		print(result)

	def valueAt(self, pos):
		currentNode = self.head
		position = 0
		while not position == pos:
			currentNode = currentNode.next
			position += 1
		return currentNode.data

	def create(self,arr):
		for i in arr:
			self.insertEnd(i)

def merge(h1, h2):
	temp = None
	if h1 == None:
		return h2
	if h2 == None:
		return h1
	if h1.data < h2.data:
		temp = h1
		temp.next = merge(h1.next,h2)
	else:
		temp = h2
		temp.next = merge(h1,h2.next)
	return temp


h1 = LinkedList()
h1.insertEnd(2)
h1.insertEnd(5)
h2 = LinkedList()
h2.insertEnd(3)
h2.insertEnd(4)
h3 = LinkedList()
h3.head = merge(h1.head, h2.head)
h3.printList()

