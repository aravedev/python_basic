
# For loops are like forEach in other langugaes.

friends = ["Rolf","Jen","Anne"]

for f in friends:
    print(f)

# Running for loop with index position
for index, friend in enumerate(friends):
    print(f"Hello {friend}, you are the number {index+1} in the queue")


# using a dictionary
students = [

    {"name":"Rolf", "grade":90},
    {"name":"Bob", "grade":78},
    {"name":"Jen", "grade":100},
    {"name":"Anne", "grade":80}

]

print("white space left...")

for student in students:
    print(f'{student["name"]} your score was {student["grade"]}')