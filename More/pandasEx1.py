import pandas as pd

# Replace with the path to your .xls file
file_path = 'c:\\data.xls'
# df = pd.read_excel(file_path)
# Read the .xls file
df = pd.read_excel(file_path, engine='xlrd')

df['testingCol'] = df['name'] + "testing"

for index,row in df.iterrows():
    # Access data using row[column_index]
    df.at[index, 'testingCol'] =  row['name'] + row['admin']
    print(f"name: {row['name']} Tetsing coln:{row['testingCol']}")
    print(f"admin: {row['admin']}")

# Display the data
print("Data from the Excel file:\n")
print(df.to_string(index=False))