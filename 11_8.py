#Write a function dot_product(u, v) that takes two lists of numbers of the same length, and returns the sum of the products of the corresponding elements of each (the dot_product).

def dot_product(s,v):
    w=0
    for i in range(len(v)):
           w1=s[i]*v[i]
           w=w+w1   
    return w

if __name__ == '__main__':
    assert dot_product([1, 2], [1, 4]) == 9
    assert dot_product([1, 2, 1], [1, 4, 3]) == 12
    assert dot_product([1, 1], [1, 1]) == 2
    

