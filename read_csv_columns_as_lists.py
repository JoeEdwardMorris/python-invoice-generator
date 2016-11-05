#NOTE THIS READS IN A LIST ELEMENT THAT HAS ALREADY BEEN SPLIT
# out from a CSV file by read_csv_lines_as_lists...
# so that module must be run first

def read_csv_columns_as_lists (line_list_element) :

    cols_list = line_list_element.split(",")
    
    return cols_list
