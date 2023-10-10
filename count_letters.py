import re
user_words = input("Please enter 5 random words separated with ',': ")
clean_list = re.sub("[!@#$%^&*()_+|\/? .0123456789]","", user_words.lower())
split_list = clean_list.split(",")
chars = "abcdefghijklmnopqrstuvwxyz"
my_dictionary = {}

if len(split_list) < 5:
    print("You have entered not enought words!")
else:
    for char in chars:
        count = clean_list.count(char)
        if count > 0:
            my_dictionary[char]=count
    
    print(my_dictionary)