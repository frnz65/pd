# Scrapes pontiadorea's AIS data

# Load ship data
from aisexplorer.AIS import AIS
import pandas as pd
import sys, getopt
import os


def get_data(MMSI:int=247193010):
    return AIS(return_df=True).get_location(MMSI);

def save_data(df:pd.DataFrame,filename:str):
    # Check if file exists
    exists = os.path.isfile(filename)
    df.to_csv(filename,mode = 'a', header= not exists)

def print_progress(data:pd.DataFrame):
    print_data = data[['SHIPNAME','LAT','LON','LAST_POS']].values.tolist()[0]
    print("%s LAT: %f9 LON: %f9 TIME: %d11"%(print_data[0],float(print_data[1]),float(print_data[2]),print_data[3]))

def main(argv):
    outputFilename  = 'track.csv'
    MMSI             = 247193010
    try:
        opts, args = getopt.getopt(argv,"ho:m:")
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ('-h','--help'):
            print ('scraper.py -o <output file> -m <SHIP MMSI>')
            sys.exit()
        
        elif opt in ('-o','--output','--file'):
            outputFilename = arg
        elif opt in ("-m", "--mmsi", "--MMSI"):
            MMSI = int(arg)
    
    data = get_data(MMSI)
    save_data(data,outputFilename)
    print_progress(data)


if __name__ == '__main__':
    main(sys.argv[1:])