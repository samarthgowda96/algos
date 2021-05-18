class Solution(object):
    def searchRange(self,nums,target):
        left= 0
        right= len(nums)-1
        start=-1
        end=-1
        while left<=right:
            mid= (left+right)//2
            if nums[mid]< target:
                left= mid+1
            elif nums[mid]>target:
                right= mid-1
            else:
                start= mid
                end=mid
                while start > left:
                    leftmid= (start+left)//2
                    if nums[leftmid]<target:
                        left= leftmid+1
                    else:
                        start=leftmid
                while end+1<=right:
                    rightmid=(right+end+1)//2
                    if nums[rightmid]>target:
                        right= rightmid-1
                    else:
                        end=rightmid
                return [start, end]
        return [start, end]


s= Solution()
nums=[2,3,4,6,6,9]
target=6
print(s.searchRange(nums,target))