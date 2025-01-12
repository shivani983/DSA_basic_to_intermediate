class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        n = len(arr)
        low = 0
        high = n-1
        target = k
        while low <= high :
            mid = (low+high)//2
            if arr[mid] == target:
                return mid
            
            elif arr[mid] > target:
                high = mid-1
                
            elif arr[mid] < target:
                low = mid+1
            
            else:
                return -1