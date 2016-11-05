def excel_save_csv (template_filename, csv_filename) :

    #Imports OS functions for applescript launching
    import os

    # Generate applescript
    # applescript Pt 1: Launch Excel and load file 
    applescript_for_excel_list=["""tell application "Microsoft Excel" \n"""]

    # Pt 1: A - generate POSIX paths
    applescript_for_excel_list.append("\t set loadPath to POSIX file \"")
    applescript_for_excel_list.append(template_filename)
    applescript_for_excel_list.append("\"\n")
    applescript_for_excel_list.append("\t set savePath to POSIX file \"")
    applescript_for_excel_list.append(csv_filename)
    applescript_for_excel_list.append("\"\n")

    # Pt 1: B - open file
    applescript_for_excel_list.append("\t open file loadPath \n")

    # applescript Pt 2: Save Excel file
    applescript_for_excel_list.append("""\t tell workbook 1 \n""")
    applescript_for_excel_list.append("""\t\t tell sheet 1 \n""") 
    applescript_for_excel_list.append("\t\t\t save in savePath")
    applescript_for_excel_list.append(" as CSV file format \n")
    applescript_for_excel_list.append("""\t\t end tell \n""") 
    applescript_for_excel_list.append("\t close without saving \n")
    applescript_for_excel_list.append("\t end tell \n")
    applescript_for_excel_list.append("end tell \n")
      
    # Joins elements of applescript list into one string
    applescript_for_excel=''.join(applescript_for_excel_list)

    # Print applescript for debugging
    #print (applescript_for_excel)

    # Run applescript
    os.system ("osascript -e \'" + applescript_for_excel + "\'")

