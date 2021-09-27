import math
def cakes(recipe, available):
    total = -1
    for k,v in recipe.items():
        if available.get(k) is not None:
            currentval = math.floor(available.get(k) / v)
            if total == -1 or total > currentval:
                total = currentval
        else:
            return 0
    return total
