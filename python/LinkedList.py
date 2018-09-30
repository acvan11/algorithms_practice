class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None
		self.size = 0

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
newLL.insertEnd(1)
newLL.insertFront(2)
newLL.insertPosition(55,2)
newLL.printList()
