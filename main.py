import sys
from AVL.avl_tree import Avl
from INSERT_SORT.insert_sort import insert_sort_a

def main():
    print "Avl tree program is executed"
    tree = Avl()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(1)
    tree.insert(9)
    tree.print_tree()
    print "Insert Sort is executed"
    array = [3,6,8,9,1,5]
    insert_sort_a(array)
    print "Program Finished"

if __name__ == "__main__":
    main()
