#---- string in revers, length, upper, lower, copy into another string
a = "Raze""Reyna""Clove""Omen""Chamber"

print(f"The string contants these elements: {a}")


print(f"The length of the string is : {len(a)}")

print("Printing in upper case")

a = a.upper()
print(f" The string in Uppercase is :{a}")

a= a.lower()
print(f"The string in lowercase is : {a}")


b = " Cypher " + a



print(f"The copy of the string a is : {b}")

for i in range(1, len(a),1):
    print( a[-i] )
    

#------- Vowels in a given string 

strin = input("Enter the string to find vowels")

for i in range(len(strin)):
    if "aeiouAEIOU" in strin:
        print(f"This letter is a vowel {strin}")
    else:
        print(f"There are no vowels")
