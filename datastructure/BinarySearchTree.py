'''
 * @file   BinarySearchTree.py
 * @author NaX
'''
from enum import Enum, auto

class TreeTraversalOrder(Enum):
  PRE_ORDER = auto()
  IN_ORDER = auto()
  POST_ORDER = auto()
  LEVEL_ORDER = auto()

class Node():
    def __init__(self, left, right, elem):
        self.data = elem
        self.left = left
        self.right = right

class BinarySearchTree():
    def __init__(self):
        self.nodeCount = 0
        self.root = None

    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return self.nodeCount

    # Add functionality

    def add(self, elem):
        if self.contains(elem):
            return False
        else:
            self.root = self.__add(self.root, elem)
            self.nodeCount += 1
            return True

    def __add(self, node, elem):
        if node == None:
            node = Node(None, None, elem)
        else:
            if elem < node.data:
                node.left = self.__add(node.left, elem)
            else:
                node.right = self.__add(node.right, elem)

        return node

    # Remove functionality

    def remove(self, elem):
        if self.contains(elem):
            root = self.__remove(self.root, elem)
            self.nodeCount -= 1
            return True
        
        return False

    def __remove(self, node, elem):
        if node == None:
            return None

        # Compared Value

        if elem < node.data:
            node.left = self.__remove(node.left, elem)
        elif elem > node.data:
            node.right = self.__remove(node.right, elem)
        else:
            
            # This is the case with only a right subtree or
            # no subtree at all. In this situation just
            # swap the node we wish to remove with its right child.

            if node.left == None:
                rightChild = node.right
                node.data = None
                node = None

                return rightChild

            # This is the case with only a left subtree or
            # no subtree at all. In this situation just
            # swap the node we wish to remove with its left child.

            elif node.right == None:
                leftChild = node.left
                node.data == None
                node = None

                return leftChild

            # When removing a node from a binary tree with two links the
            # successor of the node being removed can either be the largest
            # value in the left subtree or the smallest value in the right
            # subtree. In this implementation I have decided to find the
            # smallest value in the right subtree which can be found by
            # traversing as far left as possible in the right subtree.
            else:

                # Use findMax for left subtree
                tmp = self.findMin(node.right)
                node.data = tmp.data
                node.right = self.__remove(node.right, tmp.data)

            return node


    def findMin(self, node):
        while node.left is not None:
            node = node.left
        
        return node

    def findMax(self, node):
        while node.right is not None:
            node = node.right

        return node
    
    def contains(self, elem):
        return self.__contains(self.root, elem)

    def __contains(self, node, elem):

        if node == None:
            return False
        
        if node.data < elem:
            return self.__contains(node.left, elem)
        elif node.data > elem:
            return self.__contains(node.right, elem)
        else:
            return True


    def height(self):
        return self.__height(self.root)

    
    def __height(self, node):
        if node == None:
            return 0
        else:
            return max(self.__height(node.left), self.__height(node.right)) + 1


    def traverser(self, order):
        if order is TreeTraversalOrder.PRE_ORDER:
            return self.preOrderTraversal()
        if order is TreeTraversalOrder.IN_ORDER:
            return self.inOrderTraversal()
        if order is TreeTraversalOrder.POST_ORDER:
            return self.postOrderTraversal()
        if order is TreeTraversalOrder.LEVEL_ORDER:
            return self.levelOrderTraversal()

    def preOrderTraversal():
        pass
    def inOrderTraversal():
        pass
    def postOrderTraversal():
        pass
    def levelOrderTraversal():
        pass
            