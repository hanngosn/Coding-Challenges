class Node(object):

	def __init__(self, data = None, next_node = None):
		self.data = data
		self.next_node = next_node

	def getData(self):
		return self.data

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		self.next_node = new_next

class LinkedList(object): #singly linked list
	
	def __init__(self, head=None):
		self.head = head

	def size(self):
		current = self.head
		count = 0 
		while current:
			count += 1
			current = current.get_next()
		return count

	# O(1), kind of pushing other nodes backward	
	def insertAtHead(self, data):
		tmpNode = Node(data)
		tmpNode.set_next(self.head)
		self.head = tmpNode

	# O(n)
	def insertAtEnd(self, data):
		current = self.head
		newNode = Node(data)

		while current.get_next():
			# print("Current value: "+ str(current.getData()))
			current = current.get_next()


		# print(type(current)) #None-type becase it points to the one after ending node
		current.set_next(newNode)


	def printList(self):
		lst = []
		current = self.head
		while current:
			lst.append(str(current.getData()))
			current = current.get_next()
		print('->'.join(lst))


	def search(self, data):
		current = self.head
		count_found = 0
		while current:
			if current.getData == data:
				count_found += 1
			current = current.get_next()
		
		return count_found

	def delete(self, data):		#vl
		prev, current = None, self.head

		while current:
			#match at head
			if self.head.data == data:
				self.head = self.head.get_next()
				prev = current
			elif current.data == data:
				prev.set_next(current.get_next())
			else: 
				prev = current

			current = current.get_next()

	def shortDel(self, data): #stupic deletion
 		n = self.head

 		if n.data == data:
 			print("Del at head")
 			self.head = self.head.get_next()

 		while n.get_next():
 			print(n.data)
 			if n.get_next().data == data: #this doesnt work as it failed cases 2 consecutive targets 
 				 n.set_next(n.get_next().get_next())
 			n = n.get_next() 	

	def removeDuplicates(self): #using a dictionary to store all different values 
		'''
		prev, current <-- None, head  
		Do this continuously: 
			if current is the new element:
				push it to the dictionary 
			if current is already in the dictionary:
				prev sets its next being current's next

			prev = current
			current = current.next
		Head case doesnt count as the first element is always a newly-discovered
		'''

		dic = {}
		prev, current = None, self.head
		while current: 
			if dic.get(current.data) is None: 
				dic[current.data] = 1
				prev = current
			else: 
				prev.set_next(current.get_next())

			current = current.get_next() 

	def removeDuplicates2(self): #no extra buffer, taking O(n^2)
		'''
		Use three pointers, two to delete node and one to keep going 
		'''

		prev, i = None, self.head 

		while i: 
			curr = i
			prev = curr
			while curr.get_next():
				curr = curr.get_next()				
				if curr.data == i.data:
					prev.set_next(curr.get_next())
				else:
					prev = curr
			i = i.get_next()

	def partition(self, value): # all less on left, all more on right
		'''
		Create 2 extra linked list, one less and one more then merge 
		Advantage: cheap and stable 
		'''
		pnt = self.head
		less, right = Node(), Node()
		lessstart = less
		#create 2 linked list
		while pnt:
			if pnt.data < value:
				less.set_next(pnt)
				less = less.get_next() 
			else: 
				right.set_next(pnt)
				right = right.get_next()				

			pnt = pnt.get_next()

		#merging
		less.set_next(self.head)
		self.head = lessstart.get_next()
	
	def partition_2(self, value):	#2 variables
		'''
		every smaller node is put at head, every larger node is put at tail 
		not stable but less variables 
		'''
		return

	def reverse(self):				
		prev, curr = None, self.head
		while curr: 
			n = curr.get_next() 
			curr.set_next(prev)
			prev = curr
			curr = n 
		self.head = prev
		return self.head

def sumBackward(l1, l2, carry): #digits are stored backwards and addition perform to the right direction of linked list
	'''
	recursively called the next node of each linked list,
	append the result before calling the next one
	'''

	#base case 

	p1, p2 = l1.head, l2.head
	if not p1 and p2 and carry: 
		print("End nodes")
		return None

	result = 0
	if l1.head:
		result += p1.data
	if l2.head:
		result += p2.data 
	if carry: 
		result += carry

	result = result%10 
	n = Node(result, None)
	print(n.data)

	while p1 or p2:
		tmp = sumBackward(p1.get_next() if p1.get_next() else null, p2.get_next() if p2.get_next() else null, 0 if result < 10 else 1)
		n.set_next(tmp)

	return n

 

def sumForward(l1, l2, carry):
	return 

def isPalindrome(l1): #clone the reverse list and compare the two
	l2 = l1
	l1.reverse()
	print(l1.head.data)
	print(l2.head.data)
	while l1.head and l2.head:
		if l1.head.data != l2.head.data:
			return False
		else:
			l1.head = l1.head.get_next()
			l2 = l2.get_next()
	return True
def findIntersection(l1, l2): 
	return

def hasLoop(l1,l2):
	return 



head = Node(5)
list = LinkedList(head)
list.insertAtEnd(1)
list.insertAtEnd(2)			#215
# list.insertAtEnd(4)
# list.insertAtEnd(6)
# list.insertAtEnd(3)
# list.insertAtEnd(3)
# list.insertAtEnd(30)
# list.insertAtEnd(90)
# list.insertAtEnd(90)
# list.insertAtEnd(3)
# list.insertAtEnd(3)

# list.printList()
# list.delete(3)
# list.printList()
# list.shortDel(90)
# list.removeDuplicates2()
# list.partition_2(3)
# list.reverse()
# list.printList()
# print(isPalindrome(list))


head1 = Node(3)
list1 = LinkedList(head1)
list1.insertAtEnd(2)
list1.insertAtEnd(1)		


# sumLists = sumBackward(list, list1, 0)
# sumLists.data

def test_recursion(a):
	a = a/2 - 1
	print("before if a = {}".format(a))
	if a > 0:
		b = test_recursion(a)
		print("b: {}".format(b))
		a = b + 1
		print("a: {}".format(a))
	else:
		print("Outbound 0")
	print("outside of if a = {}".format(a))
	return a

print(test_recursion(8))


