import random
class Node:
    def __init__(self,value):
        self.title=value
        self.next=None
    

class playList():
    def __init__(self):
        self.head=None
    
    def addToEnd(self,value):
        newNode=Node(value)
        if not self.head:
            self.head=newNode
            return
        current=self.head
        while(current.next):
            current=current.next
        
        current.next=newNode
    
    def add_index(self,index,value):
        newNode=Node(value)
        current=self.head
        for i in range (index-1):
            current=current.next
        
        newNode.next=current.next
        current.next=newNode

    def getlength(self):
        current=self.head
        count=0
        while current.next:
            count+=1
            current=current.next
        return count
    
    def shuffle(self):
        count=self.getlength()
        randInt=random.randint(0,count)
        current=self.head
        for i in range (randInt):
            current=current.next
        print (current.title)

    def addToBegin(self,value):
        newNode=Node(value)
        newNode.next=self.head
        self.head=newNode

    def Travers(self):
        current=self.head
        while current:
            print (current.title,end="----->")
            current=current.next
        
        print('Null')


song=playList()


song.addToEnd('Boushret Kheir')
song.addToEnd('Etnset')
song.addToEnd('Ma Baaref')
song.addToBegin('Tamally Maak')
song.Travers()
song.shuffle()