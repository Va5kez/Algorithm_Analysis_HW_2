import sys
from AVL.avl_tree import Avl

def main():
    print "Avl tree program is executed"
    tree = Avl()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(1)
    tree.insert(9)
    tree.print_tree()
    print "Program Finished"

if __name__ == "__main__":
    main()
