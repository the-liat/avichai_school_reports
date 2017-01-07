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
    if not os.path.exists(file_name):
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


def get_values_from_table(i, table, labels_rows, y):
    # Y is the index of the value needed to be pulled from the spss table
    row = table.get_row(i)
    for d in labels_rows:
        match = True
        for col, label in d['labels'].iteritems():
            if row[col] != label:
                match = False
                break
        if not match:
            continue
        return row[y], d['row']
    return None, None


def populate_excel_by_row_labels(tables, labels_rows, ws, y):  # for exhibits 7, 9, 10, 13, 17, 18, 20
    for d in tables:
        i = 0  # i is the index of the table line
        while i < len(d['table'].data):
            value, row = get_values_from_table(i, d['table'], labels_rows, y)
            if value is None:
                i += 1
                continue
            col = d['column']
            cell = "{}{}".format(col, row)
            ws.Range(cell).Value = value
            i += 1


def get_values_exhibits_6_17(i, j, table, labels_rows, y):
    value = table.get_row(i)[y]
    row = labels_rows[j]['row']
    return value, row


def populate_exhibit6(table_dict, workbook):
    ws = workbook.Worksheets('Exhibits 6,7,8,9')
    # where each value in table goes in excel rows
    labels_rows = [
        dict(labels={0: 'it connects Jews around the world',
                     1: 'Agree/Strongly Agree'}, row=5),
        dict(labels={0: 'it makes one feel a part of the group when people mix Hebrew into English',
                     1: 'Agree/Strongly Agree'}, row=6),
        dict(labels={0: 'it is a part of being Jewish',
                     1: 'Agree/Strongly Agree'}, row=7),
        dict(labels={0: "it maintains the Jewish people's language",
                     1: 'Agree/Strongly Agree'}, row=8),
        dict(labels={0: 'it helps in forming a connection with Israel',
                     1: 'Agree/Strongly Agree'}, row=9),
        dict(labels={0: 'it prepares one to make Aliyah in case one wants to',
                     1: 'Agree/Strongly Agree'}, row=12),
        dict(labels={0: 'it helps when visiting Israel',
                     1: 'Agree/Strongly Agree'}, row=13),
        dict(labels={0: 'it allows one to read modern Israeli books, newspapers, websites or music lyrics',
                     1: 'Agree/Strongly Agree'}, row=14),
        dict(labels={0: 'it helps in communicating with other Jews around the world',
                     1: 'Agree/Strongly Agree'}, row=15),
        dict(labels={0: 'it helps communicate with people who only speak Hebrew',
                     1: 'Agree/Strongly Agree'}, row=16),
        dict(labels={0: 'Learning a second language contributes to brain development',
                     1: 'Agree/Strongly Agree'}, row=18)
    ]
    # defining tables to get information from
    t_parents_own = table_dict[('own_school', 'parents')][0]
    t_students_own = table_dict[('own_school', 'students')][0]
    t_staff_own = table_dict[('own_school', 'staff')][0]
    t_parents_com = table_dict[('comparison_schools', 'parents')][0]
    t_students_com = table_dict[('comparison_schools', 'students')][0]
    t_staff_com = table_dict[('comparison_schools', 'staff')][0]
    # where each table data goes in excel columns
    tables = [
        dict(table=t_staff_own, column='D'),
        dict(table=t_students_own, column='C'),
        dict(table=t_parents_own, column='B'),
        dict(table=t_staff_com, column='G'),
        dict(table=t_students_com, column='F'),
        dict(table=t_parents_com, column='E')
    ]
    # in each table, it will go to the line and find the appropriate
    # value for this line and put it in the right position, iterate on all lines
    y = 2  # Y is the index of the value needed to be pulled from the spss table
    for d in tables:
        i = 1  # i is the index of the table line
        j = 0
        while i < len(d['table'].data):
            value, row = get_values_exhibits_6_17(i, j, d['table'], labels_rows, y)
            col = d['column']
            cell = "{}{}".format(col, row)
            ws.Range(cell).Value = value
            i += 2
            j += 1


def populate_exhibit7(table_dict, workbook):  # table_dict is the dictionary for the spss tables
    ws = workbook.Worksheets('Exhibits 6,7,8,9')
    # where each value in table goes in excel rows
    labels_rows = [
        dict(labels={1: 'Not at all satisfied'}, row=26),
        dict(labels={1: 'A little bit satisfied'}, row=27),
        dict(labels={1: 'Somewhat satisfied'}, row=28),
        dict(labels={1: 'Satisfied'}, row=29),
        dict(labels={1: 'Very satisfied'}, row=30)
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
    y = 4  # Y is the index of the value needed to be pulled from the spss table
    populate_excel_by_row_labels(tables, labels_rows, ws, y)


def populate_excel_by_row_labels_ex8(tables, labels_rows, ws, y):
    for d in tables:
        i = 0  # i is the index of the table line
        while i < len(d['table'].data):
            value, row = get_values_from_table(i, d['table'], labels_rows, y)
            if value is None:
                i += 1
                continue
            col = d['column']
            cell = "{}{}".format(col, row)
            if value >= 33:
                ws.Range(cell).Value = 'X'
            i += 1


def populate_exhibit8(table_dict, workbook):  # table_dict is the dictionary for the spss tables
    ws = workbook.Worksheets('Exhibits 6,7,8,9')
    # where each value in table goes in excel rows
    labels_rows = [
        dict(labels={1: 'Challange-The teachers do not have expertise in second language instruction'},
             row=43),
        dict(labels={1: 'Challange-The teachers are not knowledgeable in Hebrew for everyday communication'},
             row=44),
        dict(labels={1: 'Challange-The Hebrew curriculum used is not good enough (e.g, outdated, not challenging)'},
             row=45),
        dict(labels={1: 'Challange-Hebrew for everyday communication instruction is mainly conducted in English'},
             row=46),
        dict(labels={1: 'Challange-The teachers do not care about Hebrew for everyday communication proficiency'},
             row=47),
        dict(labels={1: 'Challange-It is not a priority of the school'},
             row=48),
        dict(labels={1: 'Challange-There is not enough time devoted to Hebrew for everyday communication'},
             row=49),
        dict(labels={1: 'Challange-The diversity of Hebrew levels in the class'},
             row=50),
        dict(labels={1: 'Challange-There are too many children in the classroom'},
             row=51),
        dict(labels={1: 'Hebrew for everyday communication is the first class that gets canceled for an activity'},
             row=52),
    ]
    # defining tables to get information from
    t_parents_own = table_dict[('own_school', 'parents')][1]
    t_staff_own = table_dict[('own_school', 'staff')][1]
    t_parents_com = table_dict[('comparison_schools', 'parents')][1]
    t_staff_com = table_dict[('comparison_schools', 'staff')][1]
    # where each table data goes in excel columns
    tables = [
        dict(table=t_staff_own, column='C'),
        dict(table=t_parents_own, column='B'),
        dict(table=t_staff_com, column='E'),
        dict(table=t_parents_com, column='D')
    ]
    # in each table, it will go to the line and find the appropriate
    # value for this line and put it in the right position, iterate on all lines
    y = 4  # Y is the index of the value needed to be pulled from the spss table
    populate_excel_by_row_labels_ex8(tables, labels_rows, ws, y)


def populate_exhibit9(table_dict, workbook):  # table_dict is the dictionary for the spss tables
    ws = workbook.Worksheets('Exhibits 6,7,8,9')
    # where each value in table goes in excel rows
    labels_rows = [
        dict(labels={1: 'Ongoing professional development opportunities'}, row=57),
        dict(labels={1: 'Enough time to prepare'}, row=58),
        dict(labels={1: 'Administrative support'}, row=59),
        dict(labels={1: 'Hebrew for everyday communication assessment instrument'}, row=60),
        dict(labels={1: 'Classroom support(e.g., teaching assistant)'}, row=61),
        dict(labels={1: 'Hebrew for everyday communication curriculum'}, row=62),
        dict(labels={1: 'Resources for special needs / gifted students'}, row=63),
        dict(labels={1: 'Text and Prayer Hebrew assessment instrument'}, row=64),
        dict(labels={1: 'Text and Prayer Hebrew curriculum'}, row=65),
        dict(labels={1: 'Pedagogical materials(books, resources)'}, row=66),
    ]
    # defining tables to get information from
    t_staff_own = table_dict[('own_school', 'staff')][0]
    t_staff_com = table_dict[('comparison_schools', 'staff')][0]
    # where each table data goes in excel columns
    tables = [
        dict(table=t_staff_own, column='B'),
        dict(table=t_staff_com, column='C')
    ]
    # in each table, it will go to the line and find the appropriate
    # value for this line and put it in the right position, iterate on all lines
    y = 2  # Y is the index of the value needed to be pulled from the spss table
    for d in tables:
        i = 3  # i is the index of the table line
        j = 0
        while i < len(d['table'].data):
            value, row = get_values_exhibits_6_17(i, j, d['table'], labels_rows, y)
            col = d['column']
            cell = "{}{}".format(col, row)
            ws.Range(cell).Value = value
            i += 4
            j += 1

    """

    get_cell_value(row_index, col_index)
    get_row(row_index)
    get_col_by_index(col_index)
    get_col_by_name(col_name)
    """
