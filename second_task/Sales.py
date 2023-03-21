import pandas as pd


def sales(file):
    table = pd.ExcelFile(file)

    clear_frame = pd.DataFrame(columns=['№ TT', 'НЕДЕЛЯ', 'КОЛ-ВО'])
    frames = [clear_frame]

    for sheet in table.sheet_names:
        if 'Sales - ' in sheet:
            df = table.parse(sheet, header=None)

            if df.isnull().values.any():
                df = df.dropna()

            df = df[1:]
            df.columns = ['№ TT', 'НЕДЕЛЯ', 'КОЛ-ВО']
            df = df.reset_index(drop=True)

            frames.append(df)

    return pd.concat(frames, axis=0, ignore_index=True, sort=False)
