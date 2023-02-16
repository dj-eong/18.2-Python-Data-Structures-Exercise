def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    if len(lst) > 0:
    #if lst: empty lists are falsy in Python
        return lst[-1]
        #return lst.pop()