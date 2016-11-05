def excel_assign (source_list, destination_list) :
    from todays_date import todays_month
    # Im sure with more knowledge of keys/dictionaries could be more elegant
    destination_list[0]=source_list[0]
    destination_list[1]=source_list[1]
    todays_month(destination_list,2)
    destination_list[3]=source_list[2]
    #TURN JOB TITLE TO CAPS
    job_title=source_list[3]
    destination_list[4]=job_title.upper()

    destination_list[5]=source_list[4]
    destination_list[6]=source_list[5]
    destination_list[7]=source_list[6]
    
