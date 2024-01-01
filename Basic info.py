print("This is main\n")

#input always save a string
name = input("What is your name? ")
last_name = input('What is your last name? ')
full_name = name + " " + last_name
age = input("What is your age? ")


#use quotas when the character is special for python
quote = "I'm " + name
print(quote)

quote2 = 'It said "Hello"'
print(quote2)

#format use + Strings
template = 'Name: ' + full_name + ', Age: ' + age  + '\n'
template2 = 'Name: {}, Age {}\n'.format(full_name, age)
template3 = f"Name: {full_name}, Age: {age}\n"

print('template1', template)
print('template2', template2)
print('template3', template3)

print("Variable type")
print('Name : ' + str(type(name)))
print('Age : '  + str (type(age)))

#boolean
is_boolean = True # False
#not
print(not is_boolean)

#int and float
budget = 100
temperature = 12.12

#change data type
var = 'Nicol' #String
var = 12 #int
var = True # boolean
age_int = int(age)
age_str = str(age_int)

#operators
plus = 10 + 10 # 20
subs = 10 - 5
times = 10 * 10 # 100
mod = 9 % 7 # 2
div = 10 / 3 #3.333
div_int = 10 // 3 # 3 divition result in int
uxp = 2 ** 3 #8 exponent

#compare operators
# >, <, >=, <=, ==, !=, 
x = 3.3
y = 1.1 + 2.2
# x (3.3) and y (3.3000000002) are different
y_str = format ( y , ".2g")
print(float(y_str) == x)

#tolerance use
#abs = absolute value
tolerance = 0.00001
print(abs(x - y) < tolerance)

#logic operators
print('AND\nOR')
print('True and True => ', True and True)
print('True and False => ', True and False)
print('True or False => ', True or False)
print('False or False => ', False or False)

#contiditonals
if True:
    print("if true")
elif False:
    print("dont print")

if False:
    print ("Should not")
else:
    print("Else")