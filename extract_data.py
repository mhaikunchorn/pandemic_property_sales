# Importing libraries
from extract_functions import *
import pandas as pd
import numpy as np
import requests
import csv
import os

# 2012
url = 'http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-2012.csv'
filename = 'pp_2012.csv'
download_data(url, filename)

# 2013
url = 'http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-2013.csv'
filename = 'pp_2013.csv'
download_data(url, filename)

# 2014
url = 'http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-2014.csv'
filename = 'pp_2014.csv'
download_data(url, filename)

# 2015
url = 'http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-2015.csv'
filename = 'pp_2015.csv'
download_data(url, filename)

# 2016
url = 'http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-2016.csv'
filename = 'pp_2016.csv'
download_data(url, filename)

# 2017
url = 'http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-2017.csv'
filename = 'pp_2017.csv'
download_data(url, filename)

# 2018
url = 'http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-2018.csv'
filename = 'pp_2018.csv'
download_data(url, filename)

# 2019
url = 'http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-2019.csv'
filename = 'pp_2019.csv'
download_data(url, filename)

# 2020
url = 'http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-2020.csv'
filename = 'pp_2020.csv'
download_data(url, filename)

# 2021
url = 'http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-2021.csv'
filename = 'pp_2021.csv'
download_data(url, filename)

# 2022
url = 'http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-2022.csv'
filename = 'pp_2022.csv'
download_data(url, filename)

# Call the concat_csv function
filenames = ['data/pp_2012.csv',
             'data/pp_2013.csv',
             'data/pp_2014.csv',
             'data/pp_2015.csv',
             'data/pp_2016.csv',
             'data/pp_2017.csv',
             'data/pp_2018.csv',
             'data/pp_2019.csv',
             'data/pp_2020.csv',
             'data/pp_2021.csv',
             'data/pp_2022.csv']

new_filename = 'data/pp_decade.csv'
concat_csv(filenames, new_filename)