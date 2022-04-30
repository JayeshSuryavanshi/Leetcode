class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: 
            return '0'
        map = '0123456789abcdef'
        final = ''
        if num<0: 
            num = num + 2 ** 32
        while num > 0:
            digit = num % 16
            num = (num-digit) // 16
            final = final + str(map[digit])
        return final[::-1]
            
            
        
        
            