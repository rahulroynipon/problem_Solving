def decoder(n):
    x = n%3
    n = n//3
    
    if x==0:
        a = b = n
    elif x==1:
        a = n+1
        b = n
    elif x==2:
        a = n
        b = n+1

    return [a,b]


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(*decoder(n))