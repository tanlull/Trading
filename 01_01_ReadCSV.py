import pandas as pd


def test_run():
    """Function called by Test Run."""
    df = pd.read_csv("data/GBPJPY1440.csv")
    print(df.tail())
    # TODO: Print last 5 rows of the data frame


if __name__ == "__main__":
    test_run()



