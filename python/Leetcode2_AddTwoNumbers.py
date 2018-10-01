from LinkedList import LinkedList

def AddTwoNumbers(llist1, llist2):
	llist3 = LinkedList()
	position = 0
	carry = 0

	while position < llist1.size or position < llist2.size:
		if position >= llist1.size:
			x = 0
		else:
			x = llist1.valueAt(position)
		if position >= llist2.size:
			y = 0
		else:
			y = ll2.valueAt(position)
		
		llist3.insertEnd((x+y+carry) % 10)
		carry = (x+y)//10
		position += 1
	if carry == 1:
		llist3.insertEnd(1)
	llist3.printList()


ll1 = LinkedList()
ll1.create([1,2,5])
ll2 = LinkedList()
ll2.create([3,4,5])
ll1.printList()
ll2.printList()
AddTwoNumbers(ll1,ll2)


