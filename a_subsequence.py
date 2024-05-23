class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        u = 0
        v = 0 
    
        while u < len(s) and v < len(t):
            if s[u] == t[v]:
                u += 1
                v += 1
            else:
                v += 1 

        if u == len(s):
            return True
        else: 
            False 