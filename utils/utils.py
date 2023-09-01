

def valueToDisplayValue(value):
    num = value
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    result = round(value / (1000**magnitude),2)
    return '{}{}'.format(result, ['', 'K', 'M', 'B', 'T'][magnitude])


def QueryDocToList(response):
    result = []
    for x in response :
        result.append(x)
    return result