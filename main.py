def calc(subTotal, percent):
    tip = subTotal * (percent / 100)
    total = subTotal + tip

    total = str(total)
    tip = str(tip)

    return "The total is $" + total + ". The tip is $" + tip