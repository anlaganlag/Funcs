#def editdistance(str1,str2):
    #if str1 == '':
        #return len(str2)
    #if str2 == '':
        #return len(str1)
    #if str1[0] == str2[0]:
        #return editdistance(str1[1:],str2[1:])
    #d = editdistance(str1[1:],str2)
    #u = editdistance(str1[1:],str2[1:])
    #i = editdistance(str1,str2[1:])
    #return min(d,u,i) +1
#print(editdistance('sport','sort'))
#print(editdistance('commuter','computer'))
#print(editdistance('sunday','saturday'))

import functools
class Solution:
    @functools.lru_cache(None)
    def minDistance(self, str1: str, str2: str) -> int:
        if not str1 or not str2:
            return len(str1)+len(str2)
        if str1[0] == str2[0]:
            return self.minDistance(str1[1:],str2[1:])
        d = self.minDistance(str1[1:],str2)
        u = self.minDistance(str1[1:],str2[1:])
        i = self.minDistance(str1,str2[1:])
        return min(d,u,i) +1
