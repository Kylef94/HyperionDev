
def hotel_cost(nights):
    '''returns cost of hotel stay
    inputs: nights - int'''
    price_per_night = 100
    return nights * price_per_night

def plane_cost(city):
    '''returns cost of flight
        inputs: city - string'''
    cost = {"London": 200,
            "New York": 700,
            "Paris": 150,
            "Hanoi": 1500,
            "Zurich": 200}
    return cost[city]

def car_rental(days):
    '''returns cost of car rental
        inputs: days - int'''
    day_rate = 50
    return days * day_rate

def holiday_cost(nights, city, car_days):
    '''returns cost of overall holiday
        inputs:
        nights - int
        city - string
        days - int'''
    return hotel_cost(nights) + plane_cost(city) + car_rental(car_days)

print(holiday_cost(5, 'London', 5))
print(holiday_cost(15, 'Hanoi', 12))
print(holiday_cost(7, 'Paris', 5))