def decoder(x, arr):
    odd = 0
    even = 0
    for i in arr:
        if i % 2 == 1:
            odd += 1
        else:
            even += 1
    
    if odd != even:
        return False
    return True
        

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        x = int(input())
        arr = list(map(int, input().split()))
        print('Yes' if decoder(x, arr) else 'No')


