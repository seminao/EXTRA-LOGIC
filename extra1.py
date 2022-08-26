# compering all the element and taking out the max value
# values = [[3, 4, 5, 1], [33, 6, 1, 2],[4,87,56,2]]
# v = values[0][0]
# for row in range(0, len(values)):
#     for column in range(0, len(values[row])):
#         if v < values[row][column]:
#             v = values[row][column]
# print(v)

# compering all the element and taking out the min value
# values = [[3, 4, 5, 1], [33, 6, 1, 2]]
# v = values[0][0]
# for i in values:
#     for j in i:
#         if v > j:
#             v = j
#             print(v)

# l=[[3, 4, 5, 1],[33, 6, 1, 2]]
# v=l[0][0]
# i=0
# # max=0
# while i<len(l):
#     j=0
#     while j<len(l):
#         if v>l[i][j]:
#             v=l[i][j]
#         j=j+1
#     i=i+1
# print(v)

# arr = list(map(int, input().strip().split()))
# a=[1,3,5,7,9]
# i=0
# max=a[1:]
# min=a[:-1]
# s=0
# s1=0
# while i<len(max) or i<len(min):
#     s=s+max[i]
#     s1=s1+min[i]
#     i=i+1
# print(s,s1)
# a=[1,3,5,9,7,9]
# i=0
# max=0
# e=[]
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     i=i+1
# j=0
# c=0
# while j<len(a):
#     if a[j]==max:
#         c=c+1
#     j=j+1
# print(c)

# a=["maanpreet","bobby","canan"]
# i=0
# user=int(input("enter your choice: "))
# while i<len(a):
#     if user==i:
#         print(a[i])
#     i=i+1

# bubble short
# a=[31,50,21,47,18,90,78,0,10]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a)-1:
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
#         j=j+1
#     i=i+1
# print(a)


# simple to nested
# list=[2,4,6,8,10,11,8,9]
# a=[]
# i=0
# while i<len(list):
#     k=[list[i],list[i+1]]
#     a.append(k)
#     i+=2
# print(a)


# list=[2,4,6,8,10,11,8,9]
# a=[]
# i=0
# while i<len(list):
#     k=[list[i],list[i+1]]
#     a.append(k)
#     i+=2
# print(a)

# **sum of consecutive number
# l=[1,2,3,4]
# i=0
# s=0
# a=[]
# while i<len(l)-1:
#     s=l[i]+l[i+1]
#     a.append(s)
#     i=i+1
# print(a)


# a=[1,2,[3,4],5,6]
# e=[]
# i=0
# s=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             s=s+a[i][j]
#             j+=1
#     else:
#         s+=a[i]
#     i+=1
# print(s)