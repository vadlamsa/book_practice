#Write a function count that returns the number of occurrences of target in a nested list:



def count(target,lst):
    cnt=0
    for n in lst:
        if type(n)==type([]):
           cnt=cnt+count(target,n)
        else:
            if n == target:
               cnt=cnt+1
    return cnt
       

if __name__ == '__main__':
   assert count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4
   assert count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2
   assert count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0
   assert count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6
   assert count("a", [["this",["a",["thing","a"],"a"],"is"], ["a","easy"]]) == 4
