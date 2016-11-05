def return_csv_as_array (filename) :

    from read_csv_lines_as_lists import read_csv_lines_as_lists
    from read_csv_columns_as_lists import read_csv_columns_as_lists

    # read csv file

    line_list=read_csv_lines_as_lists (filename)

    # get number of rows (each row is an invoice except line 1)

    number_of_invoices=len(line_list)
    number_of_invoices_range=range(2, number_of_invoices)

    # get columns length

    cols_list_first_line=read_csv_columns_as_lists (line_list[1])

    number_of_columns=len(cols_list_first_line)
    number_of_columns_range=range(number_of_columns)

    # initialise invoice array with line 1 (ignore title line)
    invoice_array = [cols_list_first_line] 

    for this_invoice in number_of_invoices_range :
        invoice_array.append (read_csv_columns_as_lists (line_list[this_invoice]) ) 

    # returns array of [invoices[columns]]
    return invoice_array       


