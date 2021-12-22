import pytest
import pandas as pd
from pandas._testing import assert_series_equal
from scripts.analysis import count_unique_rows, no_unpaid_invoices

def test_count_unique_rows(read_invoices):
    # in: series
    # out: series
    # use read_invoices from conftest
    unique_rows=read_invoices['id'].drop_duplicates().shape[0]
    assert unique_rows>0
    assert unique_rows==count_unique_rows(read_invoices)

def test_no_unpaid_invoices(read_invoices):
    # in: series
    # out: series
    # use read_invoices from conftest
    unpaid_invoices=read_invoices[read_invoices['status']=="UNPAID"]
    grouped_unpaid_invoices=unpaid_invoices.groupby("organisation_id").size()
    assert_series_equal(grouped_unpaid_invoices,no_unpaid_invoices(read_invoices))

def test_no_overdue_invoices(transform_df):
    # in: series
    # out: series

    # filter unpaid, due date less than todays date
    # use transform_df from conftest    
    unpaid_invoices=transform_df[transform_df['status']=="UNPAID"]
    grouped_overdue_invoices=unpaid_invoices[unpaid_invoices['due_date']<unpaid_invoices["todays_date"]].\
        groupby("organisation_id").size()
    assert grouped_overdue_invoices.shape[0]==2
    assert grouped_overdue_invoices.shape==(2,)


