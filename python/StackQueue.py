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

from collections import deque

class Queue:
	def __init__(self):
		self.data = deque()

	def enqueue(self, item):
		self.data.append(item)
	
	def dequeue(self):
		return self.data.popleft()
	
	def __len__(self):
		return len(self.data)
	
myStack = Stack()
myStack.push('A')
myStack.push('N')
myStack.push('D')
myStack.push('Y')

print("myStack:", myStack)
temp=Queue()
while len(myStack)>0:
	temp.enqueue(myStack.pop())

while len(temp)>0:
	myStack.push(temp.dequeue())
print("myStack:", myStack.data)
print("temp:", temp.data)


# class Stack_Node():
#     def __init__(self, payload=None):
#         self.next = None
#         self.payload = payload

#     def get_payload():
#         return self.payload

#     def set_payload(self,payload):
#         self.payload = payload
#         return self.payload
    
#     def get_next():
#         return self.next

#     def set_next(self,node):
#         self.next = node

#     def __str__(self): 
#         return str(self.payload)

# class Stack:
#     def __init__(self):
#         self.head = None

#     def push(self, payload):
#         new_node = Stack_Node(payload)
#         if self.head is None:
#             self.head = new_node
#         else:
#             new_node.set_next(self.head)
#             self.head = new_node

#     def pop(self):
#         to_return = self.head
#         if to_return is not None:
#             self.head = to_return.next
#         return to_return

# stack = Stack()

# stack.push(1)
# stack.push(2)
# stack.push(3)

# print(stack.pop())
# print(stack.pop())
# print(stack.pop())