# Hopefully possible to do more elegantly with key/dictionaries at a later date
def figure_currency_final_string (source_list, string_list) :
    import locale
    final_list=string_list
    # NOTE this one adds pound signs where needed and formats numbers correctly
    final_list[4]=remove_spare_zeros(locale.currency(source_list[0]))
    final_list[5]=remove_spare_zeros(locale.currency(source_list[1]))
    final_list[6]=remove_spare_zeros(locale.currency(source_list[2]))
    final_list[8]=remove_spare_zeros(locale.currency(source_list[3]))
    final_list[9]=remove_spare_zeros(locale.currency(source_list[4]))
    final_list[10]=str(source_list[5])
    final_list[11]=remove_spare_zeros(locale.currency(source_list[6]))
    final_list[12]=remove_spare_zeros(locale.currency(source_list[7]))
    final_list[13]=str(source_list[8])
    final_list[14]=remove_spare_zeros(locale.currency(source_list[9]))
    final_list[17]=remove_spare_zeros(locale.currency(source_list[10]))
    final_list[18]=remove_spare_zeros(locale.currency(source_list[11]))
    final_list[19]=remove_spare_zeros(locale.currency(source_list[12]))
    final_list[20]=remove_spare_zeros(locale.currency(source_list[13]))
    final_list[21]=remove_spare_zeros(locale.currency(source_list[14]))
    final_list[22]=remove_spare_zeros(locale.currency(source_list[15]))
    final_list[23]=remove_spare_zeros(locale.currency(source_list[16]))
    final_list[24]=remove_spare_zeros(locale.currency(source_list[17]))
    return final_list    

def remove_spare_zeros (string) :
    new_string=string.replace('.00','')
    return new_string
