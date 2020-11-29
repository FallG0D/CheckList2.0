from datetime import date
import pandas as pd

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

def read_db(name):
    df = pd.read_csv(name, index_col=0)
    return df

def write_db(data, name):
    df = read_db(name)
    
    df = df.append(data, ignore_index=True)
    
    df = df.dropna(how='all', axis=0)
    df = df.drop_duplicates(subset=df.columns[:-2], keep='last')
    
    df.to_csv(name, index=True)