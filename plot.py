import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
from time_series import *



'''
Function plots given amount of rows
input dataframe ordered by max sales and raw dataframe, also staring and finish row for plotting
return None, plots series
'''
def plot_n_rows(start, fin, df_raw, df_sum, rolling_periods):
    for i in range(start, fin):
        part_number = df_sum['PartNumber'][i]

        part_number_index = get_index_of_part_number(df_raw, part_number, 'PartNumber')

        #plot series in two weeks periods
        row = row_to_time_series(df_raw, part_number_index)[0]

        #plot row in monthly represent
        #row = row_to_month_represent(df_raw, part_number_index)
        plot_rolling(row, part_number, rolling_periods)

def plot_2_columns(column1_id, column2_id):
    ax = column1_id.plot()
    column2_id.plot(ax=ax, color = 'yellow')
    plt.show()


MB_data = pd.read_csv('/Volumes/Data/Dropbox/Dropbox/Coding/Sales Prediction/MB_full_raw.csv', dtype={'PartNumber': str}) #, converters={'PartNumber': lambda x: str(x)})


#plots time series and its rolling mean
def plot_rolling(row, part_number, rolling_periods):
        plt.figure('Rolling', figsize=(20,15))
        row.index = pd.to_datetime(row.index, format='%y%m', infer_datetime_format=True)
        plt.clf()
        plt.plot(row.index, row.values, label = 'Реальні дані')
        row.rolling(rolling_periods).mean().plot(title=part_number + '  Rolling mean', label = 'Зважена середня')
        plt.legend(loc = 'upper right')
        plt.show()




