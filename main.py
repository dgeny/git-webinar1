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
<<<<<<< HEAD
=======
<<<<<<< HEAD

=======
def main():
    dataset = pd.read_csv('https://github.com/SamHuang1018/Bike-Sharing-from-UCI-datasets/raw/main/day.csv')
    pp_dataset(dataset)
>>>>>>> parent of 676853a (add custom print function #2)
=======
>>>>>>> parent of 69926c9 (git reset --mixed by task #3)
    print('======== resample by month ===========')
    dataset['dteday'] = dataset['dteday'].astype('datetime64[ns]')
    dataset = dataset.reset_index().set_index('dteday')
    dataset = dataset.resample('W').sum([ 'registered', 'cnt']).filter([ 'registered', 'cnt'])
    pp_dataset(dataset)
<<<<<<< HEAD
=======
>>>>>>> parent of 9046d58 (remove resampling by example)
>>>>>>> parent of 69926c9 (git reset --mixed by task #3)

if __name__ == '__main__':
    main()
