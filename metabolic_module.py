def diabetes_risk(bmi,activity,sugar):

    score = 0

    if bmi > 30:
        score += 30

    if activity < 2:
        score += 25

    if sugar > 50:
        score += 25

    return min(score,100)
