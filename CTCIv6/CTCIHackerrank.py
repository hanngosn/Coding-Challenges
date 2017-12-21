import itertools

################################### Dynamic Programming ###################################  
# Input n: amount of $$, S [types of coins] {0,1,..., m-1}
# Output number of ways + solutions  

def count(S, m, n):	#RECURSIVE - overlapping subproblems 
	
	if n == 0:
		return 1	#one way to change counted
	if n < 0:
		return 0
	if n >= 1 and m <= 0:	#no coins and n >= 1 
		return 0
	
	#the point is either take the coin or not 
	return count(S, m, n-S[m-1]) + count(S, m-1, n)

def dp_count(S, m, n):

	#construct table of m rows (coins) x n+1 ($$ to change)
	#set all 0
	table = [[0 for x in range(m)] for x in range(n+1)]
	table[0] = 1

	#rest cases
	# for i in range(1, n+1):
	# 	for j in range(m):
	# 		x = table[i - S[j]][j] if i-S[j] >= 0 else 0	#including S[j]
	# 		y = table[i][j-1] if j >= 1 else 0 				#excluding S[j]
	# 		table[i][j] = x + y								

	return table[n][m-1]

# print(count([1,2,3],3,3))

################################### Intuit Coding Challenge ###################################  
employees_input = [
  "1,Richard,Engineering",
  "2,Erlich,HR",
  "3,Monica,Business",
  "4,Dinesh,Engineering",
  "6,Carla,Engineering",
  "9,Laurie,Directors"
]

friendships_input = [
  "1,2",
  "1,3"	,
  "1,6",
  "2,4"
]

def get_employee_stats(employees_input, friendships_input):	

	dicta = {} 
	 
	for each in employees_input:
		dept = each.split(",")[2] 

		if not dicta.get(dept): #if dept is not listed
			dicta[dept] = [each.split(",")[0]]
		else: 
			dicta[dept].append(each.split(",")[0])

	print(dicta)

	#create parallel arrays of friendships
	a, b = [], []
	for each in friendships_input:
		a.append(each.split(",")[0])
		b.append(each.split(",")[1])


	#augment dic keys with final (int)value being the number of friends that have friends outside of the dept 
	for each in dicta.keys(): 	#each being department
		nested = {}
		count = 0
		for i in dicta[each]:
			for inx, val in enumerate(a):
				if i == val and b[inx] not in dicta[each]:
					count += 1
					break
				if i == b[inx] and a[inx] not in dicta[each]:	
					count += 1
					break

		#custom nested dict
		no_emp = len(dicta[each])
		nested["employees"] = no_emp
		nested["employees_with_outside_friends"] = count
		dicta[each] = nested 

	print(dicta)
	return 


# get_employee_stats(employees_input, friendships_input)

################################### Stack/Queue ###################################  



################################### Permutation ###################################  
#Extract one by one, place them at first and add recur for the remaining list

def permutation(lst):	#lst is concat string

	if len(lst) == 0:
		return []
	if len(lst) == 1:
		return [lst]

	result = []
	for i in range(0,len(lst)):
		first = lst[i]	#element at index i to extract 
		remn = lst[:i] + lst[i+1:]

		for p in permutation(remn):
			result.append(first + p)

	return result

print(permutation('abc'))

################################### Left Rotation ###################################  
def rotate(a, n): 	#a: array, n: number of rotations 
	return a[n:] + a[:n]
# print(rotate([1,2,3,4,5],3))

################################### Making anagram ###################################  
#how many letters need deleted to make anagrams 
def make_anagram(a, b): 	#a,b are strings
	
	table = [0]*26 			#26 alphabets
	offset = ord('a')		#return an integer representing the Unicode letter e.g. 'a' -> 97
	for each in a:
		table[ord(each) - offset] += 1
	for each in b:
		table[ord(each) - offset] -= 1
	count = 0 
	for each in table:
		count += abs(each)
	return count 

print(make_anagram("han","anha"))

################################### Check if contains same substring ###################################  
def containSameSubstring():
	cases = int(input("How many cases: "))
	offset = ord('a')

	for each in range(cases):
		a = input()
		b = input() 
		store_a = [False]*26
		store_b = [False]*26 
		for each in a:
			store_a[ord(each)-offset] = True 
		for each in b:
			store_b[ord(each)-offset] = True	
		for i in range(26):
			if store_a and store_b:	#if both are true meaning they have something in similar
				print("YES")
				return  
	print("NO")

# containSameSubstring()

################################### Sherlock and anagrams ###################################  
print("Sherlock & Anagrams")
def findAnagramPairs(a):	#a is a string 
	
	n = len(a)
	count = 0 

	for i in range(1, n):			#right part
		dic = {}
		for j in range(0,n-i+1): 	#left part
			key = [x for x in a[j:j+i]]	#REMEMBER THIS! ways of slicing all subsets! 
			# print(key)
			key.sort()
			key = ''.join(key)
			if dic.get(key):		#no one-line If-else huh?
				dic[key] += 1 
			else:
				dic[key] = 1
			count += dic[key] - 1
			# print(key + " " + str(dic[key]) + " " + str(count))
		
findAnagramPairs('abcbb')

################################### Alternating Characters ###################################  
def alterating_characters():
	s = input("Enter string including just As & Bs: ")
	deletions = 0

	for i in range(0, len(s)-1):
		if s[i] == s[i+1]:
			deletions += 1
	return deletions
	
# alterating_characters()
		
################################### Bigger is Greater ###################################  
print('Try comparator for custom sort')
import itertools

def next_permutation(s):
	s = list(s)
	compute_permutation(s, lambda x, y: x >= y)

def compute_permutation(s, comparator):
	n = len(s)
	i, j = n-1, n-1

	while i > 0 and comparator(s[i-1], s[i]):	
		i -= 1
	if i == 0: 
		return False
	while comparator(s[i-1], s[j]):
		j -= 1
	s[i-1], s[j] = s[j], s[i-1]
	
	print(''.join(s))
	return True 
next_permutation('abcdefd')


################################### Permutations Algorithm ###################################  
def permute(ls): 

	if len(ls) == 0: 
		return []
	if len(ls) == 1:
		return [ls]

	result = []
	for each in range(len(ls)):
		first = ls[each]
		left = ls[:each] + ls[each+1:]

		for p in permute(left):
			result.append(first+p)
	return result 
# print(permute('abc'))

################################### Regex Syntax ###################################  
import re
match = re.search(r'iii', 'piiig') #return yes/no and word found span

################################### Funny String ###################################  
def isFunny(s):
	n = len(s)-1
	for i in range(n):

		if not abs(ord(s[i+1]) - ord(s[i])) == abs(ord(s[n-i-1]) - ord(s[n-i])):
			return False
		return True

print(isFunny('bcxz'))

################################### Game Of Thrones ###################################  


################################### Bit Manipulation/Lonely Integer ###################################  
#Find unique elements of the list consisting all pairs
from functools import reduce

def find_lonely_integer():
	numbers = input("List of numbers with a lonely one: ")
	numbers = [int(x) for x in numbers.split()]

	lonely_integer = reduce(lambda x, y: x^y, numbers)
	return lonely_integer
# print(find_lonely_integer())

# def find_multiple_lonely_integers():
# 	numbers = input("List of numbers with a lonely one: ")
# 	numbers = [int(x) for x in numbers.split()]

def lonelyinteger(a):
    res = 0
    for each in a:
        res ^= each
        print(res)
    return res

# print(lonelyinteger([5,1,2,1,4,4]))

################################### David's staircase ###################################  
def count_steps(n):
	if n == 0:
		return 1
	if n == 1:
		return 1
	if n == 2:
		return 2
	if n == 3:
		return 4
	return count_steps(n-1) + count_steps(n-2) + count_steps(n-3)   #O(3^n)

# print(count_steps(7))
def dp_count_steps(n):
	table = [0 for each in range(n+1)]
	table[0], table[1], table[2], table[3] = 1,1,2,4

	for i in range(4, n+1):
		table[i] = table[i-1] + table[i-2] + table[i-3]

	return table[i]

# print(dp_count_steps(7))

################################### Game Of Thrones ###################################  
def isAnagram(s):

	store = {} 
	for each in s:
		if store.get(each):
			store[each] += 1
		else:
			store[each] = 1
	result = False
	for each in store.keys():
		if not store[each] % 2:	#even (remainder = 0)
			result = True
			return result
		else:
			result = False

	return result

# print("Game of Thrones")
# print(isAnagram("cdcdcdcdeeeef"))

################################### Pangrams ###################################  
# def isPangram():
# 	st = input('Sentence: ').replace(" ", "")
# 	print(st)
# 	table = [0]*26
# 	for each in st.lower():
# 		table[abs(ord(each)-ord('a'))] += 1

#  	for i in range(0,26):
#  		if table[i] == 0:
#  			return False
# 	return True

# print(isPangram())	

################################### Longest common subarray ###################################  
def subset(s,a):
	n = len(s)
	result = ''
	for i in range(1,n):	#len of a subset
		
		for j in range(0, n-i+1):
			subset = s[j:j+i]
			if subset in a and i > len(result):
				result = subset

	print("result - " + result)

# subset("abcdefd", "abcdeddd")

################################### Gemstones ###################################  
def gem():
	s1 = ["abcdde","baccd","eeabg"]
	result = []
	num = len(s1)


	table = [[0]*3 for i in range(26)]			#weird behavior of Python n-dim array

	offset = ord('a')
	for i,each in enumerate(s1):
		print(each)
		for letter in each:
				row = ord(letter)-offset
				table[row][i] = 1			

	for i in range(26):
			if sum(table[i]) == num:
				result.append(chr(i+offset))
	
	print(result)

	return result

# print("---")
# gem()

################################### Practice Recursion ###################################  
def cal(s): #s being a string
    
    st = s.strip().split('+')
    result = 0
    sum = 0
    for part in st: 
        if '-' in part:
            sub_part = part.split('-')
            sum = sum+int(sub_part[0])
            for i in range(1, len(sub_part)):
                sum = sum - int(sub_part[i])
        else:
            result = result + int(part)  
    result += sum
    print(result)
    return result
    
cal("1+1+4+-1-5")
################################### Practice Recursion ###################################  
def appearSubs(word, part):
	count = 0

	if len(word) < len(part): 
		return count
	
	
	if word[0:len(part)] == part:
		count += 1
		return count + appearSubs(word[len(part):], part)
	else:
		return count + appearSubs(word[1:], part)

# print(appearSubs("catcocatwcat", "cat"))

def moveXToEnd(s):
	if len(s) == 0:
		return ''
	if s[0] == 'x':
		return moveXToEnd(s[1:]) + 'x'
	else: 
		return s[0] + moveXToEnd(s[1:])

# print(moveXToEnd("hixtix"))

def separateString(s):
	if len(s) == 1:
		return s
	return s[0] + '*' + separateString(s[1:])

# print(separateString("hello"))

def nestParen(s):
	
	if len(s) == 0 or len(s) == 1: 
		return False
	
	if s[0] == '(' and s[len(s)-1] != ')': 
		return False or nestParen(s[:len(s)-1])

	if s[0] != '(' and s[len(s)-1] == ')':	
		return False or nestParen(s[1:len(s)])
	else: 
		if len(s) == 2 or len(s) == 3:
			return True 
		else: 
			return True and nestParen(s[1:len(s)-1])

# print("Nested Paren")
# print(nestParen("(((d())))"))
