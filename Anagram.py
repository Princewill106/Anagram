from collections import Counter    
def Anagram(a,b):
        if(Counter(a) != Counter(b)):
            return True
        else:
            return False
a = 'silent';
b = 'listen';
Anagram(a,b)
