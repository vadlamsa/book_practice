#Write a function cross_product(u, v) that takes two lists of numbers of length 3 and returns their cross product. You should write your own tests.
def cross_product(a,b):
    w=[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
    return w

if __name__ == '__main__':
    assert cross_product([1,1,1], [1,1,1]) == [0,0,0]
    assert cross_product([1, 2, 3], [4, 5, 6]) == [-3,6,-3]
    assert cross_product([0,1,2], [3,3,3]) == [-3,6,-3]
     

