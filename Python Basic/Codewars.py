
"""
def take(arr,n):
 return arr[:n]

arr = [0, 1, 2, 3, 5, 8, 13]

n=4

print(take(arr,n))

"""

"""
Problem 2:

Description:

Americans are odd people: in their buildings, the first floor is actually the ground floor and there is no 13th floor (due to superstition).

Write a function that given a floor in the american system returns the floor in the european system.

With the 1st floor being replaced by the ground floor and the 13th floor being removed, the numbers move down to take their place. In case of above 13, they move down by two because there are two omitted numbers below them.

Basements (negatives) stay the same as the universal level.

More information here

Examples
1  =>  0 
0  =>  0
5  =>  4
15  =>  13
-3  =>  -3

My solution:

def get_real_floor(n):

    if n==0 or n==1:
        return 0 
    elif n<=12 and n>=2:
        return n-1
    elif n>=13:
        return n-2
    else:
        return n


print(get_real_floor(15))

Forum solution:

def get_real_floor(n):
    return n - (n > 0) - (n > 13)

"""

