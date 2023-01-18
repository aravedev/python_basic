"""
Comparations: This is an example based in the comparators of javascript
&& = and
|| = or

Booleans
print(bool(0)) // gives you false
print(bool("")) // gives you false too
print(bool(1)) // gives you true
print(bool("Danny")) // gives you true

not False = True
not True = False

"""
name= input("What is your name?: ")
age=input("How old are you?: ")
age=int(age)
sex=input("Type M if you are a Man, otherwise type F for Female: ")

if age>=18 and sex=="M":
    print(f"Gym services start at 9am {name}")
else:
    print(f"Miss {name}, the gym services start at 8 AM with the sumba class")
