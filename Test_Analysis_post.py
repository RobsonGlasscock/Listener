import pandas as pd
import os

os.chdir("anon\\tools\\python\\listener")

contents= os.listdir()

# Scan the contents of the directory
for i in contents:
    # Identify any .xlsx file in the directory
    if '.xlsx' in i:
        # Read in the Excel file as a dataframe
        df= pd.read_excel(i)
        # Trivially add a new column named "new" that is equal to 3 for all records
        df['new']= 3
        # Export the processed data into an Excel file.
        df.to_excel('C:\\users\\robso\\onedrive\\c\\tools\\python\\listener\\Processed_Data\\Test_Output.xlsx', index=False)
