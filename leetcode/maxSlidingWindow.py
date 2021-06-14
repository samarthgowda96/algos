from collections import deque
def maxSlidingWindow(nums,k):

    if not nums:
        return []
    if k==0:
        return nums
    
    deq=deque()
    result=[]
    for i in range(k):
        while deq:
            if nums[i]> nums[deq[-1]]:
                deq.pop()
            else:
                break
        deq.append(i)
    for i in range(k,len(nums)):
        result.append(nums[deq[0]])
        if deq[0] < i- k + 1:
                deq.popleft()
        while deq:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break
        deq.append(i)
    result.append(nums[deq[0]])
    return result


nums=[1,3,-1,-3,5,3,6,7]
k=3
print(maxSlidingWindow(nums,k))