def calculate_powers(limit=10**9):
    result = []
    n = 0
    while True:
        value = 3 * (2 ** n)
        if value > limit:
            break
        result.append(value)
        n += 1
    return result

print(calculate_powers())
