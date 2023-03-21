import pandas as pd


def store(file):
    table = pd.ExcelFile(file)

    df = table.parse(table.sheet_names[1])
    pd.set_option('display.max_columns', None)

    df.loc[149:, (df.columns[3:])] = df.loc[149:, (df.columns[2:8])]

    return df
