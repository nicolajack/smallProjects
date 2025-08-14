# importing pandas
import pandas as pd

# needs to seperate by row, and for each row send the name, age, and occupation to piscoc api

# reading the excel file
def read_excel_file(file_path):
    # initialize a dataframe
    df=pd.read_excel(file_path)

    # separate by row
    rows = df.iterrows()

    # for each row, send the name, age, and occupation to piscoc api
    for index, row in rows:
        name = row[0]
        age = row[1]
        occupation = row[2]

        # send to piscoc api
        sendToPiscoc(name, age, occupation)

    # temp return statement
    return df

def sendToPiscoc(name, age, occupation):
    # implement the API call here
    pass