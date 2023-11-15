#import json
from Tree.TreeNode import TreeNode
import csv

class BinaryTree:

    def __init__(self):
        self.root = None #root = None

    def insert(self, root, n):
        if root is None:
            self.root = n
            return

        if n.key < root.key:
            if root.left is None:
                root.left = n
            else:
                self.insert(root.left, n)
        elif n.key > root.key:
            if root.right is None:
                root.right = n
            else:
                self.insert(root.right, n)

    def search(self, root, key):
        if root is None:
            return None

        if root.key == key:
            return root.key #return root
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def min(self, root):
        if root is None:
            return None
        if root.left is None:
            return root
        return self.min(root.left)

    def max(self, root):
        if root is None:
            return None
        if root.right is None:
            return root
        return self.max(root.right)

    def delete(self, root, key):
        if root is None:
            return root #return None
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.min(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root

    def print_in(self, root, level):
        if root is not None:
            self.print_in(root.left, level + 1)
            print("\t" * level, root)
            self.print_in(root.right, level + 1)

    def print_pre(self, root):
        if root is not None:
            print(root)
            self.print_pre(root.left)
            self.print_pre(root.right)

    def print_post(self, root):
        if root is not None:
            self.print_post(root.left)
            self.print_post(root.right)
            print(root)

#Funciones que se van a utilizar para leer y escribir en un archivo

def serialize_tree_to_csv(root, filename):
    if root is None:
        return

    def serialize_node(node):
        if node is None:
            return []
        return [node.value] + serialize_node(node.left) + serialize_node(node.right)

    serialized_data = serialize_node(root)

    with open(filename, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(serialized_data)

def deserialize_tree_from_csv(filename):
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        serialized_data = next(csv_reader)

    def deserialize_node(data_iter):
        if not data_iter:
            return None
        value = data_iter.pop(0)
        if value == '':
            return None
        node = TreeNode(int(value))
        node.left = deserialize_node(data_iter)
        node.right = deserialize_node(data_iter)
        return node

    return deserialize_node(serialized_data)

'''# Example usage:
# Create a sample tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Serialize the tree to a CSV file
serialize_tree_to_csv(root, 'tree_file.csv')

# Deserialize the tree from the CSV file
new_root = deserialize_tree_from_csv('tree_file.csv')
'''


