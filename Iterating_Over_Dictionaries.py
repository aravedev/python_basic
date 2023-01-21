
friend_ages = {"Rolf":27, "Anne":37, "Bob":22}

"""

Iterating using a for loop to get the key:values
1- For loop for keys
2- For loop for values

"""
# Getting the keys
for key in friend_ages:
    print(f'{key}')

# Getting the values:
for value in friend_ages.values():
    print(value)

# Getting both using destructuring:
for key,value in friend_ages.items():
    print(f'{key} is {value} years old')