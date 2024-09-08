def days_in_month(month):
    switcher={
            'january':31,
            'february':28,
            'march':31,
            'april':30,
            'may':31,
            'june':30,
            'july':31,
            'august':31,
            'september':30,
            'october':31,
            'november':30,
            'december':31
            }
    return switcher.get(month,"invalid month")
print(days_in_month("february"))
print(days_in_month("april"))
print(days_in_month("invalid"))

