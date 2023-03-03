# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 21:27:11 2023

@author: Ahmad Al Musawi
Binary Linked list
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            curr_node = self.root
            while True:
                if value < curr_node.value:
                    if curr_node.left is None:
                        curr_node.left = new_node
                        break
                    else:
                        curr_node = curr_node.left
                else:
                    if curr_node.right is None:
                        curr_node.right = new_node
                        break
                    else:
                        curr_node = curr_node.right

    def inorder_traversal(self, node, nodes):
        if node is not None:
            self.inorder_traversal(node.left, nodes)
            nodes.append(str(node.value))
            self.inorder_traversal(node.right, nodes)

    def to_linked_list(self):
        nodes = []
        self.inorder_traversal(self.root, nodes)
        for i in range(len(nodes) - 1):
            node = Node(nodes[i])
            node.right = Node(nodes[i+1])
            nodes[i] = node
        return nodes[0] if nodes else None

    def __str__(self):
        nodes = []
        self.inorder_traversal(self.root, nodes)
        return '->'.join(nodes)

# create a binary tree with some values
bt = BinaryTree()
bt.insert(4)
bt.insert(2)
bt.insert(6)
bt.insert(1)
bt.insert(3)
bt.insert(5)
bt.insert(7)

# convert the binary tree to a linked list
ll_head = bt.to_linked_list()

# print the linked list
curr_node = ll_head
while curr_node is not None:
    print(curr_node.value)
    curr_node = curr_node.right
