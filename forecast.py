from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from plot import *
from time_series import *
from statsmodels.tsa.stattools import adfuller


# import datasets
df_MB = pd.read_csv('/Volumes/Data/Dropbox/Dropbox/Coding/Sales Prediction/MB_full_raw.csv')
df_MB_sum = pd.read_csv('/Volumes/Data/Dropbox/Dropbox/Coding/Sales Prediction/MB_full_sum.csv')
df_VAG = pd.read_csv('/Volumes/Data/Dropbox/Dropbox/Coding/Sales Prediction/VAG_full_raw.csv')
df_VAG_sum = pd.read_csv('/Volumes/Data/Dropbox/Dropbox/Coding/Sales Prediction/VAG_full_sum.csv')

# plot_n_rows(0, 20, df_MB, df_MB_sum, 6)


# ARIMA
def arima_func(row):
    model = ARIMA(row.as_matrix(), order=(1, 1, 0))
    model_fit = model.fit(disp=0)
    print(model_fit.summary())

    X = row.values
    size = int(len(X) * 0.8)
    train, test = X[0:size], X[size:len(X)]
    history = [x for x in train]
    predictions = list()

    for t in range(len(test)):
        model = ARIMA(history, order=(2, 1, 1))
        model_fit = model.fit(disp=0)
        output = model_fit.forecast()
        yhat = output[0]
        predictions.append(yhat)
        obs = test[t]
        history.append(obs)
        print('predicted=%f, expected=%f' % (yhat, obs))
    error = mean_squared_error(test, predictions)
    print('Test MSE: %.3f' % error)

    # plot
    # plot_rolling(row, '0001802609', 4)
    # plt.subplot(211)

    plt.figure('ARIMA')
    plt.clf()
    plt.plot(test)
    plt.plot(predictions, color='red')



    plt.show()



def adfuler(timeseries):
    # Determing rolling statistics
    rolmean = pd.rolling_mean(timeseries, window=12)
    rolstd = pd.rolling_std(timeseries, window=12)

    # Plot rolling statistics:
    orig = plt.plot(timeseries, color='blue', label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)

    # Perform Dickey-Fuller test:
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical Value (%s)' % key] = value
    print(dfoutput)

    if dftest[4]['5%'] > dftest[0]:
        print('Series is stationary')
        return True
    else:
        print('Series is non stationary')
        return False

#plot rolling MB
# for i in range(20):
#     index = get_index_of_part_number(df_MB, df_MB_sum['PartNumber'][i], 'PartNumber')
#     row = row_to_time_series(df_MB, index)[0]
#     part_number = row_to_time_series(df_MB, index)[1]
#     plot_rolling(row, part_number, 4)

#plot rolling VAG
# for i in range(20):
#     index = get_index_of_part_number(df_VAG, df_VAG_sum['PartNumber'][i], 'PartNumber')
#     row = row_to_time_series(df_VAG, index)[0]
#     part_number = row_to_time_series(df_VAG, index)[1]
#     plot_rolling(row, part_number, 4)

#run ARIMA VAG
for i in range(5):
    index = get_index_of_part_number(df_VAG, df_VAG_sum['PartNumber'][i], 'PartNumber')
    row = row_to_time_series(df_VAG, index)[0]
    print(adfuler(row))
    arima_func(row)



# #run ARIMA MB
# for i in range(5):
#     index = get_index_of_part_number(df_MB, df_MB_sum['PartNumber'][i], 'PartNumber')
#     row = row_to_time_series(df_MB, index)[0]
#     print(adfuler(row))
#     arima_func(row)

