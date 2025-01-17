class Solution:
  def total_ones(arr):
    counts = 0
    for i in range(len(arr)):
      if arr[i]==1:
        counts +=1

      else:
        pass
    return counts 


arr = [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]  
total_ones(arr)     
