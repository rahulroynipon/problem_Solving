class Solution:
    def countCharacters(self,words,chars):
        myDict = {}
        for i in chars:
            if i in myDict:
                myDict[i]+=1
            else:
                myDict[i] = 1
        
        count = 0
        
        for word in words:
            flag = True
            myWord = {}
            for i in word:
                if i in myWord and i in myDict:
                    myWord[i]+=1
                elif i in myDict:
                    myWord[i] = 1
                else:
                    flag = False
                    break
            
            if flag:
                newFlag = True
                for i in myWord.keys():
                    if myWord[i]>myDict[i]:
                        newFlag = False
                
                if newFlag:
                    count+=len(word)
            
        return count







if __name__ == "__main__":
    x = Solution()
    print(x.countCharacters(["cat","bt","hat","tree"],"atach"))