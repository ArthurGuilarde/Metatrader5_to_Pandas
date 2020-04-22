import pandas as pd
from MetaTrader5_Pandas import formatingMT5Data

# Intraday example
df = pd.read_csv('intraday_example.csv', delimiter="\t")
formatingMT5Data(df)

# Daily example
df = pd.read_csv('daily_example.csv', delimiter="\t")
formatingMT5Data(df, isIntraday=False)