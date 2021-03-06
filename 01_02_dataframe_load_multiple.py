import pandas as pd

def test_run():
    start_date='2016.01.01'
    end_date='2016.01.08'
    dates=pd.date_range(start_date,end_date)
    print(dates[0])
    df1=pd.DataFrame(index=dates)
    dfEU = pd.read_csv("data/EURUSD1440.csv",index_col="Date",parse_dates=True,usecols=['Date','Close'],
                           na_values=['nan'])

    dfEU = dfEU.rename(columns={'Close':'EURUSD'})

    df1=df1.join(dfEU,how='inner')
   # df1=df1.dropna()

    symbols = ['GBPJPY','USDCHF','USDJPY']
    for symbol in symbols:
        dfTmp = pd.read_csv("data/{}1440.csv".format(symbol), index_col="Date", parse_dates=True, usecols=['Date', 'Close'],
                           na_values=['nan'])

        dfTmp = dfTmp.rename(columns={'Close': symbol})
        df1 = df1.join(dfTmp)

    print(df1)

if __name__ == "__main__":
    test_run()