#Write a function, recursive_min, that returns the smallest value in a nested number list. Assume there are no empty lists or sublists

def r_min(nxs):
    smallest=None
    first_time=True
    for e in nxs:
        if type(e)==type([]):
           val=r_min(e)
        else:
            val=e
        if first_time or val<smallest:
            smallest=val
            first_time=False

    return smallest

if __name__ == '__main__':
   assert r_min([2,9,[1,13],8,6]) == 1
   assert r_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1
   assert r_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7
   assert r_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13              
