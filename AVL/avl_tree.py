from avl_node import Node

class Avl(object):

    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(None, value)
        if self.root is None:
            self.root = node
        else:
            self.root.insert_node(node)
        self.balance(node)

    def left_rotation(self, node):
        curr_node = node.right_child
        curr_node.parent_node = node.parent_node
        if curr_node.parent_node is None:
            self.root = curr_node
        else:
            if curr_node.parent_node.left_child is node:
                curr_node.parent_node.left_child = curr_node
            elif curr_node.parent_node.right_child is node:
                curr_node.parent_node.right_child = curr_node
        node.right_child = curr_node.left_child
        if node.right_child is not None:
            node.right_child.parent_node = node
        curr_node.left_child = node
        node.parent_node = curr_node
        run_u_heights(node, curr_node)

    def right_rotation(self, node):
        curr_node = node.left_child
        curr_node.parent_node = node.parent_node
        if curr_node.parent_node is None:
            self.root = curr_node
        else:
            if curr_node.parent_node.left_child is node:
                curr_node.parent_node.left_child = curr_node
            elif curr_node.parent_node.right_child is node:
                curr_node.parent_node.right_child = curr_node
        node.left_child = curr_node.right_child
        if node.left_child is not None:
            node.left_child.parent_node = node
        curr_node.right_child = node
        node.parent_node = curr_node
        run_u_heights(node, curr_node)

    def search(self, value):
        return self.root.search(value)

    def balance(self, node):
        while node is not None:
            u_height(node)
            if get_height(node.left_child) >= 2 + get_height(node.right_child):
                if get_height(node.left_child.left_child) >= get_height(node.left_child.right_child):
                    self.right_rotation(node)
                else:
                    self.left_rotation(node.left_child)
                    self.right_rotation(node)
            elif get_height(node.right_child) >= 2 + get_height(node.left_child):
                if get_height(node.right_child.right_child) >= get_height(node.right_child.left_child):
                    self.left_rotation(node)
                else:
                    self.right_rotation(node.right_child)
                    self.left_rotation(node)
            node = node.parent_node

    def print_tree(self):
        if self.root is None:
            print("Tree is empty\n")
        else:
            self.root.print_nodes();

def get_height(curr_node):
    if curr_node is None:
        return -1
    else:
        return curr_node.height

def u_height(curr_node):
    curr_node.height = max(get_height(curr_node.left_child), get_height(curr_node.right_child)) + 1

def run_u_heights(node , curr_node):
    u_height(node)
    u_height(curr_node)
