#Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday. Write a function which is given the day number, and it returns the day name (a string).

def week(i):
 
    if i==0:
       return('Sunday')
    elif i==1:
       return('Monday')
    elif i==2:
       return('Tuesday')
    elif i==3:
       return('Wednesday')
    elif i==4:
       return('Thursday')
    elif i==5:
       return('Friday')
    elif i==6:
       return('Saturday')
    return None

if __name__ == '__main__':
    assert week(0) == 'Sunday'
    assert week(5) == 'Friday'
    assert week(8) == None
