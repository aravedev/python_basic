
def greet():
    name=input("What is your name?\n")
    print(f"Hello {name}")

#



car ={

    "make":"Ford",
    "model":"Fiesta",
    "mileage":2300,
    "fuel_consumed":460

}

cars =[

    {"make":"Ford","model":"Fiesta","mileage":23000,"fuel_consumed":460},
    {"make":"Ford","model":"Focus","mileage":17000,"fuel_consumed":350},
    {"make":"Mazda","model":"MX-5","mileage":49000,"fuel_consumed":900},
    {"make":"Mini","model":"Cooper","mileage":31000,"fuel_consumed":235},

]

def calculate_mpg(car_to_calculate:dict):
    mpg= car_to_calculate['mileage']/car_to_calculate['fuel_consumed']
    name=f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles per gallon")

for auto in cars:
    calculate_mpg(auto)