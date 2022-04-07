import pandas as pd 

inp = [
    {'A':1, 'B':1}, 
    {'A':2,'B':2}, 
    {'A':3,'B':3},
    {'A':None,'B':None},
    {'A':None,'B':5},
    {'A':6,'B':6}
    ]

def solution_one(df): #Part A
    Col1_value = set(df['A'].unique())
    df['exists'] = df['B'].map(lambda x : True if x in Col1_value  else  False) 
    occurenceCheckDf = df.loc[df['exists'] == False]
    print(type(occurenceCheckDf))
    missingValue = occurenceCheckDf.loc[occurenceCheckDf['B'] != None]
    #missingValue = occurenceCheckDf ['B'].
   

def solution_two(df): #Part B
    #res = df[~df[['A','B']].isna().all(axis=1)]
    res = df.notnull()
    print(res)

df = pd.DataFrame(inp)

print("Missing value that exists in column “B”, but not in column “A” :",solution_one(df).to_string(index=False))

print(solution_two(df))
