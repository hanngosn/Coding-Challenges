'''
Created on Oct 25, 2017

@author: Hannie
'''
import math
from pip._vendor.distlib.compat import raw_input


################################### Find PI to the Nth Digit ###################################  
def pi_ndigit(n):           #REMIND: reverse a string: string[::-1]
    
    result = str(math.pi)[:n+2]
    return result

################################### Fibonacci ###################################  
def fibonacci(n):
    
    # return 0 if n == 0 #Doesnt work, needs else! 

    if n == 0: 
        return 0
    if n == 1: 
        return 1


    #otherwise - DP basic
    a = []
    a.append(0) #syntax
    a.append(1)
     
    for i in range(2, n):
        a.append(a[-1] + a[-2])         #NEW SYNTAXXXXXXXX
     
    return a

def fibonacci_2(n):
    # This is smart lol
    a , n = 0,1
    while n < 1000:
        print(n)
        a,n = n,a+n


################################### Hashtable ###################################  

def try_Hash():
    #list of tuples can be used as dict/not really efficient as it costs more for linear search 
    map = [('Han', '4'), ('Anh', 5), ('Hung', 4), ('San', 10)]
    # print(map[3])
    # print(map[0][1])
     
    #function to set a
#     hash_key = hash('06770')%len(map)
    
    dicta = {}
    dicta['Hannie'] = 3
    dicta['Ann'] = 4
    dicta['San'] = 2
    dicta['Hung'] = 1

#     print(dicta)
#     print(dicta['Hannie']) #>> Senior 
    dicta.clear();
    
    print(dicta)
    return
    dicta.pop('San') 
    del dicta['Hannie']
    
    print(dicta.get('Hannie')) #None by default
    print(dicta.get('Ann'))
    
    dicta.setdefault('Ba ngoai', 5)
    dicta.setdefault('Thuy', 5)  #if key exists, return its value. If not, set it to the new custom
    print("Dict values: " + str(dicta.keys()))      
    print(dicta)
    
################################### Enumerate ###################################  

def try_enumerate():
    a = ['han','ba Hung','anh']
    for inx, val in enumerate(a):
        print(str(inx) + " " + str(val))

################################### Capital 1 ###################################  
#Given 2 strings, write a method to decide if one is the permutation of the other
#decide what type of characers in a string,create arrays of [256] to minimize memory footprint and update count for 2 arrays
# http://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/
def if_permutation(a, b):       #Create 2 hashtables
    
    #case if len(a) != len(b)
    
    dicta, dictb = {},{}
    for each in a:
        if dicta.get(each):
            dicta[each] += 1
        else: 
            dicta[each] = 1
    
    for each in b:
        if dictb.get(each):
            dictb[each] += 1
        else:
            dictb[each] = 1
    
    for keya in list(dicta.keys()):
        if dicta[keya] == dictb.get(keya):
            del dicta[keya]
            del dictb[keya]
        
    if not (dicta and dictb):           #both have to be empty 
            return True
    return False
        
################################### Prime Factorization ###################################  

def primeFactors(n):
    factors = lambda n: [x for x in range(1,n+1) if not n%x] #if n mod x = 0
    # print("Factors of 10: " + str(factors(10))) #n = 10 gives 1,2,5,10

    #check if the number is prime itself (if its number of factors is just 2)
    is_prime = lambda n: len(factors(n)) == 2

    #filter() is pretty useful!
    is_prime_factor = lambda n: list(filter(is_prime, factors(n)))  #note: is_prime WITH NO PARENTHESIS

    print("prime factors of 25: " + str(is_prime_factor(25)))

# primeFactors(25)
################################### Next Prime Number ###################################  
#Have the program finds prime number until the user chooses to stop asking for the next one

def find_nextPrime():

    
    def Pgenerator():
        print("@generator")
    
        factors = lambda n: [x for x in range(1, n+1) if not n%x]
        is_prime = lambda n: len(factors(n)) == 2
        
        yield 2
        number = 3
        while True:
            if is_prime(number):
                yield number
            number += 2

    print("Keep printing next prime numbers until indicated to stop")

    all_gen = Pgenerator()

    while True: 
        input = raw_input()
    
        if input == 'x':     
            break
        elif input == 'c':
            print(all_gen.next())

    
# find_nextPrime()

################# Mortgage calculator ###################################  
#Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate.
#Figure out how long to pay back 

def mortgageCal():

    months = int(raw_input("Enter mortgage term in months (terms): "))
    loan = float(raw_input("Enter loan amount: "))
    rate = float(raw_input("Enter interest rate: "))

    payment_1Month = (loan/12)*(1+(rate/12/100))
    print("Payment per month with loan {} and rate {} is {}".format(loan, rate, payment_1Month))        #format print Py3

# mortgageCal()

################################### String manipulation ###################################  

def Mystring():   
    
    def print_Reverse():
        print(raw_input()[::-1])

    def count_vowels():
        string = "Hannieeee"
        vowels = 'aeoui'
        count_vowels = lambda n: [x for x in string if x in vowels] 
        print("count vowels of Hannie")
        print(len(count_vowels(string)))

# Mystring()
    

################################### Change Return Program ###################################  


################################### Binary to Decimal ###################################  


################################### Factorial Finder ###################################  
def fact_find_re(n):    #recursively 
    if n == 1: 
        return 1

    return n*fact_find_re(n-1)

# print("Factorial finder: " + str(fact_find_re(3)))

################################### Collatz Conjecture ###################################  
#input n, count steps as follows: odd *3+1, even /2 

def collatz(n):
#recursively
    
    # #base case
    # if n == 1:
    #     return 1
    # if n%2 == 0: #even 
    #     n = n/2 
    #     count += collatz(n)
    #     return count
    # if not n%2 == 0:    #odd
    #     n = n*3 + 1
    #     count += collatz(n)
    #     return count

#that doesnt work, count is not stored locally

#iteratively 
    count = 0
    if n == 1:
        return 1
    while n>1: 
        if n%2==0:
            n = n/2 
            count += 1
        else:
            n = n*3 + 1
            count += 1

    return count

def collatz_re(n, count): 

    if n == 1:
        return count
    if n%2 == 0:
        n = n/2
        count += 1 
        return collatz_re(n, count)
    if not n%2 == 0:
        n = n*3 + 1
        count += 1 
        return collatz_re(n, count)

################################### Mergesort ###################################  
def merge(a, left, right):
    i, j, k = 0,0, 0
    result_array = []
    while (i < len(left) and j < len(right)):
        if left[i] <= right[j]:
            result_array.append(left[i])
            i += 1 
        elif left[i] > right[j]:
            result_array.append(right[j])
            j += 1
        k += 1

    #the leftover in left and right array 
    result_array.append(left[i:])
    result_array.append(right[j:])

    return result_array

def mergeSort(a):       #divide and conquer method
    mid = len(a)//2 #floor division 

    left = a[:mid]
    right = a[mid:]

    merge(left)
    merge(right)
    
    return mergeSort(a, left, right)

################################### Odd/Even Indexes ###################################  
def oddevenIndexes():
    
    word = input("Give a word: ")
    allEven = word[::2] 
    allOdd = word[1::2]
    print(allEven + " " + allOdd)

# oddevenIndexes()

################################### Anagrams ###################################  
#https://www.hackerrank.com/challenges/anagram/problem
#just count how many rearrangements needed
def checkRearrangements(): 

    s = input("Input: ")
    if len(s)%2:
        return -1
    mid = len(s)//2
    s1 = s[:mid]
    s2 = s[mid:]

    def containSubstring(s1,s2):     #check how many common letters of s1 and s2

        same = 0                #number of common elements
        offset = ord('a')
        st1 = [0]*26
        st2 = [0]*26 
        for each in s1: 
            st1[ord(each)-offset] += 1          #OOOOH already initialized to be 0
        for each in s2: 
            st2[ord(each)-offset] += 1
        for i in range(26):
            if st1[i] and st2[i]:
                same += min(st1[i], st2[i])

        return same

    return len(s1) - containSubstring(s1,s2)
# print(checkRearrangements())


#return the first non-repeating character in the string
def firstUnique(s):  
    '''
    Create a table each cell has 2 subcells, 
    - first store index, 
    - second store the number of reoccurences
    Index of cell is the difference between the letter in s and a
    '''
    st = [0, 0] * 26 
    offset  = 'a'
    for i, e in enumerate(s):
        if st[ord(e) - offset][1] == 0: #already discovered
            count = st[ord(e) - offset][1]
            st[ord(e) - offset] = [i, count+1]
        else: #never discovered
            st[ord(e) - offset] = [i, 1]

    minIndex = len(s)
    for i in range(26):
        if st[i][1] == 1: 
            if i < minIndex: 
                minIndex = i 


    if st[minIndex][1] == 1:
        return s[minIndex]
    else: 
        return False

FirstUnique("Hannie")







################################### Main ###################################  
 
# precision = int(raw_input("How many spaces? "))
# print('%.*f'.format(precision, math.pi))
# print("Sammy has {} balloons.".format(5))
# try_Hash()
# print(if_permutation("hana", "anh"))
# print(fibonacci(5))         # fibonacci_2(5)
# print(collatz(3))
# print(collatz_re(3, 0))


def englishRead(d): #read 3 digit number 
    a = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    b = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eightteen', 'nineteen']
    c = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    l = len(str(d))
    re = ''

    # if l == 1: 
    #     return a[d-0]
    for i,v in enumerate(str(d)):
        print(v)
        #first digit - hundred 
        # if i == 0: 
        #     if v == 0:
        #         pass
        #     else: 
        #         re = a[v] + " hundred"

        #last two digits
        # if i == 1:      #tenth 
        #     if v == 1:  #case b
        #         re = re + b[int(str(d)[i+1])]    #peek at the rightmost unit
        #     else: 
        #         re = re + c[v]
    print(re)

# englishRead(123)

            








