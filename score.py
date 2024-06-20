def decoder(n, x):
    score_track = []
    
    for i in range(len(x)):
        tLen = len(score_track)
        if x[i] == "+":
            # Add the sum of the last two scores
            z = score_track[tLen-2] + score_track[tLen-1]
            score_track.append(z)
        elif x[i] == "D":
            # Add double the last score
            z = score_track[tLen-1] * 2
            score_track.append(z)
        elif x[i] == "C":
            # Remove the last score
            score_track.pop()
        else:
            # Convert the string to integer and add to the score list
            z = int(x[i])
            score_track.append(z)
    
    print(score_track)
    
    return sum(score_track)

if __name__ == "__main__":
    n = int(input())
    x = input().split()
    print(decoder(n, x))
