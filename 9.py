class Solution:
    def isPalindrome(self, x: int) -> bool:
        newstr = ""
        for i in range(len(str(x)) - 1, -1 , -1):
            newstr += str(x)[i]
        if newstr == str(x):
            return True
        else:
            return False