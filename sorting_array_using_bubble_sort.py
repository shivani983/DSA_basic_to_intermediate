#User function Template for python3

class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr):
        # code here
        n = len(arr)
        
        for i in range(n):
            swapped = False
            
            for j in range(0,n-i-1):
                if arr[j] > arr[j+1]:
                    
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
