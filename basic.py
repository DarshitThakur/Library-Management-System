

# a = int(input("Enter num 1 :-"))
# b = int(input("Enter num 2 :-"))
# print("Sum :- ",a+b)

# age  = int(input("Enter your age :- "))
# if (age >= 18):
#     print("Eligible for voting ")
# else :
#     print("Not eligible ")

# num = int(input("Enter any number :- "))
# if (num == 0 ):
#     print("Number is Zero")
# elif (num>0):
#     print("Number is postive ")
# else :
#     print("Number is Negative ")

# num1 = int(input("Enter any number 1 :- "))
# num2 = int(input("Enter any number 2 :- "))
# num3 = int(input("Enter any number 3 :- "))

# if (num1>num2>num3):
#     print(num1,"is largest")
# elif (num1<num2>num3):
#     print(num2,"is largest")
# else :
#     print(num3,"is largest")

# year = int(input("Enter Year : - "))
# if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
#     print("Year is Leap Year ", year)
# else: 
#     print("Year is not leap year")

# for i in range (21):
#     if (i % 2 == 0):
#         print(i)

# num = int(input("Enter any number :- "))
# for i in range (1,num+1):
#     if (i % 2 == 0):
#         print(i,end =" ")

#count down timer from 10 to 1 
# count = int(input("Enter timer to start"))
# while(count>0):
#     print(count,end = " ")
#     count -=  1

# num = 5
# fact = 1 

# for i in  range (num,1,-1):
#     fact = fact*i
# print(fact)

# password  = "ish"
# user = ""
# for a in range (3,0,-1):
#     while password != user:
#         print("Attempts remaining ", a )
#         user  = input("Enter your pass:-")
#         if (password != user):
#             print("pravesh nishidh")
#             break
#         else :
#             print("swagat he chooti master ")
        

# a = float(input("Enter 1st num:- "))
# b = float(input("Enter 2nd num:- "))

# def add(a,b):
#     print(a+b)

# def sub(a,b):
#     print(a-b)

# def mul(a,b):
#     print(a*b)

# def div(a,b):
#     print(a/b)

# add(a,b)
# sub(a,b)
# mul(a,b)
# div(a,b)

# for i in range(2,51):
#         for j in range(2,i):
#             if(i%j == 0):
#                 break
#         else :
#                 print(i , end=" ")

# list1 = [1,2,3,"Darshit","Darshit"]
# list2.extend([77,77,89,55,69])
# list2.append(99)
# list2.insert(2,45)
# list2.remove(2)
# list2.pop()
# print(list2)
# print("Length=",len(list2))
# print("Sum=",sum(list2))
# print("Max=",max(list2))
# print("Min=", min(list2))
# list4 = [1,2,3,9,8,2,9,9]
# list4.sort()
# print(list4)
# print("2nd largest=",list2[-2])
# print("Reversed=",list2.reverse())
# print("count=",list2.count(77))

# list2 = [1,2,3,9,8,2,9,9]
# list3 = []
# for i in list2:
#     if (list2.count(i) >= 2 ):
#         list3.append(i)
#     else:
#         continue
# list3.sort()
# print(list3)

# l = [89,45,21,45]
# t = (78,45,63,15)
# print(l.__sizeof__)
# tup = (2,3,4,5,6,7,8,9,0,1)
# tup2 = (3,3,4,5,9,6,6)
# tup = sorted(tup)
# print(tup)

#H.W duplicate in tup 

# set = {1,2,34,89,112,112,}
# set.add(5)
# set.discard(54)
# set.remove(89)
# set.pop()
# # set.clear()
# print(set)

# s = {1,2,3,4,5,6,7}
# n = int(input("Enter the number :- ") )
# for  i in s: 
#     if ( n == i):
#         print("IS present")
#     else :
#         print("not present")

# s1 = {10,20,30,40}
# s2 = {20,30} 

# print(s1.intersection(s2))
# for i in s1:
#     for j in s2:
#         if ( i == j):
#             print (i)

#print(s2.issubset(s1))

dict = {
    "City": "Mumbai",
    "Country":"India",
    "Popluation" : 656556,
    "Population" : 5613245
}
# print(dict.pop("City"))
# print(dict.popitem())
print(dict.keys())
print(dict.values())
d = input("Enter the key : - ")
for d in dict:
    if (d == dict):
        print("present")
else :
        print("not present")