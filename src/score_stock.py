def score_stock(stock):
    score = 0
    if stock["pass"]:
        score += 1
    if stock["iv_jump"] > 20:
        score += 1
    if stock["call_put_ratio"] > 1:
        score += 1
    if stock["premium"] > 50000:
        score += 1
    return score

