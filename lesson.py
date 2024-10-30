import re

# total_slots = 100

# print(total_slots)

# used_slots = 5

# available_slots = total_slots - used_slots 

# print(available_slots)

# my_lists = [100, 5, 95]
# total_slots, used_slots, available_slots = my_lists

# print(my_lists)



# print(9 / 2)
# print(9 % 2)

### STRINGS ###

# # fname = "james"
# # mname = "mark"
# # sname = "Daniel"
# # age = 40
# # city = "Ado Ekiti"
# # pcode = 360001

# intro = "My name is {}, I am {} years old".format(fname, age)
# intro = "My name is {0}, I am {1} years old".format(fname, age)
# intro = "My name is {0}, I am {1} years old. \nI am from {3}. \nMy father\'s name is {2}".format(fname, age, sname, city)
#intro = f"My name is {fname}, I am {age} years old. \nI am from {city}. \n My father\'s name is {sname}"

# print(intro)

#firstnumber = 10
#secondNumber = "60"

#result = int(secondNumber)

#checktype = type(secondNumber)

#print(type(secondNumber))

#print(result)

#print(secondNumber)

#result = str(firstnumber)
#checktype = type(result)

#print(type(result))

#print(result)


#firstName = "Deven"
#lastName = "Ogbebor"

#print(firstName + lastName)
#print(firstName + " " + lastName)

# age = int(input('what is your age sir: '))

# int(age)

# if age < 18:
#    print("you are not allowed to drive")
# elif 18 >= age < 90:
#    print("yes my man you are allowed to drive")
# elif 90 == age > 110:
#    print("get the f@ck off my wheels")
# else:
#     print("commot body jor")
     
     
#time = int(input('wetin be time chairman: '))

#int(time)

#if time < 12:
#    print('Good morning boss')
#elif time >= 12 and time < 16:
#    print('Good afternoon boss')
#else:
#    print('Good evening boss')    
    


# COLLECTIONS

#Lists

# Fruits = ['orange', 'banana', 'cashew', 'pineapple', 'pawpaw', 'guava', 'apple', 'lemons']
# print(len(Fruits))
# print(Fruits[5])

#print(Fruits)

# print out range
# print(Fruits [2 : 4])

# print(Fruits)
# Fruits.append('coconut')
# print(Fruits)
# Fruits.pop(0)
# print(Fruits)
# print(Fruits.__contains__('pineapple'))

# Fruits = ['orange', 'banana', 'cashew', 'pineapple', 'pawpaw', 'guava', 'apple', 'lemon']


# cart = input('What would you like: ')

# if cart.__contains__('orange'):
#     print('There are cuurently apples available!')
    
# elif cart.__contains__('banana'):
 #    print("There are bananas available")    
    
# elif cart.__contains__('cashew'):
#     print("There are cashews available")
    
# elif cart.__contains__('pineapple'):
 #    print("pineapples are available")
    
# elif cart.__contains__('pawpaw'):
 #    print("pawpaws are available")
    
# elif cart.__contains__('guava'):
#     print("guavas are available")
    
# elif cart.__contains__('apple'):
#     print("apples are available")
    
# elif cart.__contains__('lemon'):
#     print("lemons are available")

# else:
 #   print("Does are not available right now")
 

"""
VARIABLES (INTEGERS,BOOLEANS,STRINGS,FLOAT)

INTEGERS ARE WHOLE NUMBERS

FLOAT IS A NUMBER THAT CONTAINS A DECIMAL POTION 

"""

"""
TYPE CASTING (str(),int(),float(),bool())

name: "Deven"
print(type(name))

CHANGE FROM A TYPE TO ANOTHER 

gpa = 3.2

gpa = int(gpa)
print(gpa)

"""

# PYTHON CALCULATOR
""""
operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result)) 
elif operator == "*":
    result = num1 * num2
    print(round(result))      
elif operator == "/":
    result = num1 / num2
    print(round(result))
else:
    print(f"{operator} is not a valid operator")

"""""

#TEMPERATURE CONVERTER
""""
unit = input("Is this temperature in celsuis or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))


if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is : {temp}^F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is : {temp}^F")
else:
    print(f"{unit} is an invalid unit of measurement")
"""""

# COLLECTION 

""""
Collection is a variable used to store multiple values

We have :
LISTS[] Ordered and changeable. Duplicates are OK,
SET{} Ordered and immutable Add/Remove is OK. No duplicates, 
TUPLE() Ordered and unchangeable.Duplicates OK. FASTER, 
DICTIONARIES
 
"""

#    TUPLES ASSIGNMENT

""""

my_tuple = (10, 20, 30, "apple", "banana", True, 5.6)
tuple_1 = my_tuple[1]
tuple_2 = my_tuple[6]
tuple_range = my_tuple [2 : 5]

tuple_num = (1,2,3,4,5,6,7)

tuple_len = len(tuple_num)
max_tuple = max(tuple_num)
min_tuple = min(tuple_num)


question = str(input("Ask a question: "))

if question.__contains__("the entire tuple"):
    print(f"The entire tuple is: {my_tuple}")
elif question.__contains__("access and print the second and last element of the tuple"):
    print(f"The second element of the tuple is: {tuple_1} while the last element is: {tuple_2}")
elif question.__contains__("access and print the second element of the tuple"):
    print(f"The second element of the tuple is: {tuple_1}")
elif question.__contains__("access and print the last element of the tuple"):
    print(f"Thelast element is: {tuple_2}")
elif question.__contains__("elements from the 3rd position"):
    print(f"The elements from the 3rd postion to the 5th position are: {tuple_range}")
elif question.__contains__("changing the value of the 2nd element"):
    print("The element cannot be changed cos it's a tuple unlike a list that can be changed, we first have to convert to a list before changing an element")
if question.__contains__("the length of the tuple"):
    print(f"The length of the tuple is: {tuple_len}")
elif question.__contains__("maximum and minimum value in the tuple"):
    print(f"The maximum value is {max_tuple} and the minimum value is {min_tuple}")
elif question.__contains__("maximum value in the tuple"):
    print(f"The maximum value is {max_tuple}")
elif question.__contains__("minimum value in the tuple"):
    print(f"The minimum value is {min_tuple}")    
else:
    print("ASK VALID QUESTION....U NOR DEY HEAR WORD!!")    


my_list = list(tuple_num)

my_list.append(8)
print(my_list)

"""""
""""
mydict = {
    'age' : 20,
    'name' : 'Deven', 
    'class' : 'jss2', 
    
}

print(mydict)
"""

""""
FruitLists = ['orange', 'pineapples', 'mango']

for index, fruit in enumerate(FruitLists):
    print(index, fruit) 
    
    
    
def adds_two_numbers (firstnum, secondnum):
    return firstnum + secondnum    

add = adds_two_numbers(2, 20)

print(add)
"""

# TAX CALCULATOR

""""

coperate_tax = 30
income_tax = 24
sales_tax = 7.5

tax = int(input("Please enter your salary: "))



def coperate_tax(tax):
    return tax * 30/100 

def sales_tax(tax):
    return tax * 7.5/100

def income_tax(tax):
    return tax * 24/100

print("hi enter amount to be taxed: ")
tax_amount = float(input())
print("enter taxtype if personal tax enter PER, if sales tax enter SAL, if cooperate tax enter COR ")
tax_type = input()

if tax_type == "PER" or tax_type == "per" and tax_amount is not None:
   result = income_tax(tax_amount)
   print(f"your tax is a personal tax and it amount to ${result}")
   
elif tax_type == "SAL" or tax_type == "sal" and tax_amount is not None:    
   result = sales_tax(tax_amount)
   print(f"your tax is a sales tax and it amount to ${result}")
   
elif tax_type == "COR" or tax_type == "cor" and tax_amount is not None:
   result = coperate_tax(tax_amount)    
   print(f"your tax is a cooperate tax and it amount to ${result}")
   
else:
    print("there was an error somewhere")

"""

# PASSWORD VALIDATOR

""""

def password_checker(password: str):
    if len(password) < 8:
        print("your password is less than 8")
        return False
    if not any(char.isupper() for char in password):
        print("at least one uppercase should be present")
        return False
    if not any(char in() for char in password):
        print("password should contain a lowercase")
        return False
    if not any(char in "#@$%^&*_-" for char in password):
        print("The password should contain special characters")
        return False
    if not any(char in "0123456789" for char in password):
        print("the password should contain numbers")
        return False
    else:
        print("your password meets all requirements")
        return True
    
print("enter your password")
password = input()
password_checker(password)

"""

##  constructor is a special method that is invoke when a function is created 

"""""

class deven:
    def __init__(self, name, age, eduLevel, sex, complexion, bestfood):
        #attr
        self.name = name
        self.sex = sex
        self.age = age
        self.eduLevel = eduLevel
        self.complexion = complexion
        self.bestfood = bestfood
        
    def introduce(self):
        print(f'hi my name is {self.name} and i am a {self.sex} i am {self.age} years old, i am currently an undergraduate')



dev1 = deven('deven', 20, 'undergraduate', 'male', 'black', 'pie opp BBA')
dev2 = deven('deven brother', 55, 'graduate', 'male', 'black', 'spagg')

dev1.introduce()
dev2.introduce()


class book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def get_description(self):
        print(f'{self.title} by {self.author}, published in the {self.year}')

book1 = book('Things fall apart', 'Chinua Achebe', 2006)
book1.get_description()            

book2 = book('How to beat artificial intelligence', 'Deven', 2025)
book2.get_description()            

"""

"""""

def credit_card_checker(number: str):
    
    total_num = 0    
    
    for num in range(len(number)):
        digit = int(number[len(number) - 1 - num])
        
        if num % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
  
    total_num += digit    
                
    return total_num % 10 == 0         

print("Enter Your Credit card Number:")
number = input()   
credit_card_checker(number)


"""

def filter_persons(people):
    
    persons_result = []
    
    for person in people:
        if person.get('age', 0) and person.get('city') == 'New york':
            persons_result.append(person.get('name'))
    
    return persons_result
    

persons = [
    {
    'name' : 'Deven', 
    'age' : 20,
    'city' : 'Fleetwood', 
    },
    
    {
    'name' : 'ogbebor', 
    'age' : 30,
    'city' : 'New york', 
    },
    
    {
    'name' : 'Bolu', 
    'age' : 40,
    'city' : 'New york', 
    },
    
    {
    'name' : 'Phillip', 
    'age' : 19,
    'city' : 'Los angeles', 
    },
    
    {
    'name' : 'Ayo', 
    'age' : 15,
    'city' : 'Rainham', 
    },
    
    {
    'name' : 'Victor', 
    'age' : 46,
    'city' : 'Gotham', 
    }
]

filtered = filter_persons(persons)
print(filtered)


def email_checker(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern,email))


print("Enter your email: ")
email = str(input())
email_checker(email)