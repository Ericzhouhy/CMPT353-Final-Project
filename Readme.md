data_since_1977.7z are the entire datasets for the LabourForce data.
LabourForce2023 records only up to June 2023
covid19-download.csv is the entire dataset for the pandemic data

All the source code in this project are provided in the folder 'Source Code'
The 14100287-eng.zip, 14100287-SDMX.zip, and covid19-download.csv are in the folder 'Resource Files'
All the output we produce in data processing and data cleaning, and data analyzing are provided in the folder 'Result Files'

Required packages/libraries:
Pandas,
Numpy,
Matplotlib,
scikit-learn,
SciPy,
statsmodels,
seaborn,
tensorflow

How to run:
0. ensure that 'python' command invokes python 3.10, or replace each 'python' command below with one that does so, for example 'python3'
1. First we need to be in the 'Source Code' folder, then
2. run 'python combine-csv.py' to get 'Result Files/combined.csv'
3. run 'python reformat_combined.py' to get 'combined_reformatted.csv'
4. 


The Folders 'Eric', 'Gary', and 'Issac' were created for the convenience of our cooperation,
all the files in these folders have been duplicated in the three folders I mentioned above based on their function.

To execute the source codes, you need to unzip the data_since_1977.7z and put all the files from 'Source Code' and 'Resource Files' in one folder.
Then execute the Python files, and you will get the output we mentioned in the report.
