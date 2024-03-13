def decoder(n,arr):
    small = min(arr)
    count = 0

    for i in arr:
        count += (i-small)
    
    return count
    


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        print(decoder(n,arr))