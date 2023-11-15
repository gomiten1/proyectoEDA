#import json
from Tree.TreeNode import BTreeNode
import csv

class BTree:
    def __init__(self, t):
        self.root = None 
        self.t = t 
        
    def traverse(self):
        if self.root != None:
            self.root.traverse(0)
            
    def search(self, k):
        return None if self.root == None else self.root.search(k)
    
    def insert(self, data):
        if self.root == None:
            self.root = BTreeNode(self.t, True)
            self.root.keys[0] = data
            self.root.n = 1
        else:
            if self.root.n == 2 * self.t - 1:
                s = BTreeNode(self.t, False)
                s.C[0] = self.root
                s.splitChild(0, self.root)
                i = 0
                if s.keys[0].key < data.key:
                    i += 1
                s.C[i].insertNonFull(data)
                self.root = s
            else:
                self.root.insertNonFull(data)
    
    

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
        node = BTreeNode(int(value))
        node.left = deserialize_node(data_iter)
        node.right = deserialize_node(data_iter)
        return node

    return deserialize_node(serialized_data)




