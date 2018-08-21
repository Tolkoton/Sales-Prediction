import pandas as pd


'''
converts a dataset row to time series
input dataset and row number
returns time series object and part number as a variable
'''
def row_to_time_series(dataset, row_number):

    # correcting date columns
    col_list = []
    for i in dataset.columns[1:]:
        x = str(i).split(' ')
        col_list.append(x[0])

    part_number_column_name = dataset.columns[0]
    col_list.insert(0, part_number_column_name)
    dataset.columns = col_list

    row_0 = dataset.iloc[row_number]
    part_number = row_0.values[0]
    row_0 = row_0[1:]
    pd.to_datetime(row_0.index)

    return row_0, part_number


'''
input dataframe and part number
returns index row of that part number
'''
def get_index_of_part_number(df, part_number, index_col):

    index_list = df[index_col].tolist()
    return index_list.index(part_number)


def row_to_month_represent(df, row):

    row = row_to_time_series(df, row)[0]
    row_sum = []
    for i in range(0, len(row.values+2), 2):
        try:
            row_sum.append(row.values[i] + row.values[i+1])
        except IndexError:
            pass

    index = pd.date_range('1/1/2017', periods=len(row_sum), freq='M')

    series_m = pd.Series(row_sum, index=index)
    return series_m

