# Write a function that removes all occurrences of a given letter from a string

def remove(letter,strng):
    ans=''
    for ch in strng:
        if ch!=letter:
           ans=ans+ch
    return ans
if __name__ == '__main__':
    assert remove("a", "apple") == "pple"
    assert remove ("a", "banana") == "bnn"
    assert remove("z", "banana") == "banana"
    assert remove("i", "Mississippi") == "Msssspp"
    assert remove("b", "") == ""
    assert remove("b", "c") == "c"

