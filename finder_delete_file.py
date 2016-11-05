def finder_delete_file (delete_filename) :

    #Imports OS functions for applescript launching
    import os

    # Generate applescript
    # applescript Pt 1: Launch finder and load file 
    applescript_for_finder_list=["""tell application "Finder" \n"""]
    applescript_for_finder_list.append("\t delete POSIX file \"")
    applescript_for_finder_list.append(delete_filename)
    applescript_for_finder_list.append("\" \n")
    applescript_for_finder_list.append("end tell \n")
      
    # Joins elements of applescript list into one string
    applescript_for_finder=''.join(applescript_for_finder_list)

    # Run applescript
    os.system ("osascript -e \'" + applescript_for_finder + "\'")

