# a=[[4,2,1],[3,2,6],[9,8]]
# i=0
# e=[]
# while i<len(a):
#     j=-1
#     while j<len(a[i])-1:
#         e.append(a[i][j])
#         j=j-1
#         break
#     i=i+1
# print(e)

# a={'a':1,'b':2,'c':3}
# b=a.values()
# c=a.keys()
# d=list(b)
# f=list(c)
# e=[]
# i=0
# while i<len(b):
#     n=[f[i],d[i]]
#     e.append(n)
#     i=i+1
# print(e)

# user=int(input("enter the number"))
# a=user%10
# i=0
# while i<a:
#     if a%2==0:
#         print(a,"even")
#         break
#     elif a!=0:
#         print(a,"odd")
#         break
#     i=i+1


# num=input("enter no.:-")
# len=len(num)
# num1=int(num)
# l=[]
# i=0
# place=1
# while(i<len):
#     num2=num1%10
#     expand=num2*place
#     num1=num1//10
#     place*=10
#     if expand>0:
#         l.append(expand)
#     i+=1
# l.reverse()
# k=l
# j=0
# while j<len(k):
#     n=l[k]
#     j+=1
# print("'",n,"'")
    

# a=[[0],[4,7,9,45],[4,76],[45,67,5,8,9,2]]
# i=0
# max=0
# while i<len(a):
#     j=0
#     c=0
#     while j<len(a[i]):
#         c=c+1
#         if c>max:
#             max=c
#             n=a[i]
#         j=j+1
#     i=i+1
# print(max,n)

# l=[2,3,5,6,4,8,7,9,12]
# i=0
# a=[]
# while i<len(l)-1:
#     n=l[i]-l[i+1]
#     a.append(n)
#     i=i+1
# print(a)

# num=input("enter no.:-")
# len=len(num)
# num1=int(num)
# l=[]
# i=0
# place=1
# while(i<len):
#     num2=num1%10
#     expand=num2*place
#     num1=num1//10
#     place*=10
#     l.append(str(expand))
#     i+=1
# l.reverse()
# p="+".join(l)
# print(p)

#  o/p-[[1,"red"],[2,"green"],[3,"black"],[4,"white"],[5,"black"]]
# l=[1,"red",2,"green",3,"black",4,"white",5,"black"]
# a=len(l)
# i=1
# e=[]
# while i<len(l):
#     k=l[-i],l[-i-1]
#     e.append(list(k))
#     i=i+2
# print(e)

# i=10
# while i<=10:
#     if i%2==0 and i>=2:
#         print(i)
#     i=i-1
    
# a={'a':1,'b':2,'c':3}
# l=[]
# for i in a:
#     if i in a:
#         b=[]
#         b.append(i)
#         b.append(a[i])
#     l.append(b)
# print(l)


# a=[[4,2,1],[3,2,6],[9,8]]
# e=[]
# for i in a:
#     for j in i:
#         k=j.reverse()
#         e.append(k)
#         break
# print(e)

# l=[2,4,4,1,5,6,7]
# l1=[8,9,9,10]
# i=0
# a=[]
# while i<len(l):
#     c=l+l1
#     j=0
#     while j<len(c):
#         if c[j] not in a:
#             a.append(c[j])
#         j=j+1
#     i=i+1
# a.sort()
# print(a) 

# a=["0:5", "0:6", "2:6","0:1","5:8","7:8"]
# i=0
# k=[]
# e=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if a[i][j] in a[i] :
#             k.append(a[i][j])
#             e.append(a[i][j+2])
#             break
#         j=j+1
#     i=i+1
# s=k
# t=e
# c=0
# w=0
# x=0
# y=0
# while c<len(s):
#     if s[c]>t[c]:
#         w=w+3
#     if s[c]<t[c]:
#         x=0
#     if s[c]==t[c]:
#         y=y+1
#     c=c+1
# print(w,x,y)

# requesting something to the server
# to get information
# protocal is just like a rule
# package,
# to get the data,post add any data,put by using we can chane something in data

# n=5
# i=0
# h=50
# x=h
# c=x
# a=[]
# while i<=n:
#     c=x*i
#     a.append(c)
#     i=i+1
# print(a) 

# i=9
# while  True:
#     if i%3==0:
#         break
#     print("divisible")

# i=9
# while  True:
#     if i%3==0:
#         pass
#     print("divisible")
# l="kivi"
# print(l[3])

# a={}
# u=int(input("enter the number"))
# i=0
# while i<3:
#     name=input("enter the name")
#     # r_n=input("enter the real name")
#     d=input("enter the details")
#     eye=input("enter the eye color")
#     height=input("enter the age")
#     hair=input("enter the hair color")
#     # a={}
#     a["name"]=name
#     a["details"]=
#     a["eye color"]=eye
#     a["height"]=height
#     a["hair color"]=hair
#     # u=u+1
#     i+=1
# print(a)



# l=[[1,200,3,4],[5,6,7,8],[9,10,11,12]]
# i=0
# max=0
# a=[]
# while i<len(l):
#     j=0
#     while j<len(l[i]):
#         if l[i][j]>max:
#             max=l[i][j]
#         j=j+1
#     a.append(max)
#     k=0
#     while k<len(a):
#         if a[k]>max:
#             max=a[k]
#         k=k+1
#     i=i+1
# print(max)
# l=[1,3,4,5,7,8,9,10,15,16,20]
# i=0
# a=[]
# while i<l[-1]:
#     n=i+1
#     if n not in l:
#         a.append(n)
#     i=i+1
# print(a)

# o/p=[[2,1],2,3,[2,4],5,1]
# a=[1,1,1,2,3,4,4,5,1]


# l=[4,2,5,6,7,89,3,56,32,12,45]
# i=0
# a=[]
# while i<len(l):
#     j=0
#     c=0
#     while j<len(l):
#         if l[j]>l[i]:
#             c=c+1
#         j=j+1
#     i=i+1
#     a.append(c)
# print(a)


# u=int(input("enter the number"))
# u1=int(input("enter the number"))
# i=0
# b="0"
# while i<u1:
#     print(str(u)+b*i)
#     i=i+1