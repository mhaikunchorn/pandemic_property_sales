# Importing libraries
import pandas as pd
import numpy as np
import requests
import csv
import os

def download_data(url, filename):
    """
    Downloads the raw data from the url, converts to a DataFrame and saves as a .csv file

    Parameters:
        - url : string
        HTTP url ending with .csv

        - filename : string
        the filename the dataframe will be saved as, ending with .csv

    Returns:
        downloaded data as the filename as ending with .csv

    """
    # Check if the filename already exists
    if not os.path.isfile(filename):
        print('Downloading {}...'.format(filename))
        with requests.Session() as s:
            download = s.get(url)

            decoded_content = download.content.decode('utf-8')

            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            df = pd.DataFrame(cr)
            df.to_csv('data/' + filename)

        # Prompt user once download is successful
        print('Download is complete for {}'.format(filename))

    else:
        print('File {} already exists'.format(filename))


def concat_csv(filenames, new_filename):
    """
    Read in multiple yearly .csv files and save them to a single new .csv file

    Parameters:
        - filenames : string
            list of files names with .csv extension to be read

        - new_filename : string
            the filename the multiple concatenated .csv files will be saved as, ending with .csv

    Returns:
        a single .csv file with multiple .csv files concatenated

    """

    if not os.path.isfile(new_filename):
        print('Saved downloaded files as {}'.format(new_filename))
        raw = pd.concat((pd.read_csv(i)
                         for i in filenames))

        return raw.to_csv('data/pp_decade.csv', index=False)

    else:
        print('File {} already exists'.format(new_filename))
