def overall_health_score(bmi,hydration,cardio,diabetes):

    score = 100

    if bmi > 30:
        score -= 15

    if hydration < 60:
        score -= 10

    score -= cardio * 0.2

    score -= diabetes * 0.2

    return int(max(score,0))
