# Air Quality Dashboard ✨

## Introduction

This Streamlit dashboard provides insights into air quality data collected from multiple stations in Beijing. The data includes various air quality metrics such as PM2.5, PM10, SO2, NO2, CO, and more. The dashboard allows users to explore the data based on different criteria and visualizes key aspects of air quality.

## Getting Started

### Prerequisites

Make sure you have the required dependencies installed in your Python environment. You can set up the environment using the following commands:

```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit
```

## Running the Streamlit App
To launch the Streamlit app, run the following command:
```bash
streamlit run dashboard.py
```

This will open a local development server, and you can access the dashboard in your web browser.

### Dashboard Features
Filtered Data:
Filter the data by station and date range using the calendar at the top right.

Average Temperature Scoreboard:
Displays the average temperature based on the selected criteria.

Average Wind Speed Scoreboard:
Shows the average wind speed alongside the temperature scoreboard.

Rain Precipitation Lineplot:
Presents a line plot of rain precipitation over time.

Vehicle Pollutions Lineplot:
Displays a line plot of the average amounts of vehicle pollutions (NO2, SO2, CO) filtered by daily data.

Industrial Pollutions Lineplot:
Shows a line plot of the average amounts of industrial pollutions (PM2.5, PM10) filtered by daily data.

About and Creator Sidebar:
Provides information about the dashboard and the creator.
Feel free to explore the dashboard and gain insights into air quality trends.

