# import math

# def is_triangular_number(num):
#     return math.isqrt(8 * num + 1) ** 2 == 8 * num + 1

# # Example usage:
# num = int(input())
# if is_triangular_number(num):
#     print("YES")
# else:
#     print("NO")
# def max_dominoes(M, N):

#     total_squares = M * N

#     max_dominoes = total_squares // 2
    
#     return max_dominoes


# M, N = map(int, input().split())

# print(max_dominoes(M, N))


# def is_dangerous(s):

#     for i in range(len(s) - 6):
#         if s[i:i+7] == '0000000' or s[i:i+7] == '1111111':
#             return "YES"
#     return "NO"


# s = input()


# print(is_dangerous(s))


# def can_construct_haiku(A, B, C):

#     total_syllables = A + B + C
#     if total_syllables == 17:
#         return "YES"
#     else:
#         return "NO"


# A, B, C = map(int, input().split())


# print(can_construct_haiku(A, B, C))


# t = int(input())
# target = "Timur"
# target_sorted = ''.join(sorted(target))

# for _ in range(t):
#     n = int(input())
#     s = input().strip()
#     s_sorted = ''.join(sorted(s))
#     if s_sorted == target_sorted:
#         print("YES")
#     else:
#         print("NO")


# # Input
# num1 = input()
# num2 = input()

# # Calculate the answer
# answer = ''.join(['1' if num1[i] != num2[i] else '0' for i in range(len(num1))])

# # Output
# print(answer)
# Input
# Input
# Function to calculate the minimum number of operations needed for a single test case
# Input
# n = int(input())
# d = list(map(int, input().split()))
# a, b = map(int, input().split())

# # Calculate the total number of years needed
# total_years = sum(d[a-1:b-1])

# # Output the result
# print(total_years)


# Input
# r, g, b = map(int, input().split())

# # Calculate the minimal time
# min_time = max((r - 1) // 2, 0) * 3 + 30  # Calculate the time for red cablecars
# min_time = max(min_time, (g - 1) // 2 * 3 + 31)  # Calculate the time for green cablecars
# min_time = max(min_time, (b - 1) // 2 * 3 + 32)  # Calculate the time for blue cablecars

# # Output
# print(min_time)

# Input
# Input
# Input
# Input
# Input
# Input

def reflection(n):
    return int(str(n).translate(str.maketrans('0123456789', '9876543210')))

def max_weight(l, r):
    max_weight = 0
    for n in range(l, r + 1):
        weight = n * reflection(n)
        max_weight = max(max_weight, weight)
    return max_weight


l, r = map(int, input().split())


print(max_weight(l, r))