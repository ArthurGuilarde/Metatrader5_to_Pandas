import pandas as pd
def formatingMT5Data(df, isIntraday=True):
  #Formating columns
  def formatingColumns(df_columns_values):
    columnsLowerFormat = map(str.lower, df_columns_values)
    columnsFormated = map(lambda x: x.replace('<', '').replace('>', ''), list(columnsLowerFormat))

    return list(columnsFormated)

  #Create column dateTime
  def dateTimeColumnFormat(df, isIntraday=True):
    if isIntraday:
      df.date =  df.date + ' ' + df.time
      del df['time']

    df.date = pd.to_datetime(df.date)

    return df

  df.columns = formatingColumns(df.columns)
  
  return dateTimeColumnFormat(df, isIntraday)