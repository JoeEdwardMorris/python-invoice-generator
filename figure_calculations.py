# Hopefully possible to do more elegantly with key/dictionaries at a later date
def figure_calculations (decimal_list, vat_percentage) :
    from decimal import Decimal
    
    #TOTAL FEE = FEEPERDAY*FEEDAYS    
    decimal_list[3]=decimal_list[4]*decimal_list[5]
    #ASSISTANT FEE = ASFEE*ASPERDAY
    decimal_list[6]=decimal_list[7]*decimal_list[8]
    #EXPENSES INCREMENTAL TOTAL
    decimal_list[9]=decimal_list[6]
    decimal_list[9]+=decimal_list[10]
    decimal_list[9]+=decimal_list[11]
    decimal_list[9]+=decimal_list[12]
    decimal_list[9]+=decimal_list[13]
    decimal_list[9]+=decimal_list[14]
    decimal_list[9]+=decimal_list[15]
    decimal_list[9]+=decimal_list[16]
    decimal_list[9]+=decimal_list[17]
    #AMOUNT DUE = TOTAL FEE + EXPENSES
    decimal_list[0]=decimal_list[3]+decimal_list[9]
    #VAT DUE IS CALCULATED THIS VERSION ON EVERYTHING EXCEPT EQUIPMENT
    vat_rate=Decimal(vat_percentage/100)
    vattable_total=decimal_list[3] #+TOTAL FEE
    vattable_total+=decimal_list[6] #+ASSISTANT FEE
    vattable_total+=decimal_list[10] #+ PROCESSING
    vattable_total+=decimal_list[12] #+ SUBSISTENCE
    vattable_total+=decimal_list[13] #+ PARKING
    vattable_total+=decimal_list[14] #+ CONGESTION
    vattable_total+=decimal_list[15] #+ MILEAGE
    vattable_total+=decimal_list[16] #+ POSTAGE
    vattable_total+=decimal_list[17] #+ MISC
    #decimal_list[1]=decimal_list[0]*vat_rate
    decimal_list[1]=vattable_total*vat_rate
    #TOTAL DUE = AMOUNT DUE + VAT DUE
    decimal_list[2]=decimal_list[0]+decimal_list[1]
    
    
    
