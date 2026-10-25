
def calculate_total(salaries):
    total = 0

    for salary in salaries:
        total += salary

    return total


def calculate_average(total, n):
    return total / n


def count_high_salary(salaries):
    count = 0

    for salary in salaries:
        if salary > 30000:
            count += 1

    return count

