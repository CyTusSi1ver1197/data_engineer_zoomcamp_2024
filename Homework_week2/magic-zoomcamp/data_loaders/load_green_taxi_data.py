import io
import os
import pandas as pd
import requests as rqts
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    #download data
    months = [10, 11, 12]
    full_taxi_df = pd.DataFrame()

    for month in months:
        str_file_name = "green_tripdata_2020-" + str(month) + ".csv.gz"
        # Online URL to get data
        # url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/green/download"

        # local url if already downloaded (on cmd input python -m http.server 
        # open another cmd then input ipconfig to find port)
        url = "http://172.25.240.1:8000/"
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
        
        date_parses = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
        
        ans_df = pd.read_csv(full_url,sep = ",", compression = "gzip", dtype = taxi_dtype, parse_dates=date_parses)
        
        full_taxi_df = pd.concat([full_taxi_df,ans_df], ignore_index = True)
        

    return full_taxi_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'