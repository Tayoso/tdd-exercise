import pytest
import pandas as pd
from pandas._testing import assert_series_equal
# from scripts.analysis import read_invoices
from scripts.analysis import addition, count_unique_rows

def test_addition(x,y):
    z=addition(x,y)
    assert z==5

def test_count_unique_rows(read_invoices):
    # in: dataframe
    # out: dataframe
    unpaid_invoices=read_invoices[read_invoices['status']=="UNPAID"]
    assert_series_equal(unpaid_invoices.groupby("organisation_id").size(),count_unique_rows(read_invoices))

# def test_read_invoices():
#     invoices_data=pd.read_csv('../data/invoices.csv')
#     assert invoices_data==read_invoices()

# @pytest.fixture
# def invoices():
#     with open("../data/invoices.csv") as f:
#         yield list(DictReader(f))


# def test_empty_list():
#     consume_invoices([])
