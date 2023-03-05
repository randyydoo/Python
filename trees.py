class Node:
    def __init__(self, value):
      self.left = None
      self.right = None
      self.value = value
    def insert(self, value):
        # set as root
        if self.value == None: 
            self.value = value
            #check if less than
        elif value < self.value:
            #go left and if none, insert node
            if self.left == None:
                self.left == Node(value)
            #if node is to left, we will start the insert function at the left which is the new "root"
            else:
                self.left.insert(value)
            #value is greater than root
        else:
            if self.right == None:
                self.right == Node(value)
            else:
                self.right.insert(value)
    #printing  tree in order
        list = []
        stack = []
        cur = root
        def inOrder(root):
         #iterativly
            while cur or stack is not None:  #to clear out stack and use frame to append to list when cur = none
                while cur is not None:
                    #add to stack until none
                    stack.append(cur)
                    cur = cur.left
                cur = stack.pop()
                list.append(cur.val)
                #if cur.right == value then go into second frame of while loop to append to stack
                cur = cur.right

         
         
         
         
         #recursivly   
            if not root:
                return
            inOrder(root.left)
            list.append(root.value)
            inOrder(root.right)
        inOrder(root)
        return list


#create root
root = Node("g")
root.insert("c")
root.insert("b")
root.insert("a")
root.insert("e")
root.insert("d")
root.insert("f")
root.insert("i")
root.insert("h")
root.insert("j")
root.insert("k")

