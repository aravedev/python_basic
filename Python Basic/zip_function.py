
friends = ["Rolf","Bob","Jen","Anne"]
time_since_seem = [3,7,15,11]

# Creating a dictionary that takes the key in a new dictionary and set as value the time_since_seem
long_timers = {

    friends[i]:time_since_seem[i]
    for i in range(len(friends))

}

print(long_timers)

"""
zip function does exactly the same as the code above but with less lines.

dict(zip(arr1,arr2)) or list(zip(arr1,arr2))

"""
print("using zip function")
print(dict(zip(friends,time_since_seem)))

"""
Using zip function also works for more than 2 list, but this method only works for list not with dictionaries
"""

number = [3,4,5,6]

print(list(zip(friends,time_since_seem,number)))