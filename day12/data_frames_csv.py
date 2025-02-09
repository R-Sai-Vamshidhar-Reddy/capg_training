import pandas as pd
df=pd.read_csv('customers-100.csv')
print(df)

filtering=df[['First Name','Email']]       #filtering the large dataset
print("filtering: \n",filtering)
sorting=df.sort_values(by='First Name',ascending=True) #sorting by Frist name in ascending order
print("sorting: \n",sorting)
#If we use ascending=False - it will sort in decending order
grp=df.groupby('Subscription Date').count()     #grouping
print("grouping: \n",grp)