def moves(string):
    x=0
    y=0
    


    for i in string:
        if (i=="U"):
            y=y+1
        elif (i=="D"):
            y=y-1
        elif(i=="R"):
            x=x+1
        elif(y=="L"):
            x=x-1
    return (x,y)


print(moves("UU"))