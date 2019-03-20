def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    output_value = items.copy() # in place protection on items
    for i in range(len(output_value)):
        for j in range(len(output_value)-1-i):
            if output_value[j] > output_value[j+1]:
                output_value[j], output_value[j+1] = output_value[j+1], output_value[j]
    return output_value


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
    if len(items) == 1 or len(items) == 0:
        return items
    else:
        pivot = items[0]
        i = 0
        for j in range(len(items)-1):
            if items[j+1] < pivot:
                items[j+1],items[i+1] = items[i+1], items[j+1]
                i += 1
        items[0],items[i] = items[i],items[0]
        first_part = quick_sort(items[:i])
        second_part = quick_sort(items[i+1:])
        first_part.append(items[i])
        return first_part + second_part
