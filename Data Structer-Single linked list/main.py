class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
    

class SingleLinkedList():
    def __init__(self):
        self.head=None


    def add_to_back(self,value):
        newNode=Node(value)
        if not self.head:
            self.head=newNode
            return
        
        current=self.head
        while(current.next):
            current=current.next
        current.next=newNode

    def display(self):
        current=self.head
        while(current):
            print(current.data,end="---->")
            current=current.next

s_list=SingleLinkedList()

s_list.add_to_back(5)
s_list.add_to_back(10)
s_list.add_to_back(20)
s_list.add_to_back(30)
s_list.display()
















# node1=Node(5)
# node2=Node(10)
# node3=Node(15)

# node1.next=node2
# node2.next=node3

# # after they connected:make copy of node1
# current=node1 

# while(current):
#     print (current.data,end='---->')
#     current=current.next