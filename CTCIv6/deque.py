#Deque from Python Collections, can push/pop on both end sides of the list 
from collections import deque

d = deque("ghi")
print(' - '.join(d))

d.append('j')
d.appendleft('f')
print(list(d))

d.pop()  #pop rightmost item 
d.popleft() 

d[0]	 #peek at leftmost item 
d[-1]	 #peek at rightmost item 

print(list(reversed(d)))
d.rotate(1)		#right rotation, input param is the number of items to shift
d.rotate(-1)	#left rotation


