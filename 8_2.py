#Modify:
#prefixes = "JKLMNOPQ"
#suffix = "ack"
#for letter in prefixes:
    #print(letter + suffix)
#so that Ouack and Quack are spelled correctly.



def suffix():
    prefixes='JKLMNOPQ'
    suffix ='ack'
    for letter in prefixes:
        if letter=='Q' or letter=='O':
           print(letter+"uack")
        else:
           print(letter+suffix)
 
suffix()

