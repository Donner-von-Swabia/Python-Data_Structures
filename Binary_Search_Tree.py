"""
Author: Seth Everett
Start Date: March 13, 2023
Description: Learning Linked Lists
"""

class node:
    def __init__(self,value=None):
        self.value = value
        self.left_child=None
        self.right_child=None

class Binary_Search:
    def __init__(self):
        self.root=None
    
    def insert(self,value):
        if self.root == None:
            self.root =node(value)
        else:
            self._insert(value,self.root)
    
    def _insert(self,value,c_node):
        if value < c_node.value:
            if c_node.left_child == None:
                c_node.left_child = node(value)
            else:
                self._insert(value,c_node.left_child)
        elif value > c_node.value:
            if c_node.right_child == None:
                c_node.right_child = node(value)
            else:
                self._insert(value,c_node.right_child)
        else:
            print("Value already in tree")
    
    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)
    
    def _print_tree(self,c_node):
        if c_node != None:
            self._print_tree(c_node.left_child)
            print (str(c_node.value))
            self._print_tree(c_node.right_child)
    
    def height(self):
        if self.root != None:
            return self._height(self.root,0)
        else:
            return 0
    
    def _height(self, c_node, c_height):
        if c_node == None:
            return c_height
        left_height = self._height(c_node.left_child, c_height+1)
        right_height = self._height(c_node.right_child, c_height+1)
        return max(left_height, right_height)
    
    def search(self,value):
        if self.root != None:
            return self._search(value,self.root)
        else:
            return False
        
    def _search(self,value,c_node):
        if value == c_node.value:
            return True
        elif value < c_node.value and c_node.left_child != None:
            return self._search(value, c_node.left_child)
        elif value < c_node.value and c_node.right_child != None:
            return self._search(value,c_node.right_child)
        else:
            return False


def fill(tree, number_of_elements=100, max_integer = 100):
    from random import randint
    for i in range(number_of_elements):
        current_element = randint(0,max_integer)
        tree.insert(current_element)
    return tree


tree = Binary_Search()
tree = fill(tree)
tree.print_tree()
print(tree.height())
for x in range (tree.height()):
    print(tree.search(x))