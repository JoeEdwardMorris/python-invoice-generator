# -*- coding: iso-8859-15 -*-

# this module takes the 'replace list' produced from the input CSV file,
# automatically adds date and VAT rate, converts figures to decimal numbers,
# calculates various totals including VAT, and returns the calculated data
# to the initial 'string' list. It then generates a second, final, string 'list'
# upon which it formats the currency figures where necessary.
# The function RETURNS this final list.

def main_calculations (list_replace) :

    from todays_date import todays_date
    from figure_assign import figure_assign
    from figure_calculations import figure_calculations
    from figure_to_string import figure_to_string
    from figure_currency_final_string import figure_currency_final_string
    
    #add today's date at 'invoice date' address
    todays_date (list_replace,2)
    
    #produce new list of decimal number values for relevant parameters
    # (for number manipulation where necessary)
    figure_list=figure_assign (list_replace, 18)
    
    #produce a floating point number VAT percentage
    vat_percentage=float(list_replace[26])
    
    # carry out calculations on decimal figures
    figure_calculations (figure_list, vat_percentage)
    
    # returns decimal data to initial 'string' list
    figure_to_string (figure_list, list_replace)

    # produces final list from initial list with currency formatting
    # (Adds £ signs, formats to two decimal places, removes trailing zeroes .00)
    final_list_replace = figure_currency_final_string (figure_list, list_replace)

    # Rteurns final, currency formatted list
    return final_list_replace
