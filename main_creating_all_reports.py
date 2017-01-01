"""
1. Create list of dictionaries. Each dictionary represents one school and contains: School code, School name,
                                School sector (3 options), number of grades tested (3 options)

2. Start a loop on the schools list
    a. spss_analyses - syntax of data analysis
        Each syntax includes:
        Your School analyses (select school)
            Activate Student data file, run student syntax, export to file, close output
            Activate Parent file, run parent syntax, export to file, close output
            Activate Staff file, run staff syntax, export to file, close output
        Comparison School analyses (select schools)
            Activate Student data file, run student syntax, export to file, close output
            Activate Parent file, run parent syntax, export to file, close output
            Activate Staff file, run staff syntax, export to file, close output
    b. copy_raw_paste_to_template
        Open created excel file
        Open template file
        Save as - tamplate file to file with school name in it
        21 Exhibits, for each one locate data in excel file and transport to template
        Save file

"""
import sys
sys.path.insert(0,r'C:\Program Files\IBM\SPSS\Statistics\24\Python\Lib\site-packages')
import spss
import spssaux

from school_list import schools
from part_a_spss_analyses import spss_results
from create_exhibits import copy_raw_paste_to_template

for school_name, school_code, number_of_grades, sector_code, grades_dict in schools.iteritems():
    spss_results(school_code)
    copy_raw_paste_to_template(s)

f = r'C:\Users\Liat\Google Drive\102-04  ACF Hebrew in Jewish Day Schools\Data Bases and Data Files\Survey Responses\Student Responses\Researching_Hebrew_in_Day_Schools_Student_Survey__V22 LS 20161203 USE THIS.sav'
spssaux.OpenDataFile(f)

# spss.submit()