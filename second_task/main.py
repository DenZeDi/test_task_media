from Sales import sales
from Store import store

file = 'store_sales_data.xlsx'

store(file).to_excel(excel_writer='dataset.xlsx', sheet_name='Store')
sales(file).to_excel(excel_writer='dataset.xlsx', sheet_name='Sales')


