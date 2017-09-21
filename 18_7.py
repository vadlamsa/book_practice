#Write a function flatten that returns a simple list containing all the values in a nested list:

def flatten(lst):
    ans=[]
    for e in lst:
        if type(e)==type([]):
           ans=ans+(flatten(e))
    
        else:
            ans=ans+[e]
    print(ans)
    return ans

if __name__ == '__main__':
   assert flatten([2,9,[2,1,13,2],8,[2,6]]) == [2,9,2,1,13,2,8,2,6]
   assert flatten([[9,[7,1,13,2],8],[7,6]]) == [9,7,1,13,2,8,7,6]
   assert flatten([[9,[7,1,13,2],8],[2,6]]) == [9,7,1,13,2,8,2,6]
   assert flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]) ==["this","a","thing","a","is","a","easy"]
   assert flatten([]) == []
