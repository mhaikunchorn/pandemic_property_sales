# Exploratory Data Analysis and Proof of Concept

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

# Work on a copy of the pp_decade_clean data
df = data.copy(deep=True)

# Preparing the dataframes
print(df.info())

# Change dtype date and month_year from object to datetime
df['date'] = pd.to_datetime(df['date'])
df['month_year'] = pd.to_datetime(df['month_year'])


### Proof of Concept
# Analysing Greater London county as the proof of concept to verify analysis before performing on the analysis on the full dataframe.

# Creating a dataframe for GREATER LONDON
greater_london = df[df.county == 'GREATER LONDON']

# Checking the data dimensions
print(greater_london.shape)

# What is the summary of the price paid for properties in Greater London between 2012 - 2022?¶
print(greater_london.price.describe())

plt.figure(figsize=(16, 12))
plt.boxplot(greater_london['price'])
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
plt.gca().yaxis.set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))
plt.xticks([])
plt.yticks(size=16)
plt.ylabel('Price (£)', size=18)
plt.title('Summary of price paid for properties in \n Greater London between 2012 - 2022', size=20)
plt.savefig('figures/boxplot_price_gl.png')
plt.show()
plt.close()

# ==== REVISE BELOW
### What was the trend of the average price paid in Greater London between 2012 - 2022?
# Monthly of mean and percentage and respective percentage change
monthly_mean_gl = greater_london.groupby('month_year').mean()['price'].round().reset_index()
monthly_mean_gl['mean_pct_change'] = monthly_mean_gl.price.pct_change()
monthly_mean_gl = monthly_mean_gl.rename(columns={'price': 'mean_price'})
monthly_mean_pct_change = monthly_mean_gl
print('Monthly of mean and percentage and respective percentage change')
print(monthly_mean_pct_change)

# Monthly of median and percentage and respective percentage change
monthly_median_gl = greater_london.groupby('month_year').median()['price'].round().reset_index()
monthly_median_gl['median_pct_change'] = monthly_median_gl.price.pct_change()
monthly_median_gl = monthly_median_gl.rename(columns={'price': 'median_price'})
monthly_median_pct_change = monthly_median_gl
print('Monthly of median and percentage and respective percentage change')
print(monthly_median_pct_change)

# Yearly of mean and percentage and respective percentage change
yearly_mean_gl = greater_london.groupby('year').mean()['price'].round().reset_index()
yearly_mean_gl['mean_pct_change'] = yearly_mean_gl.price.pct_change()
yearly_mean_gl = yearly_mean_gl.rename(columns={'price': 'mean_price'})
yearly_mean_pct_change = yearly_mean_gl
print('Yearly of mean and percentage and respective percentage change')
print(yearly_mean_pct_change)

# Yearly of median and percentage and respective percentage change
yearly_median_gl = greater_london.groupby('year').median()['price'].round().reset_index()
yearly_median_gl['median_pct_change'] = yearly_median_gl.price.pct_change()
yearly_median_gl = yearly_median_gl.rename(columns={'price': 'median_price'})
yearly_median_pct_change = yearly_median_gl
print('Yearly of median and percentage and respective percentage change')
print(yearly_median_pct_change)

# Plot monthly_mean_pct_change
plt.plot(monthly_mean_pct_change['month_year'], monthly_mean_pct_change['mean_price'])
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
plt.ylim(0, 1250000)
plt.xlabel('Date')
plt.ylabel('Price (£)')
plt.title('Monthly Mean Price')
plt.savefig('figures/monthly_mean_pct_change')

#Plot monthly_median_pct_change
plt.plot(monthly_median_pct_change['month_year'], monthly_median_pct_change['median_price'])
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
plt.ylim(0, 1250000)
plt.xlabel('Date')
plt.ylabel('Price (£)')
plt.title('Monthly Median Price')
plt.savefig('figures/monthly_median_pct_change')

#Plot yearly_mean_pct_change
plt.plot(yearly_mean_pct_change['year'], yearly_mean_pct_change['mean_pct_change'])
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
plt.ylim(0, 900000)
plt.xlabel('Year')
plt.ylabel('Price (£)')
plt.title('Yearly Mean Price')
plt.savefig('figures/yearly_mean_pct_change')

# Plot yearly_median_pct_change
plt.plot(yearly_median_pct_change['year'], yearly_median_pct_change['median_pct_change'])
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
plt.ylim(0, 900000)
plt.xlabel('Year')
plt.ylabel('Price (£)')
plt.title('Yearly Median Price')
plt.savefig('figures/yearly_median_pct_change')

# ==== REVISE ABOVE

# ====Plot Annual Average Mean and Median Price Paid in Greater London

# ====Plot of Annual Mean and Median Price Change in Greater london

### What is the trend in total number of sales for each property type for Greater London between 2012 - 2022?
print(greater_london['type'].value_counts())
values = greater_london['type'].value_counts().keys().tolist()
counts = greater_london['type'].value_counts().tolist()

plt.figure(figsize=(12, 8))
plot = plt.bar(values, counts, color=('#2b540d', 'grey', 'grey', 'grey', 'grey'),
               zorder=3)
plt.grid(zorder=0)
plt.xticks(['F', 'T', 'S', 'D', 'O'],
           ['Flats/Maisonettes', 'Terraced', 'Semi-Detached', 'Detached', 'Other'],
           size=16)
plt.yticks(size=16)
plt.ylim(0, 650000)
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
plt.gca().yaxis.set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))
plt.title('Total number of sales for each property type for \n Greater London between 2012 - 2022',
          size=20, fontweight='bold')
plt.xlabel('Property Type', loc='center', size=18)
plt.ylabel('Number of Sales', size=18)
plt.bar_label(plot, size=16, labels=[f'{x:,.0f}' for x in plot.datavalues])
plt.savefig('figures/bar_sales_per_type_gl.png')
plt.show()
plt.close()

### What was the preferred property age?
print(greater_london['new_build'].value_counts())
values = greater_london['new_build'].value_counts().keys().tolist()
counts = greater_london['new_build'].value_counts().tolist()

plt.figure(figsize=(12, 8))
plot = plt.bar(values, counts, color=('#2b540d', 'grey'))
plt.xticks(['N', 'Y'], ['Established Residential Building', 'New Build Property'], size=16)
plt.yticks(size=16)
plt.ylim(0, 1200000)
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
plt.gca().yaxis.set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))
plt.title('The most popular property age for \n Greater London between 2012 - 2022',
          size=20, fontweight='bold')
plt.xlabel('Property Age', loc='center', size=18)
plt.ylabel('Number of Sales', size=18)
plt.bar_label(plot, size=16, labels=[f'{x:,.0f}' for x in plot.datavalues])
plt.savefig('figures/bar_sales_per_age_gl.png')
plt.show()
plt.close()

### What was the preferred type of tenure?
print(greater_london['duration'].value_counts())
values = greater_london['duration'].value_counts().keys().tolist()
counts = greater_london['duration'].value_counts().tolist()

plt.figure(figsize=(12, 8))
plot = plt.bar(values, counts, color=('#2b540d', 'grey'))
plt.xticks(['L', 'F'], ['Leasehold \n(>7 Years)', 'Freehold'], size=16)
plt.yticks(size=16)
plt.ylim(0, 700000)
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
plt.gca().yaxis.set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))
plt.title('The most popular type of property tenure for \n Greater London between 2012 - 2022',
          size=20, fontweight='bold')
plt.xlabel('Tenure', loc='center', size=18)
plt.ylabel('Number of Sales', size=18)
plt.bar_label(plot, size=16, labels=[f'{x:,.0f}' for x in plot.datavalues])
plt.savefig('figures/bar_sales_per_duration_gl.png')
plt.show()
plt.close()

### What was the most common of Price Paid Transaction?
print(greater_london['ppd_category'].value_counts())
values = greater_london['ppd_category'].value_counts().keys().tolist()
counts = greater_london['ppd_category'].value_counts().tolist()

plt.figure(figsize=(12, 8))
plot = plt.bar(values, counts, color=('#2b540d', 'grey'))
plt.xticks(['A', 'B'], ['Standard Price Paid Entry \n', 'Additional Price Paid Entry'], size=16)
plt.yticks(size=16)
plt.ylim(0, 1200000)
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
plt.gca().yaxis.set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))
plt.title('The most common price paid transaction for \n Greater London between 2012 - 2022',
          size=20, fontweight='bold')
plt.xlabel('Price Paid Category', loc='center', size=18)
plt.ylabel('Number of Sales', size=18)
plt.bar_label(plot, size=16, labels=[f'{x:,.0f}' for x in plot.datavalues])
plt.savefig('figures/bar_sales_per_ppdcat_gl.png')
plt.show()
plt.close()

### What was the trend in annual sales?
# Total annual sales and percentage change for Greater London
annual_sales_gl = greater_london.groupby('month_year').count()['id'].round().reset_index()
annual_sales_gl['pct_change'] = annual_sales_gl.id.pct_change()
annual_sales_gl = annual_sales_gl.rename(columns={'id': 'sales'})
total_annual_sales_pct_gl = annual_sales_gl
print(total_annual_sales_pct_gl.head(11))

# Plot of Total Annual Sales for Greater London
plt.figure(figsize=(16, 14))
plt.plot(total_annual_sales_pct_gl['month_year'], total_annual_sales_pct_gl['sales'],
                 linewidth=2, color='#004488')
months_format = DateFormatter('%b-%Y')
plt.gca().xaxis.set_major_formatter(months_format)
plt.gca().yaxis.set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=6))
plt.xticks(rotation=45, size=16)
plt.yticks(size=16)
plt.ylim(0, 30000)
plt.xlabel('Date', size=18)
plt.ylabel('Number of Sales', size=18)
plt.title('Annual Property Sales for Greater London', size=20, fontweight='bold')
plt.savefig('figures/annual_sales_gl')
plt.show()
plt.close()

# Plot of Total Annual Sales Change for Greater London
plt.figure(figsize=(16, 14))
plt.plot(total_annual_sales_pct_gl['month_year'], total_annual_sales_pct_gl['pct_change'],
                 linewidth=2, color='#004488')
months_format = DateFormatter('%b-%Y')
plt.gca().xaxis.set_major_formatter(months_format)
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=6))
plt.xticks(rotation=45, size=16)
plt.yticks(size=16)
plt.xlabel('Date', size=18)
plt.ylabel('Percentage Change (%)', size=18)
plt.title('Annual Property Sales Change for Greater London', size=20, fontweight='bold')
plt.savefig('figures/annual_sales_pct_gl')
plt.show()
plt.close()



# ==== TESTING CODE
# x1 = greater_london.groupby('month_year').count()['id'].round().reset_index()
# x1['pct_change'] = x1.id.pct_change()
# print(x1)

# ==== OLD CODES
# # Table of mean, median and percentage and respective percentage change
# yearly_mean_gl = greater_london.groupby('year').mean()['price'].round().reset_index()
# yearly_median_gl = greater_london.groupby('year').median()['price'].round().reset_index()
# mean_median_gl = yearly_mean_gl.merge(yearly_median_gl, on='year', how='left')
# mean_median_gl.columns = ['year', 'mean_price', 'median_price']
# pct_change_mean = mean_median_gl.mean_price.pct_change()
# pct_change_mean = pd.merge(mean_median_gl, pct_change_mean, left_index=True, right_index=True)
# pct_change_median = pct_change_mean.median_price.pct_change()
# pct_change_median = pd.merge(pct_change_mean, pct_change_median, left_index=True, right_index=True)
# mean_median_pct_change = pct_change_median
# mean_median_pct_change.columns = ['year', 'mean_price', 'median_price', 'mean_pct_change', 'median_pct_change']
# print(pct_change_median)
#
# yearly_median = greater_london.groupby('year').median()['price'].reset_index()
# yearly_mean = greater_london.groupby('year').mean()['price'].reset_index()
#
# plt.figure(figsize=(12, 8))
# plt.plot(yearly_mean['year'], yearly_mean['price'], marker='.', color='#c2591d', label='Mean')
# plt.plot(yearly_median['year'], yearly_median['price'], marker='.', color='blue', label='Median')
# plt.ylim(0, 900000)
# plt.ticklabel_format(useOffset=False, style='plain', axis='y')
# plt.gca().yaxis.set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('£{x:,.0f}'))
# plt.xticks(size=16)
# plt.yticks(size=16)
# plt.title('The Average and Median price paid for \n Greater London between 2012 - 2022', size=20,
#           fontweight='bold')
# plt.xlabel('Year', loc='center', size=18)
# plt.ylabel('Price (£)', size=18)
# plt.legend(fontsize=16)
# plt.savefig('figures/line_mean_median_gl.png')
# plt.show()
# plt.close()

# ===== OLD CODE FOR MAKING DF for mean median and pct.
# yearly_mean_gl = greater_london.groupby('year').mean()['price'].round().reset_index()
# yearly_mean_gl['mean_pct_change'] = yearly_mean_gl.price.pct_change()
# yearly_median_gl = greater_london.groupby('year').median()['price'].round().reset_index()
# yearly_median_gl['median_pct_change'] = yearly_median_gl.price.pct_change()
# mean_median_pct_price_gl = yearly_mean_gl.merge(yearly_median_gl, on='year', how='left')
# mean_median_pct_price_gl.columns = ['year', 'mean_price', 'mean_pct_change', 'median_price', 'median_pct_change']
# print(mean_median_pct_price_gl.tail())