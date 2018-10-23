class Node:
	def __init__(self,value=None):
		self.value=value
		self.left_child = None
		self.right_child = None

class BST:

	def __init__(self):
		self.root = None

	def insert(self, value):
		newNode = Node(value)
		if self.root == None:
			self.root = newNode
		else:
			if value < self.root.value:
				insert(self.root.left_child, value)
			else:
				insert(self.root.right_child, value)

	def print(self, root):
		current = self.root
		if (self.root.left_child != None):
			left = current.left_child
			print(self, left)
		else:
			print(" ",current.value )
		if (self.root.right_child != None):
			right = current.right_child
			print(self, right)

bst = BST()
bst.insert(8)
bst.print(8)
bst.insert(4)
bst.print(8)
bst.insert(10)
bst.print(8)
bst.insert(7)
bst.print(8)
bst.insert(9)
bst.print(8)
bst.insert(13)
bst.print(8)
bst.insert(12)
bst.print(8)
bst.insert(6)
bst.print(8)
