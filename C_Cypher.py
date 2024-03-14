def decoder(current,n,move):

    ans = []
    arr = [0,1,2,3,4,5,6,7,8,9]

    for index,item in enumerate(move):
        up = item[-1].count('U')
        down = item[0] - up
        
        role = down-up

        
        position = current[index]+role
        position = position%10
        ans.append(arr[position])
       
            
       
        
    return ans




if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        current = list(map(int,input().split()))
        move = []
        for _ in range(n):
            x,y = list(input().split())
            move.append([int(x),y])
        
        print(*decoder(current,n,move))