
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


## Another example

import random
names=[
    {"name":"Juan", "person":"0"},
    {"name":"Joud", "person":"0"},
    {"name":"Melania", "person":"0"},
    {"name":"Danny", "person":"0"}
    
    ]
    
name_list=["Juan","Joud","Melania","Danny"]
random.shuffle(name_list)    
i=0

while(i<len(name_list)):
    names[i]['person']=name_list[i]
    print(f'{names[i]["name"]} corresponds {names[i]["person"]}')
    i=i+1