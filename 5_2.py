#You go on a wonderful holiday on day 0 (sunday).You return home after 137 sleeps. Write a general version of the program which takes day number of the start of vacation and the length of stay as the input parameters will tell you the name of day of the week you will return on.

def week(s,l):
    m = s + l
    i =(m % 7)
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
   
if __name__ == '__main__':
    assert week(2,3) == 'Friday'
    assert week(5,100) == 'Sunday'
   

