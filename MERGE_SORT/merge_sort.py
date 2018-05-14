def merge(left, right):
    result = []
    while left is not None and right is not None:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(left[0])
        else:
            result.append(right[0])
            right.pop(right[0])
    while left is not None:
        result.append(left[0])
        left.pop(left[0])
    while right is not None:
        result.append(right[0])
        right.pop(right[0])
    return result

def merge_sort(array):
    if len(array) == 1:
        return array
    left = array[:len(array)/2]
    right = array[len(array)/2:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
