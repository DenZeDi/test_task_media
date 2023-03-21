import pandas as pd

from Sales import sales
from Store import store

file = 'store_sales_data.xlsx'


with pd.ExcelWriter('dataset.xlsx') as writer:
    store(file).to_excel(excel_writer=writer, sheet_name='Store')
    sales(file).to_excel(excel_writer=writer, sheet_name='Sales')


