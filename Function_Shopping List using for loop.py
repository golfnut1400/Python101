

shopping_list = ["banana","orange","apple"]

stock = {"banana": 6, "apple": 10, "orange":32, "pear": 15}

prices = {"banana": 4.0, "apple": 2.0, "orange": 1.5, "pear": 3.0}


def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total = total + prices[item]
            stock[item] = stock[item] - 1
    return total



print (compute_bill(shopping_list))



