# add users with password to be able to add products

# add a system to sell the items and automatically calculate the final price and remove the right quantity of the
# spreadsheet
# half done


from openpyxl import load_workbook

workbook = load_workbook(filename='products.xlsx', data_only=True)
sheet = workbook.active

for items in sheet.iter_cols(min_col=2, max_col=2, values_only=True):
    for products in items:
        print(products)