Write a function which removes all punctuation from the string, breaks the string into a list of words, and counts the number of words in your text that contain the letter “e”. 

import string
def remove_punct(s):
    s_without_punct=""
    print(string.punctuation)
    for letter in s:
        if letter not in string.punctuation:
           s_without_punct=s_without_punct+letter
    return s_without_punct


wds=remove_punct('Hello!How are you doing?').split()
cnt=0
for i in wds:
    print(i)
    if 'e' in i:
       cnt=cnt+1
    print(cnt)


