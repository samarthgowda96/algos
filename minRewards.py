def minRewards(score):
    rewards=[1 for i in score]
    #print(rewards)
    for i in range(1,len(score)):
        j=i-1
        if score[i]>score[j]:
            rewards[i]=rewards[j]+1
        else:
            while j>=0 and score[j]>score[j+1]:
                rewards[j]= max(rewards[j],rewards[j+1]+1)
                j-=1
    return sum(rewards),(rewards)


score=[8, 4, 2, 1, 3, 6, 7, 9, 5]

print(minRewards(score))
