class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
        self.value = self.price / self.weight


class Activity:
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def get_finish(self):
        return self.finish


# min possible lines for train station based on arrivals and departures
def train_lines(arraivals, departures):  # O(nlogn)
    arraivals.sort()
    departures.sort()  # nlogn
    max_trains = 0
    curr_trains = 0
    a = 0
    d = 0
    while a < len(arraivals):  # len(arrivals) + len(departures) -> O(m+n)
        if arraivals[a] < departures[d]:
            curr_trains += 1
            a += 1
        else:
            curr_trains -= 1
            d += 1
        max_trains = max(max_trains, curr_trains)
    return max_trains


# fill the sack with max possible value of items. for better alg need to do it with dynamic programming
def knapsack(items, sacksize):  # О(nw) n - num of items, w - sack weight
    sack = []
    curr_weight = 0
    while len(items):  # w - times
        max_value_item = None
        for item in items:  # n - times
            if max_value_item == None or item.value > max_value_item.value:
                max_value_item = item
        if max_value_item.weight + curr_weight <= sacksize:
            sack.append(max_value_item)
            curr_weight += max_value_item.weight
        items.remove(max_value_item)
    return sack


# algorithm chooses as much as possible activities from activity list without crossing
def activity_selection(activities):  # O(nlogn) = n + nlogn
    result = []
    activities.sort(key=Activity.get_finish)  # nlogn
    last_activity = None
    for activity in activities:  # n
        if last_activity is None or last_activity.finish < activity.start:
            result.append(activity)
            last_activity = activity
    return result


if __name__ == '__main__':
    pass
