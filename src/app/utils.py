import pandas as pd

def load_combined_data():
    files = {
        'Benin': '../../data/benin_clean.csv',
        'SierraLeone': '../../data/sierraleone_clean.csv',
        'Togo': '../../data/togo_clean.csv'
    }
    combined = []
    for country, path in files.items():
        df = pd.read_csv(path)
        tmp = df[['GHI','DNI','DHI']].copy()
        tmp['country'] = country
        combined.append(tmp)
    combined = pd.concat(combined, ignore_index=True)
    return combined

def summary_table(df):
    metrics = ['GHI','DNI','DHI']
    summary = df.groupby('country')[metrics].agg(['mean','median','std'])
    summary.columns = ['_'.join(col).strip() for col in summary.columns.values]
    return summary.reset_index()
