def findMedianSortedArrays(A, B):
    '''
    There are two sorted arrays A and B of size m and n respectively.
    Find the median of the two sorted arrays.
    The overall run time complexity should be O(log (m+n)).

    >>> findMedianSortedArrays([5,7,11,17,18,21], [13,16,19,22,27,30,31])
    18.0
    >>> findMedianSortedArrays([5,7,11,17,18,21], [16,19,22,27,30,31])
    18.5
    >>> findMedianSortedArrays([1], [13,16,19,22,27,30,31])
    20.5
    >>> findMedianSortedArrays([], [13,16,19,22,27,30,31])
    22.0
    >>> findMedianSortedArrays([13,16,19,22,28,30,31,40], [])
    25.0
    >>> findMedianSortedArrays([], [1])
    1.0
    >>> findMedianSortedArrays([1,2], [1,1])
    1.0
    >>> findMedianSortedArrays([1], [1])
    1.0
    >>> findMedianSortedArrays([1], [2,3])
    2.0
    >>> findMedianSortedArrays([2], [1,3])
    2.0
    '''
    def middle(low, high):
        return low + (high - low) / 2

    def binarySeach(A, low, high, key):
        while low <= high:
            mid = middle(low, high)
            if key == A[mid]: return mid
            if key > A[mid]:
                low = mid + 1
            else:
                high  = mid - 1
        return low

    def findMedianSortedArrayHelper(A, B, lowA, highA, lowB, highB):
        mid = middle(lowA, highA)
        pos = binarySeach(B, lowB, highB, A[mid])
        num = mid + pos
        m = len(A)
        n = len(B)

        if num == (m + n)/2:
            if (m + n)%2 == 1: return float(A[mid])
            if mid > 0 and pos > 0:
                first = A[mid - 1] if A[mid - 1] > B[pos - 1] else B[pos - 1]
            elif pos > 0:
                first = B[pos - 1]
            elif mid > 0:
                first = A[mid - 1]

            return (first + A[mid])/2.0

        if num < (m + n)/2:
            lowA = mid + 1
            lowB = pos
        elif num > (m + n)/2:
            highA = mid - 1
            highB = pos - 1

        if highA - lowA > highB - lowB:
            return findMedianSortedArrayHelper(A, B, lowA, highA, lowB, highB)
        return findMedianSortedArrayHelper(B, A, lowB, highB, lowA, highA)

    m = len(A)
    n = len(B)
    if m == 0 and n == 0: return 0.0
    if m == 0: return float(B[n/2]) if n%2==1 else (B[n/2-1] + B[n/2])/2.0
    if n == 0: return float(A[m/2]) if m%2==1 else (A[m/2-1] + A[m/2])/2.0

    if m >= n:
        return findMedianSortedArrayHelper(A, B, 0, m - 1, 0, n - 1)
    return findMedianSortedArrayHelper(B, A, 0, n - 1, 0, m - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

