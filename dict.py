# rite a Python program to combine values in python list of dictionaries. 
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: {'item1': 1150, 'item2': 300}

# d=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# e={}
# f={}
# s=0
# i=0
# while i<len(d)-1:
#     if d[i]=="item1":
#         s=s+d[i]["amount"]
#     else:
#         e["item2"]=d[i]["amount"]
#     i=i+1
# e["item1"]=s
# print(e)
# for i in d:
#     f=d[0]["amount"]+d[2]["amount"]
#     e["item1"]=f
#     e["item2"]=d[1]["amount"]
# print(e)

# o/p=[4.8, 5.8, 6.8, 8.0, 11.0]
# l=[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
# i=0
# a=[]
# b=[]
# max=0
# avg=0
# while i<len(l):
#     j=0
#     c=0
#     while j<len(l[i]):
#         c=c+1
#         if c>max:
#             max=c
#         j=j+1
    # k=0
    # s=0
    # while k<(max):
    #     s=s+l[i][j] 
    #     a.append(s)
    # k=k+1
    
    # avg=s/len(a)
#     i=i+1
# print(max)
# [[11,19], [12,18],[13,17]]
# n = [10, 11, 12, 13, 14, 17, 18, 19]
# i=0
# a=[]
# while i<len(n):
#     j=0
#     while j<len(n):
#         if n[i]+n[j]==30  and n[i]<n[j]:
#             c= n[i],n[j]
#             a.append(list(c))
#         j=j+1
#     i=i+1
# print(a)

# n = [[10, 11,8], [12,8, 13], [14, 9,17], [18,4, 19]]
# i=0
# a=[]
# while i<len(n):
#     j=0
#     s=0
#     l=len(n[i])
#     while j<len(n):
#         s=s+n[j-l][i-l]
#         j=j+1
#     a.append(s)
#     i=i+1
# print(a[:len(n[0])])

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

# a=list(map(int,input().split()))
# i=0
# e=[]
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[i]+a[j]==14 and a[i]<a[j]:
#             c=a[i],a[j]
#             e.append(list(c))
#         j=j+1
#     i=i+1
# print(e)

# s=input()
# x=eval(s)

# 89 90 78 93 80
# 90 91 85 88 86
# 91 92 83 89 90.5

# N,X=map(int,input().split())
# i=1
# e={}
# while i<=X:
#     a=list(map(str,input().split()))
#     e[i]=a
#     i=i+1
# j,k,l=e.values()
# m=0
# c=0
# avg=0
# while m<len(j):
#     s=0
#     s=s+float(j[m])+float(k[m])+float(l[m])
#     m=m+1
#     avg=s/3
#     print(avg)

# l=[-9,-7,-345,-456]
# max=l[0]
# i=0
# while i<len(l):
#     if l[i]>max:
#         max=l[i]
#     i=i+1
# print(max)

# u=int(input("enter the number"))
# i=0
# max=0
# min=1000
# while i<=u:
#     u2=int(input("enetr the number"))
#     if u2>max:
#         max=u2
#     elif u2<min:
#         min=u2
#     i=i+1
# print(min)

# u=int(input("enter the number"))
# i=0
# max=-1000
# min=0
# while i<=u:
#     u2=int(input("enetr the number"))
#     if u2>max:
#         max=u2
#     elif u2<min:
#         min=u2
#     i=i+1
# print(max,min)

# Sample Input 0
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# Sample Output 0

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]
# l=int(input())
# i=0
# a=[]
# while i<(l):
#     l1=input().split()
#     if  l1[0]=="print":
#         print(a)
#     if l1[0]=="append":
#         a.append(int(l1[1]))
#     if l1[0]=="insert":
#         a.insert(int(l1[1]),int(l1[2]))
#     if l1[0]=="remove":
#         a.remove(int(l1[1]))
#     if l1[0]=="sort":
#         a.sort()
#     if l1[0]=="pop":
#         a.pop()
#     if l1[0]=="reverse":
#         a.reverse()
#     i=i+1

# list=[
#      [8,3,4],
#      [1,5,9],
#      [6,7,2]
#      ]
# i=0 
# a=0
# b=0
# c=0
# d=0
# e=0
# f=0
# g=0
# h=0
# while i<len(list):
#      a=a+list[0][i]
#      b=b+list[1][i]
#      c=c+list[2][i]
#      d=d+list[i][0]
#      e=e+list[i][1]
#      f=f+list[i][2]
#      g=g+list[i][i]
#      h=h+list[i][2-i]
#      i=i+1
# if a==b==c==d==e==f==g==h:
#      print("Magic Square")
# else:
#      print("Not Magic Squa")


l=[[0, 1, 2], [2, 3, 4], [3, 4, 5]]
i=0
n=3
a=[]
while i<len(l):
    j=0
    while j<len(l):
        if i+j==n-1:
            a.append(l[i][j])
        j=j+1
    i=i+1
print(a)