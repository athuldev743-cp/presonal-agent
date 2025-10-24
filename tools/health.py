def check_heart_rate(rate: int):
    if rate < 60:
        return "Your heart rate is a bit low, you should rest."
    elif rate > 100:
        return "Your heart rate is high, please relax."
    else:
        return "Your heart rate looks normal."
