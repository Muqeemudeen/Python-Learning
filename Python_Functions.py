# ------------Creating Functions in python for first time LOL

def Display_invoice(Name,amount,due_date):
    print(f"hello {Name}")
    print(f"Your bill of amount $ {amount:.2f} is due: {due_date}")

Display_invoice("Muqeem", 21000, "21/01/23")    
    
#f-strings (formatted strings):
# An f-string is a string literal prefixed with f or F introduced in Python 3.6.
# It allows embedding expressions inside curly braces {} which will be evaluated at runtime
# The 2f is often used in string formatting to specify the number of decimal places for floating-point numbers.

# ---------------To print the length of the list we can use map function !!
strings = ["a","b","c"]
lengths = map(len,strings)# Map allows us to do various operations on desired list,tuple etc
print(list(lengths))

# ---------------to add anything simultaneously in a list 
string = ["a","b","c"]
lengths = map( lambda x: x + "s" ,string)
print(list(lengths))

         # OR
 
#string = ["a","b","c"]
#def add_s(string):
    #return string + "s"
#lengths = map( add_s ,string)
#print(list(lengths))

#------------using filter built in function 
def long(stringg):
    return len(stringg)>4
stringg = ["abnnbn","bbnb","cnb"]
filtered = filter(long,stringg)
print(list(filtered))

#-------- sorting numbers in list or tuple using built in Sorted 
numbers = {7,3,6,4,6}
sorted_nums = sorted(numbers)
print(sorted_nums)

#------------File Handling !!!

file = open("", "w")                          
file.write("hello World \n")          
file.close()
#or 
 #With open("","w") as file: # it closes by itself after using file 
#file.write("here")