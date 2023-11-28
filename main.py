#!/usr/bin/env python3
import pandas as pd
import seaborn as sns 


def pp_dataset(ds: pd.DataFrame):
    mn = ds['registered'].mean()
    med = ds['registered'].median()
    mn2 = ds['cnt'].mean()
    med2 = ds['cnt'].median()
    print(f'Registered values: mean - {mn}, median - {med} ')
    print(f'Count values: mean - {mn2}, median - {med2} ')


def main():
    dataset = pd.read_csv('https://github.com/SamHuang1018/Bike-Sharing-from-UCI-datasets/raw/main/day.csv')
    pp_dataset(dataset)
    print('======== resample by month ===========')
    dataset['dteday'] = dataset['dteday'].astype('datetime64[ns]')
    dataset = dataset.reset_index().set_index('dteday')
    dataset = dataset.resample('W').sum([ 'registered', 'cnt']).filter([ 'registered', 'cnt'])
    pp_dataset(dataset)

if __name__ == '__main__':
    main()
