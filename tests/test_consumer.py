import pytest
import pandas as pd
# from scripts.analysis import read_invoices
from scripts.analysis import addition

def test_addition(x,y):
    z=addition(x,y)
    assert z==5

# def test_read_invoices():
#     invoices_data=pd.read_csv('../data/invoices.csv')
#     assert invoices_data==read_invoices()

# @pytest.fixture
# def invoices():
#     with open("../data/invoices.csv") as f:
#         yield list(DictReader(f))


# def test_empty_list():
#     consume_invoices([])
