import numpy as np
import pandas as pd
# Import date, datetime class from datetime module
from datetime import date, datetime
import pytest

@pytest.fixture()
def read_invoices():
    # in: link
    # out: series
    df=pd.read_csv('./data/invoices.csv')
    return df


@pytest.fixture()
def transform_df():
    # in: link 
    # in data is transformed to add new columns
    # out: series
    transformed_df=pd.read_csv('./data/invoices.csv')
    transformed_df["todays_date"]=date.today()
    transformed_df["raised_date"]=pd.to_datetime(transformed_df["raised_date"])
    transformed_df["due_date"]=pd.to_datetime(transformed_df["due_date"])
    transformed_df["paid_date"]=pd.to_datetime(transformed_df["paid_date"])
    transformed_df["todays_date"]=pd.to_datetime(transformed_df["todays_date"])
    return transformed_df
