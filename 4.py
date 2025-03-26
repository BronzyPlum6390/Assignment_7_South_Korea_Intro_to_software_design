def get_cars_by_make(cars_list, maker):
    cars_by_make = []
    for car in cars_list:
        if car['maker'] == maker:
            cars_by_make.append(car)
            
    return cars_by_make

def get_cars_by_price(cars_list, min_price, max_price):
    cars_by_price = []
    for car in cars_list:
        if min_price <= car['price'] <= max_price:
            cars_by_price.append(car)
            
    return cars_by_price
    
def get_user_input() -> int:
    user_input = input("***** Search method *****\n1. Make\n2. Price\n3. Exit\nChoose a method: ")

cars_list = [
{'maker': 'Toyota', 'model': 'Camry', 'year': 2019, 'color':
'red', 'price': 22000},
{'maker': 'Honda', 'model': 'Civic', 'year': 2020, 'color':
'blue', 'price': 18000},
{'maker': 'Hyundai', 'model': 'Tucson', 'year': 2023,
'color': 'grey', 'price': 27000},
{'maker': 'Tesla', 'model': 'Model 3', 'year': 2021, 'color':
'white', 'price': 40000},
{'maker': 'Chevrolet', 'model': 'Corvette', 'year': 2022,
'color': 'black', 'price': 65000},
{'maker': 'Tesla', 'model': 'Model Y', 'year': 2022, 'color':
'blue', 'price': 70000}
]


user_input = input("***** Search method *****\n1. Make\n2. Price\n3. Exit\nChoose a method: ")

while int(user_input) != 3:
    user_input = int(user_input)
    if user_input == 1:
        make = input("Enter the make of the car: ")
        print(get_cars_by_make(cars_list, make))
        user_input = input("***** Search method *****\n1. Make\n2. Price\n3. Exit\nChoose a method: ")
    elif user_input == 2:
        min_price = int(input("minimum price: "))
        max_price = int(input("maximum price: "))
        print(get_cars_by_price(cars_list, min_price, max_price))
        user_input = input("***** Search method *****\n1. Make\n2. Price\n3. Exit\nChoose a method: ")
    elif user_input == 3:
        break

    
print("bye")
        




