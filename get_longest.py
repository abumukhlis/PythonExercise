def get_longest(words):
    """This function accepts a list of words and returns the longest word"""
    _, longest = max((len(word), word) for word in words)
    return longest

# Alternate solution


def get_longest(words):
    """This function accepts a list of words and returns the longest word"""
    return max(words, key=len)
