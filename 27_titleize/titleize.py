def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    str_list = phrase.split(' ')
    for i in range(len(str_list)):
        str_list[i] = str_list[i][0].upper() + str_list[i][1:].lower()
    return ' '.join(str_list)
