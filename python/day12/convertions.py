import pandas as pd
df=pd.read_csv('customers-100.csv')
df.to_html('html_output.html')      #converts file to html

df.to_json('json_output.json')      #converts to json format

