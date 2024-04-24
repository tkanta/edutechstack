
def if_statement():
    num = 5
    if num == 5:  # The condition is true
        print("The number is equal to 5")  # The code is executed

    if num > 5:  # The condtion is false
        print("The number is greater than 5")  # The code is not executed


def condition_logical():
    num = 12
    if num % 2 == 0 and num % 3 == 0 and num % 4 == 0:
        # Only works when num is a multiple of 2, 3, and 4
        print("The number is a multiple of 2, 3, and 4")
    if num % 5 == 0 or num % 6 == 0:
        # Only works when num is either a multiple of 5 or 6
        print("The number is a multiple of 5 and/or 6")


def nested_if():
    num = 63

    if 0 <= num <= 100:
        if 50 <= num <= 75:
            if 60 <= num <= 70:
                print("The number is in the 60-70 range")


def create_edit():
    num = 10
    if num > 5:
        num = 20  # Assigning a new value to num
        new_num = num * 5  # Creating a new value called newNum

    # The if condition ends, but the changes made inside it remain
    print('num: ', num)
    print('new number: ', new_num)


def conditional_exp():
    num = 30
    output = "The number is less than 60" \
        if num < 60 else "The number is greater than 60"
    # output = 24 if num < 60 else 56
    print(output)


def if_else():
    num = 60

    if num <= 50:
        print("The number is less than or equal to 50")
    else:
        print("The number is greater than 50")


def if_elif_else():
    light = "Red"

    if light == "Green":
        print("Go")

    elif light == "Yellow":
        print("Caution")

    elif light == "Red":
        print("Stop")

    else:
        print("Incorrect light signal")


if __name__ == '__main__':
    # if_statement()
    # condition_logical()
    # nested_if()
    # create_edit()
    # conditional_exp()
    # if_else()
    if_elif_else()
