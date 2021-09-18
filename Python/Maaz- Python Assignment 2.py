#!/usr/bin/env python
# coding: utf-8

# In[6]:


# 1. Simple Message: Store a message in a variable, and then print that message.


message = ('''
Hello Maaz!
Welcome to the Python world! ''')

print(message)


# In[10]:


""" 2. Store a message in a variable and print that message. 
    Then change the value of your variable to a new message and print the new message. """

message = ("Good Morning, Maaz")

print(message)

message = ("Good Mroning, Bose!")

print(message)
    


# In[5]:


"""
3. Store a person’s name in a variable and print a message to that person. 
Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

"""


mes = "Hello Maaz, "
print(mes + "How are you today?")


# In[6]:


"""
4. Find a quote from a famous person you admire. 
Print the quote and the name of its author. 
Your output should look something like the following, 
including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”
"""

print('Margaret Mead once said, "Always remember that you are absolutely unique.') 
print('Just like everyone else."')
      


# In[11]:


"""
5. Repeat Exercise 4, but this time store the famous person’s name in a variable called famous_person. 
Then compose your message and store it in a new variable called message. Print your message.
"""

famous_person = ('Margaret Maed once said ')
Quote = ('"Always remember that you are absolutely unique. Just like everyone else."')
print(famous_person + Quote)


# In[17]:


"""
6. Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your operations in print statements to see the results. You should create four lines that look like this: print (5 + 3)
Your output should simply be four lines with the number 8 appearing once on each line.
"""

print(5+3)
print(28-20)
print(4*2)
print(int(16/2))


# In[7]:


"""
7. Store your favourite number in a variable.
Then, using that variable, create a message that reveals your favourite number. Print that message.
"""


favourite_num = 7
mine = "My faourite number is" + str(favourite_num) + "!"
print (mine)


# In[2]:


"""
8. Choose two of the programs you’ve written and add at least one comment to each. 
If you don’t have anything specific to write because your programs are too simple at this point,
just add your name and the current date at the top of each program file. 
Then write one sentence describing what the program does.
"""


# Program - 1 This Code will wish you if you have a birthday in todya's date. You shold type today's date in order to get wishes!

import datetime
current_date = datetime.date.today().strftime('%Y-%m-%d')
current_date_lst = current_date.split('-')

b_date = input("Enter Birthday in yyyy-mm-dd format: ")

name = input("Name of Birthday Legend? ")
b_date = b_date.split( '-' )

if current_date_lst[1] == b_date[1] and current_date_lst[2] == b_date[2]:

  age = int(current_date_lst[0]) - int(b_date[0])
  ordinal_suffix = {1: 'st', 2: 'nd', 3: 'rd', 11: 'th', 12: 'th', 13: 'th'}.get(age % 10 if not 10 < age <=13 else age % 14, 'th')

  print(f" It's {name}'s' {age}{ordinal_suffix} Birthday")

else:

    print("Sorry today is not your Birthday!")
    
    
    
 


# In[3]:


# Program - 2 Python program to check if year is a leap year or not


# To get year (integer input) from the user

year = int(input("Enter a year: "))         # year = int(input("Enter a year: "))




if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year)) 


# In[3]:


# 9. Store the names of a few of your friends in a list called names.
# Print each person’s name by accessing each element in the list, one at a time.

names = ["Maaz", "Faiz", "Saad"]
print(names[0])
print(names[1])
print(names[2])


# In[5]:


# 10. 10. Start with the list you used in Exercise 9, but instead of just printing each person’s name, print a message to them. 
# The text of each message should be the same, but each message should be personalized with the person’s name.


names = ["Maaz", "Faiz", "Saad"]
message = "I am, " + names[0].title() + "."
print(message)
message = "I am, " + names[1].title() + "."
print(message)
message = "I am, " + names[2].title() + "."
print(message)


# In[3]:


# 11. Think of your favourite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
# Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”


vehicles = ["Lamborghini", "Bugatti", "Lykan Hypersport", "Corvette", "Dodge SRT"]

x = vehicles[0].title()
print("I will owe, " + x)
x = vehicles[1].title()
print("I will owe, " + x)
x = vehicles[2].title()
print("I will owe, " + x)
x = vehicles[3].title()
print("I will owe, " + x)
x = vehicles[4].title()
print("I will owe, " + x)

