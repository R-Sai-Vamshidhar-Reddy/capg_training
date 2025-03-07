#dataframes convert the data to 2D data
import pandas as pd
data={
    'Name':['Alice',"Bob","Charlie","David"],
    'Age':[25,30,35,40],
    'City':['New York','Los Angeles','Chicago','Houston']

}

df=pd.DataFrame(data)
print(df)

#df.head() display the first few rows of the data
df.head()