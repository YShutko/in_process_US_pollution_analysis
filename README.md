# US Pollution Analysis Project

The US Pollution Data project leverages a comprehensive dataset covering air pollution measurements across the United States — consisting of over 1.4 million observations and around 28 variables that record concentrations of major pollutants such as nitrogen dioxide (NO₂), sulfur dioxide (SO₂), carbon monoxide (CO), and ozone (O₃). 

This dataset spans several years and states, allowing detailed spatio-temporal analysis of pollutant levels, seasonal trends, and geographic variation. The primary objective of this project is to transform this raw data into clean, analysis-ready formats (e.g., Parquet), conduct exploratory data analysis (EDA) to uncover patterns and insights, and — where possible — apply machine learning techniques to forecast pollutant concentrations, classify air‑quality levels, or identify key factors driving pollution.

Given the public health importance of air quality, this project has the potential not only to improve our understanding of pollution trends in the U.S., but also to inform policy, raise awareness, or support predictive systems that warn populations about deteriorating air conditions.


## Project content
1. Dataset from [Kaggle](https://www.kaggle.com/datasets/sogun3/uspollution)
2. [Notebook](https://github.com/YShutko/US_pollution-_analysis/blob/faefa759121f8faf6deed4847dd77c73ba352c07/notebooks/etl_eda.ipynb)

## Data
The dataset is too large to include directly. Parquet technic was used to convert data from csv and store it in dedicated repo on GitHub.

Dataset content:
* State Code: Numeric code representing the U.S. state
* County Code:	Numeric code for the county within the state
* Site Num:	Identifier for the air monitoring site
* Address:	Street address of the monitoring station
* State:	Full name of the U.S. state
* County:	Name of the county
* City:	City where the measurement site is located
* Date Local:	Date of the observation (YYYY-MM-DD)
* NO2 Units:	Units used for nitrogen dioxide measurements
* NO2 Mean:	Daily average NO₂ concentration
* NO2 1st Max Value:	Highest NO₂ value recorded that day
* NO2 1st Max Hour:	Hour when the highest NO₂ was recorded
* NO2 AQI:	Air Quality Index for NO₂ on that day
* O3 Units:	Units used for ozone measurements
* O3 Mean:	Daily average ozone concentration
* O3 1st Max Value:	Highest O₃ value recorded that day
* O3 1st Max Hour:	Hour when the highest O₃ was recorded
* O3 AQI:	Air Quality Index for O₃ on that day
* SO2 Units:	Units used for sulfur dioxide measurements
* SO2 Mean:	Daily average SO₂ concentration
* SO2 1st Max Value:	Highest SO₂ value recorded that day
* SO2 1st Max Hour:	Hour when the highest SO₂ was recorded
* SO2 AQI:	Air Quality Index for SO₂ on that day
* CO Units:	Units used for carbon monoxide measurements
* CO Mean:	Daily average CO concentration
* CO 1st Max Value:	Highest CO value recorded that day
* CO 1st Max Hour:	Hour when the highest CO was recorded
* CO AQI:	Air Quality Index for CO on that day


