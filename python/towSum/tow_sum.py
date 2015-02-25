def twoSun(numbers, target):
    '''
    Given an array of integers, find two numbers such that they add up to a specific target number.

    The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

    You may assume that each input would have exactly one solution.

    Input: numbers={2, 7, 11, 15}, target=9
    Output: index1=1, index2=2

    >>> twoSun([2,7,11,15], 9)
    (1, 2)
    >>> twoSun([2,6,11,15], 21)
    (2, 4)
    >>> twoSun([2,6,11,14], 21)
    (0, 0)
    '''
    indexs = {}
    for index2, num in enumerate(numbers):
        index1 = indexs.get(target - num, None)
        if index1 is not None:
            return index1 + 1, index2 + 1
        else:
            indexs[num] = index2

    return 0, 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()
