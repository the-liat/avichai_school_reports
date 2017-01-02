import win32com.client as win32
import os


def open_excel():
    x = win32.gencache.EnsureDispatch('Excel.Application')
    x.DisplayAlerts = False
    return x


def close_excel(x):
    x.Application.Quit()


school_name = 'Berman'


def create_school_workbook_from_template(school_name):
    f = r'C:\Users\Liat\Google Drive\102-04  ACF Hebrew in Jewish Day Schools\Deliverables\School Reports\ACF HebDS All Exhibits for School Report TEMPLATE LS20170101.xlsx'


"""
get_cell_value(row_index, col_index)
get_row(row_index)
get_col_by_index(col_index)
get_col_by_name(col_name)
"""
