class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        if s == "":
            return 0
        
        if s.count(" ") == 0:
            return len(s)

        counter = 0
        for i in range(-1, - len(s) - 1, - 1):
            if s[i] == " " and counter > 0:
                return counter
            elif s[i] != " ":
                counter += 1
            if s[i] != " " and i == -len(s):
                return counter