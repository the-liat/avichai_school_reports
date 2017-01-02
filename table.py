"""Convert textual table from SPSS output to a table object

a SPSS table looks like that

|_____|_____________________|_________|_______|_____________|__________________|
|     |                     |Frequency|Percent|Valid Percent|Cumulative Percent|
|_____|_____________________|_________|_______|_____________|__________________|
|Valid|Did not Finish Survey|146      |4.6    |4.6          |4.6               |
|     |_____________________|_________|_______|_____________|__________________|
|     |Finished Survey      |3060     |95.4   |95.4         |100.0             |
|     |_____________________|_________|_______|_____________|__________________|
|     |Total                |3206     |100.0  |100.0        |                  |
|_____|_____________________|_________|_______|_____________|__________________|
"""
from pprint import pformat


class Table(object):
    def __init__(self, lines):
        self.lines = [line[1:-1] for line in lines]
        # Process headers
        headers = self.lines[1].split('|')
        self.headers = [x.strip() for x in headers]
        self.data = self.process_data(lines, len(self.headers))

    @staticmethod
    def process_data(lines, col_count):
        """Parse data rows

        Take into account the following:
        - Separators
        - Vertically merged cells
        - Rows whose values overlap multiple rows
        - Empty lines
        """
        result = []

        # Keep values from previous non-separated row
        merge_values = [''] * col_count
        row_values = [''] * col_count
        for line in lines[3:]:
            values = [v.strip() for v in line.split('|')[1:-1]]
            row_type = Table.get_row_type(values, col_count)
            if row_type == 'ignore':
                continue
            if row_type == 'separator':
                # Add the current data row
                data_row = (' '.join((x, y)) for x, y in zip(merge_values, row_values))
                data_row = [x.strip() for x in data_row]
                if all(v == '' for v in data_row):
                    continue

                # Parse numbers if possible
                for i, v in enumerate(data_row):
                    try:
                        data_row[i] = int(v)
                    except ValueError:
                        try:
                            data_row[i] = float(v)
                        except ValueError:
                            pass
                result.append(data_row)

                # Reset the merge values for separated rows
                for i, v in enumerate(values):
                    if set(v) == {'_'}:
                        merge_values[i] = ''
                    else:
                        merge_values[i] = row_values[i]
                # Reset the row values
                row_values = [''] * col_count
            else:
                row_values = [' '.join((x, y)) if x else y for x, y in zip(row_values, values)]

        return result

    @staticmethod
    def get_row_type(values, col_count):
        """Detect if a row is empty, has horizontal merge, separator or has data

        empty rows and rows with horizintal merge can be ignored.

        """
        # Check for horizintal merge where the number of values is less than the headers
        if len(values) < col_count:
            return 'ignore'

        compressed_values = [set(v) for v in values]
        # Check if all values are either spaces or underscores
        if all(cv == set() or cv == {' '} for cv in compressed_values):
            return 'ignore'
        elif all(cv == set() or cv == {'_'} for cv in compressed_values):
            return 'separator'

        return 'data'

    def get_cell_value(self, row_index, col_index):
        return self.data[row_index][col_index]

    def get_row(self, row_index):
        return self.data[row_index]

    def get_col_by_index(self, col_index):
        return [r[col_index] for r in self.data]

    def get_col_by_name(self, col_name):
        col_index = self.headers.index(col_name)
        return self.get_col_by_index(col_index)

    def __repr__(self):
        return pformat([self.headers] + self.data)