def canVisitAllRooms(rooms):
    seen = [False]*len(rooms)
    seen[0]=True
    stack=[0]

    while stack:
        ele= stack.pop()
        for i in rooms[ele]:
            if not seen[i]:
                seen[i]=True
                stack.append(i)

    return all(seen)


rooms=[[1],[2],[3],[]]
print(canVisitAllRooms(rooms))