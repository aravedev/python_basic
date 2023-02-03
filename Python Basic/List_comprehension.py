
numbers = [1,2,3,4]
double_n=[]
# using list comprehension:

"""
I want to take a number and multiply it by 2 , in my list of numbers
"""
for number in numbers:
    double_n.append(number*2)

# the aboove code is exactly the same as below example 

double_numbers= [number * 2 for number in numbers]
print(double_numbers)

names = ["Rolf","Boob","Jen"]
names_lower_case = [name.lower() for name in names]
print(names_lower_case)

countries = ["Spain","Poland","USA","Colombia"]
nationality = input("Where are you from?")

countries = [country.lower() for country in countries]
if nationality.lower() in countries:
    print(f"{nationality} is a nice country, I have been there once :)")
else:
    print("Wow, sounds great! I should go there someday") 