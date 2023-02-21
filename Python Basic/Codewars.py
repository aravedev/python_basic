
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


"""
You need to write a function that reverses the words in a given string. A word can also fit an empty string. If this is not clear enough, here are some examples:

As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

Example (Input --> Output)

"Hello World" --> "World Hello"
"Hi There." --> "There. Hi"

My solution:
str = 'joihapg  rauflry go'

def reverse(st):
    st=st.strip().split(" ")
    arr=[] 
    for l in reversed(st):
        if l != '':
            arr.append(l)
    
    return ' '.join(arr)
    

Forum solution:
def reverse(st):
    st = st.split()
    st.reverse()
    return ' '.join(st)

something you should know:
# for x in reversed(st):
#        arr.append(x)

Reversing using slice
#st = st[::-1]

Reversing using reverse
str.reverse()

"""
"""
Philip's just turned four and he wants to know how old he will be in various years in the future such as 2090 or 3044. His parents can't keep up calculating this so they've begged you to help them out by writing a programme that can answer Philip's endless questions.

Your task is to write a function that takes two parameters: the year of birth and the year to count years in relation to. As Philip is getting more curious every day he may soon want to know how many years it was until he would be born, so your function needs to work with both dates in the future and in the past.

Provide output in this format: For dates in the future: "You are ... year(s) old." For dates in the past: "You will be born in ... year(s)." If the year of birth equals the year requested return: "You were born this very year!"

"..." are to be replaced by the number, followed and proceeded by a single space. Mind that you need to account for both "year" and "years", depending on the result.

Good Luck!

Test: test.assert_equals(calculate_age(2012, 2016),"You are 4 years old.")
test.assert_equals(calculate_age(1989, 2016),"You are 27 years old.")
test.assert_equals(calculate_age(2000, 2090),"You are 90 years old.")
test.assert_equals(calculate_age(2000, 1990),"You will be born in 10 years.")
test.assert_equals(calculate_age(2000, 2000),"You were born this very year!")
test.assert_equals(calculate_age(900, 2900),"You are 2000 years old.")
test.assert_equals(calculate_age(2010, 1990),"You will be born in 20 years.")
test.assert_equals(calculate_age(2010, 1500),"You will be born in 510 years.")
test.assert_equals(calculate_age(2011, 2012),"You are 1 year old.")
test.assert_equals(calculate_age(2000, 1999),"You will be born in 1 year.")

My solution:

def calculate_age(year_of_birth, current_year):
    
    age = abs(current_year - year_of_birth)
    
    if age == 1 and (year_of_birth < current_year):
        return f"You are 1 year old."
    elif year_of_birth>current_year and age==1:
        return f"You will be born in 1 year."
    else:
        if year_of_birth<current_year:
            return f"You are {current_year-year_of_birth} years old."
        elif year_of_birth>current_year:
            return f"You will be born in {year_of_birth-current_year} years."
        else:
            return f"You were born this very year!"


Forum solution:

def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    if age == 0:
       return "You were born this very year!"
    elif age > 0:
       return "You are {} year{} old.".format(age, 's' if age > 1 else '')
    else:
       return "You will be born in {} year{}.".format(abs(age), 's' if abs(age) > 1 else '')

"""

"""
Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error".

def problem(a):
    if type(a) == str:
        return "Error"
    else:
        return (a*50)+6


print(problem(1))

"""


    





