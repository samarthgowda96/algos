def groupAna(words):
    book={}
    for i in words:
       sortedWord= "".join(sorted(i))
       if sortedWord not in book:
            book[sortedWord]=[i]
       else:
            book[sortedWord].append(i)
    res=[]
    for i in book.values():
        res.append(i)
    return res
  
words=["eat", 'tea', 'tan']
print(groupAna(words))
