def cardio_risk(age,bmi,exercise,stress):

    risk = 0

    if age > 40:
        risk += 20

    if bmi > 30:
        risk += 25

    if exercise < 2:
        risk += 20

    if stress > 7:
        risk += 20

    return min(risk,100)
