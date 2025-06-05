import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type='pandas')
# print(df[0:],df[10:].columns)

# Find rows with missing data
df_missing = df[df.isnull().any(axis=1)]
print(df_missing)
# Convert the 'strength' column to float
df['strength'] = df['strength'].str.replace(r'\D', '', regex=True)
df['strength'] = df['strength'].astype(float)
print(df['strength'].dtype)

print(df[0:],df[10:].columns)

# scatter plot of strength vs. frequency
fig = px.scatter(df, x='frequency', y='strength', color='direction', title='Wind Data Strength vs Frequency',hover_data=['direction'])
fig.write_html('wind.html')