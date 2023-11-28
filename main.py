#!/usr/bin/env python3
import pandas as pd
import seaborn as sns 


def pp_dataset(ds: pd.DataFrame):
    mn = ds['registered'].mean()
    med = ds['registered'].median()
    print(f'Registered values: mean - {mn}, median - {med} ')

def main():
    dataset = pd.read_csv('https://github.com/SamHuang1018/Bike-Sharing-from-UCI-datasets/raw/main/day.csv')
    pp_dataset(dataset)

if __name__ == '__main__':
    main()
