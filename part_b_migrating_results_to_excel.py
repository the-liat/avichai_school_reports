import shutil
import win32com.client as win32
import os

xl_app = None

def open_excel():
    global xl_app
    xl_app = win32.gencache.EnsureDispatch('Excel.Application')
    xl_app.DisplayAlerts = False


def close_excel():
    xl_app.Application.Quit()


def create_school_workbook_from_template(school_name):
    f = r'C:\Users\Liat\Google Drive\102-04  ACF Hebrew in Jewish Day Schools\Deliverables\School Reports\ACF HebDS All Exhibits for School Report TEMPLATE LS20170101.xlsx'
    dir_name = r'C:\Users\Liat\Google Drive\102-04  ACF Hebrew in Jewish Day Schools\Deliverables\School Reports\Final Excel Sheets for Reports Production'
    file_name = os.path.join(dir_name, 'ACF HebDS. {}.xlsx'.format(school_name))
    shutil.copyfile(f, file_name)
    wb = xl_app.Workbooks.Open(file_name)
    return wb, file_name

def populate_exhibit(exhibit_number, table_dict, workbook):
    func = globals()['populate_exhibit{}'.format(exhibit_number)]
    func(table_dict, workbook)

def populate_exhibit2(table_dict, workbook):
    t = table_dict[('own_school', 'students')][1]
    g5, g8, g11 = t.get_row(2)[2:5]
    ws = workbook.Worksheets('Exhibits 2,3,4,5')
    ws.Range("C4").Value = g5
    ws.Range("C5").Value = g8
    ws.Range("C6").Value = g11





"""

get_cell_value(row_index, col_index)
get_row(row_index)
get_col_by_index(col_index)
get_col_by_name(col_name)
"""
