def decoder(n,arr):
    
   return len(set(arr))
    


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr  = list(map(int,input().split()))
        print(decoder(n,arr))