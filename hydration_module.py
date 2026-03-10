def hydration_score(water,weight):

    recommended = weight * 0.033

    ratio = water / recommended

    if ratio >= 1:
        return 100

    return int(ratio * 100)
