#this makes random decisions in the code
import random

#these are lists of the necessary components for a secure password
letters = ["a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,w,x,y,z"]
numbers = ["1,2,3,4,5,6,7,8,9,0"]
symbols = ["!,@,#,$,%,^,&,*,(,),-,=,_,+"]

print("Welcome to your PythonPassword buddy")
number_letters = int(input("How many letters would you like in your password?\n"))
number_numbers = int(input("How many numbers would you like in your password?\n"))
number_symbols = int(input("How many symbols would you like?\n"))

#this is a list for the password characters
password_list = []

#this selects random characters in the lists
for char in range(1, number_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, number_numbers +1):
    password_list.append(random.choice(numbers))
for char in range(1, number_symbols + 1):
    password_list.append(random.choice(symbols))

#this shuffles the password to make it secure
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")

