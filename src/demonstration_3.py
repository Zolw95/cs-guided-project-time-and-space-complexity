"""
Given two strings `a` and `b`, write a function to determine if `a` is an
**anagram** of `b`.

*Note: an anagram is a word, phrase, or name formed by rearranging the letters
of another, such as cinema, formed from iceman.*

**Example:**

Input: `a` = "anagram", `b` = "nagaram"
Output `True`

**Example:**

Input: `a` = "bat", `b` = "tar"
Output `False`
"""
def is_anagram(a, b):
    # Your code here
    # sort strings
    # if strings are identical - return True
    # if not - print false
    if (sorted(a) == sorted(b)):
        return True
    else:
        return False
result = is_anagram("junior", "orinuj")
print(result)
