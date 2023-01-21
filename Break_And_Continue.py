
cars = ["ok","ok","ok","ok","faulty","ok","ok"]

for status in cars:

    if status == "faulty":
        print(f'Found faulty car. {status}')
        #break
        continue
    else:
        print(f'This car is {status}, sending to customer')

