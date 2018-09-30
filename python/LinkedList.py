class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None
		self.size = 0

	def size(self):
		return size

	def insertFront(self,data):
		temp = self.head
		newNode = Node(data)
		self.head = newNode
		newNode.next = temp
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
				break
			previousNode = currentNode
			currentNode = currentNode.next
			currentPosition += 1
		self.size += 1

	def printList(self):
		list = []
		currentNode = self.head
		while currentNode != None:
			list.append(currentNode.data)
			currentNode = currentNode.next
		print(list)


newLL = LinkedList()
newLL.insertEnd(3)
newLL.insertEnd(6)
newLL.insertEnd(4)
newLL.insertEnd(1)
newLL.insertAt(22,2)
newLL.insertAt(100,1)
newLL.insertAt(200,0)
newLL.insertAt(500,7)
newLL.insertAt(500,90)
newLL.printList() 
