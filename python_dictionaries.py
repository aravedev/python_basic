
"""
Dictionaries store keys and values
"""

friend_ages = {
    "Rolf":24,
    "Adam":30,
    "Anne":27

}

print(friend_ages)
print(friend_ages["Rolf"])

"""
Adding values in dictinaries

"""

friend_ages["Bob"]=23

"""
Change values in a dictionary
"""
friend_ages["Rolf"]= 25

print(friend_ages)

"""
Suposse that you want to store multiple values in your dictionary for example, name and age
you can achive this task using tuples and dictionaries together
"""

friends = (

    {"name":"Rolft Smith", "age":24},
    {"name":"Adam Wool", "age":30},
    {"name":"Anne Pun", "age":27},

)

print(friends[0])
print(friends[0]["name"])

"""
Converting a list that contains tuples into a dictionary with the function dict
"""

friends = [("Rolf",24),("Adam",30),("Anne",27)]
friends = dict(friends)

print(friends)