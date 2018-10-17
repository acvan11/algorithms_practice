class Node:
	def __init__(self, data):
		self.next = None
		self.data = data

class LinkedList:
	def __init__(self):
		self.head = None
		self.size = 0

	def addNode(self, data):
		newNode = Node(data)
		if self.head == None:
			self.head = newNode
		else:
			temp = self.head
			while temp.next != None:
				temp = temp.next
			temp.next = newNode
		self.size +=1

	def removeNthNode(self,n):
		if self.size == n:
			temp = self.head
			self.head = self.head.next
			temp = None
		else:
			count = self.size - n
			temp = self.head
			for i in range(count):
				previous = temp
				temp = temp.next
			previous.next = temp.next
			temp = None
			self.size -= 1


	def printLL(self):
		temp = self.head
		result = ""
		while temp.next != None:
			result += str(temp.data) + "->"
			temp = temp.next
		result += str(temp.data)
		print(result)

newLL = LinkedList()
newLL.addNode(1)
newLL.addNode(2)
newLL.addNode(3)
newLL.addNode(4)
newLL.addNode(5)
newLL.removeNthNode(5)
newLL.printLL()

