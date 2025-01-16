
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.


def q1(inicial,final):
    if inicial == None or final == None: return []
    if type(inicial) != int or type(final) != int: return []
    if inicial > final: return[]
   
    
    y=[]
    for number in range(inicial,final):
        if number % 7 == 0 and number % 5 != 0:
            y.append(number)
    return y
