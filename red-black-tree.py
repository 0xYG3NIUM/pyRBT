#implementation of the red-black tree algorithm

#properties of rbt
#1. Every node is either black or red
#2. The root is black
#3. Every leaf(NIL) is black
#4. If node is Red , both its children are black
#5. For EACH node, all simple paths from the node to descendant leaves have the same number of black nodes.


from PIL import Image, ImageDraw
import random


class Node:
    def __init__(self,cargo,left,right,parent,color):
        self.cargo = cargo
        self.left  = left
        self.right = right
        self.parent = parent
        self.color = color 

    def __str__(self):
        return str(self.cargo)



#next object will represent leafs
NIL = Node('NIL',None,None,None,'BLACK') #Every leaf is black 

#root is empty 
root = NIL



def leftRotate(x):
    global root
    if x.right is NIL: return
    
    #y is the right node of x which will take place of x
    y = x.right
    
    #exchanging parents
    y.parent = x.parent
    x.parent = y
    
    #swapping nodes
    x.right = y.left
    y.left = x
    
    #updating child parents
    if x.right is not NIL: x.right.parent = x
    
    #if we rotated the root we need to update a reference to it, otherwise we update link to it
    if x is root:
         root = y
    elif y.parent.right is x:
        y.parent.right = y
    elif y.parent.left is x:
        y.parent.left = y

def rightRotate(x):
    global root
    if x.left is NIL: return
    
    y=x.left
    
    y.parent = x.parent
    x.parent = y
    
    x.left = y.right
    y.right = x
    
    if x.left is not NIL: x.left.parent = x
    
    if x is root:
         root = y
    elif y.parent.right is x:
        y.parent.right = y
    elif y.parent.left is x:
        y.parent.left = y 
    
    
def rbInsert(z):
    global root
    x = root
    y = NIL
    while x is not NIL:
        y = x
        if z.cargo < x.cargo:
            x = x.left
        else:
            x = x.right
    z.parent = y
    
    if y is NIL: root = z
    elif z.cargo < y.cargo: y.left = z
    else: y.right = z
    
    z.left = NIL
    z.right = NIL
    z.color = 'RED'
    
    rbInsertFixup(z)            

def rbInsertFixup(z):
    
    while z.parent is not NIL and z.parent.color is 'RED':
        if z.parent is z.parent.parent.left:
            uncle = z.parent.parent.right #uncle of z
            if uncle.color is 'RED': #CASE 1
                z.parent.color = 'BLACK'
                uncle.color = 'BLACK'
                z.parent.parent.color = 'RED'
                z = z.parent.parent
            else:
                if z is z.parent.right: #case 2
                    z = z.parent
                    leftRotate(z)
                
                #case 3
                z.parent.color = 'BLACK'
                z.parent.parent.color = 'RED'
                rightRotate(z.parent.parent)
        else:
            uncle = z.parent.parent.left #uncle of z
            if uncle.color is 'RED': #CASE 1
                z.parent.color = 'BLACK'
                uncle.color = 'BLACK'
                z.parent.parent.color = 'RED'
                z = z.parent.parent
            else:
                if z is z.parent.left: #case 2
                    z = z.parent
                    rightRotate(z)
                
                #case 3
                z.parent.color = 'BLACK'
                z.parent.parent.color = 'RED'
                leftRotate(z.parent.parent)        

    root.color = 'BLACK'

###### program

#U = random.sample(range(1,111),10)

#for u in U:
#    rbInsert(Node(u,NIL,NIL,NIL,'RED'))
