class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        low = 0
        high = len(arr)-1
        target = k
        result = -1
        while low <= high :
            mid = (low+high)//2
            
            if arr[mid] == target:
                result =  mid
                high = mid-1
            
            elif arr[mid] > target:
                high = mid-1
                
            else:
                low = mid+1
        
                   
        return result