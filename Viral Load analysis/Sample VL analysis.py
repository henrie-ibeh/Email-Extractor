import pandas as pd
import numpy as np

# importing the dataframe
data = pd.read_csv('./Book1.csv', low_memory=False)

# selecting unique patient identifiers
# expected col= patient_unique_id
df1 = pd.DataFrame()
df1['ID'] = data['patient_unique_id'].unique()

# patient ART start date
# deriving patient uniqueID, ART Start Date, date confirmed positive
df2 = data[['patient_unique_id', 'art_start_date', 'date_confirmed_positive']].drop_duplicates().reset_index(drop=True)

# Getting the first and last visit dates and merging them into 1 DF
df_lastvisitdate = data.groupby('patient_unique_id').max()['visit_date']
df_firstvisitdate = data.groupby('patient_unique_id').min()['visit_date']

# the merge
df3 = pd.merge(df2, df_lastvisitdate, how='inner', on='patient_unique_id')
df4 = pd.merge(df3, df_firstvisitdate, how='inner', on='patient_unique_id')
df4.rename(columns={'visit_date_x': 'last_visit_date', 'visit_date_y': 'first_visit_date'}, inplace=True)
# dealing with null values
df4 = df4.fillna(0)
# formatting date columns
df4['last_visit_date'] = pd.to_datetime(df4['last_visit_date'], errors='coerce')
df4['art_start_date'] = pd.to_datetime(df4['art_start_date'], errors='coerce')
df4['first_visit_date'] = pd.to_datetime(df4['first_visit_date'], errors='coerce')

# calculating date differences
'''
df4['DurationSinceDiagnosis'] = ((df4.last_visit_date - df4.art_start_date)/np.timedelta64(1, 'M'))
df4['DurationSinceDiagnosis'] = df4['DurationSinceDiagnosis'].astype(int)
'''
df4['DurationSinceDiagnosis'] = df4['last_visit_date'].dt.to_period('M').astype(int) - df4[
    'art_start_date'].dt.to_period('M').astype(int)



# print(df4[['art_start_date', 'last_visit_date', 'DurationSinceDiagnosis']])

# Exporting it into a CSV File
# df4.to_csv('export.csv')
