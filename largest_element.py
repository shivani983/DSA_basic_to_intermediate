from typing import List


class Solution:
    def largest(self, arr):
        # code here
        largest_element = 0
        n = len(arr)
        for i in range(n):
            if arr[i] > largest_element:
                largest_element = arr[i]
                
        return largest_element