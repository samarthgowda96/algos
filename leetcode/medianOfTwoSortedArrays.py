class Solution:
    def findMedianSortedArrays(self,nums1,nums2):
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()
        if(len(nums1)%2==0):
            mid= len(nums1)//2
            median = (nums1[mid-1]+nums1[mid])/2
        else:
            mid= len(nums1)//2
            median= nums1[mid]
        return median

sol=Solution()
nums1=[1,3]
nums2=[2]
print(sol.findMedianSortedArrays(nums1,nums2))


