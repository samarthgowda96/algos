def waterArea(heights):
    maxes=[0 for i in heights]
    leftmax=0
    for i in range(len(heights)):
        height=heights[i]
        maxes[i]=leftmax
        leftmax=max(leftmax,height)
    rightmax=0
    for i in reversed(range(len(heights))):
        height=heights[i]
        minHeight=min(rightmax,maxes[i])
        if height <minHeight:
            maxes[i]=minHeight-height
        else:
            maxes[i]=0
        rightmax=max(rightmax,height)
    return sum(maxes)


heights=[0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]

print(waterArea(heights))