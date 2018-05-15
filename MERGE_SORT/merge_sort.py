def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    while left:
        result.append(left.pop(0))

    while right:
        result.append(right.pop(0))

    return result

def merge_sort(array):
    if len(array) == 1:
        return array

    left = array[:len(array)/2]
    right = array[len(array)/2:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)
