Required packages/libraries:
Pandas,
Numpy,
Matplotlib,
scikit-learn,
SciPy,
statsmodels,
seaborn,
tensorflow

data_since_1977.7z are the entire datasets for the LabourForce data.
LabourForce2023 records only up to June 2023
covid19-download.csv is the entire dataset for the pandemic data

All the source code in this project are provided in the folder 'Source Code'
The 14100287-eng.zip, 14100287-SDMX.zip, and covid19-download.csv are in the folder 'Resource Files'
All the output we produce in data processing and data cleaning, and data analyzing are provided in the folder 'Result Files'

How to get all files in the 'Result Files' folder from scratch(code that uses models with randomized algorithms will produce slightly different files):
1. Ensure that 'python' command invokes python 3.10, or replace each 'python' command below with one that does so, for example 'python3'
2. Ensure all required packages/libraries are installed
3. Navigate to the 'Resource Files' folder. Unzip 'data_since_1977.7z' into 'data_since_1977.csv', leave it in the 'Resource Files' folder
4. Navigate to the 'Source Code' folder
5. Run 'python combine-csv.py' to get 'Result Files/combined.csv'
6. Run 'python reformat_combined.py' to get 'combined_reformatted.csv'
7. Run 'python add_total.py' to get 'combined_reformatted_total_included.csv'
8. Run "python 'Clean&Visualization.py'" to get the files starting with 'unempl_' and 'Unempl_'
9. Run 'python append_covid_data.py' to get 'covid_and_employment_total_included.csv'
10. Run 'python augment_national_covid.py' to get 'covid_and_employment_augmented_national_covid.csv'
11. Run 'python Unempl_Sex_Analysis.py' to get files 'Unemployment_Summary_Male.csv', 'Unemployment_Summary_Male.csv' and 'Sex_Compar.png'
12. Run 'python Combine_male_female.py' to get 'Unemployment_rate_AllGender.csv'
13. 


The Folders 'Eric', 'Gary', and 'Issac' were created for the convenience of our cooperation,
all the files in these folders have been duplicated in the three folders I mentioned above based on their function.

To execute the source codes, you need to unzip the data_since_1977.7z and put all the files from 'Source Code' and 'Resource Files' in one folder.
Then execute the Python files, and you will get the output we mentioned in the report.
