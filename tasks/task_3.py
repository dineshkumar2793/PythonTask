def strip_ends(arr):
    """

    :param arr:
    :return: Sliced list containing all elements except the first and last element
    """
    return arr[1:-1]

def strip_chars(string):
    """

    :param string:
    :return: new string containing every second character from given string
    [::2]
    """
    return string[::2]
