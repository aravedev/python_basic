
"""
Tuples are similar to a list, but there a few difference that we will explain later.

short_tuple = "Rolf","Bob"
a_bit_clearer= ("Rolf","Bob") // parenthesis arent requiered, but sometimes python needs them to understand
and dont get errors

"""

friends=("Rolf","Bob","Anne")
print(friends)

"""
You cant insert an extra element like in a list, the only thing that you can do is reasign the same variable
and add your new value as the example below, dont forget to put a "," after your string.
"""

friends = friends + ("Jen",)
print(friends)

"""
Conclusion: Tuples dont allowed modification, if you want to remove a value from your tuple, this isnt valid and instead you will get an error, otherwise List are used when you want to add or remove data.

"""