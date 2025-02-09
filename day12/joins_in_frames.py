import pandas as pd
df_sales=pd.DataFrame({'State':['Delhi','Tamil Nadu','West Bengal','kerala'],
                       'Sales':[15000,14000,13000,15000]})

df_profits=pd.DataFrame({'State':['Delhi','Tamil Nadu','West Bengal','telangana'],
                       'Profit':[100000,2000000,3000000,4000000]})
df_merged_inner=pd.merge(df_sales,df_profits,on='State',how='inner')      #inner join
print(df_merged_inner)

df_merged_left=pd.merge(df_sales,df_profits,on='State',how='left')      #inner join
print(df_merged_left)

df_merged_right=pd.merge(df_sales,df_profits,on='State',how='right')      #inner join
print(df_merged_right)
df_merged_outer=pd.merge(df_sales,df_profits,on='State',how='outer')      #inner join
print(df_merged_outer)