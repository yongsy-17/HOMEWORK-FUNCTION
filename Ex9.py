# EX9.Create function to find average of price
# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]
def average(array):
    total_price = 0
    for product in array:
        total_price += product["price"]
    average_price = total_price / len(array)
    return average_price
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
print("Average Price:", average(products))