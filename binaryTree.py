class Node:

    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

    def insert(self,data):
        if self.data is None:
            self.data=data
        else:
            if data < self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
    def display(self):
        if self.right:
            self.right.display()
        if self.left:
            self.left.display()
        print(self.data)

root =Node(6)
root.insert(8)
root.insert(2)


root.display()
