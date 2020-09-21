import pandas as pd
from datetime import date

pd.set_option('max_columns', 60)
csv_url = 'https://dl.dropboxusercontent.com/s/6mztoeb6xf78g5w/COVID-19.csv'
df = pd.read_csv(csv_url, low_memory=False)

selected_cols = ['年代','性別','確定日','発症日','居住都道府県','X','Y']
df1 = df[selected_cols]
df1 = df1.dropna(how='all')
df1['count'] = 1

# convert to calculatable
# 0-10 convert to 1.
# unknown convert to 50 50 is javanezes average age.
# over 90 convert to 90.
# over 100 convert to 100.
df1['年代'] = df1['年代'].apply(lambda x: x.replace('0-10','1'))
df1['年代'] = df1['年代'].apply(lambda x: x.replace('不明','50'))
df1['年代'] = df1['年代'].apply(lambda x: x.replace('90以上','90'))
df1['年代'] = df1['年代'].apply(lambda x: x.replace('100歳以上','100'))
df1['年代'] = df1['年代'].apply(lambda x: int(x))

df1.to_csv('data/covid_19_update.csv')

