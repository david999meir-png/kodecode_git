def calculate_price(items, tax=0.17):
    total = 0
    for i in items:
        total = total + i * (1 + tax)
    return total
