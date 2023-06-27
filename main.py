"""
class stringEdit(object):
    def __init__(self):
        self.s=""
    def getString(self):
        self.s=input()
    def printString(self):
        print(self.s.upper())

sttr=stringEdit()

sttr.getString()
sttr.printString()
"""
"""
Question 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,iY-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.
"""
"""


x = int(input("x: "))
y = int(input("y: "))
ar=[[0 for j in range(y)] for i in range(x)]
for i in range(x):
    for j in range(y):
        ar[i][j]=i*j

print(ar)
"""
"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

rowNum=int(input("x: "))
colNum=int(input("y: "))
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print (multilist)
"""
"""
Question 8
Level 2

Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""
input_data=input()
edited_data = input_data.split(",")
edited_data.sort()
print(','.join(edited_data))
"""
"""
#----------------------------------------#
Question 9
Level 2

Question£º
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""
lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break;
print("\n".join(lines))
"""
"""
#----------------------------------------#
Question 10
Level 2

Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.
"""
"""
data_input = input()
data_edit=data_input.split(" ")
data_edit.sort()

for val in data_edit:
    occur = data_edit.count(val)
    if occur >1 :
        data_edit.remove(val)
print(data_edit)
"""
"""
s = "hello world and practice makes perfect and hello world again"
words = [word for word in s.split(" ")]
print (" ".join(sorted(list(set(words)))))#??????????????????????????
"""
"""
#----------------------------------------#
Question 11
Level 2

Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""
data_input=input()
data=data_input.split(",")
for va in data:
    if int(va,2) % 5 == 0 :
        print(va)
"""
"""
#----------------------------------------#
Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""
vals=[]
for i in range(1000,3001):
    s=str(i)
    if(int(s[0])%2==0 and int(s[1])%2==0 and int(s[2])%2==0 and int(s[3])%2==0 ):
        vals.append(s)
print(vals)
"""
"""
#----------------------------------------#
Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
isnumeric 
"""
"""
data = input()
ret=[0]*2
for i in range(len(data)):
    if(data[i].isdigit()):
        ret[0]+=1
    if(data[i].isalpha()):
        ret[1]+=1
print(ret)
"""
"""
Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""
upper=0
lower=0
data=input()
for char in data:
    if char.isupper():
        upper+=1
    if char.islower():
        lower+=1
print("UPPER CASE "+str(upper))
print("LOWER CASE "+str(lower))
"""
"""
#----------------------------------------#
Question 15
Level 2

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""
data="a+aa+aaa+aaaa"
val=''
ret=0
for char in data:
    print(char)
    if char=='a':
        val+='9'
    elif char=='+':
        print(val)
        ret+=int(val)
        val=''
ret+=int(val)
print(ret)
"""
"""
#----------------------------------------#
Question 16
Level 2

Question:
Use a list comprehension to square each odd number in a list.The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""
Question 17
Level 2

Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""
bank=0
x=input()
while x:
    if x[0]=='D':
        bank+=int(x.removeprefix("D "))
    elif x[0] == 'W':
        bank -= int(x.removeprefix("W "))
    else:
        break;
    x = input()
print(bank)
"""
"""
#----------------------------------------#
Question 18
Level 3

Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""
import re
data="ABd1234@1,a F1#,2w3E*,2We3345"
pattern = re.compile("[A-Za-z0-9]+[@!#$%^&*]+")
for i in data.split(","):
    if len(i)>6 and 12>len(i):
        if re.search(pattern,i):
            print(i)
"""

"""
#----------------------------------------#
Question 19
Level 3

Question:
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use itemgetter to enable multiple sort keys.

"""
"""
import operator
line = input()
ret=[]
while True:
    if line:
        ar= line.split(",")
        line = input()
        ret.append(ar)
    else:
        break; #a.sort(key=operator.itemgetter(1))
ret.sort(key=operator.itemgetter(0,1,2))
print (ret)
"""
"""
#----------------------------------------#
Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield
"""
"""
def ite(n):
    i=0
    for i in range(0,n):
""""""
def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

    print(j)


putNumbers(20)
"""
"""
#----------------------------------------#
Question 21
Level 3

Question£º
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point.
 If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""
import math
data= input()
point=[0,0]
while True:
    if data:
        dir,num=data.split(" ")
        match dir:
            case "UP":
                point[1]+=int(num)
            case "DOWN":
                point[1]-=int(num)
            case "LEFT":
                point[0]-=int(num)
            case "RIGHT":
                point[0]+=int(num)
    else:
        print(int(math.sqrt(pow(point[0],2)+pow(point[1],2))))
        break;
    data = input()
"""
"""
#----------------------------------------#
Question 22
Level 3

Question:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

Hints
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""
data = input()

occur={}
for word_chk in data.split(" "):
    occur[word_chk]=occur.get(word_chk,0)+1
words=list(occur.keys())
words.sort()
for w in words:
    print(w+":"+str(occur[w]))
"""
"""
#----------------------------------------#
Question 23
level 1

Question:
    Write a method which can calculate square value of number

Hints:
    Using the ** operator
"""
"""
def sqr(n):
    return n**2
"""
"""
#----------------------------------------#
Question 24
Level 1

Question:
    Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
    Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
    And add document for your own function
    
Hints:
    The built-in document method is __doc__//python3 help()

"""
"""
#----------------------------------------#
Question 25
Level 1

Question:
    Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later
"""

"""
class test:
    some_class_variable="Var"

    def __init__(self,par="Var"):
        self.some_class_variable=par

    def get(self):
        print(self.some_class_variable)


t1=test("test")
t2=test()
t1.get()
t2.get()
t2.some_class_variable="test2"
t2.get()
"""

"""
#----------------------------------------#
Question:
Define a function which can compute the sum of two numbers.

Hints:
Define a function with two numbers as arguments. You can compute the sum in the function and return the value.




# ----------------------------------------#
"""
"""
def fun(a,b):
    return a+b

print(fun(2,4))

"""
"""
#----------------------------------------#
Question:
Define a function that can convert a integer into a string and print it in console.

Hints:

Use str() to convert a number to string.
"""
"""
def fun(num):
    return str(num)
print(type(fun(2)))
"""
"""
#----------------------------------------#
2.10

Question:
Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.

Hints:

Use int() to convert a string to integer.
"""
"""
def fun(string1,string2):
    return int(string1)+int(string2)

print(fun("3","5"))
"""
"""
#----------------------------------------#
2.10


Question:
Define a function that can accept two strings as input and concatenate them and then print it in console.

Hints:

Use + to concatenate the strings
"""
"""

def con(str1,str2):
    return str1+str2

print(con("str1","str2"))

"""
"""
#----------------------------------------#
2.10


Question:
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

Hints:

Use len() function to get the length of a string
"""
"""
def fun(str1,str2):
    if(len(str1)>len(str2)):
        print(str1)
    elif (len(str1)<len(str2)):
        print(str2)
    else:
        print(str1+"\n"+str2)

fun("str1","str2")
"""
"""
#----------------------------------------#
2.10

Question:
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

Hints:

Use % operator to check if a number is even or odd.

"""
"""
def even(num):
    if(num%2==0):
        print("It is an even number")
    else:
        print("It is an odd number")

even(2)
"""
"""
#----------------------------------------#
2.10

Question:
Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.

"""

"""

def fun():
    dict={}
    for i in range(1,4):
        dict[i]=i**2
    for i in range(1,4):
        print(dict[i])
        

fun()

"""


"""
#----------------------------------------#
2.10

Question:
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
"""

"""
def fun():
    dict={}
    for i in range(1,21):
        dict[i]=i**2
    for i in range(1,21):
        print(dict[i])

fun()

"""
"""
#----------------------------------------#
2.10

Question:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

"""
"""
def fun():
    dict={}
    for i in range(1,21):
        dict[i]=i**2
    for x in dict.values():
        print(x)

fun()

"""
"""
#----------------------------------------#
2.10

Question:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

"""
"""
def fun():
    dict={}
    for i in range(1,21):
        dict[i]=i**2
    for x in dict.keys():
        print(x)

fun()
"""
"""
----------------------------------------#
2.10

Question:
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.

"""
"""
def fun():
    list=[]
    for i in range(1,21):
        list.append(i**2)
        print(list[i-1])
fun()
"""
"""
#----------------------------------------#
2.10

Question:
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list

"""

def fun():
    list=[]
    for i in range(1,21):
        list.append(i**2)
    print(list[0:5])
fun()
