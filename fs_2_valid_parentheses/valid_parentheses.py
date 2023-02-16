def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    count = 0
    for char in parens:
        if count == -1:
            return False
        elif char == '(':
            count += 1
        elif char == ')':
            count -= 1
    return count == 0
    # return parens.count('(') == parens.count(')')
