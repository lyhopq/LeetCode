def findMedianSortedArrays(A, B): 
    '''
    There are two sorted arrays A and B of size m and n respectively.
    Find the median of the two sorted arrays.
    The overall run time complexity should be O(log (m+n)).

    >>> findMedianSortedArrays([5,7,11,17,18,21], [13,16,19,22,27,30,31])
    18
    >>> findMedianSortedArrays([5,7,11,17,18,21], [16,19,22,27,30,31])
    18.5
    >>> findMedianSortedArrays([1], [13,16,19,22,27,30,31])
    20.5
    >>> findMedianSortedArrays([], [13,16,19,22,27,30,31])
    22
    >>> findMedianSortedArrays([13,16,19,22,28,30,31,40], [])
    25.0
    >>> findMedianSortedArrays([], [1])
    1
    >>> findMedianSortedArrays([1,2], [1,1])
    1.0
    >>> findMedianSortedArrays([1], [1])
    1.0
    >>> findMedianSortedArrays([1], [2,3])
    2
    >>> findMedianSortedArrays([2], [1,3])
    2
    '''
    def medianIndex(total):
        if total == 0:
            return [0]
        if total % 2 == 0:
            return [total/2, total/2 + 1]
        return [total/2 + 1]

    def medianOfOne(A):
        indexs = medianIndex(len(A))
        smaller = A[indexs[0]-1]
        bigger = A[indexs[0]] if len(indexs) == 2 else None
        return judgeMedian(indexs, smaller, bigger)

    def judgeMedian(indexs, smaller, bigger):
        if len(indexs) == 1:
            return smaller
        else:
            return float(smaller + bigger) / 2


    if len(A) == 0:
        return medianOfOne(B)
    elif len(B) == 0:
        return medianOfOne(A)

    total = len(A) + len(B)
    indexs = medianIndex(total)

    iterSmaller = iter(A)
    iterbigger = iter(B)
    smaller = iterSmaller.next()
    bigger = iterbigger.next()

    count = 1
    while True:
        if count == indexs[0]:
            if len(indexs) == 1:
                return smaller if smaller < bigger else bigger
            else:
                try:
                    next = iterbigger.next()
                except StopIteration:
                    next = smaller
                if next < smaller:
                    smaller = next
                return float(smaller + bigger) / 2

        try:
            if smaller <= bigger:
                smaller = iterSmaller.next()
            else:
                bigger = smaller
                iterSmaller, iterbigger = iterbigger, iterSmaller

                smaller = iterSmaller.next()
        except StopIteration:
            smaller = bigger
            break
        count += 1

    delta = indexs[0] - count
    for i in range(delta - 1):
        smaller = iterbigger.next()
    bigger = iterbigger.next()
    return judgeMedian(indexs, smaller, bigger)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

