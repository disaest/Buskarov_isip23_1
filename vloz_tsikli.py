# # 1
# for x in '0123456789abcde':
#     x1 = '123' + x + '5'
#     x2 = '1' + x + '233'
#     otv = int(x1, 15) + int(x2, 15)
#     if otv % 14 == 0:
#         itog = otv // 14
#         print(itog)
#         break

# #3
# for x in '0123456789':
#     x1 = x + 'B09'
#     x2 = x + '8E8'
#     otv = int(x1, 17) + int(x2, 15)
#     if otv % 155 == 0:
#         itog = otv // 155
#         print(itog)
#         break

# 4
# for x1 in '0123456789a':
#     for y1 in '0123456789a':
#         xy1 = y1 + '04' + x1 + '5'
#         for x2 in '01234567':
#             for y2 in '01234567':
#                 xy2 = '253' + str(x2) + str(y2)
#                 otv = int(xy1, 11) + int(xy2, 8)
#                 if otv % 117 == 0:
#                     itog = otv // 117
#                     itog2 = itog // 10
#                     print(itog, itog2)
#                     exit()


#5
# otv = 7 * 512**1912 + 6 * 64**1954 - 5 * 8**1991 - 4 * 8**1980 - 2022
# count = 0
# while otv > 0:
#     if otv % 8 == 7:
#         count += 1
#     otv //= 8
# print(count)
