from collections import defaultdict

import spssaux

from part_b_migrating_results_to_excel import open_excel, close_excel, create_school_workbook_from_template, \
    populate_exhibit2, populate_exhibit
from spss_analyses import run
from all_exhibits_syntax import exhibit_stakeholders
from school_list import schools
from spss_output_parser import parse_output

stakeholder_filenames = dict(
    students=r'C:\Users\Liat\Google Drive\102-04  ACF Hebrew in Jewish Day Schools\Data Bases and Data Files\Survey Responses\Student Responses\Researching_Hebrew_in_Day_Schools_Student_Survey__V22 LS 20161226 USE THIS.sav',
    parents=r'C:\Users\Liat\Google Drive\102-04  ACF Hebrew in Jewish Day Schools\Data Bases and Data Files\Survey Responses\Parent Responses\Researching_Hebrew_in_Day_SchoolsParent_Survey_V22_LS_20161226 USE THIS.sav',
    staff=r'C:\Users\Liat\Google Drive\102-04  ACF Hebrew in Jewish Day Schools\Data Bases and Data Files\Survey Responses\Staff Responses\Researching_Hebrew_in_Day_SchoolsStaff_Survey_V22_LS_20161226 USE THIS.sav')


def build_selection_for_own_school(school, stakeholder_name):
    """ Build the spss command for selection the specific school
    populaate placehoolder in template with school code
    :param school:
    :return:
    """
    template = """USE ALL.
                  COMPUTE filter_$=(School_Name = {0}).
                  VARIABLE LABELS filter_$ 'School_Name = {0} (FILTER)'.
                  VALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'.
                  FORMATS filter_$ (f1.0).
                  FILTER BY filter_$.
                  EXECUTE."""
    result = template.format(school['code'])
    return result


def build_grade_levels(grade_levels):
    conditions = []
    if grade_levels['5th'] == 1:
        conditions.append('grade_level=1')
    if grade_levels['8th'] == 1:
        conditions.append('grade_level=2')
    if grade_levels['11th'] == 1:
        conditions.append('grade_level=3')
    result = ' or '.join(conditions)
    return result


# def build_selection_for_comparison_schools(school):
#     """Build the spss command for selection of the comparison schools
#     populate placehoolders in template with school code, sector, grades
#     :param school:
#     :return:
#     """
#     template = """
#         USE ALL.
#         COMPUTE filter_$=(School_Name <> {school_code} and School_Denomination_3_Groups={sector}
#         and ({grade_levels})).
#         VARIABLE LABELS filter_$ 'School_Name <> {school_code} and School_Denomination_3_Groups={sector}
#         and ({grade_levels})(FILTER)'.
#         VALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'.
#         FORMATS filter_$ (f1.0).
#         FILTER BY filter_$.
#         EXECUTE.
#         """
#     gl = build_grade_levels(school['grades'])
#     result = template.format(school_code=school['code'], sector=school['sector'], grade_levels=gl)
#     return result

def build_selection_for_comparison_schools(school, stakeholder_name):
    """Build the spss command for selection of the comparison schools
    populate placehoolders in template with school code, sector, grades
    :param school:
    :return:
    """
    template = """
        USE ALL.
        COMPUTE filter_$=(School_Name <> {school_code} and School_Denomination_3_Groups={sector}
        {grade_levels}).
        VARIABLE LABELS filter_$ 'School_Name <> {school_code} and School_Denomination_3_Groups={sector}
        {grade_levels}(FILTER)'.
        VALUE LABELS filter_$ 0 'Not Selected' 1 'Selected'.
        FORMATS filter_$ (f1.0).
        FILTER BY filter_$.
        EXECUTE.
        """
    if stakeholder_name == 'students':
        gl = 'and ({})'.format(build_grade_levels(school['grades']))
    else:
        gl = ''
    result = template.format(school_code=school['code'], sector=school['sector'], grade_levels=gl)
    return result


def run_spss_syntax_per_exhibit(school, exhibit_number, stakeholder_commands, selection):
    result = defaultdict(list)
    for stakeholder_name, exhibit_cmd in stakeholder_commands.items():
        filename = stakeholder_filenames[stakeholder_name]
        spssaux.OpenDataFile(filename)
        for selection_name, func in selection.iteritems():
            print '--- exhibit: {}, stakeholder: {}, selection: {}'.format(exhibit_number,
                                                                           stakeholder_name,
                                                                           selection_name)
            commands = func(school, stakeholder_name)
            cmd_list = commands.split('\n')
            run(cmd_list)
            out = run([exhibit_cmd])
            lines = out.split('\r\n')
            tables = parse_output(lines, tables_only=True)
            for i, table in enumerate(tables):
                print ('[{}] --- Table {} ---'.format(selection_name, i))
                print table
                result[(selection_name, stakeholder_name)].append(table)
    return result


def run_analyses(school):
    wb, file_name = create_school_workbook_from_template(school['name'])
    selection = dict(
        own_school=build_selection_for_own_school,
        comparison_schools=build_selection_for_comparison_schools)
    for exhibit_number, stakeholder_commands in exhibit_stakeholders.iteritems():
        table_dict = run_spss_syntax_per_exhibit(school, exhibit_number, stakeholder_commands, selection)
        populate_exhibit(exhibit_number, table_dict, wb, school)
    wb.SaveAs(file_name)



def main():
    open_excel()
    for school in schools:
        run_analyses(school)
    # close_excel()


if __name__ == '__main__':
    main()
