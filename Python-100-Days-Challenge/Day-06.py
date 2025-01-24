##________ Day--06____________##

# Code Blocks
# Functions
# While loops

# Functions _______ Built-in-Function_________


# print("Hello")

# num_char = len("Hello")

# print(num_char)



# def my_function():
#     print("Hello")
#     print("Bye")

# my_function()




# --------------Defination of Function--------------###

# def my_function():
#     #do this 
#     #then do this 
#     #Finally do this 

# # ------------- Calling the function------------##

# my_function()



#_____________________Identation____________________#

#             Def my_function():
#                  print(my_function)

# def my_function():
#     if sky == "clear":
#         print("blue")
#     elif sky == "cloudy":
#         print("grey")
#     print("Hello")
    
# print("Hello")


#_____________For Loop______________#
#----------For 
#----------For item in list_of_items:
#----------#Do something to each item
# for number in range(a, b):
#     print(number)


#------------------While---------------#
 
# while something is true:
#     #Do something repeatedly



# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
 
# number_of_hurdles = 6 
# while number_of_hurdles >0:
#     jump()
#     number_of_hurdles -= 1
#     print(number_of_hurdles)



# while not at_goal():
#     jump()






##-----------------Maze Challenge---------------###

def turn_right():
    # Define turning right as three left turns
    turn_left()
    turn_left()
    turn_left()

# Move to the starting wall if not already at one
while front_is_clear():
    move()
turn_left()

# Navigate the maze using the right-hand rule
while not at_goal():
    if right_is_clear():  # Turn right if possible and move
        turn_right()
        move()
    elif front_is_clear():  # Move forward if the front is clear
        move()
    else:  # Turn left otherwise
        turn_left()






