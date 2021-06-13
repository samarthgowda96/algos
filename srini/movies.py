def watchMovies(d,mov):
    res=[]
    for i in range(len(mov)):
        for j in range(i+1,len(mov)):
            if (mov[i]+mov[j])<= d:
                res.append(mov[i]+mov[j])
    print(res)
    return max(res)

d= 250
mov= [90, 85, 75, 60, 120, 150, 125]
print(watchMovies(d,mov))