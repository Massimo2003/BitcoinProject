import pandas as pd
def get_df(csv):
    df=pd.read_csv(csv,parse_dates=True)
    df=df.set_index('time')
    return df
def getpartialcsv(csv,date1,date2):
    df=get_df(csv)
    newdf=df.loc[date1:date2,'PriceUSD']
    newcsv=newdf.to_csv('PartialCSV.csv')
    return newcsv