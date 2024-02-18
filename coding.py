# list, dict, string
'''reverse'''

# s = "abcde"
# for i in range(1, 6):
#     print(s[-i],end="")

# n = -1
# while n >= -len(s):  # -6 >= -5
#     print(s[n],end="")  # e
#     n -= 1




'''prime number'''

# def check_prime(num): # 7
#     flag = None
#     for i in range(2, num//2+1):   # 4
#         if num % i == 0:  # 15 % 3 == 0
#             flag = True
#             break
#         else:
#             flag = False
#     return flag

# if check_prime(7):
#     print("Non-prime")
# else:
#     print("Prime")



# def get_prime_numbers(start, end):
#     prime_lst = []
#     for num in range(start, end+1): # 8  40
#         flag= None
#         for j in range(2, num//2+1): # 5
#             if num % j == 0:
#                 flag = True
#                 break
#             else:
#                 flag = False
#         if not flag:
#             prime_lst.append(num)
#     print(prime_lst)

# get_prime_numbers(1, 40)

'''Fibonacci series'''

# 0 1 1 2 3 5 8 13 21 34

# def fib_series(num):
#     fib_list = [] # 0, 1 1 2
#     a = 0
#     b = 1
#     for _ in range(num): # 0
#         fib_list.append(a)  # a = 2  b = 3
#         a, b = b, a + b
#     return fib_list

# print(fib_series(5))


# def fib_series_while(num):
#     fib_list = [0, 1] # [0, 1, 1, 2, 3]
#     while num > len(fib_list):   # 6 >= 4 
#         value = fib_list[-1] + fib_list[-2]  # 3
#         fib_list.append(value)
#     return fib_list

# print(fib_series_while(5))

'''Palindrom'''
# s = "madam"  # 2   2 5
# def check_palindrome():
#     for i in range(0, len(s)//2):     # 3 
#         if s[i] != s[len(s)-1-i]: # d != d 5-1 4
#             return False
#     return True

# if check_palindrome():
#     print("Palindrome")
# else:
#     print("Not Palindrome")

'''Check given string is balanced or unbalanced'''
# s = "([{()}][()])"

# s = "[{()}]"  # [] t

# def check_bracket_str(st1):
#     br_list = ["()", "[]", "{}"]
#     while any([br in st1 for br in br_list]):  # any([False, False , True])
#         for br in br_list: # {}
#             st1 = st1.replace(br, "")
#     return st1

# if check_bracket_str(s):
#     print("unbalanced")
# else:
#     print("balanced")

    








# def fib_series_while(num: int) -> str:
#     return "Passed"

# def fib_series_while(num: int) -> str:
#     return "Passed"

# print(fib_series_while(10))

'''to count the frequency of each element in a list.'''
# lst= [3,4,5,2,1,3,4,4,3,2,4]

# def count_freq(ls):
#     dict= {}
#     for i in range(0, len(ls)):
#         if ls[i] in dict:
#             dict[ls[i]] +=1
#         else:
#             dict[ls[i]]= 1
#     return dict

# print(count_freq(lst))

'''find the common elements between two lists.'''

# lst1= [2,3,4,5,6] 
# lst2= [4,2,2,1,3,4]

# def common(l1, l2):
#     lst= []
#     for i in l1: # 2
#         for j in l2: # 4, 2, 2
#             if i == j and i not in lst:
#                 lst.append(i)
#                 break
#     return lst
# print(common(lst1, lst2))

'''sort a list of elements using the bubble sort algorithm'''

# lst= [2,6,1,7]      #7 2

# def sort_list(ls):
#     for i in range(0, len(ls)): # 6
#         for j in range(i+1, len(ls)): # 7
#             if ls[i]>ls[j]:
#                 temp= ls[i]
#                 ls[i]= ls[j]
#                 ls[j]= temp
#     return ls
# print(sort_list(lst))

'''2nd largest in the list'''
'''sort a list of elements using the bubble sort algorithm'''

# lst= [2,6,1,7]      #7 2

# def large_2nd_list(ls):
#     for i in range(0, len(ls)): # 6
#         for j in range(i+1, len(ls)): # 7
#             if ls[i]>ls[j]:
#                 temp= ls[i]
#                 ls[i]= ls[j]
#                 ls[j]= temp
#     return ls[len(ls)-2]
# print(large_2nd_list(lst))

'''Check given character is vowel or constant'''

# def check_str(letter):
#     vowel = ['a', 'e', 'i', 'o', 'i']
#     vowel_list= []
#     consonant_list = []
#     for i in letter:
#         if i in vowel:
#             vowel_list.append(i)
#         else:
#             consonant_list.append(i)
#     return vowel_list, consonant_list

# vow_lst, conso_lst = check_str("dhdhjshuebwbsaac")
# print(f"No of vovels present in {vow_lst} are",len(vow_lst) )
# print(f"No of consonenets present in {conso_lst} are",len(conso_lst) )

'''remove spaces from string'''
# st= "hello world! how are you?"
# def remove_spcaces(str):
#     for i in str:
#         str= str.replace(" ","")
#         return str
# print(remove_spcaces(st))

'''remove duplicates from a list.'''
# ls= [3,2,3,2,4,2]

# def remove_duplicates(lst):
#     for i in range(0, len(lst)):
#         for j in range(i+1, len(lst)-1):
#             if lst[i] == lst[j]:
#                 lst.remove(lst[i])
#     return lst

# print(remove_duplicates(ls))

'''get only values from nested dictionary'''

d = {
    'a': 1,
    'b': {
        'h': [2, 6, 8, {'r': 8}],
        'c': 5,
        'd': {
            'e': 8,
            'f': {'g': 9}
        }
    }
}

ls = []
def get_int_values(dct):
    for element in dct.values():
        if type(element) == dict:
            get_int_values(element)
        elif type(element) == list:
            for i in element:
                if type(i) == int:
                    ls.append(i)
                elif type(i) == dict:
                    get_int_values(i)
        elif type(element) == int:
            ls.append(element)

# get_int_values(d)
# print(ls)

##### breakdown
##1
def get_int_values(dct):
    for element in dct.values():
        if type(element) == dict:
            pass
        elif type(element) == list:
            pass
        elif type(element) == int:
            pass
##2       
# type(element) == list:
#     for i in element:
#         if type(i) == int:
#             jar tya list chya value madhe single integer asel tar print that
#         elif type(i) == dict:
#             jar tya list chya value madhe dictionary asel tar punha send kara to that function
##3
# output jar list madhe hav asel gtar ek empty list gheun append        


import os

for i in os.walk(r"D:\Sheetal\Python\Theory"):
    print("\n", i)







# '''Write a Python program to count the number of characters in a string. 
# Sample String : 'google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}'''

# st = 'google.com'
# g = st.count("g")
# o = st.count("o")
# l = st.count("l")
# e = st.count("e")
# c = st.count("c")
# m = st.count("m")
# dot = st.count(".")

# dir = {"o":o, "g":g, ".":dot, "e":e, "l":l, "m":m, "c":c}
# print("Res = ",dir)
    

# print([(chr(i), chr(i).lower()) for i in range(65,91)])
# print([chr(i)*3 for i in range(65,91)])

# for i in range(1,5): #1,2,3,4
#     for j in range(10, 13): #10, 11, 12
#         lst.append((i,j))
# print(lst)        

# lst = [(chr(i),j) for i in range(65,91) for j in range(10,13)]
# print(lst) 



























