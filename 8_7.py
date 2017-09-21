#Write a function that reverses its string argument

def reverse(s):
   y=s[::-1]
   return(y)
if __name__ == '__main__':
    assert reverse("happy") == "yppah"
    assert reverse("Python") == "nohtyP"
    assert reverse("") == ""
    assert reverse("a") == "a"

