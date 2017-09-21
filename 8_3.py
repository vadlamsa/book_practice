A function named count_letters, and generalize it so that it accepts the string and the letter as arguments. Make the function return the number of characters, rather than print the answer. The caller should do the printing.:

def count_letter(string,letter):
    count=0
    for l in string:
        if l==letter:
           count=count+1
    return count

if __name__ == '__main__':
    assert count_letter('Hello','l') == 2
    assert count_letter('bananna','n') == 3
    

 


