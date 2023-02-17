class TrackOrders:
    def __init__(self):
        self._orders = []

    def __len__(self):
        return len(self._orders)

    def add_new_order(self, customer, order, day):
        self._orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        food = dict()
        for order in self._orders:
            if order[0] == customer:
                if order[1] not in food:
                    food[order[1]] = 1
                else:
                    food[order[1]] += 1
        most_ordered_food = max(food, key=food.get)
        return most_ordered_food

    def get_never_ordered_per_customer(self, customer):
        food_list = set()
        food_ordered = set()
        for order in self._orders:
            food_list.add(order[1])
            if order[0] == customer:
                food_ordered.add(order[1])
        return food_list.difference(food_ordered)

    def get_days_never_visited_per_customer(self, customer):
        days_list = set()
        days_ordered = set()
        for order in self._orders:
            days_list.add(order[2])
            if order[0] == customer:
                days_ordered.add(order[2])
        return days_list.difference(days_ordered)

    def get_busiest_day(self):
        new_day_list = dict()
        for order in self._orders:
            if order[2] not in new_day_list:
                new_day_list[order[2]] = 1
            else:
                new_day_list[order[2]] += 1
        busiest_day = max(new_day_list, key=new_day_list.get)
        return busiest_day

    def get_least_busy_day(self):
        new_day_list = dict()
        for order in self._orders:
            if order[2] not in new_day_list:
                new_day_list[order[2]] = 1
            else:
                new_day_list[order[2]] += 1
        least_busy_day = min(new_day_list, key=new_day_list.get)
        return least_busy_day
