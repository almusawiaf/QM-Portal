# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 21:17:59 2023

@author: Ahmad Al Musawi
Control the next path given a value 
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = new_node

    def remove_node(self, value):
        if self.head is None:
            return
        
        if self.head.value == value:
            self.head = self.head.next
            return

        curr_node = self.head
        while curr_node.next is not None:
            if curr_node.next.value == value:
                curr_node.next = curr_node.next.next
                return
            curr_node = curr_node.next

    def __str__(self):
        nodes = []
        curr_node = self.head
        while curr_node is not None:
            nodes.append(str(curr_node.value))
            curr_node = curr_node.next
        return '->'.join(nodes)

# create a linked list with some values
ll = LinkedList()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.add_node(4)

# print the initial linked list
print(ll)  # output: 1->2->3->4

# remove a node with value 3
ll.remove_node(3)

# print the updated linked list
print(ll)  # output: 1->2->4
