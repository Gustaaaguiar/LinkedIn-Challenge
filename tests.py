# read qrcode

from openpyxl import load_workbook
import os


os.chdir('output')

workbook = load_workbook(filename='products.xlsx')
sheet = workbook.active

print(sheet.max_row)
