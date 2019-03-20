def sum_array(array):

    ''' Return sum of all items in array'''
    answer = 0
    for x in array:
        answer += x
    return answer


def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def factorial(n):

    '''Return n!'''
    num = 1
    while num >= 1:
        num = num * n
        n = n-1
    return num


def reverse(word):
    '''Return word in reverse'''
    if len(word) > 1:
        return word[-1] + reverse(word[:-1])
    else:
        return word
