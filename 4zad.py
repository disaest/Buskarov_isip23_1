#1
# import csv
#
# with open("36031.csv", "r") as f:
#     n = list(csv.reader(f))
#     l = []
#     for i in range(len(n)-1):
#         a = (n[i][0].split(';'))
#         a = [int(el) for el in a]
#         l.append(a)
#     print(l)
#     print(l[0][-1::-1])
#
# for i in range(len(l)-1, -1):
#     l = l[i][-1::-1]
#
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         if i == 0 and j == 0:
#             continue
#         elif j == 0:
#             l[i][j] = l[i-1][j] + l[i][j]
#         elif i == 0:
#             l[i][j] = l[i][j - 1] + l[i][j]
#         else:
#             if l[i][j-1] >= l[i-1][j]:
#                 l[i][j] = l[i][j-1] + l[i][j]
#             else:
#                 l[i][j] = l[i-1][j] + l[i][j]
# print(l[-1][-1])

#2
# import csv
#
# with open("59778.csv", "r") as f:
#     n = list(csv.reader(f))
#     l = []
#     for i in range(len(n)):
#         a = (n[i][0].split(';'))
#         a = [int(el) for el in a]
#         l.append(a)
#     a = l[:16]
#     count = 0
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             if a[i].count(a[i][j]) == 4:
#                 repeat = a[i][j]
#                 x = []
#                 for j in range(len(a[i])):
#                     if a[i][j] not in x and a[i][j] != repeat:
#                         x.append(a[i][j])
#                 summa_repeat = 4 * repeat
#                 average_sum = sum(x) / 3
#                 if average_sum > summa_repeat:
#                   count += 1
#     print(count//4)

#3
# import csv
#
# with open("29666.csv", "r") as f:
#     n = list(csv.reader(f))
#     l = []
#     for i in range(len(n)-1):
#         l.append(a)
#
#
#     print(float(str(l[0][0])+"."+str(l[1][0])))