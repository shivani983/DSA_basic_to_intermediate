class Solution:
    # Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, k):
        revert_groups = []
        n = len(arr)
        for i in range(0,n,k):
            arr[i:i+k] = reversed(arr[i:i+k])
            
        return arr    