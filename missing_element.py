class Solution:
    def missingNumber(self, arr):
        # Calculate the expected sum of numbers from 1 to n+1
        n = len(arr) + 1  # Total numbers should be n+1 including the missing one
        total_sum = n * (n + 1) // 2
        
        # Calculate the sum of the given array
        actual_sum = sum(arr)
        
        # The missing number is the difference between expected and actual sums
        return total_sum - actual_sum