
#cars = ["ok","ok","ok","ok","ok","ok","ok"]

cars = ["ok","ok","ok","ok","faulty","ok","ok"]
all_successful=True

for status in cars:

    if status == "faulty":
        print(f'Stopping production. {status} car')
        all_successful=False
        break
        #continue
else:
    print(f'All cars were successfully. No faulty cars!')

"""
The else keyword for loops can be used for while and for loops, if everything is ok or depending of your
conditions.
"""