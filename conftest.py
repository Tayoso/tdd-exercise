# import numpy as np
# import pandas as pd
# # Import date, datetime class from datetime module
# from datetime import date, datetime
import pytest

# @pytest.fixture()
# def read_invoices():
#     # in: link
#     # out: dataframe
#     invoices_data=pd.read_csv('../data/invoices.csv')
#     return invoices_data

@pytest.fixture()
def x():
    return 2

@pytest.fixture()
def y():
    return 3
