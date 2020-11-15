from datetime import date

def retype_date(string):
    seps = '/', '.', '-', ' '
    bdate = None

    idx = 0
    while idx < len(seps):
        if seps[idx] in string:
            bdate = string.split(seps[idx])
            break
        else:
            idx += 1
    day, month, year = bdate
    result = date(
        year=int(year),
        month=int(month),
        day=int(day)
    )

    return result
