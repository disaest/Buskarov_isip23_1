#1
# with open('27686.txt', 'r') as f:
#     n = f.read()
#     maxl = 0
#     nowl = 0
#     for i in range(len(n)):
#         if n[i] == 'X':
#             nowl += 1
#         else:
#             if nowl > maxl:
#                 maxl = nowl
#             nowl = 0
#     if nowl > maxl:
#         maxl = nowl
# print(maxl)

#2
# with open('36037.txt', 'r') as f:
#     s = f.read()
#
# maxl = 0
# nowl = 0
#
# for i in range(len(s)):
#     if i + 3 < len(s) and s[i] == 'X' and s[i+1] == 'Z' and s[i+2] == 'Z' and s[i+3] == 'Y':
#         if nowl > maxl:
#             maxl = nowl
#         nowl = 3
#     else:
#         nowl += 1
# if nowl > maxl:
#     maxl = nowl
# print(maxl)
