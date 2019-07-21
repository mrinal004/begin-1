class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node

    def printList(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print("---------------------------------------------------")
    def NthFromLast(self,n):
        main=self.head
        ref=self.head
        c=0
        while c<n:
            if ref ==None:
                print("value greater than number of nodes")
                return
            ref=ref.next
            c+=1
        while ref is not None:
            main=main.next
            ref=ref.next
        print("value:",main.data)    

if __name__=='__main__':
    llist=LinkedList()
    llist.push(20)
    llist.push(80)
    llist.push(29)
    llist.push(36)
    llist.push(88)
    llist.printList()
    llist.NthFromLast(3)
    llist.NthFromLast(8)