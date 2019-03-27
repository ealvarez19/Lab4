#Emmanuel Alvarez
# 80567137
#Instructor: Olac Fuentes
#last Day modified: 03-26-2019
#The objective of this code is to make some operations using a B-tree like getting the height of the tree,
#finding the smallest and largest number, extracting the items of the tree into a sorted list, printing the 
# items at a given depth, return the number of nodes and leaves that are full.

class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
        
        
def height(T):
    if T.isLeaf:
        return 0
    return 1 + height(T.child[0])# calls the same method until reach a leave and adds 1 each time it is called
        
        
def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)
        
        
def CreateSortedList(T):    
    if T.isLeaf:#base case
        sortedList = []
        for t in T.item:
            sortedList.append(t)
        #print(sortedList)
        return sortedList # returns the items in the leaf
    else:
        temp = []
        for i in range(len(T.item)):            
            temp = temp + CreateSortedList(T.child[i])
            temp.append(T.item[i])#appends the item at index i
            #print(temp)
        return temp + CreateSortedList(T.child[len(T.item)])
    
def MinAtDepth(T,d):
    #print(T.item)
    if d == 0:
        return T.item[0]#returns the smallest number when it reach the depth desired
    elif len(T.child) == 0:
        return -1 #returns -1 when it is not a valid depth
    else: 
        return MinAtDepth(T.child[0],d-1)#calls the method with the child that contains smaller numbers than the actual node
    
def MaxAtDepth(T,d):
    if d == 0:
        return T.item[len(T.item)-1] #returns the last number of the node that is the largest number
    elif len(T.child) == 0:
        return -1
    else: 
        return MaxAtDepth(T.child[len(T.child) - 1],d-1) # calls the method with the child that has the largest numbers
    
def NodesAtDepth(T,d):
    if d == 0:
        return 1
    elif d == 1:   
        for i in range(len(T.item)):
            len(T.item)
    else:
        return
def PrintAtDepth(T,d):
    if d == 0:
        print(T.item,end = ' ') #Prints the items when is the depth desired
    for i in range(len(T.child)):        
        PrintAtDepth(T.child[i], d-1) #calls the method substracting 1 to reach the depth desired 
        
def FullNodes(T):
    if T.isLeaf:
        if len(T.item) >= T.max_items:#Compares if the items are greater than the max_items
            return 1
        else:
            return 0
    else:
        sum = 0
        if(len(T.item)) >= T.max_items:
           sum += 1 
        for i in range(len(T.item)):
            sum = sum + FullNodes(T.child[i]) #Variable that sums 1 each time the items are equal or greater than max_items
        return sum + FullNodes(T.child[len(T.item)])
def FullLeaves(T):
    if T.isLeaf:
        if len(T.item) >= T.max_items:
            return 1
        else:
            return 0
    else:
        sum = 0
        for i in range(len(T.item)):
            sum = sum + FullLeaves(T.child[i])
        return sum + FullLeaves(T.child[len(T.item)])
    
def PrintBtree(T):
    if T.isLeaf:
        for t in T.item:
            print(t,end= ' ' )
    else:
        for i in range(len(T.item)):
            PrintBtree(T.child[i])
            print(T.item[i])
        PrintBtree(T.child[len(T.item)])
        
def DepthOfK(T,k):
    if k in T.item:
        return 0
    else:
        return 1 + DepthOfK(T.child[FindChild(T,k)],k) # Adds 1 each time it calls a child in order to know the depth
    
def PrintLengthOfNodes(T):# Method used to get an idea of the length of each node
    if T.isLeaf:
        print(len(T.item))
    else:
        print(len(T.item))
        for i in range(len(T.item)):
            PrintLengthOfNodes(T.child[i])
        PrintLengthOfNodes(T.child[len(T.item)])
        
    
            
    
L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6]
T = BTree()    
for i in L:
    #print('Inserting',i)
    Insert(T,i)
    PrintD(T,'') 
    #Print(T)
    print('\n####################################')
print('Height of the tree:')
print(height(T))
print('Sorted list: ', CreateSortedList(T))
print('Minimum element at depth: ', MinAtDepth(T,3))
print('Maximum element at depth: ',MaxAtDepth(T,2))
print('Nodes at Depth: ')
print(NodesAtDepth(T,2))
print('Print at Depth: ')
PrintAtDepth(T,3) 
print('Full Nodes: ', FullNodes(T))
print('Full Leaves: ', FullLeaves(T))
PrintBtree(T)
print()
print('Depth of k: ', DepthOfK(T,100))
#PrintLengthOfNodes(T)