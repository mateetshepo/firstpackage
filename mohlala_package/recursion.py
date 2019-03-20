def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    for a in range(0, len(items)-1):
        for b in range(0, len(items-1-a)):
            if items[b]>items[b+1]:
                items[b], items[b+1] = items[b+1], items[b]
    return items


def merge_sort(items):

    """Return array of items, sorted in ascending order using merge sort"""
    if len(items) >1:
        mid = len(items)//2
        left = items[:mid]
        right = items[mid:]

        merge_sort(left)
        merge_sort(right)

        i=0
        j=0
        k=0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                items[k] = left[i]
                i+=1
            else:
                items[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            items[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            items[k] = right[j]
            j+=1
            k+=1

    return items


def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
    less = []
    equal = []
    greater = []

    if len(item) > 1:
        pivot = item[0]
        for x in item:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else x > pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater)

    else:
        return item
