"""Plot High prices for IBM"""

import pandas as pd
import matplotlib.pyplot as plt


def test_run():
    df = pd.read_csv("data/GBPJPY1440.csv")
    # TODO: Your code here
    df['Close'].plot()
    df[['High','Low']].plot()
    plt.show()  # must be called to show plots


if __name__ == "__main__":
    test_run()
