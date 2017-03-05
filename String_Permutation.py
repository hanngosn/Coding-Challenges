'''
Created on Mar 5, 2017

@author: Admin
'''
# Write a program to print all permutations of a given list

def permutation(list):
    set = []
    
    if len(list) == 1:
        set.append(list[0])
    else:
        last_index = len(list) - 1
        last = list[last_index]
        rest = list[0:last_index]
        set = merge(permutation(rest), last)
        
    return set

def merge(sublist, no):
    result = []
    for each in sublist:        #if sublist have 1 element, it is not counted as a list (not list of list)
        try:
            for index in range(0, len(each)+1):
                tmp = each[0:index]+[no]+each[index:len(each)]
                result.append(tmp)
        except:
            result.append([each,no])
            result.append([no,each])
            
    return result
# 
 
print(permutation([1,2,3,4,5]))