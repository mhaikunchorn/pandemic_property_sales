# Importing libraries
import pandas as pd
import numpy as np
import csv
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import date2num
import seaborn as sns
import datetime as dt
from datetime import datetime
from matplotlib.ticker import ScalarFormatter
from matplotlib.dates import DateFormatter, MonthLocator


# Viewing options
pd.set_option('display.width', 320)
pd.set_option('display.max_columns', 17)

# Read .csv file back in for analysis
data = pd.read_csv('data/pp_decade_clean.csv', index_col=False)
england = pd.read_csv('data/pp_england.csv', index_col=False)
wales = pd.read_csv('data/pp_wales.csv', index_col=False)

# Work on a copy of the pp_decade_clean data
df = data.copy(deep=True)

# Preparing the dataframes
print(df.info())
print(england.info())
print(wales.info())

# Change dtype date and month_year from object to datetime
df['date'] = pd.to_datetime(df['date'])
england['date'] = pd.to_datetime(england['date'])
wales['date'] = pd.to_datetime(wales['date'])
df['month_year'] = pd.to_datetime(df['month_year'])
england['month_year'] = pd.to_datetime(england['month_year'])
wales['month_year'] = pd.to_datetime(wales['month_year'])

# Checking if the dtypes are correct.
print(df.info())
print(england.info())
print(wales.info())

### What is the summary of the price paid for properties in England and Wales between 2012 - 2022?¶
print(df.price.describe())

plt.figure(figsize=(16, 12))
plt.boxplot(df['price'])
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
plt.gca().yaxis.set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))
plt.xticks([])
plt.yticks(size=16)
plt.ylabel('Price (£)', size=18)
plt.title('Summary of price paid for properties in \n England and Wales between 2012 - 2022', size=20)
plt.savefig('figures/boxplot_price_ew.png')
plt.show()
plt.close()

### What was the trend of the average price paid in England and Wales between 2012 - 2022?
# Monthly of mean and percentage and respective percentage change
monthly_mean_ew = df.groupby('month_year').mean()['price'].round().reset_index()
monthly_mean_ew['mean_pct_change'] = monthly_mean_ew.price.pct_change()
monthly_mean_ew = monthly_mean_ew.rename(columns={'price': 'mean_price'})
monthly_mean_pct_change = monthly_mean_ew
print('Monthly of mean and percentage and respective percentage change')
print(monthly_mean_pct_change)

# Monthly of median and percentage and respective percentage change
monthly_median_ew = df.groupby('month_year').median()['price'].round().reset_index()
monthly_median_ew['median_pct_change'] = monthly_median_ew.price.pct_change()
monthly_median_ew = monthly_median_ew.rename(columns={'price': 'median_price'})
monthly_median_pct_change = monthly_median_ew
print('Monthly of median and percentage and respective percentage change')
print(monthly_median_pct_change)


#England
### What was the trend of the average price paid in England between 2012 - 2022?
# Monthly of mean and percentage and respective percentage change
monthly_mean_eng = england.groupby('month_year').mean()['price'].round().reset_index()
monthly_mean_eng['mean_pct_change'] = monthly_mean_eng.price.pct_change()
monthly_mean_eng = monthly_mean_eng.rename(columns={'price': 'mean_price'})
monthly_mean_pct_change_eng = monthly_mean_eng
print('Monthly of mean and percentage and respective percentage change')
print(monthly_mean_pct_change_eng)

# Monthly of median and percentage and respective percentage change
monthly_median_eng = england.groupby('month_year').median()['price'].round().reset_index()
monthly_median_eng['median_pct_change'] = monthly_median_eng.price.pct_change()
monthly_median_eng = monthly_median_eng.rename(columns={'price': 'median_price'})
monthly_median_pct_change_eng = monthly_median_eng
print('Monthly of median and percentage and respective percentage change')
print(monthly_median_pct_change_eng)





# Load in the pp_decade_clean
# Load in england and wales


# Loading in england and wales
# Change dtype date and month_year from object to datetime
