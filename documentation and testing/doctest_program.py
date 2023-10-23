def double(list):
    '''
    This function multiply by 2 all values in a list
    Execute using python3 doctest_program.py -v^
    >>> l = [1, 2, 3, 4]
    >>> double(l)
    [2, 4, 6, 8]
    '''
    return [n*2 for n in list]

if __name__ == "__main__":
    import doctest
    doctest.testmod()