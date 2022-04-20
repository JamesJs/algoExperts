# Tempo: O(n) Espaço: O(1)
import math
def isPalindrome(string):
    if(len(string) % 2 == 0):
        i = int(len(string)/2)
        j = int(len(string)/2 - 1)
    else:
        i = int(math.floor(len(string)/2))
        j = int(math.floor(len(string)/2))
    while(i>=0 and j<len(string)):      
        if(string[i] != string[j]):
            return False
        i = i - 1
        j = j + 1
    return True

print(isPalindrome("abcdcba"))
