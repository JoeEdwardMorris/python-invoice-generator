def read_csv_lines_as_lists (filename):

    import codecs
    
    text_file = codecs.open( filename, "r", "utf-8" )
    rows_list = text_file.read().split("\r")
    
    return rows_list
