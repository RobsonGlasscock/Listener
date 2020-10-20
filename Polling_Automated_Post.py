import pandas as pd
import os, time, hashlib

#################### Attributions ###########################
# https://codeburst.io/using-python-script-for-data-etl-53138c567906
# https://stackoverflow.com/questions/49557421/how-to-automatically-run-python-script-when-file-is-added-to-folder
# https://askubuntu.com/questions/1159171/run-python-script-when-a-file-has-been-added-to-a-folder
# https://askubuntu.com/questions/784970/how-do-i-run-a-python-script-whenever-a-file-is-created-in-a-directory
# https://askubuntu.com/questions/781799/execution-permission-to-all-files-created-under-a-specific-directory-by-default/781909#781909
# https://pypi.org/project/inotify/
#########################

# Change working directory
os.chdir("anon\\tools\\python\\listener")

# List the contents of the directory
os.listdir()

# Loop that will search the contents of the directory for .xlsx files and will then open any .xlsx file found and crate a hash.
while 1:
    contents= os.listdir()
    # Prior_Hashes.xlsx was initialized to contain one null value. This table will be updated with the hashes from any file that is processed.
    prior_hashes= pd.read_excel("C:\\users\\robso\\onedrive\\c\\tools\\python\\listener\\Prior_Hashes\\Prior_Hashes.xlsx")
    # Create a list object of prior hashes that can be iterated over to see if the current has exists in the prior hash table (i.e., has the current file been processed previously)
    prior_hashes_list= prior_hashes['GUID'].tolist()
    time.sleep (10)
    for i in contents:
        try:
        # look for a .xlsx extension, and if this is in any item in the directory, calculate the hash
            if '.xlsx' in i:
                print(i)
                print('prior', prior_hashes_list)
                # Hash calculation
                hash= hashlib.md5(open(i, 'rb').read()).hexdigest()
                # Check to see if current hash does NOT exist in the cumulative Prior_Hash table:
                if hash not in prior_hashes_list:
                    print('not in prior', hash)
                    # If the hash is not in the prior hash list, then run Test_Analysis.py which is the analysis file connected to this process.
                    os.system('python Test_Analysis.py')
                    # Create a dataframe with the current hash and then append it to the Prior Hash table.
                    hash_df= pd.DataFrame([hash], columns=['GUID'])
                    prior_hashes= prior_hashes.append(hash_df, ignore_index=True)
                    # Export the updated Prior_Hash table to Excel.
                    prior_hashes.to_excel('C:\\users\\robso\\onedrive\\c\\tools\\python\\listener\\Prior_Hashes\\Prior_Hashes.xlsx', index=False)
        except Exception:
            continue
