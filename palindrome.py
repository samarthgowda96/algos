def pal(string):
    rev=""
    for i in reversed(range(len(string))):
        rev+=string[i]
    if(string==rev):
        print('it is a palidrome')
    else:
        print("it is not a palidrome")

pal("naman")
pal("sam")