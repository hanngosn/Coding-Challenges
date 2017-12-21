'''
Created on Oct 15, 2017

@author: Admin
'''
def welcomeBack():
    print("welcome back")

################################### MERGE SORT ###################################  
def merge(l, r, a):
    
    #left index, right index | k is the pointer to the resulting array 
    l_inx, r_inx, k = 0, 0, 0
    
    #compare each of the left/right side to append to result list
    while (l_inx < len(l) and r_inx < len(r)):
        if (l[l_inx] < r[r_inx]):
            a[k] = l[l_inx]
            l_inx = l_inx + 1
        else:
            a[k] = r[r_inx]            
            r_inx = r_inx + 1
        k = k + 1
    
    #in case left/right side still have elements left
    while l_inx < len(l):
        a[k] = l[l_inx]
        k = k+1
        l_inx += 1
    while r_inx < len(l):
        a[k] = r[r_inx]
        k = k+1
        r_inx += 1

    return a

def mergeSort(a):
    
    #base case:
    if len(a) == 1:
        return a
    
    mid = len(a)//2
    l = a[:mid]
    r = a[mid:]
     
    mergeSort(l) 
    mergeSort(r) 
    return merge(l,r,a)

################################### INSERTION SORT ###################################  
    
def noIdeaSort(a):
    
    for inx1 in range(0,len(a)):
        for inx2 in range(0, inx1+1): 
            if (a[inx1] < a[inx2]):
                temp = a[inx1]
                a[inx1] = a[inx2]
                a[inx2] = temp 
    return a

################################### QUICK SORT ###################################  

def median_of_medians(A, k): #better way to choose pivot    
    
    #divide A into sublists of 5
    sublists = [A[j:j+5] for j in range(0, len(A), 5)]      #range(start,stop,step) 
    medians = [sorted(sublist)[(int) (len(sublist)/2)] for sublist in sublists]
    
    if len(medians) <= 5: 
        pivot = medians[(int) (len(medians)/2)]
    else: 
        #for large size of medians,pivot is the median of medians
        pivot = median_of_medians(medians, len(medians)/2)
    
    print(pivot)
    
    #Partitioning step
    left = [i for i in A if i < pivot]
    right = [i for i in A if i >= pivot]
    
    #cases of where the pivot is 
    l_left = len(left)
    if l_left < k:
        return median_of_medians(left, l_left)
    elif l_left > k:
        return median_of_medians(right, k - l_left - 1)
    else: #l_left = k
        return pivot
    
################################### Quicksort ###################################  

def quick_sort(A):
    
    #for the return statements, have to initialize less and more first
    less, more = [], []
    
    if len(A) <= 1:
        return A
    else:   
        pivot = A[0]
        
        less = [i for i in A if i < pivot]
        more = [i for i in A if i > pivot]                         
        equal = [i for i in A if i == pivot]
                #list subtraction: list(set(A) - set(less))
        
        #less and more lists are not sorted yeeeet
        less = quick_sort(less)
        more = quick_sort(more)
        
        return less + equal + more
    
################################### Counting sort ###################################  

def countingSort(a, digit, radix):
    
    #create list b which is the resulting sorted array 
    b = [0]*len(a)
    c = [0]*radix
    
    #count the occurences of digits
#     for i in range(0, len(a)):
#             digit_Ai = a[i]/
    
################################### Selection Sort ###################################  
def selection_sort_it(alst): #iteratively
    
    for i in range(len(alst)-1, -1, -1):
        max_pos = 0 
        for j in range(i+1):
            if alst[j] > alst[max_pos]:
                max_pos = j

        alst[max_pos], alst[i] = alst[i], alst[max_pos] 
        print(alst)

# selection_sort_it([26,54,93,17,77,31,44,55,20])
       
        
        
################################### Main ###################################  
welcomeBack()
print("Merge sort: ", mergeSort([1,4,5,2,3,7,19,10]), "\n")
print("Insertion sort: ", noIdeaSort([3,2,7,4,5,3,7,19,10]), "\n")
# median_of_medians([3,2,7,4,5,3,7,19,10], 6)
print("Quicksort: ", quick_sort([20,2,7,4,5,3,7,19,10]))
