class Node:
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data
    def insert(self,data):
        if data<=self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left=Node(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right=Node(data)
    def preorder(self):
        l=[self.data]
        if self.left:
            l+=self.left.preorder()
        if self.right:
            l+=self.right.preorder()
        return l
    def inorder(self):
        l=[]
        if self.left:
            l+=self.left.inorder()
        l.append(self.data)
        if self.right:
            l+=self.right.inorder()
        return l
    def postorder(self):
        l=[]
        if self.left:
            l+=self.left.postorder()
        if self.right:
            l+=self.right.postorder()
        l.append(self.data)
        return l
n=int(input())
l=[int(i) for i in input().split()]
root=Node(l[0])
for i in range(1,len(l)):
    root.insert(l[i])
l=root.preorder()
print(*l,sep=' ')
l=root.inorder()
print(*l,sep=' ')
l=root.postorder()
print(*l,sep=' ')
