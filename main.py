#!/usr/bin/env python3
import pandas as pd
import seaborn as sns 


def pp_dataset(ds: pd.DataFrame):
    df = pd.DataFrame(ds['registered'].mean())
    df.merge(ds.cnt.mean(), left_index=on, right_index=on)
    print(df)

def main():
    dataset = pd.read_csv('https://github.com/SamHuang1018/Bike-Sharing-from-UCI-datasets/raw/main/day.csv')
    print(dataset.info())

if __name__ == '__main__':
    main()
