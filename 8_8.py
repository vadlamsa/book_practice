def reverse(s):
   y=s[::-1]
   ans = s+y
   return ans
if __name__ == '__main__':
    assert reverse("good") == "gooddoog"
    assert reverse("Python") == "PythonnohtyP"
    assert reverse("") == ""
    assert reverse("a") == "aa"
