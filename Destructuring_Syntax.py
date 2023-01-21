
# Destructuring 

currencies = (0.8, 1.2)

"""
This means, we are going to take first value of currencies and put it in usd, the second value of currencies will be assigned to eur
"""
usd,eur = currencies

print(f" Current value for Usd {usd}, current value for EUR {eur}")

"""
Destructuring a list of tuples
"""

friends = [("Rolf",25),("Anne",37),("Charlie",31),("Bob",22)]

# 1) Using for loop
for friend in friends:
    print(friend) # You will get a tupple ("Rolf",25)

print("white space")
#2) Using destructuring:
for name,age in friends:
    print(name, age) 

print("white space")

countries =[
    {"name":"Colombia", "currency":"Peso"},
    {"name":"USA", "currency":"Dolar"},
    {"name":"Spain", "currency":"Euro"}
]

for country in countries:
    print(f'{country["name"]}')

for c in countries:
    print(f'{c["name"]} only manages {c["currency"]}')

print("another example with tuples")

people = [
	("Bob", 42, "Mechanic"),
	("James", 24, "Artist"),
	("Harry", 32, "Lecturer")
]

for name, age, profession in people:
	print(f"Name: {name}, Age: {age}, Profession: {profession}")


"""
From a list of dictionary to dictionary of list:


# create an empty dictionary
dictionary_of_list = {}
 
# for loop to convert list of dict
# to dict of list
for item in data:
    name = item['name']
    dictionary_of_list[name] = item
 
# display
dictionary_of_list

#Output

{'bobby': {'name': 'bobby', 'subjects': ['c/cpp', 'java']},
 'gnanesh': {'name': 'gnanesh', 'subjects': ['html', 'sql']},
 'ojsawi': {'name': 'ojsawi', 'subjects': ['iot', 'cloud']},
 'rohith': {'name': 'rohith', 'subjects': ['php', 'os']},
 'sravan': {'name': 'sravan', 'subjects': ['java', 'python']}}

"""