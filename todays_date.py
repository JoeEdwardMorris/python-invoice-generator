def todays_date (list, address) :
    import datetime as dt
    list[address]=dt.datetime.today().strftime("%d/%m/%Y")

def todays_month (list, address) :
    import datetime as dt
    list[address]=dt.datetime.today().strftime("%B")
    
    
