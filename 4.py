
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

# Test Cases
print(get_cars_by_make(cars_list, 'Tesla'))
print(get_cars_by_price(cars_list, 20000, 50000))
print(get_cars_by_make(cars_list, 'Ford'))
print(get_cars_by_price(cars_list, 10000, 20000))

print(get_cars_by_make(cars_list, 'Buick'))


