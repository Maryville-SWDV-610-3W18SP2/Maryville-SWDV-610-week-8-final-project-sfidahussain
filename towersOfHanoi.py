'''
    Towers of Hanoi Problem Solution (Implemented both recursively and with the use of a stack)
'''

# Node class used for Stack Implementation
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

# Stack Implementation using a Linked List
class Stack:
    # Constructor
    def __init__( self):
        self.length = 0
        self.top = None

    def push(self, item):
        self.length += 1
        # Create a new node with the value
        n = Node(item)
        # if list is empty, set the next value to null
        if self.top == None:
            n.next = None
        # if it's not empty, set the next value to top
        else:
            n.next = self.top
        # set top to the new node
        self.top = n
    
    def pop(self):
        if self.top == None:
            print('Cannot pop on empty stack.')
        else:
            # Copy into temporary variable to return value of later
            n = self.top
            # Set the top equal to the next value, cancelling out top
            self.top = self.top.next
            self.length-=1
            return n.getData()
    
    def peek(self):
        return self.top.getData()
    
    def isEmpty(self):
        return self.top == None
    
    def size(self):
        return self.length
 
# Recursive Class for Towers of Hanoi
class TowerRecursive:
    def __init__(self):
        self.counter = 0
    
    ''' Referenced Textbook Interactive Python
        Recursive Function:
            1. Moves the tower of height - 1 to a helper pole, using the the final pole as the destination
            2. Moves the disk to the final destination
            3. Moves the tower of height - 1 from the helper pole to the final pole using the original pole. 
    '''
    def moveTower(self, height, fromPole, toPole, withPole):
        if height >= 1:
            self.counter += 1
            self.moveTower(height-1,fromPole,withPole,toPole)
            self.moveDisk(height, fromPole,toPole)
            self.moveTower(height-1,withPole,toPole,fromPole)
     # Helps to see what is moving where
    def moveDisk(self, h, fp,tp):
        print("Moving disk {0} from rod {1} to rod {2}".format(h, fp, tp))

# Stack based implementation (still uses recursive elements)

class TowerStack:
    def __init__(self):
        return
    def moveTower(self, height, initial, progress, final):
        if height >= 1:
            # recursive move tower using the progress stack as a helper
            self.moveTower(height - 1, initial, final, progress)
            # move disk from initial tower to final tower, if there is a disk in the initial tower
            if initial[0]:
                disk = initial[0].pop()
                print("Moving disk {0} from rod {1} to rod {2}".format(str(disk), initial[1], final[1]))
                # placing it in the correct location
                final[0].append(disk)
            # recurisve move tower using progress as helper 
            self.moveTower(height - 1, progress, initial, final)
        
def main():
    towerRecursive = TowerRecursive()
    print('Tower Recursive')
    towerRecursive.moveTower(3,"A","B","C")
    
    print()
    
    towerStack = TowerStack()
    print('Tower Stack')
    # sets up disk in intial stack
    initialStack = ([3, 2, 1], "A")
    finalStack = ([], "B")
    progressStack = ([], "C")
    
    towerStack.moveTower(len(initialStack[0]),initialStack,progressStack,finalStack)

main()
