class Node:
    def __init__(self, value):
      self.left = None
      self.right = None
      self.value = value
    def insert(self, value):
        if self.value:
            #check if less than
            if value < self.value:
                #go left and if none, insert node
                if self.left == None:
                    self.left == Node(value)
                else:
                    self.left.insert(value)
            #value is greater than root
            elif value > self.value:
                if self.right == None:
                    self.right == Node(value)
                else:
                    self.right.insert(value)
            else: 
                self.value = value




#create note
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

