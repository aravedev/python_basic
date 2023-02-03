"""

List on python is the same than an array in javascript

"""

friend=["Juan","Melania","Joud"]
print(friend[0])
print(f"the length of your friend's list is {len(friend)}")

"""
Creating a list with list inside of itself
"""

friends = [
            ["Juan",24],
            ["Melania",17],
            ["Joud",18],
            ["Kudzai",18]
        ]

print(friends[1][0])

"""
Add a new element to the list:
friend.append("Yegor") // This string will be added at the end of the list
friend.remove("Jaun") // This will remove the name from the list


"""

friend.append("Yegor")
print(friend)
friend.remove("Juan")
print(friend)

"""
The same way if you want to remove any data of a list with multiples list inside.
friends.remove(["Joud",18])
"""
print(friends)
friends.remove(["Joud",18])
print(friends)
