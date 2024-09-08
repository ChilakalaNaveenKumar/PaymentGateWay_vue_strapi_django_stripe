def calculate_total_cost(base_price, tax_rate=0.1, discount=None):
    tax = base_price * tax_rate
    total = base_price + tax

    if discount:
        total -= discount

    return total
