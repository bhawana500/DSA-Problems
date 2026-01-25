class Node:
    def __int__(self,data):
        self.data = data
        self.next = next

def takeInput():
    inputList = [int(m) for m in input().split()]
    head = None
    
    for currData in inputList:
        if currData == -1:
            break
        
        newNode = Node(currData)
        
        if head == None:
            head = newNode
        else:
            temp = head
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
    return head



        
            