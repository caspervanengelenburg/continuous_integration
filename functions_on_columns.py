import pandas as pd

def print_column_headers(a, print_columns=False):
   """
   Extract headers from excel file - including an option to print them.
   For printing the default is False. 
   
   Parameters:
   :a: relative pathname of file
   :type a: str
   :print_columns: optional parameters, `False` by default
   :type print_columns: boolean
   
   Output:
   :column_headers: headers of the columns
   :type column_headers: pd.DataFrame
   """
    
   b = pd.read_excel(a)
   column_headers = list(b.columns.values)
   
   #printing out columns row-wise
   if print_columns:
       print("\n".join(column_headers))
   return column_headers
