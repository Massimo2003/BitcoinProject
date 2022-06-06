import pandas as pd
def get_df(csv):
    df=pd.read_csv(csv,parse_dates=True)    
    return df
def getpartialcsv(date1,date2):
    df=get_df('btc.csv')
    df=df.set_index('time')
    newdf=df.loc[date1:date2,'PriceUSD']
    newcsv=newdf.to_csv('PartialCSV.csv')
    dffinal=get_df('PartialCSV.csv')
    return dffinal
