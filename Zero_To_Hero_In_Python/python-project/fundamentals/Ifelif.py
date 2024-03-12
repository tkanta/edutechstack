# if elif condition
def if_elif():
    light = "Red"
    if light == "Green":
        print("Go")
    elif light == "Yellow":
        print("Caution")
    elif light == "Red":
        print("Stop")
    else:
        print("Incorrect light signal")


# discounted price
def discounted_price():
    price = 50
    if price >= 300:
        price *= 0.7  # (1 - 0.3)
    elif price >= 200:
        price *= 0.8  # (1 - 0.2)
    elif price >= 100:
        price *= 0.9  # (1 - 0.1)
    elif 100 > price >= 0:
        price *= 0.95

    print('price -->', price)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if_elif()
    discounted_price()
