def unit_converter(item_weight, item_unit):
    """convert grams or ml to kg and l"""
    if item_unit == "ml" or item_unit == "g":
        item_weight = item_weight / 1000
    else:
        item_weight = item_weight
    return item_weight

weight = int(input("what is the weight? "))
unit = input("what is the unit? ")
a = unit_converter(weight, unit)
print(a)