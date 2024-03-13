
def decoder(n,arr):
    count = 0
    i = 1
    while i<n-1:
        if (n-1-i>=6 and arr[i] =='m' and arr[i+1]=='a' and arr[i+2]=='p' and arr[i+3] =='p' and arr[i+4]=='i' and arr[i+5]=='e'):
            count+=1
            i+=5
        elif arr[i-1] =='m' and arr[i]=='a' and arr[i+1]=='p' :
            count+=1
            i+=2
        elif arr[i-1] =='p' and arr[i]=='i' and arr[i+1]=='e' :
            count+=1
            i+=1

        i+=1
    
    print(count)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        x = input()
        decoder(n,x)



        #mapie and mapiemapie