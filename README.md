# Sales-Prediction
Car parts sales prediction using averages and ARIMA

tables_merge_and_group.py
Data came in 3 xlsx  files each from different time period.
It has to be preprocessed, cleaned and merged into one csv. Data needs to grouped by partnumber, so we get total sales over whole time period.
Also Mercedes parts are identical if they have identical first 10 digits, so we cut the numbers before grouping.


sum_and_average.py
This one creates predictions using simple averages. We didn't use weighted averages since sales depend mostly on relationships with clients and political issues, so we are going for 'safe bet' here.


time_series.py
This one takes one row from dataframe(which is is one partnumber with its sales over time period) and converts it to pandas time series for future analysis.


plot.py
This one plots the data, rolling mean and predictions.


forecast.py
Here I implemented a Dickey-Fuller test and ARIMA forcast for the given data.
