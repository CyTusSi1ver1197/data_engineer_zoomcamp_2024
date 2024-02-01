import requests as rqts
import os
import pandas as pd



#download data
months = [10, 11, 12]
full_taxi_df = pd.Dataframes()

for month in months:
    str_file_name = "green_tripdata_2020-" + str(month) + ".csv.gz"
    url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/green/download"
    full_url = os.path.join(url, str_file_name)
    response = rqts.get(full_url)
    
    taxi_dtype = {
        'VendorID': pd.Int64Dtype(),
        'passenger_count': pd.Int64Dtype(),
        'trip_distance': float,
        'RatecodeID': pd.Int64Dtype(),
        'store_and_fwd_flag': str,
        'PULocationID': pd.Int64Dtype(),
        'DOLocationID':pd.Int64Dtype(),
        'payment_type': pd. Int64Dtype(),
        'fare_amount': float,
        'extra': float,
        'mta_tax': float,
        'tip_amount': float,
        'tolls_amount': float,
        'improvement_surcharge': float,
        'total_amount': float,
        'congestion_surcharge': float
    }
    
    date_parses = ['tpep_pickup_datetime', 'tpep_dropoff_datetime']
    
    ans_df = pd.read_csv(full_url,sep = ",", compression = "gzip", dtype = taxi_dtype, parse_dates = date_parses)
    
    full_taxi_df = pd.concat([full_taxi_df,ans_df], ignore_index = True)
    
    
    
# Show size of csv
full_taxi_df


# Querying (Filtering) data:
res_df = full_taxi_df[full_taxi_df['passenger_count'] > 0 & full_taxi_df['trip_distance'] > 0]
res_df.info()


# Data Transformations
full_taxi_df['lpep_pickup_date'] = full_taxi_df['lpep_pickup_datetime'].dt.date


# Show unique values in 'VendorID':
print(full_taxi_df['VendorID'].unique())


# Finding how many columns have not follow snake case:
print([col for col in full_taxi_df.columns if not(col__contains__("_"))])