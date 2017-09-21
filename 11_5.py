#Write a function add_vectors(u, v) that takes two lists of numbers of the same length, and returns a new list containing the sums of the corresponding elements of each:
def add_vectors(u,v):
    w=[]
    for i in range(len(u)):
        if len(u)==len(v):
           w1=u[i]+v[i]
           w.append(w1)
    return w
if __name__ == '__main__':
    assert add_vectors([1, 1], [1, 1]) == [2, 2]
    assert add_vectors([1, 2], [1, 4]) == [2, 6]
    assert add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4]

