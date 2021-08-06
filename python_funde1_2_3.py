print("Hello World!")
input("'data science'")
# answer if you put data science like that without qoutes theb it will give you an error a synatx error:invalid syntax easily to remedy by adding qoutes to data science.
a = 5
if a == 5:
    # 4 indented spaces to this block of code
  print("a equals 5")

myString = 'hello world'
print(type(myString))

n = 10
print(type(n))

n_float = 7.5
print(type(n_float))

single_string = 'It\'s a single quote string'
print(single_string)
#  File "<ipython-input-11-dbe7c6e4d27f>", line 1
#     single_string = 'It's a single quote string'
#                         ^
# SyntaxError: invalid syntax
# the reason that this will give us a Syntax error would be that you need to add (\)this said symbol in the middle of It\'s 
double_string = "It's a double quote string"
print(double_string)

n1 = 5
n2 = 7.5
print(n1+n2)

nstr1 = "abc"
print(f'{nstr1}{n1}')
# in order to concatetate the string and integer i had to use f string.

nstr2 = "def"
print(nstr1 + nstr2)

n1, n2 = 10, 11
print(n1)
print(n2)

result = 3 + 4.0 / 2 * 5  # DMAS
print(result)

# module operator %
remainder = 17%10
print(remainder)


# x ^ n
x = 5
n = 4
print(x ** n)

nstr = "abc"
ans = nstr * 10
print(len(ans))

name = "Harshit"
print("%s is a data scientist!" %name)
print(name.upper())
print(name.lower())

nstr = "it is a nice day today."
print(nstr.capitalize())
print(name.index('s'))
print(name[2:5])
print(name[2:6:2])

alist = [3,4,5]
print(alist)


alist = ['harshit', 2, 5.5]
print(alist)

alist.append(10)
alist.append(15)
print(alist)
print(alist.pop())
print(alist[3])
print(
alist[1:])

alist.append([1,2,3])
print(alist)
print(alist*2)
print(alist + alist)



# Python Fundamentals - part II

alist = ['Tom', 54, 'Julia', 78]
print(alist)

print(alist.append(help))
print(alist)
# print(help())

blists = [
    ['Tom', 54],
    ['Julia', 78]
]

print(blists)
print(blists[-1])
print(blists[-2][0])

blists.append(['Mak', 90])
print(blists)


a = [0]*5
print(a)


cols = 5
rows = 4
a = [[0]*cols]*rows
dlist = [[1]*cols]*rows
print(dlist)


tup1 = ('Tom', 78)
# tup1[1] = 90
# tuples are immutable  so we needed to change it to a list in order to do so I created a variable name l and stored list of tuple.then I had to creat another variable to access the list which l[1 and the value is 90]. the last step is I took this variable named l and made a variable name t_change to store the conversion of the tuple tp list then I print the variable named t_change.

l = list(tup1)
l[1] = 90
t_change = tuple(l)
# 

print(t_change)
tup2 = ('Julia', 89)
print(tup1 + tup2)
print(tup1)

tup3 = tup1 + tup2
print(tup3)
print(len(tup3))


# dictionary
country_code = {'India': 1, 'USA': 2, 'China': 3}
print(country_code)
print(country_code['China'])

country_code['UAE'] = 4
print(country_code)

if 'Inda' in country_code:
    print(True)
else:
        print(False)

x = True
print(type(x))

print(1 == 2)
print(1!=2)

a = 1
b = 2
print(a == b)
print(a > b)
print(a < b)
print(a != b)

color = 'red'
if color == 'red':
    print("Color is red!")
    
print("Color problem is solved!!")


color = 'green'
if color == 'red':
    print("Color is red!")
    
elif color == 'green':
    print("Color is green!")
    
else:
    print("color is not red!")
    
print("Color problem is solved!!")

age = 15
if age >= 18:
    print("Adult")
    
else:
    print("Juvenile")

    a = 0
print(not(a))

a = 3
print(not(a))

a = True
print(not(a))

score = 74
percentile = 83

if score > 75 or percentile > 90:
    print("Admission successful!")
else:
    print("Try again next year")

    # all you have to do is change the score value next to the variable to read below 75 and the else condtion is automatically accessed
print(range(5))

for i in range(5):
    print(i)

for product in range(1, 10, 2):
    product = 8 * product 
    print(product)  

    # instead of saying for i, switched up to product since below the for loop the variable product is being giving the value of 8 times product and print out product.

names = ('harshit', 'shubham', 'sahil')
for name in names:
    print(name.upper())  

age = [12,43,45,10]
i = 0
while i < len(age):
    if age[i] >= 18:
        print("Adult")
    else:
        print("Juvenile")
    i += 1 

    # list comprehension

cubes = [n** 3 for n in range(1,10)]
print(cubes) 

cubes = []
for i in range(1,10):
    cubes.append(i ** 3)
print(cubes)

# print(help(abs))

print(abs(2-5))

def add_two_numbers(a, b):
    sum = a + b
    return sum
print(add_two_numbers(5,11))



def fahr_to_celsius(temp):
    """
    This function converts temperature from fahrenheit
      to celsius.
      Args:
      -----
        tempInFahr: temperature in fahrenheit

      Returns:
      --------
        tempInCel: temperature in celsius
    """
    tempInCel = (temp - 32) * 5/9
    return tempInCel
print(fahr_to_celsius(50))


# Python Fundamentals - part II

a = 5
print(type(a))

alist = [1,2,'a']
print(type(alist))

heights = [5,4,6,7,3,5]
heights.sort()
print(heights)

alist.reverse()
print(alist)

astring = 'hello world'
bstring = astring.replace('world', 'there!')
print(bstring)

(dir(alist))
 
class Rectangle:
    # constructor for Initialization
    def __init__(self):
        # The only members are length and width
        self.length = 1
        self.width = 1

    # Write Setters methods for width and length
    def set_width(self, width):
        self.width = width

    def set_length(self, length):
        self.length = length

    # Write Getters methods for the both instance variables
    def get_width(self):
        return self.width

    def get_length(self):
        return self.length
    # find area method
    def find_area(self):
        return self.length * self.width

    # show String representation of object
    def __str__(self):
        return 'length = {}, width = {}'.format(self.length, self.width)

rect1 = Rectangle()
# set width and length of rectangle1 object
rect1.set_width(10)
rect1.set_length(12)
# call find_area( ) method 
ar = rect1.find_area();
# display values of instance variables of rectangle1 object
print(rect1)
# show area of rectangle1 object
print("Area = ",ar)
print(type(rect1))

print(dir(rect1))

import math

print(type(math))

print(dir(math))

print(math.log(100,10))

print(math.pi)


import math as mt
print(mt.log(100,10))


from math import log, pi
print(log(100,10))






        

    
        
