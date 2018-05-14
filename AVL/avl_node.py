class Node(object):

    def __init__(self, parent_node, value):
        self.value = value
        self.parent_node = parent_node
        self.left_child = None
        self.right_child = None
        self.height = 0

    def insert_node(self, new_node):
        if new_node is None:
            return
        if new_node.value < self.value:
            if self.left_child is None:
                new_node.parent_node = self
                self.left_child = new_node
            else:
                self.left_child.insert_node(new_node)
        else:
            if self.right_child is None:
                new_node.parent_node = self
                self.right_child = new_node
            else:
                self.right_child.insert_node(new_node)

    def search(self, in_value):
        if in_value == self.value:
            return self
        elif in_value < self.value:
            if self.left_child is None:
                return None
            else:
                return self.left_child.search(in_value)
        else:
            if self.right_child is None:
                return None
            else:
                return self.right_child.search(in_value)

    def __str__(self):
        return str(self.value)

    def print_nodes(self):
        if self.left_child is not None:
            self.left_child.print_nodes()
        print self
        if self.right_child is not None:
            self.right_child.print_nodes()
