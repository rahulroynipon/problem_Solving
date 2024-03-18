
arr = [73,67,38,33] 

ans = []

for i in arr:
    x = i%10
    y = x//5

    if y==0 and 5-x<3 and i>=38:
        i = i-x+5
        ans.append(i)
    elif y==1 and 10-x<3 and i>=38:
        i = i-x+10
        ans.append(i)
    
    else:
        ans.append(i)


print(ans)

    
    
