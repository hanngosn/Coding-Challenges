'''top down approach '''
def fibbonaci(n):
	table = [None]*(n+1)
	return fibbonaci_re(n, table)

def fibbonaci_re(n, table):
	if n == 0 or n == 1: 
		return n

	if not table[n]:
		table[n] = fibbonaci_re(n-1, table) + fibbonaci_re(n-2, table) 

	return table[n]

# print(fibbonaci(6))

'''bottom up approach'''
def fibbonaci_bu(n):
	if n == 0 or n == 1:
		return n
	
	table = [None]*(n+1)
	table[0], table[1] = 0, 1
	for i in range(2, n+1):
		table[i] = table[i-1] + table[i-2]
	return table[i]

# print(fibbonaci_bu(6))

def fibbonaci_r(n):
	a,b = 0,1 
	
	for i in range(2,n+1):
		a,b = b, a+b 
	return b

# print(fibbonaci_r(6))

''' Check prime '''

def isPrime(n):
	
	for i in range(2, int(n**.5)):
		if not n % i: 
			return False

	return True  

# print(isPrime(12))
# print(isPrime(59))

''' Sieve of Eratosthenes '''
def sieveOfEratosthenes(max): 
	flagSt = [True]*(max+1) 
	prime = 2
	while (prime < len(flagSt)):
		flagSt, prime = crossoff(flagSt, prime)
		prime = nextPrime(flagSt, prime)
	return flagSt

def crossoff(st, p):
	for i in range(p*p, len(st), p):
		st[i] = False
	return st,p

def nextPrime(st, p):
	next = p + 1 
	while (next < len(st) and not st[next]):
		next += 1

	return next

# print(sieveOfEratosthenes(6))

'''Triple stairs'''
def countWaysStepping(n):
	table = [0]*(n+1) 
	if n <= 0: 
		return 0
	if n == 1: 
		return 1
	if n == 2: 
		return 2
	table[0], table[1], table[2] = 0,1,2

	for i in range(3, n+1):
		table[i]  = table[i-1] + table[i-2] + table[i-3]

	return table[n]

# print(countWaysStepping(3))

'''brute force is dumb! binary search tree variation would be a better choice!'''
def magicIndex(a, l, r):
	if l > r:
		return False

	mid = (l+r)//2
	if a[mid] == mid:
		return True
	if a[mid] >= mid:
		return magicIndex(a,l,mid)
	else: 
		return magicIndex(a, mid+1, r)

# print("MagicIndex")
# print(magicIndex([-40,-20,-1,1,2,3,5,7,9,12,13], 0, 10))

def bst_find(a, l, r, n):
	if l > r:
		return False 

	mid = (l+r)//2
	if a[mid] == n:
		return True
	elif a[mid] < n:
		return bst_find(a, mid+1, r, n)
	else: 
		return bst_find(a, l, mid-1, n)

# print(bst_find([-40,-20,-1,1,2,3,5,7,9,12,13], 0, 10, 12))

'''Get bit to check number is odd/even'''
def isEven(n): #positive number n
	return (1) & n 
	#1 means there is 1 at the end, 0 means not
print(isEven(193))
	




