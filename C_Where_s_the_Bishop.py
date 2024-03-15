import math

def decoder(n, arr):
    fLoc = None
    lLoc = None
    for i in range(n):
        count = 0
        fLoc = None
        lLoc = None
        for j in range(n):
            if arr[i][j] == '#':
                if fLoc is None:
                    fLoc = [i, j]
                else:
                    lLoc = [i, j]
                count += 1

        if count == 2:
            break
    
    role = lLoc[-1] - fLoc[-1]
    role = math.ceil(role / 2) + 1

    return [fLoc[0] + role, fLoc[-1] + role]

if __name__ == "__main__":
    t = int(input()) 

    for _ in range(t):
        input()
        arr = []
        for _ in range(8):
            x = input()
            arr.append(x)
        result = decoder(8, arr)
        print(*result)
