class Solution:
    def find(self, arr, x):
        # Returns the first and last occurrence of x in arr
        first_index = self.first(arr, x)
        last_index = self.last(arr, x)
        return [first_index, last_index]
    
    def first(self, arr, x):
        low, high = 0, len(arr) - 1
        result = -1  # Default to -1 if x is not found
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                result = mid
                high = mid - 1  # Continue searching on the left
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return result

    def last(self, arr, x):
        low, high = 0, len(arr) - 1
        result = -1  # Default to -1 if x is not found
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                result = mid
                low = mid + 1  # Continue searching on the right
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return result