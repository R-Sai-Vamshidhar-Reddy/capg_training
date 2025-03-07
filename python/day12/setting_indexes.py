import pandas as pd
data={
    'Name':['Alice','Bob','Charlie','David'],
    'Age':[25,35,30,40],
    'City':['New York','Los Angeles','Chicago','Houston']

}

df=pd.DataFrame(data)
df.set_index(['Age'],inplace=True) 
print(df)

