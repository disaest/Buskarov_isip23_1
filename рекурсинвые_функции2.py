#1 
# def ispolnitel(a = 3,b = 12, ten = False):
#     if a > b:
#         return 0
#     if a == b:
#         return 1 if ten else 0
        
#     now_ten = ten or (a == 10)
#     way1 = ispolnitel(a + 1, b, now_ten)
#     way2 = ispolnitel(a + 2, b, now_ten)
#     way3 = ispolnitel(a * 2, b, now_ten)
#     ways = way1 + way2 + way3
#     return ways
# print(ispolnitel())
    
#2 
# def ispolnitel(a = 1,b = 27, twosix = False):
#     if a > b:
#         return 0
#     if a == b:
#         return 1 if not twosix else 0
        
#     now_twosix = twosix or (a == 26)
#     way1 = ispolnitel(a + 1, b, now_twosix)
#     way2 = ispolnitel((a * 2 + 1), b, now_twosix)
#     ways = way1 + way2
#     return ways
# print(ispolnitel())

#3
# def ispolnitel(a = 2,b = 18, fourten = False, nine = False):
#     if a > b:
#         return 0
#     if a == b:
#         return 1 if nine and not fourten else 0
        
#     now_fourten = fourten or (a == 14)
#     now_nine = nine or (a == 9)
#     way1 = ispolnitel(a + 1, b, now_fourten, now_nine)
#     way2 = ispolnitel(a + 2, b, now_fourten, now_nine)
#     ways = way1 + way2
#     return ways
# print(ispolnitel())