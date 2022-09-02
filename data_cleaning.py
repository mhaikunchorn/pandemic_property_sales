# Importing libraries
import pandas as pd
import numpy as np
import requests
import csv
import os
import matplotlib.pyplot as plt

# Viewing options
pd.set_option('display.width', 320)
pd.set_option('display.max_columns', 17)

# Read .csv file back in
data = pd.read_csv('data/pp_decade.csv', index_col=False).drop(['Unnamed: 0'], axis=1)

# Preview the first 5 lines of the dataframe
print(data.head())

# Summary of the dataframe
print(data.info())

# Check the data dimension
print(data.shape)

# Work on a copy of the dataframe
df = data.copy(deep=True)
print(df.head())

# Rename columns
df.columns = ['id',
            'price',
            'date',
            'postcode',
            'type',
            'new_build',
            'duration',
            'primary_address',
            'secondary_address',
            'street',
            'locality',
            'town_city',
            'district',
            'county',
            'ppd_category',
            'record']

# Change the date from object to datetime
df['date'] = pd.to_datetime(df['date'])

# Sort the date by ascending order
df.sort_values('date', ascending=True, inplace=True)

# Check the dataframe
print(df.head())

# Check for missing values
df = df.replace(' ', np.nan)
df.isnull().sum()

# Check the & of missing values for each col
for col in df.columns:
    missing_pct = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(missing_pct*100)))

# Drop irrelevant columns
cols_to_drop = ['secondary_address', 'locality']
df.drop(cols_to_drop, axis=1, inplace=True)
print(df.head())

# Identifying outliers in price
plt.boxplot(df['price'])
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
plt.gca().yaxis.set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('£{x:,.0f}'))
plt.ylabel('Sale Price (£)', size=12)
plt.xticks([])
plt.title('Boxplot of Sale Price', size=16)
plt.savefig('figures/boxplot_price.png')
plt.show()
plt.close()

# Preview of the price distribution
print(df.price.describe())

# Preview the outliers of properties sold over £500,000,000
print(df[df.price >= 500000000])

# Preview the outliers of properties sold for £1
print(df[df.price == df.price.min()])

# Remove duplicated rows
duplicated_row = df[df.duplicated(subset=['price',
            'date',
            'postcode',
            'type',
            'new_build',
            'duration',
            'primary_address',
            'street',
            'town_city',
            'district',
            'county',
            'ppd_category',
            'record'])].head()

# Remove duplicated rows
df_clean = df.drop_duplicates(subset=['price',
            'date',
            'postcode',
            'type',
            'new_build',
            'duration',
            'primary_address',
            'street',
            'town_city',
            'district',
            'county',
            'ppd_category',
            'record'])

# Adding year, month and month_year columns to group by later in EDA
df_clean['year'] = df_clean['date'].dt.year
df_clean['month'] = df_clean['date'].dt.month
df_clean['month_year'] = df['date'].apply(lambda x: x.strftime('%b-%Y'))
print(df_clean.info())

# Save clean data for analysis
df_clean.to_csv('data/pp_decade_clean.csv', index=False)

# Create separate datasets for 'England' and 'Wales'
# Preview the unique number of town_city, district and county

print(df_clean['town_city'].nunique())
print(df_clean['district'].nunique())
print(df_clean['county'].nunique())

# Checking the unique county names
towns_cities = df_clean['town_city'].unique()
towns_cities.sort()
print(towns_cities)

# Checking the unique county names
counties = df_clean['county'].unique()
counties.sort()
print(counties)

# Sorting counties belonging to England and Wales
english_counties = ['BATH AND NORTH EAST SOMERSET', 'BEDFORD', 'BLACKBURN WITH DARWEN',
                    'BLACKPOOL', 'BOURNEMOUTH','BOURNEMOUTH, CHRISTCHURCH AND POOLE',
                    'BRACKNELL FOREST', 'BRIGHTON AND HOVE', 'BUCKINGHAMSHIRE',
                    'CAMBRIDGESHIRE', 'CENTRAL BEDFORDSHIRE', 'CHESHIRE',
                    'CHESHIRE EAST', 'CHESHIRE WEST AND CHESTER', 'CITY OF BRISTOL',
                    'CITY OF DERBY', 'CITY OF KINGSTON UPON HULL', 'CITY OF NOTTINGHAM',
                    'CITY OF PETERBOROUGH', 'CITY OF PLYMOUTH', 'CORNWALL',
                    'COUNTY DURHAM', 'CUMBRIA', 'DARLINGTON',
                    'DERBYSHIRE', 'DEVON', 'DORSET',
                    'EAST RIDING OF YORKSHIRE', 'EAST SUSSEX', 'ESSEX',
                    'GLOUCESTERSHIRE', 'GREATER LONDON', 'GREATER MANCHESTER',
                    'HALTON', 'HAMPSHIRE', 'HARTLEPOOL',
                    'HEREFORDSHIRE', 'HERTFORDSHIRE', 'ISLE OF WIGHT',
                    'ISLES OF SCILLY', 'KENT', 'LANCASHIRE', 'LEICESTER',
                    'LEICESTERSHIRE', 'LINCOLNSHIRE', 'LUTON',
                    'MEDWAY', 'MERSEYSIDE', 'MIDDLESBROUGH',
                    'MILTON KEYNES', 'NORFOLK', 'NORTH EAST LINCOLNSHIRE',
                    'NORTH LINCOLNSHIRE', 'NORTH NORTHAMPTONSHIRE', 'NORTH SOMERSET',
                    'NORTH YORKSHIRE', 'NORTHAMPTONSHIRE', 'NORTHUMBERLAND',
                    'NOTTINGHAMSHIRE', 'OXFORDSHIRE', 'POOLE',
                    'PORTSMOUTH', 'READING', 'REDCAR AND CLEVELAND',
                    'RUTLAND', 'SHROPSHIRE', 'SLOUGH',
                    'SOMERSET', 'SOUTH GLOUCESTERSHIRE', 'SOUTH YORKSHIRE',
                    'SOUTHAMPTON', 'SOUTHEND-ON-SEA', 'STAFFORDSHIRE',
                    'STOCKTON-ON-TEES', 'STOKE-ON-TRENT', 'SUFFOLK',
                    'SURREY', 'SWINDON', 'THURROCK',
                    'TORBAY', 'TYNE AND WEAR', 'WARRINGTON',
                    'WARWICKSHIRE', 'WEST BERKSHIRE', 'WEST MIDLANDS',
                    'WEST NORTHAMPTONSHIRE', 'WEST SUSSEX', 'WEST YORKSHIRE',
                    'WILTSHIRE', 'WINDSOR AND MAIDENHEAD', 'WOKINGHAM',
                    'WORCESTERSHIRE', 'WREKIN', 'YORK']

welsh_counties = ['BLAENAU GWENT', 'BRIDGEND',
                  'CAERPHILLY', 'CARDIFF', 'CARMARTHENSHIRE',
                  'CEREDIGION', 'CONWY', 'DENBIGHSHIRE',
                  'FLINTSHIRE', 'GWYNEDD', 'ISLE OF ANGLESEY',
                  'MERTHYR TYDFIL', 'MONMOUTHSHIRE', 'NEATH PORT TALBOT',
                  'NEWPORT', 'PEMBROKESHIRE', 'POWYS',
                  'RHONDDA CYNON TAFF', 'SWANSEA', 'THE VALE OF GLAMORGAN',
                  'TORFAEN', 'WREXHAM']

# Creating the 'england' dataframe
england = df_clean[df_clean['county'].isin(english_counties)]

# Creating the 'wales' dataframe
wales = df_clean[df_clean['county'].isin(welsh_counties)]

# Add a month_year column
england['month_year'] = england['date'].apply(lambda x: x.strftime('%b-%Y'))
wales['month_year'] = wales['date'].apply(lambda x: x.strftime('%b-%Y'))

# Checking the summary of newly created dataframes
print(england.info())
print(wales.info())

# Save the 'england' and 'wales' dataframes as .csv files for future analysis
england.to_csv('data/pp_england.csv', index=False)
wales.to_csv('data/pp_wales.csv', index=False)