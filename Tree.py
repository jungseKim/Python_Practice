class Node:
    def __init__(self,data,left=None,right=None):
        self.left=left
        self.right=right
        self.data=data
        
# n5=Node()
# n4=Node()
# n3=Node()
# n2=Node()
# n1=Node()
# n=Node()

# n.left=n1
# n.right=n2
# n.data=0

# n1.left=n3
# n1.right=n4
# n1.data=1

# n3.data=3
# n4.data=4

# n2.left=n5
# n2.data=2

# n5.data=5

def fc(node):
    print(node.data)
    if(node.left):
         fc(node.left)
    if(node.right):
         fc(node.right)
# fc(n)

# def fc2(node):
#     if(node.left):
#         fc2(node.left)
#     if(node.right):
#         fc2(node.right)
#     print(node.data)
# fc2(n)

# def fc3(node):
#     if(node.left):
#          fc(node.left)
#     print(node.data)
#     if(node.right):
#          fc(node.right)
# # fc3(n)
# n=Node(3)
# def input(node,n):
#     if(node.data==n):
#         return
#     if(node.data<n):
#         if(node.right):
#             input(node.right,n)
#         else:
#             node.right=Node(n)
#     else:
#         if(node.left):
#             input(node.left,n)
#         else:
#             node.left=Node(n)
# input(n,4)
# input(n,1)
# input(n,5)
# input(n,2)

# fc(n)

def search(node,n):
    if(node.data==n):
        return print('good')
    if(node.data<n):
        if(node.right):
            search(node.right,n)
    else:
        if(node.left):
            search(node.left,n)
        else:
            print('no')
# search(n,-2)

def destory(node,n):
    if(node.data==n ):
        if(~(node.left and node.right)):
            del node
        if(node.left):
            a=node
            node=node.left
            del a
            return
        if(node.right):
            a=node
            node=node.right
            del a
            return
    if(node.data<n):
        if(node.right):
            destory(node.right,n)
        else:
          return  print('noData')
    else:
        if(node.left):
            destory(node.left,n)
        else:
           return print('nodata')
# destory(n,4)
# fc(n)
# print(~(None and None))

class NodeAll:
    def __init__(self):
        self.root=None
   
    def input(self,node,data):
        if node==None:
            return Node(data)
        if data==node.data:
            return node
        if(node.data<data):
            node.right=self.input(node.right,data)
        else:
            node.left=self.input(node.left,data)
        return node
    def search(self,node,n):
        if(node.data==n):
             return print('good')
        if(node.data<n):
            if(node.right):
                self.search(node.right,n)
            else:
                print('no')
        else:
            if(node.left):
                self.search(node.left,n)
            else:
                print('no')
    def destroy(self,node,n):
        if node.date==n:
            if(node.left):
                pass

nodeAll=NodeAll()
temp=[1,2,45,232,5,3]
for i in temp:
    nodeAll.root=nodeAll.input(nodeAll.root,i)
fc(nodeAll.root)
nodeAll.search(nodeAll.root,11)
