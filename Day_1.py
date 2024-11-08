# Loops and Conditionals in Python

#Conditionals - 
print("-------------Conditionals------------")
# if
a = 10
if(a == 10):
    print(f"a is equal to {a} in if statment") 
    # the f is the format string that is used to show the value of variable inside a string

# if-else

b = "" # the string is empty so answer will be false
if(b): #expects true here
    print("Not Empty in if-else statement")
else:
    print("Empty in if-else statement")

# if-elif-else

if():
    print()
elif ():
    print()
else:
    print()

##Loops
print("-----------Loops-----------")
# for loop:
print("For loops:")
for i in range(1,11):
    print(i)

print("Range thing in loops")
for i in range(1,11,2): 
    #skip the one number
    print(i)

# while loop:
print("While loops")
a = 0
while a < 10:
    print(a)
    a = a+1 # to not get a infinite stuff

#Control Flow:
print("Control flows")

# break
print("Break in for loop")
for i in range(1,21):
    print(i)
    if i == 2:
        break

print("Break in while loop")
b = 0
while b < 10:
    print(b)
    b = b + 1
    if b == 4:
        break

#Continue
print("Continue in for loop")
for i in range(1,21):
    if i == 2:
        # this will skip the 2 and will continue
        continue
    print(i)

    # ------------Creating Functions in python for first time LOL

def Display_invoice(Name,amount,due_date):
    print(f"hello {Name}")
    print(f"Your bill of amount $ {amount:.2f} is due: {due_date}")

Display_invoice("Muqeem", 21000, "21/01/23")    
    
#f-strings (formatted strings):
# An f-string is a string literal prefixed with f or F introduced in Python 3.6.
# It allows embedding expressions inside curly braces {} which will be evaluated at runtime
# The 2f is often used in string formatting to specify the number of decimal places for floating-point numbers.


# ---- parameter function !
def TMKC(para1,para2):
    print(f" its been so long {para1}, but it feels like we broke up just {para2} weeks ago ")

TMKC("X",2)

#----- using default parameter!
def Defaultpara(pera,pera2, pera3 = 7):
    print(pera+pera2+pera3)

Defaultpara(1,2)


#------ using return statement instead of print - to use the same value multiple time across the program.

def word(num):
    if num>2:
        return True
    else:
        return False
    
variable = word(5)



#-------- Strings -----

#---- indexing of strings
a = "Hamari Adhuri Kahani"
print (f"iNEXING OF A STRING {a} : {a[0]}" )

#--- using range slicing 

print (f"iNEXING OF A STRING {a} : {a[0::4]}" ) #1st space is starting 2nd space is end point 3rd space is steps

#------ searching each character of the string

print("To search each char in a string")
if "Hamari" in a : # we can do with single letter as well 
    print(True)
else:
    print(False)    

# to print each charcter of the sting line by line 
for i in range(0,len(a)):
    print(a[i])

#------ String Methods

upper = a.upper()
print ( f" The string after changing to upper case {upper}") # same for lower 


#-------LIST---------

#list index 

list= ["aa","be","cee","dii"]

print (list[0])

# lsit slicing 
print(f"After slicing of the string {list[0:5:2]} ")

# list methods---------

# inserting in a stringgg
list.insert(5,"eee")# index wise inserting into the list 
print(list)

# appending a string
list.append("FEC")
print(list)

# removing a char from a string
list.remove("FEC")
print(list)


#using  pop method
list.pop()  # defalut pops the char from the last or else can give an index
print(list)