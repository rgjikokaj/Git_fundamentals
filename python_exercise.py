
# Python fundamentals Exercises 1(Expressions, Strings, Lists, Tuples) 


# Q1: What is 84 / 12 + 2 * 2 ?
print(84 / (12+ (2 * 2)))
# answer is 11.0

# Q2: What is the type of the answer variable in this expression:
print(12/4)
# answer is a floating value 

# Q3: What is the value of num?
num = 2
num = 5*10
print(num)
# answer is 50


# Q4: What would this expression evaluate to?
name='tom' + str(1)
print(name)
# answer is tom1 and is a form of concatination 


# Q5: What would this expression evaluate to?
print('6' + '4')
# answer is 64


# Q6: What would be the output of MyString[5:12] if?
MyString = "Data Science with Harshit"
print (MyString[5:12])
# answer would be Science


# Q7: What would be the output of MyString[5:] if?
MyString = "Data Science with Harshit"
print (MyString[5:])
# answer would be Science with Harshit


# Q8: What would be the output of MyString[5::2] if?
MyString = "Data Science with Harshit"
print(MyString[5::2])
# answer it prints out is Sinewt asi


# Q9: Is there any 'go' in MyString if yes, at what index?
MyString = "You should go to your home!"
FindIt= MyString.index("go")
print(FindIt)
# answer is yes and its located at 11 position


# Q10: Evaluate the following expression and convert it to string object?
MyNum=18 + 19 * 11
My_Num= str(MyNum)
print(MyNum)
print(My_Num)


# Q11: Replace Harshit with your name in the statement below.
MyString = "Data Science with Harshit"
print(MyString.replace("Harshit","Remzi"))
# answer .replace takes the old string and subsetuted for the new string
# Q12: Use the split() function to extract all the words of MyString in a list:
MyString = "Data Science with Harshit"
extract_list= MyString.split()
print(extract_list)
# answer The split() method splits a string into a list.

# Q13: Extract the last element of the list without counting.
MyList = [23, 43, 56, 'tom', 'red', 65, 89, 90, 87]
print(MyList[-1])


# Q14: What is the length of the list below?
MyList = [23, 43, 56, 'tom', 'red', 65, 89, 90, 87]
print(len(MyList))
# answer To determine how many items a list has, use the len() function:


# Q15: Extract all the elements from 2nd index to 6th index.
MyList = [23, 43, 56, 'tom', 'red', 65, 89, 90, 87]
print(MyList[2:6])


# Q16: Extract all the elements except last 2 using slicing
MyList = [23, 43, 56, 'tom', 'red', 65, 89, 90, 87]
print(MyList[0:5])

# Q17: Are lists mutable? (Yes/No)
lists= "mutable"
if lists == "mutable":
    print("lists are mutable")
else:
  print("Not Mutable")


# Q18: Sort the below list using the in-built list class function:
MyList = [23, 43, 56, 65, 89, 90, 87]
Sorted_list= sorted(MyList)
print(Sorted_list)
# answer using sorted in a new variable and storing the old i can print it out in the terminal

# Q19: Delete 'tom' and 'red' from the list using remove() function.¶
MyList = [23, 43, 56, 'tom', 'red', 65, 89, 90, 87]
print(MyList.remove('tom'))
print(MyList)
print(MyList.remove('red'))
print(MyList)

# Q20: Tuples are mutable(True/False)

Tuples= "not_mutable"
if Tuples == "not_mutable":
    print("Tuples are not mutable")
else:
  print("They are Mutable")


# # Q21: From a 
tuple= (23, -1, 34, [1 , 3] , 90)
tuple[3][1]
if 3 in tuple[3]:
  print("Yes,the 'element' exicst")
  # answer there are immutable cant be remove item

# Q22: What is right method to clone a list? Create a clone the list below. Imp (Hint: slicing)
MyList = [23, 43, 56, 'tom', 'red', 65, 89, 90, 87]
MyList_two= MyList[:]
print(MyList)
print(MyList_two)


# Python fundamentals Exercises (Conditionals, Loops)



# Q1: What would be the output of the following code block?
count = 4
print(count == 2)
print(count != 4)
print(count > 4)
print(count < 6)

# Answer would be False,False,False,True


# Q2: What would be the output of the following code block?
color = "red"
category = "fruit"

if color == "red" and category == "fruit":
    print("We have an Apple!")

if color == "red" and category == "vegetable":
    print("We have tomatoes")
# "SyntaxError: EOL while scanning string literal(which translates to: The SyntaxError: EOL while scanning string literal error in python occurs when while scanning a string of a program the python hit the end of the line due to the following reasons:Missing quotes
# Strings spanning multiple lines) (So I added an  end qoute to balance it out on line 55, and it prints out  We have an Apple!)


# Q3: What would be the output of the following code block?
requested = ['blueberry', 'banana']
fruits = ['apple', 'banana', 'watermelon', 'kiwi', 'rasberry']

if requested not in fruits:
    print("Sorry, We don't have bananas in stock. Please review your order!")

else:
    print("Order is placed!")

    # the output for the following code would be (Sorry, We don't have bananas in stock. Please review your order!)
    # Q4: What would be the output of the following code block?
scores1 = [1,2,3]
scores2 = [1,2,3]

print(scores1 == scores2)
# answer would be name 'score1' and 'score2' is not defined because the variable is written as scores1 and scores2 so with adding the proper spelling to the print names it will continue to print out the dsesired reuslts which both of the list will equal to true because the have the same elements in them.


# Q5: What would be the output of the following code block? Learn about 'is' operator.
scores1 = [1,2,3]
scores2 = [1,2,3]

print(scores1 == scores2)
print(scores1 is scores2)

# answer is as above lacking the proper spelling when passing through print, didnt match the varaibls, so I fixed that. for the first print statement it return as True because the equal eachother. Now as I was learning about is operator and i find out that The Equality operator (==) compares the values of both the operands and checks for value equality. Whereas the 'is' operator checks whether both the operands refer to the same object or not.



# Q6: Print the following pattern using for loops:


## Q3: What would be the output of the following code block?

# ```python
scores = [67, 90, 89, 78, 99, 100]
for score  in scores:
  print(score)

# ```


# Python fundamentals Exercises (Dictionaries, Functions)



# Q1: What are the keys in the following dictionary?
MyDict = {
  "Color": "red", 
  "name": "apple", 
  "type": "fruit"
  }
print(MyDict)

# the key it this dictionary are (Color,name.type) and the vslues to those keys are (red,apple,fruit)


# Q2: Extract all the keys of the dictionary below.
MyDict = {
   "Color": "red",
   "name": "apple", 
   "type": "fruit"
   }
print(MyDict.keys())


# Q3: Iterate over the dictionary to print the corresponding key and value.
MyDict = {
  "Color": "red", 
  "name": "apple", 
  "type": "fruit"
  }
print(MyDict)