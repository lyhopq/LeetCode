def lengthOfLongestSubstring(str):
    '''
    Given a string, find the length of the longest substring without repeating characters. 
    For example, the longest substring without repeating letters for "abcabcbb" is "abc", 
    which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

    >>> lengthOfLongestSubstring('abcabcbb')
    3
    >>> lengthOfLongestSubstring('bbbbb')
    1
    >>> lengthOfLongestSubstring('a')
    1
    '''
    occur = {}
    length = 0
    longest = 0
    startIndex = 0
    for index, c in enumerate(str):
        lastIndex = occur.get(c, None)
        if lastIndex is None:
            length += 1
        else:
            for i in range(startIndex, lastIndex):
                del occur[str[i]]
            if length > longest: longest = length
            startIndex = lastIndex + 1
            length = index - lastIndex
        occur[c] = index

    if length > longest: longest = length

    return longest

if __name__ == '__main__':
    import doctest
    doctest.testmod()
