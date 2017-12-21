'''
Created on Oct 22, 2017

@author: Hannie 
'''


################################### Binary Search Tree ###################################  
# BST help find square root
#Iteratively

def it_bst(a, target):

    first = 0
    last = len(a) - 1
    
    while first<=last: 
        mid = (last + first)//2 #floor division #DARRRRN last + first NOT last - first
        mid_val = a[mid]
        
        if target == mid_val: #remember == to compare values of the variables
            print("Iteratively found target: " + str(target))
            return 
        else: 
            if target < mid_val:
                last = mid - 1
            else: 
                first = mid + 1
    
    print("Not found target")
    return None                     #like void 



#Recursively 
def re_bst(a, target):
    
    #base case
    if len(a) == 0:
        print("Not found target")
        return None
    
    #recursion 
    mid = len(a)//2         #int type
    mid_val = a[mid]
    
    if target == mid_val:
        print("Recursively found target: " + str(mid))
        return 
    elif target < mid_val:
        return re_bst(a[0:mid], target)     #RETURN to CALL BACK the result at the end!!!!
    else:                                   #MA nho return 
        return re_bst(a[mid+1:], target)
        
#Application of Binary Search Tree to find square root
def find_sqrt(n):
    
    first, last = 0, n
    precision = 10e-8
    
    while last-first>precision :
        mid = (last+first)/2
        if mid **2 == n:
            return mid
        elif mid **2 < n:
            first = mid
        elif mid **2 > n:
            last = mid 
            
    return mid

# it_bst([2,3,5,6,8,10], 3)
# re_bst([2,3,5,6,8,10], 8)
# print("Square root: " + str(find_sqrt(4)))
# print(find_sqrt(9))
# print(find_sqrt(8))

################################### BST Implementation ###################################  
# https://www.laurentluce.com/posts/binary-search-tree-library-in-python/comment-page-1/

class Node: 
    def __init__(self, data):
        self.left = None
        self.right = None 
        self.data = data

    def children_count(self):   #count number of children of specific node
        cnt = 0 
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt 

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else: 
                self.left.insert(data)
        elif data > self.data: 
            if self.right is None: 
                self.right = Node(data)
            else: 
                self.right.insert(data)
        else: 
            self.data = data

    def lookup(self, data):      
        if data < self.data:
            if self.left is None:
                return None, None 
            else:
                return self.left.lookup(data)
        elif data > self.data:
            if self.right is None:
                return None, None 
            else:
                return self.right.lookup(data)
        else: 
            return self 

    # def delete(self, data):             #delete node containing data 


    def print_tree(self):       #L_root_R order
        if self.left: 
            self.left.print_tree()
  
        print(self.data) 
  
        if self.right:
            self.right.print_tree()

    def compare_trees(self, node):  #recursive 
        if node is None:
            return False
        if node.data != self.data:
            return False
        res = True
        if self.left is None:
            if node.left:
                return False
        else:
            res = self.left.compare_trees(node.left)
        if res is False:
            return False
        if self.right is None:
            if node.right:
                return False
        else: 
            res = self.right.compare_trees(node.right)

        return res

    def get_tree_data(self):    #generator to get tree data & stacks to traverse in a non recursive way 
        
        stack = []
        node = self
        while node or stack:    #either one of those two has something with it
            if node: 
                stack.append(node)
                node = node.left 
            else: 
                node = stack.pop()
                yield node.data
                node = node.right 

def bfs(root): #print out layer by layer
    
    lists = [] 
    current = [] 
    current.append(root)
    lists.append(current)
    while len(current) != 0:    #base case when the pointer reaches leaf nodes
        lists.append(current)         
        parent = current #copy before initialize 
        current = [] 
        for each in parent:
            if each.left: 
                current.add(each.left)
            if each.right:
                current.add(each.right)
    return lists 

def dfs(root): 

    



root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)
root.print_tree()

