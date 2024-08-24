def core_calculate_total(subtotal, shipping, discount, tax_percent):
    amount = subtotal + shipping - discount
    if amount < 0:
        total = 0
    else:
        total = amount * (1 + tax_percent)

    rounded = round(total, 2)
    return rounded