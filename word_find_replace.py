def word_find_replace (template_filename, new_path, new_filename, list_find, list_replace):
    
    #Imports OS functions for applescript launching
    import os

    # Return length of list_find and make a range for iteration
    length_of_list=len(list_find)
    list_range=range(length_of_list)

    # Generate applescript list of string elements
    # applescript Pt 1: Launch Word and load file

    applescript_for_word_list=["""tell application "Microsoft Word" \n"""]
    # Pt 1: A - generate POSIX paths
    applescript_for_word_list.append("\t set loadPath to POSIX file \"")
    applescript_for_word_list.append(template_filename)
    applescript_for_word_list.append("\"\n")
    applescript_for_word_list.append("\t set savePath to POSIX file \"")
    applescript_for_word_list.append(new_path)
    applescript_for_word_list.append("\"\n")
    # Pt 1: B - set path
    #applescript_for_word_list.append("\t tell application \"Microsoft Word\" to set default")
    #applescript_for_word_list.append(" file path file path type documents path path loadPath \n")
    # Pt 1: C - open file
    applescript_for_word_list.append("\t open file ")
    applescript_for_word_list.append("loadPath")
    applescript_for_word_list.append("\n")
        
    # applescript Pt 2: iterates find and replace applescript for each item on list
    for this_element in list_range :
        applescript_for_word_list.append("\t set findRange to find object of selection \n ")
        applescript_for_word_list.append("\t tell findRange \n ")
        applescript_for_word_list.append("\t \t execute find find text \"")
        applescript_for_word_list.append(list_find[this_element])
        applescript_for_word_list.append("\" replace with \"") 
        applescript_for_word_list.append(list_replace[this_element])
        applescript_for_word_list.append("\" replace replace all with match case\n ")
        applescript_for_word_list.append("\t end tell \n ")

    # applescript Pt 3: Concludes applescript with save and 'end tell'

    # Pt 3: A - set path
    applescript_for_word_list.append("\t tell application \"Microsoft Word\" to set default")
    applescript_for_word_list.append(" file path file path type documents path path savePath \n")

    # Pt 3: B - set path
    applescript_for_word_list.append("\t save as active document file name \"")
    applescript_for_word_list.append(new_filename)
    applescript_for_word_list.append("\" file format format document\n")
    applescript_for_word_list.append("\t close active document \n")
    applescript_for_word_list.append("end tell \n")
      
    # Joins elements of applescript list into one string
    applescript_for_word=''.join(applescript_for_word_list)

    #Print applescript (for debugging only)
    #print (applescript_for_word)

    # Run applescript
    os.system ("osascript -e \'" + applescript_for_word + "\'")
