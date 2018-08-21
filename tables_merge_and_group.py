import pandas as pd
import numpy as np


#merges 3 datasets
#takes 3 datasets and output filename as input
#returns merged dataset, creates csv with merged datasets
def merge_3_tables(dataset1, dataset2, dataset3, filename):

    #replace empty values by 0.
    dataset1 = dataset1.replace(np.NaN, 0)
    dataset2 = dataset2.replace(np.NaN, 0)
    dataset3 = dataset3.replace(np.NaN, 0)

    #merge and output tables
    merged_table = pd.merge(dataset1, dataset2, on='PartNumber', how = 'outer')
    full_table = pd.merge(merged_table, dataset3, on = 'PartNumber', how = 'outer')
    full_table = full_table.replace(np.NaN, 0)
    full_table.to_csv(filename, index=False)

    return full_table


'''
takes in a dataset 
returns dataset where part_numbers which have identical first 10 digits are grouped into one position 
'''
def mercedes_group_part_numbers(dataset, filename):

    dataset['PartNumber'] = dataset['PartNumber'].str[0:10]
    grouped_data = dataset.groupby(['PartNumber']).sum()
    grouped_data.to_csv(filename)


#import source files from xlsx
excel_file1 = pd.ExcelFile('/Volumes/Data/Dropbox/Dropbox/Coding/Sales Prediction/Source_data/xls/Січень - червень 2017.xlsx', \
                           converters={'PartNumber': lambda x: str(x)}, parse_dates = False)
sheet11,sheet12 = excel_file1.sheet_names
VAG1 = excel_file1.parse(sheet11)
MB1 = excel_file1.parse(sheet12)


excel_file2 = pd.ExcelFile('/Volumes/Data/Dropbox/Dropbox/Coding/Sales Prediction/Source_data/xls/липень - грудень 2017.xlsx', \
                           converters={'PartNumber': lambda x: str(x)}, parse_dates = False)
sheet21,sheet22 = excel_file2.sheet_names
VAG2 = excel_file2.parse(sheet21)
MB2 = excel_file2.parse(sheet22)


excel_file3 = pd.ExcelFile('/Volumes/Data/Dropbox/Dropbox/Coding/Sales Prediction/Source_data/xls/Січень - березень 2018.xlsx', \
                           converters={'PartNumber': lambda x: str(x)}, parse_dates = False)
sheet31,sheet32 = excel_file3.sheet_names
VAG3 = excel_file3.parse(sheet31)
MB3 = excel_file3.parse(sheet32)


#merge them into one table
VAG_data = merge_3_tables(VAG1, VAG2, VAG3, 'VAG_full_raw.csv')
MB_data = merge_3_tables(MB1, MB2, MB3, 'MB_full_raw.csv')


#group identical parts with different numbers Mercedes
mercedes_group_part_numbers(MB_data, 'MB_full_raw.csv')


#Count number of periods in observation
number_of_periods_MB = len(MB_data.columns) - 1
number_of_periods_VAG = len(VAG_data.columns) - 1


