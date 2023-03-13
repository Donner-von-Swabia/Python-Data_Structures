"""
Author: Seth Everett
Start Date: March 13, 2023
Description: Learning Linked Lists
"""

#Sub class of linked list
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()
    
    def append(self,data):
        #Adds nodes onto the linked list
        new_node = node(data)
        current_node = self.head
        while current_node.next!=None:
            current_node = current_node.next
        current_node.next = new_node

    def length(self):
        #Finds the length of the linked list
        current_node = self.head
        total = 0
        while current_node.next!= None:
            total+=1
            current_node = current_node.next
        return total
    
    def display(self):
        #Displays the linked list as an array
        elements = []
        current_node = self.head
        while current_node.next!= None:
            current_node = current_node.next
            elements.append(current_node.data)
        print (elements)

    def get(self,index):
        #Gets a single element within the linked list
        if index>=self.length():
            #Checks if the value being indexed is withint the linked list
            print("Error:Out of field; Indexing number is outside of linked list.")
            return None
        current_node_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_node_index==index: return current_node.data
            current_node_index+=1

    def erase(self,index):
        #Removes a single element from within the linked list
        if index>=self.length():
            #Checks if the value being indexed is withint the linked list
            print("Error:Out of field; Indexing number is outside of linked list.")
            return None
        current_node_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_node_index == index:
                last_node.next = current_node.next
                return
            current_node_index+=1

#Testing
link_list = linked_list()
for x in range(10):
    link_list.append(x)
    x+=1
link_list.display()
print ("Element at 2nd index: %d" %link_list.get(2))
link_list.erase(2)
link_list.display()