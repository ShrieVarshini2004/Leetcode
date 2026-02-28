class Solution:
    def areIsomorphic(self, s1, s2):
        # code here 
        mapST = {}
        mapTS = {}
    
        for c1, c2 in zip(s1, s2):
    
            if c1 in mapST and mapST[c1] != c2:
                return False
    
            if c2 in mapTS and mapTS[c2] != c1:
                return False
    
            mapST[c1] = c2
            mapTS[c2] = c1
    
        return True