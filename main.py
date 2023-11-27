#!/usr/bin/env python3
import pandas as pd
import seaborn as sns 


def main():
    dataset = pd.read_csv('https://github.com/SamHuang1018/Bike-Sharing-from-UCI-datasets/raw/main/day.csv')
    print(dataset.info())

if __name__ == '__main__':
    main()
