class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # creates a Linked List from an array
    def create(self, data):

        prev = None

        while data: # iterate the data (list) while there's values

            val = data.pop(0) # grab the value and create the Node
            node = Node(val)

            if self.head is None: # set the head
                self.head = node
            else:
                prev.next = node # set values that proceed head & nodes

            prev = node # assign previous to point previous nodes to new nodes

    # adds node to end of Linked List
    def add(self, node):
        
        if self.head is None: # set the head if there's none
            self.head = node
        else: 
            current = self.head # keep track of nodes

            while current.next: # iterate while the next node is not None
                current = current.next # traversing 1 node to another
            
            current.next = node # end of list so add the node (loop terminates)
    
    
    def remove(self, index): 
        if self.head: # make sure the head exist

            if index < 0: # reverse indexing
                index = self.__len__() + index # makes it normal indexing
            
            if 0 <= index < self.__len__(): # only allow valid indices
                i = 0
                prev = None
                current = self.head

                while i != index and current.next: # iterate until you're at the desired index or end of Linked List
                    prev = current # keep track of previous 
                    current = current.next # traversing 1 node to another
                    i += 1 # index over

                if prev and current.next: # if there's a value before and after (middle removal)
                    prev.next = current.next 
                
                elif prev: # if there's only a value before (tail removal)
                    prev.next = None
                
                elif current.next: # if there's only a value ahead (head removal)
                    self.head = current.next
        
        # Index Errors
            else:
                raise IndexError
        else:
            raise IndexError

    # clears Linked List
    def clear(self):
        self.head = None
    
    def insert(self, index, node):
        if self.head: # make sure the head exist

            if index < 0: # reverse indexing
                index = self.__len__() + index # make normal indexing
            
            
            if 0 <= index < self.__len__(): # valid indices
                i = 0
                prev = None
                current = self.head

                while i != index and current.next: # iterate until you're at the index or end of list
                    prev = current # keep track of previous node
                    current = current.next # traverse 1 node to another
                    i += 1 # index over
                
                if prev and current: # value before and at the index (insert between)
                    prev.next = node
                    node.next = current
                
                elif prev: # value before only (tail insertion (add))
                    self.add(node)
                
                elif current: # value ahead (head insertion)
                    node.next = self.head
                    self.head = node

        # Index Errors
            else:
                raise IndexError
        else:
            self.head = node

    # sets data in node
    def __setitem__(self, index, data): 
        if self.head: # make sure there's a head
            node = self.__getitem__(index) # get the node
            node.data = data # assign new data
        else:
            raise IndexError

    def __getitem__(self, index):
        if self.head: # make sure there's a head

            size = self.__len__() # length of Linked List
            i = 0
            current = self.head

            if index < 0: # reverse indexing
                index = size + index # make nornal indexing

            if 0 <= index < size: # valid indices only
                while i != index and current.next: # iterate until you're at the index or end of Linked List
                    current = current.next # traverse 1 node to another
                    i += 1 # index over
                return current # after iteration return the node where the condition failed in the while loop
        # Index Errors
            else: 
                raise IndexError
        raise IndexError

    # Allows print() for Linked List
    def __str__(self):
        if self.head:

            current = self.head
            list_string = ""

            while current.next:  
                list_string += f"{current.data} -> " 
                current = current.next 
            list_string += f"{current.data}" 

            return list_string 

        return "Empty" 

    # allows len() for Linked List
    def __len__(self):
        if self.head: 
            
            current = self.head
            count = 1 
            while current.next: 
                count += 1
                current = current.next 
            
            return count 

        return 0 


if __name__ == "__main__":
    llist = LinkedList()
    llist.create(list(range(10)))
    print(llist)
    
