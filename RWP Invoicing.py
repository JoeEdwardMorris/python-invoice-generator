# -*- coding: iso-8859-15 -*-

# Imports
from excel_save_csv import *
from return_csv_as_array import *
from finder_delete_file import *
from read_text_as_list import *
from read_text_as_item import *
from word_line_breaks import *
from todays_date import *
from invoice_array_2_list_replace import *
from main_calculations import *
from figure_assign import *
from figure_calculations import *
from figure_to_string import *
from figure_currency_final_string import *
from row_calculator import *
from excel_assign import *
from word_find_replace import word_find_replace
from excel_update import excel_update
import locale
import sys


#attempt to sort out encoding issues
reload(sys)
sys.setdefaultencoding('utf8')

#Set locale for correct currency output
locale.setlocale( locale.LC_ALL, 'en_GB' )

# Set core filepaths
root_path="/Applications/RWP Invoicing/"

# Preferences filenames
preferences_path = root_path+"5 preferences/"
placeholder_filename = preferences_path+"placeholders.txt"
replacements_filename = preferences_path+"replacements.txt"
address_filename = preferences_path+"address.txt"
excel_entries_filename = preferences_path+"excel_entries.txt"
columns_filename = preferences_path+"columns.txt"
vat_rate_filename= preferences_path+"vat_rate.txt"
invoice_data_filename = preferences_path+"invoice_data_filename.txt"

# Filename setup
invoice_data_filename = root_path+"1 inputs/enter_my_invoice_data.xlsx"
csv_filename = root_path+"1 inputs/Sheet1"

word_template_filepath = root_path+"2 templates/"
word_new_filepath = root_path+"3 finished invoices/"

rfa_template_filename="Invoice Template RFA.doc"
rwp_template_filename="Invoice Template RWP.doc"

x_filepath = root_path+"4 updated spreadsheet/"
x_filename="Rachel Whiting Accounts VAT.xls"

#Concatenate paths & filenames
rfa_template_filename=word_template_filepath+rfa_template_filename
rwp_template_filename=word_template_filepath+rwp_template_filename
x_filename=x_filepath+x_filename


# Set initial variables
worksheet="Sheet1"
row_invoice_increment=1


# INITIALISE PART 2

# Read in preference data files, get relevant list lengths
list_find = read_text_as_list (placeholder_filename, '\n')
length_of_list_replace=len(list_find)
vat_rate = read_text_as_item (vat_rate_filename)
address = word_line_breaks(read_text_as_item (address_filename))
columns = read_text_as_list (columns_filename, '\n')
number_of_excel_columns=len(columns)

# Read in Excel file as CSV (WILL BE REPLACED BY UI IN LATER VERSIONS)
excel_save_csv (invoice_data_filename, csv_filename)

# Return CSV as array
invoice_array=return_csv_as_array (csv_filename)

# Delete CSV file with applescript
finder_delete_file (csv_filename)

# Find number of invoices in batch and make into range
invoice_range = range((len(invoice_array)))



#LOOP TO BE DONE FOR ALL INVOICES

for this_invoice in invoice_range:
    #INITIALISATION OF LISTS
    #initialise list_replace (temporary list used to populate replacements to placeholders)
    #to length of placeholder list loaded in from preferences
    list_replace=["" for x in range(length_of_list_replace)]
    #Initialise excel entries list with reference to columns file in preferences
    excel_entries=["" for x in range(number_of_excel_columns)]
    
    #populate this iteration's list_replace list with info from master array
    invoice_array_2_list_replace (invoice_array[this_invoice], list_replace)
        
    list_replace[26]=vat_rate
    list_replace[27]=address

    # this module TAKES the raw 'replace list' produced from the input CSV file and
    # RETURNS a currency formatted list with today's date and complete calculated figures.
    final_list_replace=main_calculations (list_replace)
    
    row=row_calculator (list_replace, 0, row_invoice_increment)
    excel_assign (list_replace, excel_entries)

    #Calculate new filenames
    rwp_new_filename="Invoice Number "+list_replace[0]
    rfa_new_filename="RGW"+list_replace[1]

    #Concatenate new filenames & paths
    #rwp_new_filename=word_new_filepath+rwp_new_filename
    #rfa_new_filename=word_new_filepath+rfa_new_filename

    #Generates custom applescripts and executes for two invoices and Excel
    word_find_replace (rwp_template_filename, word_new_filepath, rwp_new_filename, list_find, final_list_replace)
    # generate refresh invoice
    word_find_replace (rfa_template_filename, word_new_filepath, rfa_new_filename, list_find, final_list_replace)
    # update excel file
    excel_update (x_filename, excel_entries, worksheet, columns, row)

