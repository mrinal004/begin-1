class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def printList(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print("------------------------------------")
    def push(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node

    def swap_pair(self):
        temp=self.head
        while (temp!=None and temp.next!=None):
            temp.data,temp.next.data=temp.next.data,temp.data
            temp=temp.next.next
        

if __name__=='__main__':
    llist=LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.push(6)
    llist.printList()
    llist.swap_pair()
    llist.printList()

bin(20)