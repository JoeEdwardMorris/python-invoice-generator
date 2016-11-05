def excel_update (template_filename, entries, worksheet, columns, row) :

    #Imports OS functions for applescript launching
    import os

    # Return length of list_find and make a range for iteration
    length_of_list=len(entries)
    list_range=range(length_of_list)

    # Generate applescript
    # applescript Pt 1: Launch Excel and load file 
    applescript_for_excel_list=["""tell application "Microsoft Excel" \n"""]

    # Pt 1: A - generate POSIX paths
    applescript_for_excel_list.append("\t set loadPath to POSIX file \"")
    applescript_for_excel_list.append(template_filename)
    applescript_for_excel_list.append("\"\n")

    # Pt 1: B - open file
    applescript_for_excel_list.append("\t open file loadPath \n")

    # applescript Pt 2: iterates find and replace applescript for each item on list
    for this_element in list_range :
        applescript_for_excel_list.append("\t tell worksheet \"")
        applescript_for_excel_list.append(worksheet)
        applescript_for_excel_list.append("\" of active workbook \n")
        applescript_for_excel_list.append("\t \t set value of range \"")
        applescript_for_excel_list.append(str(columns[this_element]))
        applescript_for_excel_list.append(str(row)) 
        applescript_for_excel_list.append("\" to \"")
        applescript_for_excel_list.append(str(entries[this_element]))
        applescript_for_excel_list.append("\"\n")
        applescript_for_excel_list.append("\t end tell \n ")

    # applescript Pt 3: Concludes applescript with save and 'end tell'
    applescript_for_excel_list.append("\t save active workbook \n")
    applescript_for_excel_list.append("\t close active workbook \n")
    applescript_for_excel_list.append("end tell \n")
      
    # Joins elements of applescript list into one string
    applescript_for_excel=''.join(applescript_for_excel_list)

    # Print applescript for debugging
    #print (applescript_for_excel)

    # Run applescript
    os.system ("osascript -e \'" + applescript_for_excel + "\'")
