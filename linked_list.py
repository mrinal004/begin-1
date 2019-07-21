class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Llist:
    def __init__(self):
        self.head=None

    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
        print("-------------------------------------------------")
    
    def push(self,ndata):
        first=Node(ndata)
        first.next=self.head
        self.head=first

    def beech_mein(self,prev,ndata):
        if prev is None:
            print("NA")

        new_node=Node(ndata)
        new_node.next=prev.next
        prev.next=new_node


l=Llist()
l.head=Node(1)
s=Node(2)
s1=Node(3)
l.head.next=s
s.next=s1
l.printList()
l.push(4)
l.beech_mein(s,8)
l.printList()
