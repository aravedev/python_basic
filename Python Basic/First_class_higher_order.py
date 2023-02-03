
operations={

    "average": lambda seq: sum(seq) / len(seq),
    "total": lambda seq: sum(seq),
    "top": lambda seq: max(seq)

}

students=[
{"name":"Rolf", "grades":(67,90,95,100)},
{"name":"Bob", "grades":(59,78,80,90)},
{"name":"Jen", "grades":(98,90,95,99)},
{"name":"Anne", "grades":(100,100,95,100)},

]

for student in students:
    name=student["name"]
    grades= student["grades"]

    print(f'Student:{name}')
    operation=input("Enter 'average', 'total' or 'top'")

    result = operations[operation](grades)
    print(result)


"""
Dictionaries with lambda functions:

We are running a loop through students dictionary,
when the user gives us the "key"(average,total,top), we search for that key word
into our operations dictionary and its value is a lambda function that recevies one argument.

because, we are running into students, we have access to grades.
In summary , we are using 2 different dict at the same time, but our main dict is students.

result = operations[operation](grades)

"""