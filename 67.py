class Solution:
    def addBinary(self, a: str, b: str) -> str:

        maxlen = max(len(a), len(b))
        a = a.zfill(maxlen)
        b = b.zfill(maxlen)
        result = ""
        carry = 0
        for i in range(-1, - maxlen - 1, -1):
            if (int(a[i]) + int(b[i]) + carry) == 0:
                result = "0" + result
                carry = 0
            elif (int(a[i]) + int(b[i]) + carry) == 1:
                result = "1" + result
                carry = 0
            elif (int(a[i]) + int(b[i]) + carry) == 2:
                result = "0" + result
                carry = 1
            elif (int(a[i]) + int(b[i]) + carry) == 3:
                result = "1" + result
                carry = 1
            
        if carry == 1:
            result = "1" + result    
        
        return result