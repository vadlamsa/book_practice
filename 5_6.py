Write a function which is given an exam mark, and it returns a string — the grade for that mark — according to this scheme:

Mark

Grade

>= 75

First

[70-75)

Upper Second

[60-70)

Second

[50-60)

Third

[45-50)

F1 Supp

[40-45)

F2

< 40

F3

The square and round brackets denote closed and open intervals. A closed interval includes the number, and open interval excludes it. So 39.99999 gets grade F3, but 40 gets grade F2. Assume

def grade(*args):
    for g in args:
        if g>=75:
           print('First')
        if g in range(70,75):
           print('Upper Second')
        if g in range(60,70):
           print('Second')
        if g in range(50,60):
           print('Third')
        if g in range(45,50):
           print('F1 Supp')
        if g in range(40,45):
           print('F2')
        if g<40:
           print('F3')

if __name__ == '__main__':
    assert grade(83) == 'First'
    assert grade(39.9) == 'F3'
    assert grade(44.9) == 'F2'
    assert grade(50.5) == 'Third'

