class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        prev = ord(s[0])
        for i in range(1,len(s)):
            next = ord(s[i])
            total += abs(prev-next)
            prev = next
        
        return total
