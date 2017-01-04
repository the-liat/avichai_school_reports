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
    ws = workbook.Worksheets('Exhibits 2,3,4,5')
    t_students_own = table_dict[('own_school', 'students')][1]
    go5, go8, go11 = t_students_own.get_row(2)[2:5]
    ws.Range("C4").Value = go5
    ws.Range("C5").Value = go8
    ws.Range("C6").Value = go11
    t_students_com = table_dict[('comparison_schools', 'students')][1]
    gc5, gc8, gc11 = t_students_com.get_row(2)[2:5]
    ws.Range("D4").Value = gc5
    ws.Range("D5").Value = gc8
    ws.Range("D6").Value = gc11
    t_parents_own = table_dict[('own_school', 'parents')][1]
    ws.Range("C3").Value = t_parents_own.get_row(1)[2]
    t_parents_com = table_dict[('comparison_schools', 'parents')][1]
    ws.Range("D3").Value = t_parents_com.get_row(1)[2]
    t_staff_own = table_dict[('own_school', 'staff')][1]
    ws.Range("C7").Value = t_staff_own.get_row(1)[2]
    t_staff_com = table_dict[('comparison_schools', 'staff')][1]
    ws.Range("D7").Value = t_staff_com.get_row(1)[2]


def populate_exhibit3(table_dict, workbook):
    ws = workbook.Worksheets('Exhibits 2,3,4,5')
    schools_cells = (('own_school', 'J'), ('comparison_schools', 'k'),)
    for s_c in schools_cells:
        t_parents_own = table_dict[(s_c[0], 'parents')][1]
        i = 13
        j = 0
        while i < 17:
            cell = '"{}{}"'.format(s_c[1],i)
            po = t_parents_own.get_row(j)[4]
            ws.Range(cell).Value = po
            i += 1
            j += 1

    # t_parents_com = table_dict[('comparison_schools', 'parents')][1]
    # ws.Range("D3").Value = t_parents_com.get_row(1)[2]





"""

get_cell_value(row_index, col_index)
get_row(row_index)
get_col_by_index(col_index)
get_col_by_name(col_name)
"""
