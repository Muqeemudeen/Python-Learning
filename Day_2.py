#---- Starting the day with Tuples

a= (1,2,3,4,5,6)
print(f"The values from 1 to 6 are {a} and their type{ type(a) }")

# tuples are immutable so if we need to change we need to convert into list first
#step 1 change the tuple into list 
a = list(a)

print(f"The values from 1 to 6 are {a} and their type{ type(a) }")
#step 2 apply modifications 
a.insert(6,67)

#step 3 change it back to tuple 
print(f"After changing the list {a}")
a= tuple(a)

print(f"The values from 1 to 6 are {a} and their type{ type(a) }")


#----------printing using range keyword __ must use len 

for i in range(len(a)):
    print(a[i])


#-----Tuple unpacking------
print( "Tuple unpacking")

tuptup = ("Apple","Mango","orange")

print(f"The values in the tuples are {tuptup}")

a,b,c = tuptup # assigning the values in the tuple to another variable 

print(f"The value of first element in the tuple : {a}") # we can use this to map two varibles 
print(f"The value of first element in the tuple : {b}")
print(f"The value of first element in the tuple : {c}")

#---------------SETS-------

# sets can be defined using parantehesis {}
# sets must have unique values ie it will not allow duplicates ! only once the element will be printed

# we can use indexing with sets -- the whole set is addressed as one 
eg = {1,2,3,4,5,5,3,4,2,6,2}
print(f"The values of eg are : {eg}")


# to step through the values in the sets


print("The values in the variables are ")
for i in eg:
    print(i)



#----- Moving on with DICTIONARIES---
# we can search for elements using their Key 
# we can iterate through the dictionary using (in) keyword along with for loop 

day= {1:"Monday",2:"tuesday",3:"wednesday",4:"Thursday",5:"Friday"}

print( f"The days in a week are :{day}")

# we can check the length of the dict using len keyword

print(f"The length of the dictionary is :{len(day)}")

# to print specific indexed value 

print(f" The value you requested is : {day[2]}")

# creating new key: value pair

day[6] = "Saturday"
print(f"The updated week is : {day}")

# methods in dictionary
# keys must be unique !

# joining 2 dict

a = { 1:"hello",2:'hii'}
b = {3:"who are you ?", 4:"how do u do ?"}

a.update(b)

print(f"The dict after update looks like : {a}")

# looping with dict

for i in a:
    print(i)

# if you know only the values then use 

for i in a.values():
    print(i)


