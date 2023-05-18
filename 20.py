class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:  
            if char == "(":
                stack.append(")")
            elif char == "{":
                stack.append("}")
            elif char == "[":
                stack.append("]")
            elif not stack:             #checks if stack is NOT empty
                return False
            else:
                pop = stack.pop()   #removes from array AND stores in variable
                if pop != char:
                    return False
            
        if stack:       #checks if stack is empty
            return False
        else:
            return True