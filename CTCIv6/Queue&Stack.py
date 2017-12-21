################################### Stack  ###################################  
class Stack:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def peek(self):				#basically get the popped element but not actually popping it out
		return self.items[len(self.items)-1]
	def size(self):
		return len(self.items)

# s = Stack()
# s.push(4)
# s.push('dog')
# s.push('cat')
# print(s.peek())
# print(s.size())

def parChecker(str):	#check parenthesis balance or not with implementation of stack 
	s = Stack()
	for each in str:
		if each == '(':
			s.push('(')
		if each == ')':
			s.pop()
	if s.size() == 0:
		return True
	else:
		return False

print(parChecker("(()"))

################################### Queue ###################################  
class Queue: 
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def enqueue(self, item):	#insert at top position
		self.items.insert(0,item)
	def dequeue(self):
		return self.items.pop()
	def size(self):
		return len(self.items)
	def print(self):
		print(self.items)	
		

# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.dequeue()
# print(q.print()) 

def hotPotato(nameList, num):
	q = Queue()
	for each in nameList:
		q.enqueue(each)
	for i in range(num):
		last = q.dequeue()
		q.enqueue(last)

	return q.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],10))

################################### Tale of two Stacks ###################################  
class MyQueue(): 

	def __init__(self):
		self.stack1 = []
		self.stack2 = []
	def push(self, value):
		self.stack1.append(value)
	def pop(self):
		if self.stack1 or self.stack2:
			while self.stack1:
				self.stack2.append(self.stack1.pop())
			val = self.stack2.pop()
			while self.stack2:			#when a push goes after a pop
				self.stack1.append(self.stack2.pop())
			return val
		else:
			return None

	def peek(self):		#basically the same, except the pop value is not actually popped out of the queue
		if self.stack1 or self.stack2:
			while self.stack1:
				self.stack2.append(self.stack1.pop())
			val = self.stack2.pop()
			self.stack1.append(val)
			while self.stack2:			#when a push goes after a pop
				self.stack1.append(self.stack2.pop())
			return val
		else:
			return None


	def print(self):
		print(self.stack1)
		

# mq = MyQueue()
# mq.push(1)
# mq.push(2)
# mq.push(3)
# mq.push(4)
# mq.push(5)
# print(mq.pop())
# mq.push(6)
# mq.push(7)
# print(mq.pop())
# print(mq.pop())
# print(mq.peek())
# mq.print()
# mq.push(8)
# mq.print()

################################### Sorting with stack ###################################  
#Given a stack, sort it with a temporary stack
def sort_stack(lst):
	tmp = Stack()	#a temporary stack 
	
	while lst.size():
		if tmp.size() == 0:
			tmp.push(lst.pop())
		else:
			if tmp.peek() >= lst.peek():
				tmp.push(lst.pop())
			else:  #need modication to move multiple times
				x = lst.pop()
				move = 0
				while x > tmp.peek():
					move +=1
					lst.push(tmp.pop())
					if not tmp.size():
						break 
				tmp.push(x)
				for i in range(move):
					tmp.push(lst.pop())

	for i in range(tmp.size()):
		print(tmp.pop())

	return tmp

st = Stack()
st.push(5)
st.push(8)
st.push(10)
st.push(2)
st.push(5)
st.push(2)
st.push(1)
st.push(100)
sort_stack(st)
	