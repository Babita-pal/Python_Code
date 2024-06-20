# 1. Write a Python program to sum all the items in a list.

# number = list(map(int,input().split()))
# sum=0
# for x in (number):
#     sum+=x
# print(sum)

# 2. Write a Python program to multiply all the items in a list.

# num=list(map(int,input().split()))
# product=1
# for i in num:
#     product*=i
# print(product)

# 3. Write a Python program to get the largest number from a list.

# num=list(map(int,input().split()))
# k=max(num)
# print(k)

# num=list(map(int,input().split()))
# m=list[0]
# for a in num:
#     if a > m:
#         m=a
# print(m)

# word=['abc', 'xyz', 'aba', '1221']
# c=0
# for a in word:
#     if len(word)>1 and word[0]==word[-1]:
#         c+=1
# print(c)

# 8. Write a Python program to check if a list is empty or not.

# num=[]
# if not num:
#     print("empty")
# else:
#     print("fill")


# 7Write a Python program to clone or copy a list.

# original_list = list(map(int,input().split()))
# new_list = list(original_list)
# print(original_list)
# print(new_list)


# 9. Write a Python function that takes two lists and returns True if they have at least one common member.

# n=list(map(int,input().split()))
# m=list(map(int,input().split()))
# result = False
# for v in n:
#     for i in m:
#         if v==i:
#             result = True
#             break
# print(result)

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

# num =list(map(int,input().split()))
# p=str(num)
# for i in p:
#     k=p.remove(0)
#     l=p.remove(4)
#     o=p.remove(5)
#     print(k,l,o)


# 12.Write a Python program to print the numbers of a specified list after removing even numbers from it.

# num = list(map(int, input().split()))
# for x in num:
#     if x%2 !=0:
#         print(x)


# FUNCTION


# 1. Write a function that inputs a number and prints the multiplication table of that number

# def nul(num):
#     for i in range(1,11):
#         print(num,"*", i,  "=", num*i)
# num=int(input())
# nul(num)


# 2. Write a Python function to multiply all the numbers in a list.

# def mul(num):
#     prod=1
#     for i in num:
#         prod*=i
#     print(prod)
# num=list(map(int,input().split()))
# mul(num)

# 3. Write a Python function to sum all the numbers in a list.

# def mul(num):
#     sum=0
#     for i in num:
#         sum+=i
#     print(sum)
# num=list(map(int,input().split()))
# mul(num)

# 4. Write a Python program to reverse a string.

# def mul(num):
#     re=''
#     index=len(num)
#     while index>0:
#         re+=num[index-1]
#         index=index-1
#     print(re)
# num=input()
# mul(num)

# number = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, number + 1):
#     factorial *= i
# print(factorial)


# 5.Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.


# def mul(num):
#     factorial=1
#     for i in range(1,num+1):
#         factorial*=i
#     print(factorial)
# num=int(input())
# mul(num)

# 6. Write a Python program to print the even numbers from a given list.

# def nul(num):
#     e=[]
#     for i in num:
#         if(i%2==0):
#             e.append(i)
#     print(e)
# num=list(map(int,input().split()))
# nul(num)

# 7.Write a Python function to check whether a number is "Perfect" or not.

# def mul(num):
#     sum=0
#     for x in range(1,num):
#         if(num%x==0):
#             sum+=x
#     print(sum==num)
# num=int(input())
# mul(num)

# n=int(input())
# sum=0
# for i in range(1,n):
#     if(n%i==0):
#         sum+=i
# if(sum==n):
#     print("true")
# else:
#     print("false")

# 10.Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included).

# def mul(num):
#     e=[]
#     for i in range(1,21):
#         e.append(i**2)
#     print(e)
# num=list(map(int(input().split())))
# mul(num)

# def mul(num):
#     e = []
#     for i in range(1, 21):
#         e.append(i **2)
#     print(e)

# num = int(input("Enter a number: "))
# mul(num)

# Exercise 1: Create a function in Python
# 1.Write a program to create a function that takes two arguments, name and age, and print their value.

# def num(nul,mum):
#     print(nul,mum)
# nul=int(input())
# mum=int(input())
# num(nul,mum)

#  Exercise 2: Return multiple values from a function
# Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both 

# def calculation(a,b):
#     print(a-b)
#     print(a+b)
# calculation(4,6)


# t=int(input())
# for i in range(t):
#     a=list(map(int,input().split()))
#     c=sum(1 for n in a if n==2)
#     if(c%8==0):
#         print("YES")
#     else:
#         print("NO")


# Bubble sort

# def sort(nums){
#     for i in range(len(nums)-1,0,-1):
#         for j in range(i):
#             if nums[j]>nums[j+1]:
#                 temp=nums[j]
#                 nums[j]=num[j+1]
#                 nums[j+1]=temp
# }
# nums=[5,3,8,7,6,2]

# x,y,h=map(int,input().split())
# k=h-y
# j=k*y
# print(j+x)

# t=int(input())
# for i in range(t):
#     N=int(input())
#     S=int(input())
#     for S in N:



# s=input()
# k=s.title()
# print(k)

# n=int(input())
# k=string(n)
# p=[]
# s=k.split()
# if s==1:
#     print(s)
# elif()

# n = int(input())
# while n >= 10:
#     k=str(n)
#     digit_sum = sum(int(digit) for digit in k)
#     n = digit_sum
# print( n)


# n=list(map(int,input().split()))
# sum=0
# for k in n:
#     if(k>0):
#         sum+=k
# print(sum)

# your_score=int(input())
# peers_score=list(map(int,input().split()))
# sum=0
# for i in peers_score:
#     sum+=i
#     k=sum/len(peers_score)
#     if(your_score>k):
#         print("congratulation")
#         break;
#     else:
#         print("Average")


# def check(year):
#     if((year%4==0 and year%100!=0) or year%400==0):
#         print("it is leap year")
#     else:
#         print("It is not leap year")

# year=int(input())
# check(year)


# weight = float(input("Enter your weight in kilograms: "))
# height = float(input("Enter your height in meters: "))

# bmi = weight / (height * height)

# if bmi < 18.5:
#     bmi_category = "Underweight"
# elif 18.5 <= bmi < 25:
#     bmi_category = "Normal weight"
# elif 25 <= bmi < 30:
#     bmi_category = "Overweight"
# else:
#     bmi_category = "Obese"

# print(f"Your BMI is {bmi:.2f}, which falls under the category of {bmi_category}.")


# def recommend_destination(preferences, budget):
#     if preferences == "beach activities" and budget == "relaxed budget":
#         return "Destinations known for beautiful beaches and affordable accommodations."
#     elif preferences == "adventure sports" and budget == "moderate budget":
#         return "Destinations famous for adventure activities like hiking, rafting, and rock climbing, with options for budget-friendly adventure tours."
#     elif preferences == "cultural experiences" and budget == "luxury budget":
#         return "Destinations rich in history, heritage, and cultural landmarks, with luxury accommodations and exclusive guided tours."
#     elif preferences == "nature retreats" and budget == "limited budget":
#         return "Destinations with serene natural landscapes, national parks, and budget-friendly eco-lodges or camping options."
#     else:
#         return "Destinations offering a mix of activities and accommodations suitable for your preferences and budget."

# preferences = input().strip()
# budget = input().strip()
# print(recommend_destination(preferences, budget))

# def function(a):
# a[0] = 'string'
# a[1] = a[1] + 1
# # The ‘a’ array give reference to the mutable list and it changes the changes that are shared
# args = ['string', 10]
# func1(args)
# print args[0], args[1]
#This prints the value stored in the array of ‘a’


# print(2**3)

# dict1 = {'first' : 'sunday', 'second' : 'monday'}
# dict2 = {1: 3, 2: 4}
# dict1.update(dict2)
# print(dict1)
# s = {1, 2, 3, 3, 2, 4, 5, 5}
# print(s)


# Test cases
# strings = ["Dermatoglyphics", "aba", "moOse"]

# # Iterate through each string
# for string in strings:
#     # Convert the string to lowercase to ignore letter case
#     string = string.lower()
    
#     # Create a set to store unique characters
#     unique_chars = set()
    
#     # Initialize a flag to track if the string is an isogram
#     is_isogram = True
    
#     # Iterate through the characters in the string
#     for char in string:
#         # Check if the character is a letter
#         if char.isalpha():
#             # Check if the character is already in the set
#             if char in unique_chars:
#                 is_isogram = False
#                 break
#             else:
#                 unique_chars.add(char)
    
#     # Output whether the string is an isogram
#     print(is_isogram)



                                                        #    *** List ***


# 1. Write a  Python program to sum all the items in a list.

t=list(map(int,input().split()))
sum=0
for i in t:
    sum+=i
print(sum)

# 2. Write a  Python program to multiply all the items in a list.
# k=list(map(int,input().split()))
# mul=1
# for i in k:
#     mul*=i
# print(mul)


# 3. Write a Python program to get the largest number from a list.
# m=list(map(int,input().split()))
# ma=m[0]
# for a in m:
#     if a>ma:
#         ma=a
# print(ma)


# 4. Write a Python program to get the smallest number from a list.
# p=list(map(int,input().split()))
# s=list[0]
# for i in p:
#     if(i<s):
#         s=i
# print(s)



