from csv import reader


def get_maria_order(maria_food, order):
    food = order[1]
    if order not in maria_food:
        maria_food[food] = 1
    else:
        maria_food[food] += 1
