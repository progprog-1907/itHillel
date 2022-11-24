def travel(input_list_tuple):
    flight_hotel_prices = {
        "Moscow": (50, 300),
        "Kiev": (40, 230),
        "Istanbul": (60, 250),
        "Vancouver": (100, 600)
    }
    result = flight_hotel_prices[input_list_tuple[len(input_list_tuple) - 1][1]][1]
    for days, city in input_list_tuple:
        result += flight_hotel_prices[city][0] * days + flight_hotel_prices[city][1]
    return result


data = travel([(3, "Moscow"), (4, "Istanbul"), (2, "Vancouver")])
print(data)
