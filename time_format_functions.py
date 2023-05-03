def ordinal(n):
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return str(n) + suffix


def custom_date_format(date):
    day = ordinal(date.day)
    month = date.strftime('%B')
    year = date.year
    return f"{day} of {month} {year}"
