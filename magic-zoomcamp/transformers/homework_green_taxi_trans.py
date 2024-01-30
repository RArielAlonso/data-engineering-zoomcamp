import pandas as pd
import datetime as dt
import re

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    
    data=data[((data['passenger_count']>0) & (data['trip_distance'])>0)]
    data['lpep_pickup_date']=data['lpep_pickup_datetime'].dt.date
    #print(data.columns)for question 5
    data.columns = data.columns.str.replace('(?<=[a-z])(?=[A-Z])', '_', regex=True).str.lower()
    #print(data.vendor_id.unique()) #for question number 4
    
    return data


@test
def test_output(output, *args) -> None:

    assert 'vendor_id' in output.columns, 'The column vendor_id is in the dataframe columns'

@test
def test_output(output, *args) -> None:

    assert output['passenger_count'].isin([0]).sum()==0, 'The passenger columns not contains 0 passengers'

@test
def test_output(output, *args) -> None:

    assert output['trip_distance'].isin([0]).sum()==0, 'The passenger columns not contains 0 passengers'