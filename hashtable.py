# demonstrate hashtable usage


# TODO: create a hashtable all at once ,this prints in random orders
item1= dict({"key1":1,"key2":2,"key3":"three"})


# TODO: create a hashtable progressively, prints in the given order
item2={}
item2["key1"]=1
item2["key2"]=2
item2["key3"]=3
item2["key4"]=4
print(item2)

# TODO: try to access a nonexistent key
# print(item2['key4'])

# TODO: replace an item
item2["key2"]="two"
print(item2)

# TODO: iterate the keys and values in the dictionary
for i,j in item2.items():
    print("key=",i,"value=",j)
