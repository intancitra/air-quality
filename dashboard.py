import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
from zipfile import ZipFile
from io import BytesIO
import os

st.header('Air Quality Dashboard')

# Check if the dataset is available, if not, download and extract it
if not os.path.exists('PRSA_Data_20130301-20170228.csv'):
    st.write("Downloading and extracting the dataset from https://github.com/intancitra/air-quality/raw/main/Air-quality-dataset.zip")

    # Download the zip file from the GitHub repository
    url = "https://github.com/intancitra/air-quality/raw/main/Air-quality-dataset.zip"
    response = requests.get(url)
    zip_file = ZipFile(BytesIO(response.content))

    # Extract the dataset
    zip_file.extractall(".")
    zip_file.close()

# Load the raw data
aotizhongxin_df = pd.read_csv("PRSA_Data_20130301-20170228/PRSA_Data_Aotizhongxin_20130301-20170228.csv")
changping_df = pd.read_csv("PRSA_Data_20130301-20170228/PRSA_Data_Changping_20130301-20170228.csv")
dingling_df = pd.read_csv("PRSA_Data_20130301-20170228/PRSA_Data_Dingling_20130301-20170228.csv")
dongsi_df = pd.read_csv("PRSA_Data_20130301-20170228/PRSA_Data_Dongsi_20130301-20170228.csv")
guanyuan_df = pd.read_csv("PRSA_Data_20130301-20170228/PRSA_Data_Guanyuan_20130301-20170228.csv")
gucheng_df = pd.read_csv("PRSA_Data_20130301-20170228/PRSA_Data_Gucheng_20130301-20170228.csv")
huairou_df = pd.read_csv("PRSA_Data_20130301-20170228/PRSA_Data_Huairou_20130301-20170228.csv")
nongzhanguan_df = pd.read_csv("PRSA_Data_20130301-20170228/PRSA_Data_Nongzhanguan_20130301-20170228.csv")
shunyi_df = pd.read_csv("PRSA_Data_20130301-20170228/PRSA_Data_Shunyi_20130301-20170228.csv")
tiantan_df = pd.read_csv("PRSA_Data_20130301-20170228/PRSA_Data_Tiantan_20130301-20170228.csv")
wanliu_df = pd.read_csv("PRSA_Data_20130301-20170228/PRSA_Data_Wanliu_20130301-20170228.csv")
wanshouxigong_df = pd.read_csv("PRSA_Data_20130301-20170228/PRSA_Data_Wanshouxigong_20130301-20170228.csv")
df_raw = pd.concat([aotizhongxin_df,changping_df,dingling_df,dongsi_df, guanyuan_df, gucheng_df,huairou_df,nongzhanguan_df,shunyi_df,tiantan_df,wanliu_df,wanshouxigong_df], ignore_index=True)

# Data Cleaning and Processing
# Handling missing values
df_raw['wd'] = df_raw['wd'].fillna(value="NE")
num_col = df_raw.select_dtypes(exclude='object').columns
df_raw[num_col] = df_raw[num_col].fillna(value=df_raw[num_col].median())

# Convert 'date' to datetime and set it as the index
df_raw['date'] = pd.to_datetime(df_raw[['year', 'month', 'day']])
df_raw.set_index('date', inplace=True)

# Filter data based on station and date range
st.sidebar.title("Filters")
selected_station = st.sidebar.selectbox("Select Station", df_raw['station'].unique())
date_range = st.sidebar.date_input("Select Date Range", [df_raw.index.min(), df_raw.index.max()])

filtered_data = df_raw[(df_raw['station'] == selected_station) & (pd.to_datetime(df_raw.index) >= pd.to_datetime(date_range[0])) & (pd.to_datetime(df_raw.index) <= pd.to_datetime(date_range[1]))]

col_1, col_2 = st.columns(2)

# Display average temperature scoreboard
with col_1:
    average_temperature = filtered_data['TEMP'].mean()
    st.metric("Average Temperature", value=f"{average_temperature:.2f} °C")
# Display average wind speed scoreboard
with col_2:
    average_wind_speed = filtered_data['WSPM'].mean()
    st.metric("Average Wind Speed", value=f"{average_wind_speed:.2f} MPh")

st.set_option('deprecation.showPyplotGlobalUse', False)

# Lineplot of rain precipitation
st.header("Rain Precipitation Lineplot")
plt.figure(figsize=(10, 5))
sns.lineplot(data=filtered_data, x=filtered_data.index, y='RAIN')
plt.title("Rain Precipitation Over Time")
plt.xlabel("Date")
plt.ylabel("Rain Precipitation")
st.pyplot()

# Lineplot of average vehicle pollutions by daily
st.header("Vehicle Pollutions Lineplot")
pollutants_vehicle = ['NO2', 'SO2', 'CO']
plt.figure(figsize=(10, 5))
for pollutant in pollutants_vehicle:
    sns.lineplot(data=filtered_data, x=filtered_data.index, y=pollutant, label=pollutant)

plt.title("Average Vehicle Pollutions Over Time")
plt.xlabel("Date")
plt.ylabel("Pollution Level")
plt.legend()
st.pyplot()

# Lineplot of average industrial pollutions by daily
st.header("Industrial Pollutions Lineplot")
pollutants_industrial = ['PM2.5', 'PM10']
plt.figure(figsize=(10, 5))
for pollutant in pollutants_industrial:
    sns.lineplot(data=filtered_data, x=filtered_data.index, y=pollutant, label=pollutant)

plt.title("Average Industrial Pollutions Over Time")
plt.xlabel("Date")
plt.ylabel("Pollution Level")
plt.legend()
st.pyplot()

# Sidebar - About Dashboard and Creator
st.sidebar.title("About")
st.sidebar.info(
    """
    This dashboard provides insights into air quality data.
    \n- Select a station and date range using the sidebar filters.
    \n- View average temperature and wind speed.
    \n- Explore rain precipitation trends.
    \n- Analyze average amounts of vehicle and industrial pollutions by daily.

    **Dashboard Creator:**
    \nCreated by
    \nIntan Citra Phonskaningtyas
    \nintanc110@gmail.com
    """
)
