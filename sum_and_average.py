import pandas as pd
import numpy as np


#adds a column with the total amount sold
#all changes are written to the same database
def sum_total(dataset, n_periods, filename):

    col_list = list(dataset)
    col_list = col_list[:n_periods + 1]

    dataset['sum'] = dataset[col_list].sum(axis=1)
    dataset.to_csv(filename, index=False)

'''
sums certain amount of periods from dataset
input dataset, int n_periods, str filename
returns None, saves dataset with new sum to filename
'''
def sum_n_periods(dataset, n_periods, filename):
    col_list = list(dataset)
    col_list = col_list[:n_periods+1]

    dataset['sum' + str(n_periods) + 'periods'] = dataset[col_list].sum(axis = 1)
    dataset.to_csv(filename, index=False)


#adds a column with average amount sold
#all changes are written to the same database
def average(dataset, n_periods, filename):

    # prevent average ovewrite in case of additional use
    try:
        if not dataset['average'].empty:
            return
    except KeyError:
        pass

    dataset['average'] = round(dataset['sum'] / n_periods, 2)
    dataset.to_csv(filename, index=False)


'''
finds average certain amount of periods from dataset
input dataset, int n_periods, str filename
returns None, saves dataset with new sum to filename
'''
def average_n_periods(dataset, n_periods, filename):

    col_list = list(dataset)
    col_list = col_list[:n_periods + 1]

    dataset['average' + str(n_periods) + 'periods'] = round(dataset[col_list].sum(axis=1) / n_periods, 2)
    dataset.to_csv(filename, index=False)


'''
adds to prediction item if its average amount_sold over min_filter / n_periods but less than n_periods / 2
input dataset, int n_periods, int min_filter, str filename, str output_column_name
returns None, saves Prediction column to dataset  
'''
def more_than_prediction(dataset, n_periods, min_filter, prediction_column, output_column_name, filename):

    min_include = min_filter / n_periods
    half = ((n_periods + 1) / 2) / n_periods

    dataset[output_column_name] = np.where(dataset[prediction_column].between(min_include, half, inclusive=False), 1, dataset[prediction_column].round())
    dataset.to_csv(filename, index=False)


'''
sort dataset by amount sold
input dataset, filename
returns None, saves sorted dataset to filename
'''
def sort_by_sum(dataset, filename):

    dataset.sort_values(by = ['sum'], ascending=False, inplace=True)
    dataset.to_csv(filename, index=False)



#import datasets
VAG_data = pd.read_csv('/Volumes/Data/Dropbox/Dropbox/Coding/Sales Prediction/VAG_full_raw.csv', dtype={'PartNumber': str}) #, converters={'PartNumber': lambda x: str(x)})
MB_data = pd.read_csv('/Volumes/Data/Dropbox/Dropbox/Coding/Sales Prediction/MB_full_raw.csv', dtype={'PartNumber': str}) #, converters={'PartNumber': lambda x: str(x)})


#function calls
sum_total(MB_data, 29, 'MB_full.csv')
average(MB_data, 29, 'MB_full.csv')
more_than_prediction(MB_data, 29, 6, 'average', 'Averageprediction29','MB_full_sum.csv')
sort_by_sum(MB_data, 'MB_full_sum.csv')


sum_total(VAG_data, 29, 'VAG_full.csv')
average(VAG_data, 29, 'VAG_full.csv')
more_than_prediction(VAG_data,  29, 6, 'average', 'Averageprediction29', 'VAG_full_sum.csv')
sort_by_sum(VAG_data, 'VAG_full_sum.csv')