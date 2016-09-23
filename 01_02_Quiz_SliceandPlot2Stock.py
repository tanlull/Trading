"""Utility functions"""

import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}1440.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'EURUSD')

    for symbol in symbols:
        # TODO: Read and join data for each symbol
        dfTmp = pd.read_csv(symbol_to_path(symbol), index_col="Date", parse_dates=True, usecols=['Date', 'Close'],
                            na_values=['nan'])

        dfTmp = dfTmp.rename(columns={'Close': symbol})
        df = df.join(dfTmp)
        if symbol == 'EURUSD':
            df = df.dropna(subset=['EURUSD'])
            #df = df.dropna()

    return df


def plot_data(df, title="Stock prices"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    df = normalize_data(df)
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()


def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range."""
    # TODO: Your code here
    # Note: DO NOT modify anything else!
    x = df.ix[start_index:end_index,columns]
    plot_data(x)

def normalize_data(df):
    print df.ix[0]
    df = df/df.ix[0]
    return df

def test_run():
    # Define a date range
    dates = pd.date_range('2015.01.01', '2015.12.31')

    # Choose stock symbols to read
    symbols = ['GBPJPY','USDCHF','USDJPY']

    # Get stock data
    df = get_data(symbols, dates)
    plot_selected(df, ['GBPJPY', 'USDJPY'], '2015.01.01', '2015.02.10')



if __name__ == "__main__":
    test_run()
