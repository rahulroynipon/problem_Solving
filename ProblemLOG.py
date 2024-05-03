def solved(n,s):
    myDict = dict()
    for i in s:
        if i in myDict:
            myDict[i] += 1
        else:
            myDict[i] = 1
    
    solve = 0

    for key,value in myDict.items():
        if (ord(key)-64)<=value:
            solve+=1
            
    return solve
  



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        print(solved(n,s))