def insert_sort_a(array):
    i = 1
    while i < len(array):
        a = array[i]
        b = i - 1
        while b >= 0 and array[b] > a:
            array[b + 1] = array[b]
            b = b - 1
        array[b + 1] = a
        i = i + 1
    print_insertion(array)

def print_insertion(array):
    print array
