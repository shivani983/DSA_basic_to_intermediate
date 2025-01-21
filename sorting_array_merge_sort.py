class Solution:
    def mergeSort(self, arr, l, r):
        if l < r:
            mid = (l + r) // 2
            # Recursively sort the first and second halves
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid + 1, r)
            # Merge the sorted halves
            self.merge(arr, l, mid, r)

    def merge(self, arr, l, mid, r):
        # Create temporary arrays for left and right halves
        left_half = arr[l:mid + 1]
        right_half = arr[mid + 1:r + 1]
        
        i = j = 0
        k = l

        # Merge the two halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy any remaining elements of left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy any remaining elements of right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
