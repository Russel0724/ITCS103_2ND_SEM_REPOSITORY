import os

os.system('cls')

my_list = [] # empty lsit to store the numbers

word = input("Enter a word: ") # getting aa word from the user

haba = len(word)         # to get the length of the word
num = 1               # to start the count from 1

# loop through each letter from the word the user entered
for let in word:                           
    namber = input(f"Enter number {num}: ")      # ask the user to enter a number
    num += 1                                     # the count increases by 1 each time the loop runs
    my_list.append(int(namber))                  # .append() = adding the number to the list

# to get the average of the numbers
def average():
    total = 0
    for no in my_list:
        total += no
    average = total / len(my_list)
    print(f"The average of the numbers is: {average}")   # prints the average of the numbers
    return average


# prints the number on the list
print(my_list) 
print(f"The length of the word is: {haba}")     # prints the length of the word

ave = average()  

if haba > ave:
    print(f"The length of the {word} is greater than the average.")

elif haba < ave:
    print(f"The length of the {word} is less than the average.")
    
elif haba == ave:
    print(f"The length of the {word} is equal to the average.")

else:
    print("Error")



















# ave = average()   # calls the average function and stores the value in ave variable





















# my_list = []  # empty list to store the numbers

# word = input("Enter a word: ")
# haba = len(word)
# num = 1

# # loop based on the length of the word
# for _ in word:
#     namber = input(f"Enter number {num}: ")
#     num += 1
#     my_list.append(int(namber))  # .append() = adding the number to the list


# def average():
#     total = 0
#     for no in my_list:
#         total += no
#     return total / len(my_list)

# print(my_list)
# print(f"The length of the word is: {haba}")

# ave = average()
# print(f"The average of the numbers is: {ave}")

# # comparison )
# if haba > ave:
#     print(f"The length of the word '{word}' is greater than the average.")
# elif haba < ave:
#     print(f"The length of the word '{word}' is less than the average.")
# else:
#     print(f"The length of the word '{word}' is equal to the average.")
