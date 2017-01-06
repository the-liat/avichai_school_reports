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
    schools_cells = (('own_school', 'J'), ('comparison_schools', 'K'))
    for s_c in schools_cells:
        t_parents_own = table_dict[(s_c[0], 'parents')][1]
        i = 13
        j = 0
        while i < 17:
            cell = "{}{}".format(s_c[1], i)
            po = t_parents_own.get_row(j)[4]
            ws.Range(cell).Value = po
            i += 1
            j += 1


def populate_exhibit4(table_dict, workbook):
    ws = workbook.Worksheets('Exhibits 2,3,4,5')
    t_parents_own = table_dict[('own_school', 'parents')][1]
    ws.Range("J26").Value = t_parents_own.get_row(2)[4] + t_parents_own.get_row(3)[4]
    t_parents_com = table_dict[('comparison_schools', 'parents')][1]
    ws.Range("K26").Value = t_parents_com.get_row(2)[4] + t_parents_com.get_row(3)[4]
    ws.Range("J27").Value = table_dict[('own_school', 'students')][1].get_row(1)[4]
    ws.Range("J28").Value = table_dict[('own_school', 'students')][2].get_row(1)[4]
    ws.Range("J29").Value = table_dict[('own_school', 'students')][3].get_row(1)[4]
    ws.Range("J30").Value = table_dict[('own_school', 'students')][4].get_row(1)[4]
    ws.Range("K27").Value = table_dict[('comparison_schools', 'students')][1].get_row(1)[4]
    ws.Range("K28").Value = table_dict[('comparison_schools', 'students')][2].get_row(1)[4]
    ws.Range("K29").Value = table_dict[('comparison_schools', 'students')][3].get_row(1)[4]
    ws.Range("K30").Value = table_dict[('comparison_schools', 'students')][4].get_row(1)[4]


def find_cells(table):  # this should work for every table in the table dictionary
    i = 0
    x = 0
    while table.get_row(i)[1] != 'Total':
        if table.get_row(i)[1] == 'Important' or table.get_row(i)[1] == 'Very important':
            x += table.get_row(i)[4]
        i += 1
    return x  # sum of 'important' and 'very important' %


def populate_exhibit5(table_dict, workbook):
    ws = workbook.Worksheets('Exhibits 2,3,4,5')
    for school, stakeholder in table_dict:
        table = table_dict[(school, stakeholder)][1]
        value = find_cells(table)
        if school == 'own_school':
            col = 'J'
        else:
            col = 'K'
        if stakeholder == 'staff':
            row = '43'
        elif stakeholder == 'students':
            row = '44'
        else:
            row = '45'
        cell = "{}{}".format(col, row)
        ws.Range(cell).Value = value


def populate_exhibit6(table_dict, workbook):
    ws = workbook.Worksheets('Exhibits 6,7,8,9')


#     for keys in table_dict.keys():
#         school, stakeholder = keys[0], keys[1]
#         table = table_dict[(school, stakeholder)][1]

def get_values_from_table(i, table, labels_rows):
    for d in labels_rows:
        if table.get_row(i)[1] == d['label']:
            row = d['row']
            x = table.get_row(i)[4]
            return x, row
    return None


def populate_exhibit7(table_dict, workbook):
    ws = workbook.Worksheets('Exhibits 6,7,8,9')
    # where each value in table goes in excel rows
    labels_rows = [
        dict(label='Not at all satisfied', row=26),
        dict(label='A little bit satisfied', row=27),
        dict(label='Somewhat satisfied', row=28),
        dict(label='Satisfied', row=29),
        dict(label='Very satisfied', row=30)
    ]
    # defining tables to get information from
    t_parents_own = table_dict[('own_school', 'parents')][1]
    t_staff_own = table_dict[('own_school', 'staff')][1]
    t_parents_com = table_dict[('comparison_schools', 'parents')][1]
    t_staff_com = table_dict[('comparison_schools', 'staff')][1]
    # where each table data goes in excel columns
    tables = [
        dict(table=t_staff_own, column='K'),
        dict(table=t_parents_own, column='L'),
        dict(table=t_staff_com, column='M'),
        dict(table=t_parents_com, column='N')
    ]
    # in each table, it will go to the line and find the appropriate
    # value for this line and put it in the right position, iterate on all lines
    for d in tables:
        i = 0
        while d['table'].get_row(i)[1] != 'Total':
            value, row = get_values_from_table(i, d['table'], labels_rows)
            col = d['column']
            cell = "{}{}".format(col, row)
            ws.Range(cell).Value = value
            i += 1


"""

get_cell_value(row_index, col_index)
get_row(row_index)
get_col_by_index(col_index)
get_col_by_name(col_name)
"""
