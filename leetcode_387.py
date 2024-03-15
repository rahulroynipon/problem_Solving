class Solution:
    def decoder(self,s):

        myDict = {}

        n = len(s)
        for i in range(n):
            if s[i] in myDict:
                myDict[s[i]][-1]+=1
            else:
                myDict[s[i]] = [i,1]
        
        for value in myDict.values():
            if value[-1]==1:
                return value[0]
        
        return -1

if __name__ == "__main__":
    x = Solution()
    print(x.decoder("leetcode"))
        

        