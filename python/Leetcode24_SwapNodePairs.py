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

	def swapNodes(self):
		if self.size >=2:
			prev = self.head
			temp = self.head.next
			while True:
				if abs(prev.data - temp.data) == 1:
					data = prev.data
					prev.data = temp.data
					temp.data = data
					if temp.next != None:
						prev = temp.next
						if prev.next != None:
							temp = prev.next
						else:
							break
					else:
						break
				else:
					if temp.next != None:
						prev = temp
						temp = temp.next
					else:
						break


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
newLL.printLL()
newLL.swapNodes()
newLL.printLL()