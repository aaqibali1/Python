#Final Project--> Password Generator

#For Loop ---> Allows us to exicute same line of code multiple times.



# for item in list_of_items:
#     #do something to each item



# fruits = ['Apple', 'Peach', 'Pear']

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

# print(fruits)



# student_scores = [ 23, 34, 34, 34, 54, 23, 63 , 67,77, 74,74, 84, 48, 83, 93, 38, 34, 94 ]

# # total_exame_score = sum(student_scores)
# # print(max(student_scores))


# # # print(total_exame_score)

# # sum = 0

# # for score in student_scores:
# #     print(score)

# # for score in student_scores:
   
# #     sum += score

# # print(sum)

# max_score = 0 
# for score in student_scores:
#     if score > max_score:
#         max_score = score

# print(max_score)



# --------------->For Loop------------>#
# 
# for item in list_of_items:
# do somethin to each item



#-----------Using for loop in range function---------------#

# Range(a, b)

# a = 1
# b = 11
# sum = 0
# for number in range(a, b):
#     print(number)
#     sum += number


# print(sum)

# for number in range(1, 12, 2):
#     print(number)


# total = 0 

# for number in range(1, 101):
#     total += number

# print(total)


# for number in range(1, 100 + 1):
#     if number % 5 == 0 and number % 3 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)



import random

# Complete lists of letters (both lowercase and uppercase) and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '=', '^', '@', '~', '{', '}', '[', ']', ':', ';', "'", '"']

# Welcome message
print("Welcome to the PyPassword Generator!")

# Taking input from the user
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# password_list = []

# password_list += random.choices(letters, k=nr_letters)  
# password_list += random.choices(symbols, k=nr_symbols)  
# password_list += random.choices(numbers, k=nr_numbers)

# random.shuffle(password_list)

# password =''.join(password_list)

# print(f"Your generated password is: {password}")


# password = " "

# #range(1, 101)

# # for char in range(1, nr_letters + 1):
# #     password += random.choice(letters)

# # for char in range(1, nr_symbols + 1):
# #     password += random.choice(symbols)

# # for char in range(1, nr_numbers + 1):
# #     password += random.choice(numbers)

# # print(password)


# for char in range(0, nr_letters):
#     password += random.choice(letters)

# for char in range(0, nr_symbols):
#     password += random.choice(symbols)

# for char in range(0, nr_numbers):
#     password += random.choice(numbers)



# print(password)

password_list = []

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)

random.shuffle(password_list)

print(password_list)

password = " "

for char in  password_list:
    password += char

print(f"Your password is: {password}")

