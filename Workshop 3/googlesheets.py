import gspread

gc = gspread.service_account(filename="key.json")
sh = gc.open_by_key('11b7VPUtbI9Vu7P0daUQlwgtrfvdv1RGWhMdRLJVJk3c')
worksheets = sh.sheet1

# res = worksheets.get_all_records()
# res = worksheets.get_all_values()
# res = worksheets.col_values('A')
# res = worksheets.get('A2:C2')
# user = ["Susan", 25, "Sydney"]
# worksheets.insert_row(user, 4)

# worksheets.update_cell(7, 2, 90)

# worksheets.delete_rows(1)
# print(res)
