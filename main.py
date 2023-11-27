#!/usr/bin/env python3
import pandas as pd
import seaborn as sns 


def main():
    dataset = pd.read_csv('https://www.kaggle.com/datasets/damianogalassi/bike-sharing-datasets/download?datasetVersionNumber=1')
    print(dataset.info())

if __name__ == '__main__':
    main()
