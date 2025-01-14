class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        set_a = set(a)
        set_b = set(b)
                
        return set_b.issubset(set_a)        
        