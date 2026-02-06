def calculate_health_score(revenue, expenses):
    if revenue <= 0:
        return 0

    margin = (revenue - expenses) / revenue

    if margin > 0.3:
        score = 85
    elif margin > 0.15:
        score = 70
    elif margin > 0:
        score = 50
    else:
        score = 30

    return score
