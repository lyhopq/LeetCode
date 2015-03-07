def longestPalindrome(s):
    '''
    Given a string S, find the longest palindromic substring in S.
    You may assume that the maximum length of S is 1000,
    and there exists one unique longest palindromic substring.

    >>> longestPalindrome('1233214')
    '123321'
    >>> longestPalindrome('123321414123321111111111111111112')
    '21111111111111111112'
    '''
    def findPalindrome(s, left, right):
        n = len(s)
        while left >= 0 and right < n and s[left] == s[right]:
            left = left - 1
            right = right + 1
        return s[left+1:right]

    n = len(s)
    if n <=1: return s
    longest = ''
    for i in range(n):
        str = findPalindrome(s, i, i)
        if len(str) > len(longest): longest = str

        str = findPalindrome(s, i, i+1)
        if len(str) > len(longest): longest = str

    return longest

if __name__ == '__main__':
    import doctest
    doctest.testmod()
