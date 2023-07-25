import os
import pandas as pd

#combine all the csv files in the folders
def combine_csvs_in_folder(folder_path):
    all_dataframes = []
    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            file_path = os.path.join(folder_path, file)
            df = pd.read_csv(file_path)
            all_dataframes.append(df)
    combined_df = pd.concat(all_dataframes, ignore_index=True)
    return combined_df

folders = [
    'C:/Users/ericz/Desktop/CMPT353/CMPT353-Final-Project/ProjectData/LabourForce2019',
    'C:/Users/ericz/Desktop/CMPT353/CMPT353-Final-Project/ProjectData/LabourForce2020',
    'C:/Users/ericz/Desktop/CMPT353/CMPT353-Final-Project/ProjectData/LabourForce2021',
    'C:/Users/ericz/Desktop/CMPT353/CMPT353-Final-Project/ProjectData/LabourForce2022',
    'C:/Users/ericz/Desktop/CMPT353/CMPT353-Final-Project/ProjectData/LabourForce2023',
]

combined_dataframes = [combine_csvs_in_folder(folder_path) for folder_path in folders]

final_combined_df = pd.concat(combined_dataframes, ignore_index=True)

final_combined_df.to_csv('C:/Users/ericz/Desktop/CMPT353/CMPT353-Final-Project/ProjectData/combined.csv', index=False)