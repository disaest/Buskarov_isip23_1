# #1
# el = [0, 1]
# n = int(input())
# for i in range(n - 2):
#     new_el = el[0] + el[1]
#     el[0] = el[1]
#     el[1] = new_el
#     print(new_el)

#2
# n = int(input())
# el = [1, 2, 4]
# for i in range(n - 3):
#     new_el = el[0] + el[1] + el[2]
#     el[0] = el[1]
#     el[1] = el[2]
#     el[2] = new_el
# print(el[2])


#3
# N = [
#     [0, 1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0, 1],
#     [0, 40, 70, 0, 0, 1],
#     [100, 0, 0, 0, 0, 1]
# ]
#
# for i in range(len(N)):
#     for j in range(len(N[i])):
#         if i == 0 and j == 0:
#             continue
#         elif j == 0:
#             N[i][j] = N[i-1][j] + N[i][j]
#         elif i == 0:
#             N[i][j] = N[i][j - 1] + N[i][j]
#         else:
#             if N[i][j-1] >= N[i-1][j]:
#                 N[i][j] = N[i][j-1] + N[i][j]
#             else:
#                 N[i][j] = N[i-1][j] + N[i][j]
# print(N[-1][-1])