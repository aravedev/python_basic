
friends = ["Rolf","Charlie","Anna","Bob","Jen"]

# Getting friends position 2 and 4
print(friends[2:4])

"""
With slicing we excludes the last element, is like when you use the symbols < or >

slice[starts:ends]

Skipping elements:
friends[1:] ... give me all the results except first element.

Note: Here we arent talking about index, we know that with index in a list
the position starts from 0 , but with slice

friends[1:] , first position makes reference to index 0.
print(friends[:4]) elements from first position except fourth position

Copying the elements of a list:
friends[:]

* Taking elements in reverse
friends[starts:ends]
friends[-3:] .. the counting starts from last element,move -3 positions and from there takes the rest of data

"""

print(friends[1:])
print(friends[:4]) # elements from first position except fourth position

copy_friends = friends[:]
print(copy_friends)

print("Starting in reverse order")
print(friends[-3:])
print("another one")
print(friends[-3:4])
print(f'friends[stars:ends] ... friends[:-2] is {friends[:-2]}')