
friends = ["Rolf","Anne","Charlie"]

print(f"My friends are {friends}")

"""
As you see, we get an awful result
My friends are ['Rolf', 'Anne', 'Charlie']

We can solve this situation using join:
comma_separated = ", ".join(friends)

Basically, join takes each value of friend's list and add them the ", " , printing out a better statement
We will get at the end a string with the values as in javascript.

"""
comma_separated = ", ".join(friends)
print(comma_separated)