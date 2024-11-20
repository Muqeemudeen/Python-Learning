#---- string in revers, length, upper, lower, copy into another string
a = "Raze""Reyna""Clove""Omen""Chamber"

print(f"The string contants these elements: {a}")


print(f"The length of the string is : {len(a)}")

print("Printing in upper case")

a = a.upper()
print(f" The string in Uppercase is :{a}")

a= a.lower()
print(f"The string in lowercase is : {a}")


b = a
print(a)



print(f"The copy of the string a is : {b}")


print("The Reverse of the string is ")
reve =a[::-1]
print(reve)
   
    

#------- Vowels in a given string 

#strin = input("Enter the string to find vowels")

#for j in range(len(strin)):
   # if "aeiouAEIOU" in strin:
   #     print(f"This letter is a vowel {j}")
   # else:
    #    print(f"There are no vowels")



#--- arrange the string in lowercase first and upper case second

hehe = "Yoo Brother Im in love"
hehe2 = hehe.split()
hehe3 =""



for i in hehe2:
    if i.islower():
        hehe3 = hehe3 +i
print(hehe3)
for i in hehe2:
    if i.isupper():
        hehe3 = hehe3 +i
print("Ordering lower case first and then upper case in a string:")
print(hehe3)





# next question !!
#count all letters digit and special char from a given string 
#count nos 


str = "p@#yn26at^8i5ve"

chr =0
dig =0
spchr =0 

for i in str :
    if i.isdigit():
        dig =dig +1 