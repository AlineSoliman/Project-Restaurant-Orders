from csv import reader


def get_maria_order(maria_food, order):
    food = order[1]
    if order not in maria_food:
        maria_food[food] = 1
    else:
        maria_food[food] += 1


def data_from_csv(
    maria_food,
):
    most_ordered = None
    ordered_times = 0

    for order in maria_food:
        if maria_food[order] > ordered_times:
            most_ordered = order
            ordered_times = maria_food[order]

    with open("data/mkt_campaign.txt", mode="w") as file:
        file.writelines(f"{most_ordered}\n")
        file.close()


def get_csv_data(csv_list):
    maria_food = {}

    for client, order in csv_list:
        if client == "maria":
            get_maria_order(maria_food, order)

    data_from_csv(maria_food)


def analyze_log(path_to_file):
    pass
