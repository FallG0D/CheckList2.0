from datetime import datetime

def retype_date(string='20/06/2006'):
    seps = '/', '.', '-', ' '
    bdate = None

    idx = 0
    while idx < len(seps):
        if seps[idx] in string:
            bdate = string.split(seps[idx])
            break
        else:
            idx += 1

    return bdate

retype_date()