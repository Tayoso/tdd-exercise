

import numpy as np
import pandas as pd
# Import date, datetime class from datetime module
from datetime import date, datetime

# Returns the current local date
today = date.today()

def count_unique_rows(df):
    # in: dataframe
    # out: dataframe
    return df['id'].drop_duplicates().shape[0]

def no_unpaid_invoices(df):
    # in: dataframe
    # out: dataframe
    unpaid_invoices=df[df['status']=="UNPAID"]
    return unpaid_invoices.groupby("organisation_id").size()

def no_overdue_invoices(df):
    # in: dataframe
    # out: dataframe
    # convert to time series
    df["todays_date"]=today
    df["raised_date"]=pd.to_datetime(df["raised_date"])
    df["due_date"]=pd.to_datetime(df["due_date"])
    df["paid_date"]=pd.to_datetime(df["paid_date"])
    df["todays_date"]=pd.to_datetime(df["todays_date"])

    # filter unpaid, due date less than todays date
    unpaid_invoices=df[df['status']=="UNPAID"]
    return unpaid_invoices[unpaid_invoices['due_date']<unpaid_invoices["todays_date"]].\
        groupby("organisation_id").size()


def no_paid_invoices(df):
    # in: dataframe
    # out: dataframe
    # convert to time series
    df["todays_date"]=today
    df["raised_date"]=pd.to_datetime(df["raised_date"])
    df["due_date"]=pd.to_datetime(df["due_date"])
    df["paid_date"]=pd.to_datetime(df["paid_date"])
    df["todays_date"]=pd.to_datetime(df["todays_date"])

    # filter paid, get b/down per month per organisation
    paid_invoices=df[df['status']=="PAID"]
    paid_invoices['paid_month']=pd.DatetimeIndex(paid_invoices['paid_date']).month
    return paid_invoices.groupby(["organisation_id","paid_month"]).size()