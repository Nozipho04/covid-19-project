# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
df = pd.read_csv('owid-covid-data.csv')

# Display column names
print(df.columns)

# Preview the first few rows
print(df.head())

# Identify missing values
print(df.isnull().sum())

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Filter for specific countries
countries = ['Kenya', 'United States', 'India']
df_countries = df[df['location'].isin(countries)]

# Drop rows with missing critical values
df_countries = df_countries.dropna(subset=['total_cases', 'total_deaths'])

# Handle missing numeric values
df_countries.fillna(method='ffill', inplace=True)
# Plot total cases over time for selected countries
plt.figure(figsize=(12, 6))
for country in countries:
    country_data = df_countries[df_countries['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)
plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.show()

# Calculate death rate
df_countries['death_rate'] = df_countries['total_deaths'] / df_countries['total_cases']

# Plot death rate over time
plt.figure(figsize=(12, 6))
for country in countries:
    country_data = df_countries[df_countries['location'] == country]
    plt.plot(country_data['date'], country_data['death_rate'], label=country)
plt.title('COVID-19 Death Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Death Rate')
plt.legend()
plt.show()

# Plot total vaccinations over time
plt.figure(figsize=(12, 6))
for country in countries:
    country_data = df_countries[df_countries['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)
plt.title('Total COVID-19 Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.show()

# Prepare the latest data
latest_date = df['date'].max()
latest_data = df[df['date'] == latest_date]

# Create a choropleth map for total cases
fig = px.choropleth(latest_data, locations='iso_code',
                    color='total_cases',
                    hover_name='location',
                    color_continuous_scale='Reds',
                    title='Total COVID-19 Cases by Country')
fig.show()



