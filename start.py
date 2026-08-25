#it can be an input
name = "Yanis Laceb" 

#to remove spaces fro the str
name = name.strip()
print(name)

#can use .strip() after an input
# name = input("your name").strip()
#or inside print()

#to capitalize the 1st word
print(name.capitalize())
#to capitalize all words
print(name.title())



 
#to add something to your print
print("Hi my name is " + name + ".") 
 
#to count how many characters are there /the space is a character
print(len(name)) 
 
#to print the position of a character or the position start of a bunch of characters /just the first one in the phrase
print(name.index("a")) 
 
#to print the character of a position 
print(name[0]) 
 
#to write it with big or small characters
print(name.upper()) 
print(name.lower()) 
 
#to know if the sting is writen with big or small characters
print(name.isupper()) 
print(name.islower()) 
 
#to replace a word with another
print(name.replace("Yanis", "Samir"))





num = 19 


#to make the num as a string
print(str(num) + " is the best num") 
 
#to get the absolute value of a num
print(abs(num)) 
 
#to use to power function
print(pow(num, 2)) 
 
#to choose the highest or the lowest num 
print(max(num, 20)) 
print(min(num, 20)) 
 
#to round a num
print(round(7.19)) 
 
#from here you must use this command to use those functions
from math import * 
 
#to round the num to the highest or lowest num 
print(ceil(18.2)) 
print(floor(18.2)) #can use trunc(x) 
 
#some math functions
#   calcul
print(sqrt(49)) #square root 
print(cbrt(8)) #cube root 
print(exp(2)) 
print(exp2(3)) #2 raised to the power 3 
print(log(2)) #it's ln 
print(log2(8)) #2 is the base 
print(log10(1000)) 
print(log(81, 3)) 
print(factorial(5)) 
#   angles
print(cos(pi)) 
print(sin(pi)) 
print(tan(pi)) 
#   algebra
print(gcd(15, 12)) #PGCD 
print(lcm(15, 12)) #PPCM 
print(remainder(2026, 3)) # x=num[y] 
#   probability
print(comb(10, 3)) 
print(perm(10, 3)) 
 
#to combine two function
print(round(sqrt(47))) 
#   those are same btw
print(floor(sqrt(47))) 
print(isqrt(47)) 
 
#to know if two num are close
print(isclose(25, 20, abs_tol=6)) # abs(a, b) < abs_tol 
 
print("to convert angels") 
print(degrees(pi)) #radian to degree 
print(radians(180)) #degree to radian 
 
#to make a string num to a normal num after an input
print(float(num)) 