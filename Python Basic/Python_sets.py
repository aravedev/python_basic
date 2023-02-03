"""
Sets are other collection, they contain multiple values and the key difference is that set dont hold order and dont contain duplicate elements.

"""

art_friends = {"Rolf","Anne"}
science_friends={"Jen","Charlie"}

"""
Adding using .add a new friend in your set, remember that sets dont hold order, so your new value could be located in a random index
"""
art_friends.add("Jen")
art_friends.add("Jen")

print(art_friends)

"""
Removing using .remove
"""

art_friends.remove("Anne")
print(art_friends)

"""
Sets are useful when you want to compare 2 sets, which element are shared and which arent.
Some operations with sets:
set1.difference(set2)
"""

art_friends = {"Rolf","Anne","Jen"}
science_friends = {"Jen", "Charlie"}

"""
Lets check which person is only in one of the sets of friends
"""

# Rolf and Anne are in Art but not in science friends
print("\n")
art_but_not_science = art_friends.difference(science_friends) 
print("Friends that are only in Art set")
print(art_but_not_science)

"""
Simetric difference shows you which members are in both sets
"""

not_in_both = art_friends.symmetric_difference(science_friends)
print("Not in both")
print(not_in_both)

"""
In sets you also have intersection set1.intersection(set2) , it gives you the result
of which values are shared by both sets.
"""
art_and_science = art_friends.intersection(science_friends)
print("Intersection")
print(art_and_science)

"""
Getting all the values in both sets without duplicates, you can do it using
set1.union(set2)
"""

all_friends = art_friends.union(science_friends)
print("All friends using .union ")
print(all_friends)

"""
Summary:

Add ... set1.add(yourValue)
remove ..set1.remove(yourValue)
difference.. set1.difference(set2) // values are in set1 but not in set2
symmetric_difference ..set1.symmetric_difference(set2) // values arent shared in both sets
intersection ...set1.intersection(set2) // values shared in both sets
union ...set1.union(set2) // union both sets without duplicate values

"""