def solve(s):
    ans = ""
    digit = [str(i) for i in range(10)] + [chr(i) for i in range(97,123)]

    for i in digit:
        if i not in s:
            ans+=i
    
    return ans



if __name__ == "__main__":
    print(solve("rahulnipon"))