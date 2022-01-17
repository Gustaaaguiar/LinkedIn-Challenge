from openpyxl import load_workbook

workbook = load_workbook(filename='products.xlsx')
sheet = workbook.active

column = sheet['A']
print(len(column))


# row = 3
# sheet[f"B3"] = 'item_name'
# sheet[f"C3"] = 'item_price'
# sheet[f"D3"] = 'item_quantity'
#
#
# workbook.save(filename="products.xlsx")
